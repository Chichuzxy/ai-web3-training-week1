# ZKML Pipeline Agent - 风险边界说明

## MVP 范围

本项目演示的是「Agent 编排下的 ZKML Pipeline」最小闭环：
- 用户输入自然语言指令
- Agent 自主编排 6 个子步骤
- 最终在 Sepolia 链上返回可验证的 ZK 证明结果

## Mock 部分

| 环节 | Mock 策略 | 真实实现需要 |
|------|-----------|-------------|
| 模型训练 | 预训练 ONNX 文件，Step 1 直接检查 | 实时训练需要 GPU + 更大数据集 |
| EZKL 电路 | 预编译，Step 2-4 复用 | 每次训练后自动重新编译 |
| Agent 自主规划 | 预设 pipeline 顺序执行 | GLM-5.1 Function Calling 动态决策 |

## 安全边界

- 本 demo 仅在 Sepolia 测试网运行，不涉及主网资产
- .env 中的私钥仅为测试网地址（Sepolia ETH 无价值）
- ZK proof 验证 = TRUE 仅证明「推理过程可验证」，不代表模型本身无 bias
- 生产环境需要：多方 MPC 生成 SRS、审计合约、审计模型

## 隐私

- 当前 proof 的 input/output visibility 设为 public（演示用）
- 生产环境可设为 private（仅验证推理过程，不暴露数据）

## 成本

| 项目 | Sepolia |
|------|---------|
| 部署 Verifier | ~2.2M gas |
| 单次 verifyProof | ~30k gas（call，免费） |
| SRS 生成 | 本地完成，无链上成本 |

## 可靠性

- EZKL 23.0.5 Python binding 在 Windows + Python 3.13 下可运行
- ezkl.encode_evm_calldata() 生成的 calldata 格式与 Halo2Verifier 匹配
- 已验证：from-scratch setup + prove + create_evm_verifier 闭环正确

## 下一步

1. GLM-5.1 Function Calling 取代预设 pipeline
2. 多模型支持（MLP / 小型 CNN）
3. L2 部署（Arbitrum Sepolia）降低 gas 成本
4. Etherscan 合约验证（需 API Key）
5. 前端界面（Web UI 输入自然语言指令）
