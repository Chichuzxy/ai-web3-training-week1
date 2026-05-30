# Week 2 | 主方向深挖包: Privacy & Security → ZKML 推理验证

**作者:** Chichuzxy
**日期:** 2026-05-30
**主方向:** Privacy / Security / Sovereignty
**子方向:** ZKML (Zero-Knowledge Machine Learning) 推理验证

---

## 1. 流程图: ZKML 推理验证全链路

```
+----------+        +-------------------+        +------------------+        +--------------+
|          | 加密数据 |                   | 提交 Proof |                  | 读取结果 |              |
|  用户     |------->|  Prover (链下)     |-------->|  Verifier 合约    |-------->|  Consumer    |
| (数据方)  |        |                   |          |  (Sepolia 测试网)  |        | (保险公司等)  |
|          |        | 1.加载 ONNX 模型    |          |                  |        |              |
|          |        | 2.推理 → 结果 R     |          | verify(P, R) = ? |        | 拿到已验证 R  |
|          |        | 3.生成 ZK proof P   |          |                  |        | 原始数据未知   |
+----------+        +-------------------+        +------------------+        +--------------+

                         关键决策点:
                         ① 数据提交前需用户授权 (人工确认)
                         ② 推理执行全自动
                         ③ Proof 生成全自动
                         ④ Proof 上链需人工确认 (gas 费用)
                         ⑤ 验证结果自动执行 (合约逻辑)
                         ⑥ Consumer 读取自动

                         验证的内容:
                         "Prover 确实用承诺的模型 H(W)=commit_W
                          对承诺的输入 H(X)=commit_X
                          计算出了结果 R"
                         → 不暴露 W 和 X 的实际值
```

---

## 2. 典型场景: 健康数据隐私诊断

### 2.1 场景描述

一个患者 Alice 有敏感健康数据(血糖、血压、家族病史等)，想让 AI 模型评估糖尿病风险评分，但:
- 不希望原始数据泄露给任何第三方(包括 AI 服务方)
- 希望保险公司能信任这个评分结果(用于保费计算)
- 保险公司不想看到原始数据，只要验证过的评分

### 2.2 参与者

| 角色 | 实体 | 知道什么 | 不知道什么 |
|------|------|----------|------------|
| 数据提供者 | Alice (患者) | 原始健康数据 X | 模型内部参数 |
| 推理方 | Prover 服务 | 模型参数 W, 输入 X, 结果 R | -- (掌握全部临时数据) |
| 验证方 | Sepolia 上的 Verifier 合约 | commit_W, commit_X, R, proof P | W 和 X 的实际值 |
| 消费者 | 保险公司 | R (已验证的评分) | W 和 X 的实际值 |

### 2.3 完整流程

```
Step 1: Alice 加密健康数据, 发送给 Prover
Step 2: Prover 加载糖尿病风险模型 (ONNX), 推理得 R = 0.73 (高风险)
Step 3: Prover 用 EZKL 生成 ZK proof P:
        "我确实用 commit_W 对应的模型, 对 commit_X 对应的输入, 算出了 R=0.73"
Step 4: Prover 提交 (R, P) 到 Verifier 合约, 支付 gas
Step 5: 合约验证 P 有效 → 存储 R 为 "已验证"
Step 6: 保险公司读取链上已验证的 R=0.73, 据此计算保费
Step 7: Alice 的原始血糖、血压数据从未离开 Prover 的内存, 从未上链
```

### 2.4 为什么这个场景需要 AI + Web3 同时出现

- 没有 AI: 纯链上合约无法运行非线性模型推理 (算力不够)
- 没有 Web3: Prover 可以返回任意结果, 没有公开可验证的机制来确保诚实
- 只有 AI: 结果可信但无法向第三方证明; 只有 Web3: 能验证但无法推理

---

## 3. 反例: 不是 ZKML 的常见混淆

### 3.1 反例 1: "AI 分析后把结果写链上"

```
用户 → AI 分析 → 结果上链 (无 ZK 证明)
```

问题: 链上合约无法验证 AI 是否真的执行了推理、用了什么模型、输入是什么。这只是 "AI 结果存档", 不是 ZKML。

判断标准: 链上合约只存储结果, **没有 verify(proof)** → 不是 ZKML。

### 3.2 反例 2: "AI 做链上数据分析"

```
AI 读取链上公开数据 (交易记录) → 生成分析报告
```

问题: 数据本来就是公开的, 不需要隐私保护。ZKML 的核心价值在于 **保护隐私的同时可验证**, 这里两者都不需要。

判断标准: 不涉及隐私数据, 不涉及 ZK 证明 → 不是 ZKML。

### 3.3 反例 3: "用 TEE 保护模型, 结果直接返回"

```
模型跑在 SGX 里 → 结果返回用户 → 用户信任硬件
```

问题: TEE 提供了执行环境的可信性, 但没有生成可公开验证的密码学证明。第三方(如监管机构)无法独立验证。

判断标准: 信任模型基于硬件而非密码学, 无法公开验证 → 是 TEE 方案, 不是 ZKML。

### 3.4 辨别清单

| 判断维度 | 是 ZKML | 不是 ZKML |
|----------|---------|-----------|
| 有链下 AI 推理 | Yes | 可能 |
| 推理结果上链 | Yes | 可能 |
| 链上有 verify(proof) | Yes | **No ← 关键区别** |
| 隐私数据不暴露 | Yes | 不一定 |
| 第三方可独立验证 | Yes | 不一定 |

---

## 4. 关键风险

### 4.1 风险矩阵

