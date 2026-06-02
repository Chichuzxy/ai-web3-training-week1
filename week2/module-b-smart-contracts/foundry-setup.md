# Module B | Foundry 环境搭建指南

**日期:** 2026-05-29
**目的:** 为 ZKML Proposal Phase 3 的 Verifier 合约部署做准备

---

## 一、环境概览

| 组件 | 用途 |
|------|------|
| forge | Solidity 编译、测试、脚本 |
| cast | 链上数据查询、合约交互 |
| anvil | 本地以太坊节点（测试用） |

## 二、安装步骤

### Windows / Linux / macOS 通用方式

```bash
# 方式1: foundryup (推荐)
curl -L https://foundry.paradigm.xyz | bash
foundryup

# 方式2: cargo (如果已有 Rust 环境)
cargo install foundry-cli --profile release
```

### 验证安装

```bash
forge --version    # >= 1.0.0
cast --version
anvil --version
```

## 三、初始化 ZKML Verifier 项目

```bash
# 在训练营 repo 下创建 foundry 项目
cd ai-web3-training-week1/week2
mkdir zkml-verifier && cd zkml-verifier
forge init --no-commit
```

### 目录结构

```
zkml-verifier/
├── src/
│   └── Verifier.sol          # Groth16 Verifier 合约
├── script/
│   └── Deploy.s.sol          # 部署脚本
├── test/
│   └── Verifier.t.sol        # 测试
├── foundry.toml              # 配置
└── .env                      # 私钥 (不提交)
```

## 四、foundry.toml 配置

```toml
[profile.default]
src = "src"
out = "out"
libs = ["lib"]
solc = "0.8.20"

[rpc_endpoints]
sepolia = "${SEPOLIA_RPC_URL}"
arbitrum_sepolia = "${ARBITRUM_SEPOLIA_RPC_URL}"

[etherscan]
sepolia = { key = "${ETHERSCAN_API_KEY}" }
```

## 五、常用命令速查

```bash
# 编译
forge build

# 运行测试
forge test

# 部署到 Sepolia (需先设置 .env 中的私钥和 RPC URL)
forge script script/Deploy.s.sol --rpc-url sepolia --broadcast --verify

# 合约验证
forge verify-contract <address> src/Verifier.sol:Verifier --chain sepolia

# 链上交互 (cast)
cast call <contract_address> "verifyProof(bytes,uint256[])" --rpc-url sepolia
```

## 六、安全红线

- 私钥放 .env 文件，加到 .gitignore
- 部署前必须人工确认 RPC endpoint 和 chain ID
- 先在 anvil 本地节点测试，再上 Sepolia
- 合约代码人工审查后再部署

---

*下一步: 当 EZKL 生成 verification key 后，编写对应的 Solidity Verifier 合约*