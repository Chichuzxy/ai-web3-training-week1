# Hackathon 方向卡 | ZKML Pipeline Agent

## 基本信息

| 字段 | 内容 |
|------|------|
| 项目名 | ZKML Pipeline Agent |
| 赛道 | Z.AI | Web3 x Long-Horizon Task |
| 一句话 | 用一句话让 AI Agent 自主完成 ML 模型的可验证推理部署全链路 |
| 队员 | Chichuzxy (待补充) |
| 仓库 | https://github.com/Chichuzxy/ai-web3-training-week1 |

## 问题

训练 ML 模型并使其推理结果在链上可验证需要协调 Python、ONNX、ZK 电路工具、Solidity、Foundry 等至少 5 种工具链。开发者需手动执行 6 步串行流程，任一环节出错需回退重来。这不是某个算法难，是多步骤跨工具链编排难。

## 用户

Web3 开发者想把 ML 推理结果锚定到链上（链上信用评分、AI 预言机、去中心化推理市场），但不熟悉 ZK 工具链。

## 方案

AI Agent (GLM-5.1) 接收自然语言指令，自主将任务拆解为 6 个串行子任务，分别调用 Python/ONNX/EZKL/Foundry，中间失败自动重试，最终输出部署好的 Verifier 合约 + 链上验证成功交易。

```
输入: "训练一个房价预测模型，部署 ZK verifier 到 Sepolia"

Agent 自主执行:
  Step 1  训练模型 -> model.onnx
  Step 2  EZKL: ONNX -> ZK 电路 + keys
  Step 3  EZKL: 生成 witness + proof
  Step 4  EZKL: 导出 Solidity Verifier
  Step 5  Foundry: 部署到 Sepolia
  Step 6  cast call verify(proof) -> 通过

输出: 合约地址 + tx hash
```

## 技术栈

| 层 | 选型 |
|----|------|
| Agent | GLM-5.1 (sponsor) / Hermes fallback |
| ML | Python + scikit-learn + ONNX |
| ZK | EZKL v21 (ONNX auto-compile) |
| 链 | Sepolia / Arbitrum Sepolia |
| 合约 | Foundry + Solidity |

## 赛道对齐 (Z.AI Long-Horizon Task)

- 6 步串行依赖 = 需要自主任务拆解
- 跨 Python/CLI/Solidity 工具 = 需要多工具调用
- 中间失败需要重试 = 需要错误恢复
- 最终结果需链上验证 = 可度量成功/失败

## 最小 Demo (Week 4)

一句话 -> agent 全流程自动化 -> 链上可验证。模型提前训练好（mock），EZKL 电路预编译，Agent 专注编排。

## 风险 + 应对

| 风险 | 应对 |
|------|------|
| EZKL Windows 不兼容 | Colab 跑 EZKL，文件传到本地 |
| GLM API 不稳定 | Hermes + 预设脚本 fallback |
| 电路过大 | 用线性回归（<100参数），跑 L2 |
| 单人时间不够 | 预训练模型 + 预编译电路，只演示编排 |