| # | 风险 | 严重度 | 可能性 | 应对 |
|---|------|--------|--------|------|
| R1 | Prover 用错误/恶意模型推理 | 致命 | 中 | 模型哈希链上承诺, 每次验证比对 commit_W |
| R2 | ZK 电路与模型逻辑不一致 | 致命 | 中 | 电路审计, 用已知输入验证电路输出是否等于模型输出 |
| R3 | Prover 服务器被攻破, 用户数据泄露 | 高 | 中 | 数据加密传输, 推理后立即清除, 可选 TEE 加固 |
| R4 | 证明生成耗时过长 | 中 | 高 | 限制模型大小, 量化压缩, 分层证明 (recursive proof) |
| R5 | 链上 Verifier gas 过高 | 中 | 高 | 部署到 Layer2, 选择 gas 友好的证明系统 (Groth16) |
| R6 | 可信设置被破坏 (Groth16) | 低 | 低 | PoC 阶段可接受, 生产用 Halo2/Plonk 替代 |
| R7 | 模型被逆向工程 (通过多次查询推断权重) | 中 | 低 | 限流 + 结果添加噪声, 但 PoC 阶段暂不处理 |

### 4.2 风险缓解优先级

```
PoC 阶段必须处理: R1 (模型承诺), R2 (电路审计), R4 (模型限制)
Week 3 可以处理: R5 (L2 部署)
长期 (主网): R3 (TEE), R6 (Halo2), R7 (限流)
```

### 4.3 一句话总结

**ZKML 的安全假设链条:** 模型哈希可信 → 电路与模型一致 → 数学证明正确 → 链上验证无误。任何一环断裂, 整个信任链就断了。

---

## 5. 最小验证计划

### 5.1 验证目标

证明: "Circom 电路 + Groth16 证明系统能跑通 编译 → Proof → Verify 全流程"

不证明: 模型精度、生产可用性、大规模性能、经济模型

### 5.2 验证步骤 (已完成, 产物见 artifacts/circom-poc/)

| 步骤 | 做什么 | 如何验证成功 | 当前状态 |
|------|--------|-------------|----------|
| Step 1 | 编写 Circom 电路 (basicAdd.circom: a+b=c) | `circom basicAdd.circom --r1cs --wasm` 成功 | Done |
| Step 2 | 生成 Proving Key + Verification Key | `snarkjs groth16 setup` 成功, 生成 .zkey 文件 | Done |
| Step 3 | 用输入 (a=3, b=5) 生成 proof | 运行 `generate_witness` + `prove`, 产出 proof.json | Done |
| Step 4 | 本地验证 proof | `snarkjs groth16 verify` 返回 OK | Done |
| Step 5 | 导出 Solidity Verifier 合约 | `snarkjs zkey export solidityverifier` 成功 | Pending |
| Step 6 | Foundry 编译 + 部署到 Sepolia | `forge create Verifier` 成功, 返回合约地址 | Pending |
| Step 7 | 链上验证 proof | 调用 `verifyProof()`, 返回 true | Pending |

### 5.3 若验证失败

| 失败点 | 原因分析 | 调试方法 |
|--------|----------|----------|
| 电路编译失败 | Circom 版本 / 语法问题 | 检查 circom --version, 简化电路重试 |
| Proof 生成为空 | 输入格式错误 | 检查 input.json 字段名是否匹配电路 signal |
| 本地验证失败 | proof/witness/public 不匹配 | 逐文件对比 checksum |
| 合约部署失败 | gas 不足或网络问题 | 换 Sepolia faucet, 检查 RPC |
| 链上验证失败 | public input 格式/顺序不匹配 | 对比 export 合约的 input 顺序和实际传入值 |

### 5.4 当前 PoC 产物位置

```
week2/artifacts/circom-poc/
  basicAdd.circom        # 电路源码 (a+b=c)
  input.json             # 测试输入 {"a": 3, "b": 5}
  proof.json             # ZK 证明
  public.json            # 公开输出 ["8"]
  verification_key.json  # 链上验证密钥
```

### 5.5 后续扩展路径

```
PoC (Circom, 加法电路) ✅ 已完成
  ↓
Phase 2 (Circom, 线性回归电路) → 证明矩阵运算
  ↓
Phase 3 (EZKL, ONNX → 电路自动转换) → 真实 ML 模型
  ↓
Phase 4 (Halo2, 无需可信设置) → 生产可用
```

---

## 6. 与 Week 3 的承接

| 从 Week 2 带走 | 在 Week 3 用上 |
|---------------|---------------|
| ZK 电路编写经验 (Circom) | 扩展为 ML 模型电路 |
| Proof 生成 + 验证流程 | 链上 Verifier 部署 |
| 风险清单 + 缓解方案 | 项目安全设计文档 |
| 方向选择判断逻辑 | Hackathon 选题对比 |
| artifacts/circom-poc/ 产物 | 链上验证 Demo |

---

## 附录: 深挖包文件清单

| 文件 | 位置 | 说明 |
|------|------|------|
| 方向选择说明 | direction-selection.md | 为什么选 Privacy, 为什么不是纯 AI/纯 Web3 |
| 问题拆解 | problem-decomposition.md | 参与方/流程/自动化边界/验证机制 |
| 初步 Proposal | proposal-zkml.md | 技术架构/选型/时间估算 |
| Circom 调试记录 | circom-debug-log.md | 环境安装踩坑 + 解决方案 |
| PoC 产物 | artifacts/circom-poc/ | 电路源码 + proof + verification key |
| 本文档 | deep-dive-package.md | 流程图/场景/反例/风险/验证计划整合 |
