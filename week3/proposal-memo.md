# Hackathon Proposal Memo | ZKML Agentic Pipeline

**项目名:** ZKML Pipeline Agent
**赛道:** Z.AI | Web3 x Long-Horizon Task (GLM-5.1)
**队员:** Chichuzxy (单人 / 待组队)
**日期:** 2026-06-02

---

## 一、问题

训练 ML 模型、导出 ONNX、生成 ZK 电路、部署 Verifier、链上验证 —— 这 6 步目前需要开发者手动协调 Python、Circom/EZKL、Solidity、Foundry 等工具链，门槛极高。一个环节出错需要回退重来。

问题本质: ZKML 落地不是某个算法难，是**多步骤跨工具链的编排**难。

## 二、目标用户

Web3 开发者想把 ML 推理结果锚定到链上（如链上信用评分、AI 预言机），但不熟悉 ZK 工具链。

## 三、赛道对齐

对齐 Z.AI Long-Horizon Task:
- 输入: 一份训练数据和任务描述（如"训练一个糖尿病风险模型，链上可验证"）
- Agent 自主拆解为 6 步子任务
- 每步调用对应工具（Python/ONNX/EZKL/Foundry）
- 中间失败自动重试或降级
- 最终输出: 部署好的 Verifier 合约地址 + 一次成功的链上验证交易

6 步串行依赖 + 跨工具调用 + 错误恢复 = 典型 Long-Horizon Task。

## 四、最小 Demo (Week 4 可交付)

```
用户输入: "训练一个房价预测线性回归模型，部署 ZK verifier"
         |
    [GLM Agent 自主执行]
         |
    Step 1 -> Python: 训练模型，验证精度，导出 ONNX
    Step 2 -> EZKL: ONNX -> ZK 电路 + proving/verifying key
    Step 3 -> EZKL: 生成 proof（用测试输入）
    Step 4 -> Foundry: 创建项目，写入 Verifier.sol
    Step 5 -> Foundry: 部署到 Sepolia 测试网
    Step 6 -> Foundry: 调用 verify() 传入 proof，确认通过
         |
    输出: Verifier 合约地址 + tx hash + 验证结果
```

Mock 策略: Step 1 用预训练模型（不实时训练），Step 2 用 EZKL CLI 直接调用，不做 API 封装。

## 五、技术路径

| 层 | 选型 | 说明 |
|----|------|------|
| Agent 框架 | GLM-5.1 (Z.AI sponsor) | 长程任务拆解 + 工具调用 |
| ML 模型 | 线性回归 / 小型 MLP | ONNX 格式，EZKL 支持 |
| ZK 电路 | EZKL | 自动 ONNX -> 电路，避免手写 Circom |
| 链上 | Sepolia 测试网 | 免费 gas |
| 合约框架 | Foundry | Solidity Verifier 部署 + verify |
| 结果验证 | Etherscan | tx hash 公开可查 |

## 六、风险

| 风险 | 概率 | 应对 |
|------|------|------|
| EZKL 生成的电路过大，proof 超时 | 中 | 用更小模型（线性回归），限制参数数量 |
| GLM-5.1 API 限流或不稳定 | 中 | fallback: 用 Hermes 预定义 pipeline 脚本 |
| Verifier gas 超 Sepolia 限制 | 低 | 换 Arbitrum Sepolia (L2 更便宜) |
| ONNX 模型与 EZKL 版本不兼容 | 中 | 锁定 EZKL 版本，参考官方 example |
| Week 4 单人时间不够 | 高 | 预训练模型 + 预编译电路，只演示 agent 编排 |

## 七、不做什么

- 不做前端 UI（CLI + tx hash 验证即可）
- 不做复杂模型（线性回归就够了，跑通链路优先）
- 不做隐私输入层（PoC 用公开数据）
- 不做多模型支持

最小闭环 = 一句自然语言指令 -> agent 全自动完成 -> 链上可验证结果。
