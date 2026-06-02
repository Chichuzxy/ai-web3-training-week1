# Week 3 | Hackathon 启动 + 方向收敛

**日期:** 2026-06-02 ~ 2026-06-08
**主方向:** Privacy & Security -> ZKML 推理验证
**目标赛道:** Z.AI | Web3 x Long-Horizon Task

---

## 一、Week 1-2 缺口诊断

| 检查项 | 状态 | 备注 |
|--------|------|------|
| Learning Agent 可用 | done | Hermes Agent 运行中 |
| GitHub Repo 结构 | done | module-a/b/c + week2/ 结构完整 |
| 测试网交互 | done | Sepolia: 合约部署 + 4笔交易记录 |
| 最小交叉实验 | done | AI生成合约->Review->部署->区块浏览器验证 |
| 问题地图 (5+方向) | done | problem-map.md 覆盖6方向 |
| 主方向选择 | done | Privacy & Security -> ZKML |
| Proposal 初稿 | done | proposal-zkml.md |
| 深挖包 | done | deep-dive-package.md |
| 方向 backlog | done | direction-backlog.md |
| Circom PoC | done | basicAdd 电路编译+Proof生成+本地验证通过 |
| Solidity Verifier 部署 | 未完成 | PoC Phase 3: 需用 Foundry 部署到 Sepolia |

结论: Week 1-2 全部交付物完成，无严重缺口。唯一未完成项是 Circom PoC 的链上部署阶段。

---

## 二、赛道对齐分析

当前主方向 ZKML 与两条官方赛道的对齐:

| 赛道 | 对齐度 | 分析 |
|------|--------|------|
| Cobo Agentic Wallet | 弱 | 需硬套「agent支付ZKML验证服务」场景 |
| Z.AI Long-Horizon Task | 强 | ZKML 全链路(6步串行)天然是长程多步骤任务 |

ZKML 全链路作为 Long-Horizon Task:
```
训练模型 -> ONNX导出 -> ZK电路生成 -> 部署Verifier -> 推理+证明 -> 链上验证
```
6 个步骤需要自主规划、工具调用、中间结果验证、错误恢复——对齐 GLM-5.1 的长程任务拆解能力。

项目定位: AI Agent 自主完成 ML 模型的可验证推理部署全流程。

---

## 三、本周任务清单

### 课程 A - 补齐 (已基本完成)
- [x] Week 1-2 缺口诊断 (本文件)
- [ ] 更新根目录 README 反映 Week 3 状态
- [ ] 1 页 proposal memo (Hackathon 格式)

### 课程 B - 深度研究
- [ ] EZKL 阅读摘要: 解决什么、边界、缺什么
- [ ] Circom/SnarkJS 阅读摘要: 工具链成熟度、限制
- [ ] Halo2 vs Groth16 对比: 何时用哪个
- [ ] Risk memo: ZKML 方向成立的前提和失败点

### Hackathon 准备
- [ ] 选定赛道: Z.AI Long-Horizon Task
- [ ] 下载/了解 GLM API / SDK
- [ ] 项目卡片: 项目名、用户、最小功能
- [ ] 组队: 角色分工、技术栈确认
- [ ] Repo skeleton + sprint plan

### 本周交付物
1. 缺口诊断 (本文件)
2. 更新后的根 README
3. 1 页 proposal memo
4. 2-3 份深度研究摘要
5. 1 份 risk memo
6. Hackathon 方向卡
7. Repo skeleton + Week 4 sprint plan

---

## 四、今日任务 (6/2)

| 优先级 | 任务 | 预计时间 |
|--------|------|----------|
| P0 | 提交4个遗留文件 | 10min done |
| P0 | 缺口诊断 | 20min done |
| P1 | 更新根 README | 15min done |
| P1 | proposal memo | 30min done |
| P1 | 深度研究 | 30min done |
| P2 | Repo skeleton + sprint plan | 20min done |

---

## 五、安全红线

- 私钥/助记词永不暴露
- 所有链上操作仅限测试网
- 每笔交易人工确认
- AI 生成代码人工审查后部署
