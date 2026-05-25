# Module A | AI Patterns -- 问题地图

**目标：** 梳理 Week 1 的实践后，AI 这一侧还有哪些盲区、缺口、和待深化的方向。这张地图是 Week 2 的学习导航。

---

## 一、认知盲区层（不知道不知道的）

| # | 问题 | 为什么重要 | Week 2 行动 |
|---|------|-----------|-------------|
| 1 | Context Window 到底怎么计费？token 估算方法？ | 直接影响 prompt 设计和 cost 控制 | 写一个 token counter CLI demo |
| 2 | Temperature / Top-p / Max Tokens 调参有什么系统性影响？ | Week 1 做了实验但记录不够完整 | 重新做对照实验，整理对比表 |
| 3 | Structured Output（JSON Schema）如何与智能合约交互？ | 这是 AI x Web3 的关键接口 | 实现 AI 生成 JSON → 合约部署的流水线 |
| 4 | RAG vs Fine-tuning 在 Web3 场景各适合什么？ | 技术选型的基础 | 写一篇对比分析笔记 |

## 二、技能缺口层（知道不会做的）

| # | 技能 | 现状 | Week 2 目标 |
|---|------|------|-------------|
| 5 | Tool Use / Function Calling 完整流程 | 了解概念但没实操 | 搭建 Agent 可调文件+终端+搜索的 demo |
| 6 | ReAct Pattern（Reasoning + Action 循环） | 听说过 | 画一个流程图 + 写代码演示 |
| 7 | Multi-Agent Orchestration | 未了解 | 理解 orchestrator-worker 模式 |
| 8 | Error handling & retry logic in agent workflow | 未涉及 | 设计带 fallback 机制的 workflow |
| 9 | Prompt Chaining（复杂任务拆分） | 部分实践 | 设计 multi-step chain 解决实际问题 |

## 三、工程实践层（还没落地的）

| # | 实践项 | Week 1 现状 | Week 2 目标 |
|---|--------|------------|-------------|
| 10 | Git Branch Strategy + PR | 只有 main 分支直接 push | 建立 feature branch → PR → merge 流程 |
| 11 | CI/CD Pipeline | 无 | GitHub Actions 自动 lint + test |
| 12 | Logging & Observability | 无 | 给 agent workflow 加 structured logging |
| 13 | Contract Testing Framework | 无 | 搭建 Foundry/Hardhat 测试环境 |
| 14 | Gas Optimization Checklist | 有基础认知 | 写一份 gas optimization checklist |

## 四、交叉领域层（AI x Web3 特有挑战）

| # | 问题 | 复杂度 | 优先级 |
|---|------|--------|--------|
| 15 | AI 生成的合约代码如何保证安全？ | ⭐⭐⭐⭐ | P0 - 核心安全问题 |
| 16 | Agent 能安全地操作钱包吗？边界在哪？ | ⭐⭐⭐⭐⭐ | P0 - 私钥安全红线 |
| 17 | Oracle + AI 决策：链下数据可信度？ | ⭐⭐⭐ | P1 |
| 18 | Tokenized AI services 经济模型？ | ⭐⭐⭐ | P2 |
| 19 | ZKML（零知识证明机器学习）可行性？ | ⭐⭐⭐⭐ | P3 - 探索性 |

---

## 使用说明

这张地图是活的文档：
- **P0 优先解决**，打 `[x]` 标记完成
- 每周回顾一次，标记"已解决"/"延期"/"降级"
- 新遇到的问题继续追加到四个层级中
