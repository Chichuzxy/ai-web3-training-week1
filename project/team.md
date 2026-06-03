# 队伍信息 | ZKML Pipeline Agent

## 当前状态

单人队伍。优先推进技术实现，同时开放组队。

## 成员

| 角色 | 人员 | 可投入时间 (Week 4) | 职责 |
|------|------|---------------------|------|
| PM / 研究 | Chichuzxy | 每天 4-6h | 方向收敛、proposal、研究、文档 |
| 工程 | Chichuzxy | 每天 4-6h | ML 模型、EZKL 电路、Foundry 合约 |
| Agent 集成 | Chichuzxy | 每天 4-6h | GLM API / Hermes fallback 编排 |
| Demo / 文档 | Chichuzxy | 每天 4-6h | 截图、录屏、README、路演 |

## 技术栈确认

| 层 | 选型 | 确认者 |
|----|------|--------|
| Agent | GLM-5.1 / Hermes fallback | Chichuzxy |
| ML | Python 3.11+ scikit-learn onnx | Chichuzxy |
| ZK | EZKL CLI v21.0.0 | Chichuzxy |
| 合约 | Foundry (Solidity 0.8.20) | Chichuzxy |
| 测试网 | Sepolia / Arbitrum Sepolia | Chichuzxy |
| 版本控制 | Git + GitHub | Chichuzxy |

## 待确认

- [ ] GLM-5.1 API Key 获取
- [ ] EZKL 本地安装 / Colab 方案确认
- [ ] Sepolia RPC URL 和测试币
- [ ] 是否开放组队 / 找队友

## 需要向赞助方/导师提出的问题

1. GLM-5.1 API 的 rate limit 和稳定性保证？
2. Long-Horizon Task 的最小可接受步数？6 步够不够？
3. EZKL 编译的 Verifier 合约是否算"自主任务拆解"的一部分？
4. 允许预编译电路作为 mock 策略吗？还是必须从零生成？
