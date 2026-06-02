# Week 4 Sprint Plan

**目标:** 完成最小闭环 demo — 一句话输入 -> agent 编排 -> 链上 Verifier 验证通过

---

## Day 0 (Week 3 收尾)

- [x] proposal memo
- [x] 深度研究
- [x] repo skeleton
- [x] sprint plan 本文

---

## Day 1 (周一) — 模型 + EZKL 环境

| 任务 | 负责人 | 预计 |
|------|--------|------|
| 训练线性回归模型 (房价预测) -> ONNX | Chichuzxy | 1h |
| 安装 EZKL CLI / Python binding | Chichuzxy | 1h |
| 跑通 EZKL Colab demo (验证环境) | Chichuzxy | 1h |
| 生成 circuit + keys (本地或 Colab) | Chichuzxy | 1h |

交付: model.onnx + circuit 编译成功截图

---

## Day 2 (周二) — Proof 生成 + Verifier 合约

| 任务 | 负责人 | 预计 |
|------|--------|------|
| 用测试输入生成 witness | Chichuzxy | 1h |
| 生成 proof (EZKL prove) | Chichuzxy | 1h |
| 导出 Solidity Verifier 合约 | Chichuzxy | 30min |
| 初始化 Foundry 项目 + 编译 Verifier | Chichuzxy | 1h |

交付: proof.json + Verifier.sol 编译通过

---

## Day 3 (周三) — 链上部署 + 验证

| 任务 | 负责人 | 预计 |
|------|--------|------|
| 写 Deploy.s.sol 脚本 | Chichuzxy | 30min |
| 部署 Verifier 到 Sepolia | Chichuzxy | 30min |
| cast call verify(proof) 确认通过 | Chichuzxy | 30min |
| 记录合约地址 + tx hash | Chichuzxy | 30min |

交付: 合约地址 + 验证成功 tx hash

---

## Day 4 (周四) — Agent 编排 + 端到端

| 任务 | 负责人 | 预计 |
|------|--------|------|
| 接入 GLM-5.1 API (或 Hermes fallback) | Chichuzxy | 1h |
| 写 pipeline 配置文件 | Chichuzxy | 1h |
| 端到端测试: 一句话 -> 全流程自动化 | Chichuzxy | 2h |
| 录制 demo 截图 / 录屏 | Chichuzxy | 30min |

交付: 端到端跑通 + demo 截图

---

## Day 5 (周五) — 打磨 + 提交

| 任务 | 负责人 | 预计 |
|------|--------|------|
| README 完善（demo 步骤 + 截图） | Chichuzxy | 1h |
| 清理无用文件 | Chichuzxy | 30min |
| 最终端到端测试 + 录屏 | Chichuzxy | 1h |
| 准备提交材料 + 路演说明 | Chichuzxy | 1h |

交付: 完整提交包

---

## Day 6-7 (周末) — Buffer

- 处理 Day 1-5 未完成项
- 额外 polish: 美化 README、补风险说明
- 如果顺利: 尝试多模型支持或 L2 部署

---

## 提交材料清单

- [ ] GitHub repo (含 README + 截图 + tx hash)
- [ ] Demo 录屏 / GIF
- [ ] 1 页项目说明 (问题、方案、技术栈、演示)
- [ ] Sepolia 合约地址 + 验证交易哈希
