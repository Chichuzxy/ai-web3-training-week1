# Week 2 | Circom ZK 电路调试记录

**作者:** Chichuzxy  
**日期:** 2026-05-28  
**目标:** 用 Circom + SnarkJS (Groth16) 跑通 basicAdd 电路的 编译 → Witness → Proof → Verify 全流程

> **与 Proposal 的关系:** 这是任务 3 (proposal-zkml.md) Phase 1 的前置步骤。Proposal 指定最终用 EZKL + Halo2 作为生产方案，本 PoC 先用 Circom + Groth16 验证"编译 → Proof → Verify"基本流程是否可行，确认工具链和环境正常后再迁移到 EZKL + Halo2。Groth16 的优势是工具链成熟 (SnarkJS)、gas 低，适合快速验证；Halo2 无需可信设置，后续用于 ONNX 模型转换。

---

## 一、环境准备

### 1.1 发现的问题

初始环境装的是 npm 版 `circom` (旧 JS 实现, circom1)，不支持 circom2 语法：
```bash
$ circom --version
# 输出版本号但实际是旧版
$ npm list -g circom
# 发现是 npm 包
```

**解决:** 下载官方 circom2 (Rust 版) v2.2.3
```bash
# 从 GitHub Releases 下载 Windows 版
curl -sLO https://github.com/iden3/circom/releases/download/v2.2.3/circom-windows-amd64.exe
mkdir -p ~/bin
cp circom-windows-amd64.exe ~/bin/circom2.exe
circom2.exe --version  # circom compiler 2.2.3
```

### 1.2 安装 SnarkJS
```bash
npm install -g snarkjs
```

---

## 二、代码修复

### 2.1 CRLF 换行符问题

文件在 Windows 下编辑，带有 `\r\n` 换行符，circom 解析报错。

**解决:**
```bash
sed -i 's/\r$//' circuits/basicAdd.circom
```

### 2.2 Pragma 版本不匹配

原始代码:
```circom
pragma circom 0.5.46;
```

**解决:** 改为与编译器匹配的版本:
```circom
pragma circom 2.2.3;
```

### 2.3 语法变更 (circom1 → circom2)

原始代码:
```circom
signal private input a;
signal private input b;
```

circom2 中 `input` 默认就是 private 的，`private` 关键字已移除。

**解决:**
```circom
signal input a;
signal input b;
```

---

## 三、全流程执行

### 3.1 编译电路
```bash
circom2.exe circuits/basicAdd.circom --r1cs --wasm --sym -o build/
```
输出:
```
template instances: 1
non-linear constraints: 0
linear constraints: 1
public inputs: 0
private inputs: 2
public outputs: 1
wires: 4
```

### 3.2 Powers of Tau (可信设置)
```bash
cd build/
# 初始化
snarkjs powersoftau new bn128 12 pot12_0000.ptau -v
# 贡献熵
snarkjs powersoftau contribute pot12_0000.ptau pot12_0001.ptau --name="First" -e="random text"
# 准备 phase2
snarkjs powersoftau prepare phase2 pot12_0001.ptau pot12_final.ptau -v
```

### 3.3 生成证明密钥
```bash
snarkjs groth16 setup basicAdd.r1cs pot12_final.ptau basicAdd_0000.zkey
snarkjs zkey contribute basicAdd_0000.zkey basicAdd_final.zkey --name="Contributor" -e="entropy"
snarkjs zkey export verificationkey basicAdd_final.zkey verification_key.json
```

### 3.4 生成 Witness
创建 `input.json`:
```json
{"a": "3", "b": "5"}
```

```bash
node basicAdd_js/generate_witness.js basicAdd_js/basicAdd.wasm input.json witness.wtns
```

### 3.5 生成证明
```bash
snarkjs groth16 prove basicAdd_final.zkey witness.wtns proof.json public.json
```

### 3.6 验证证明
```bash
snarkjs groth16 verify verification_key.json public.json proof.json
```
输出: `snarkJS: OK!`

---

## 四、产物清单

| 文件 | 说明 |
|------|------|
| `build/basicAdd.r1cs` | 电路约束系统 |
| `build/basicAdd_js/basicAdd.wasm` | 用于生成 witness 的 WASM |
| `build/basicAdd_final.zkey` | 证明密钥 |
| `build/verification_key.json` | 验证密钥 (部署到链上) |
| `build/witness.wtns` | 见证数据 |
| `build/proof.json` | 零知识证明 |
| `build/public.json` | 公开输入/输出 (`c = 8`) |

---

## 五、下一步

- 将 `verification_key.json` 和 `proof.json` 用于链上 Verifier 合约部署
- 用 `snarkjs zkey export solidityverifier` 生成 Solidity 验证合约
- 在 Sepolia 测试网部署并验证
- **迁移到 EZKL + Halo2:** 本 PoC 验证了 Circom + Groth16 基本流程可行，接下来按任务 3 (proposal-zkml.md) Phase 2 执行：用 EZKL 将 ONNX 模型转为 ZK 电路，用 Halo2 生成证明并部署到链上
