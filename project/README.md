# ZKML Pipeline Agent

**赛道:** Z.AI | Web3 x Long-Horizon Task
**队员:** Chichuzxy
**Week 4 冲刺目标:** 用户输入一句话 -> agent 全自动完成 ONNX 模型 -> ZK 证明 -> 链上验证

---

## 目录结构

```
zkml-pipeline-agent/
├── README.md                  # 本文件
├── sprint-plan.md             # Week 4 每日任务
├── agent/
│   └── pipeline.yaml          # GLM agent 任务编排配置
├── model/
│   ├── train.py               # 训练线性回归模型 -> 导出 ONNX
│   └── model.onnx             # 预训练模型（mock: 提前生成）
├── zk/
│   ├── settings.json          # EZKL 配置
│   ├── circuit.onnx           # EZKL 编译后的电路
│   ├── pk.key                 # proving key
│   ├── vk.key                 # verifying key
│   ├── proof.json             # 生成的 proof
│   └── witness.json           # 见证数据
├── contracts/
│   ├── lib/                   # Foundry 依赖
│   ├── src/Verifier.sol       # EZKL 生成的 Verifier 合约
│   ├── script/Deploy.s.sol    # 部署脚本
│   └── test/Verify.t.sol      # 验证测试
├── artifacts/
│   ├── verifier-address.txt   # Sepolia 合约地址
│   └── verify-tx.txt          # 链上验证交易哈希
├── foundry.toml
└── .env.example
```

## 关键依赖

| 层 | 依赖 | 版本 |
|----|------|------|
| Agent | GLM-5.1 API | latest |
| ML | Python 3.11 + scikit-learn + onnx | 1.5+ |
| ZK | EZKL CLI | v21.0.0 |
| 合约 | Foundry | latest |
| 网络 | Sepolia 测试网 | - |
| Fallback | Hermes Agent (本地编排) | - |

## 最小闭环链路

```
用户: "训练一个房价预测模型，部署 ZK verifier 到 Sepolia"

Agent 执行:
  Step 1  训练模型 -> model.onnx
  Step 2  EZKL: onnx -> 电路 + keys
  Step 3  EZKL: 生成 witness + proof
  Step 4  EZKL: 导出 Solidity Verifier
  Step 5  Foundry: 部署到 Sepolia
  Step 6  Foundry: cast call verify(proof) -> 确认通过

输出: 合约地址 + tx hash + 验证截图
```

## Mock 策略

- 模型提前训练好（不实时训练），Step 1 直接读文件
- EZKL 电路预编译一次，Step 2-4 复用
- Agent 负责编排 Steps 1-6，而不是重新生成电路

## 风险 fallback

| 风险 | fallback |
|------|----------|
| GLM API 不可用 | Hermes Agent + 预设脚本（失去"自主拆解"，但链路仍完整） |
| EZKL Windows 不兼容 | Google Colab 跑 EZKL（Ezkl Python binding） |
| Sepolia gas 超限 | 切 Arbitrum Sepolia |
