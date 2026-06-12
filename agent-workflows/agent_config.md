# Agent Pipeline 配置

## Agent 引擎选择

| 引擎 | 费用 | Function Calling | 说明 |
|------|------|:--:|------|
| Hermes Agent | 免费 | tool_calls | 当前环境，即用 |
| GLM-4.7-Flash | 免费 | 支持 | Z.AI API，需 API Key |
| GLM-5.1 | $1.4/M in | 支持 | Z.AI 赛道旗舰模型 |

## MVP Demo 方案（Week 4）

用户输入: "训练房价预测模型，生成 ZK 证明，部署 verifier 到 Sepolia 并验证"

Agent 编排（Hermes / GLM 均可）:

  Step 1 - train_model()    -> model.onnx（预训练，直接读文件）
  Step 2 - ezkl_setup()     -> circuit + keys（ezkl pipeline）
  Step 3 - ezkl_prove()     -> proof.json + instances
  Step 4 - create_verifier() -> Verifier.sol
  Step 5 - deploy_contract() -> Sepolia 地址
  Step 6 - verify_onchain()  -> True/False

## 已知可用

- Hermes 已配置，可直接做 tool calling 编排
- ezkl_pipeline.py 已跑通全流程
- Sepolia 合约: 0x75dBdd07fE81628c7aef5a8b48493Ebc200afD60
- 链上验证已通过
