# Week 2 | Deep Dive: Smart Contracts + Advanced AI Patterns

**起始日期:** TBD  
**前置条件:** Week 1 完成（Learning Agent + Web3 基础 + 交叉实验）

---

## 一、Week 1 回顾

### 已完成交付物
| 模块 | 内容 | 状态 |
|------|------|------|
| A | Learning Agent 配置记录 | ✅ |
| A | Prompt 库 + 参数实验 | ✅ |
| A | Demo CLI 工具 | ✅ |
| B | 钱包创建 + Sepolia 交互 | ✅ |
| B | TraceRecorder.sol 部署 | ✅ |
| B | Gas 数据分析 | ✅ |
| C | AI x Web3 交叉实验 | ✅ |

### 遗留待深化
- Foundry/Hardhat 测试工作流未搭建
- OpenZeppelin 标准库未实践
- Agent Tool Use / ReAct Pattern 未深入
- Prompt Engineering 不够系统化
- 合约安全审计无实操经历

---

## 二、Week 2 目标

| 优先级 | 模块 | 核心内容 |
|--------|------|----------|
| P0 | Module A | AI高级模式: ReAct, Structured Output, Agent Workflow |
| P0 | Module B | Solidity深入: Gas优化, Security Audit, OpenZeppelin |
| P1 | Module C | AIxWeb3进阶: 合约审计流水线, 链上数据+AI分析 |
| P2 | Module D | L2/ZK入门: Layer2原理, ZKML概念探索 |

---

## 三、目录结构总览

```
ai-web3-training-week1/
├── week1/                              ← Week1 全部内容保留在此
│   ├── module-a-ai-fundamentals/       # learning-agent-setup, prompts-library
│   ├── module-b-web3-fundamentals/     # testnet-tx-record
│   ├── module-c-cross-experiment/      # cross-experiment-record
│   ├── docs/                           # daily-checkin, prompt experiments
│   └── artifacts/                      # tx-hashes.txt, TraceRecorder.sol
│
├── week2/                              ← Week2 新内容
│   ├── module-a-ai-patterns/           # AI高级模式
│   │   ├── problem-map.md              # 问题地图 ← 从这里开始
│   │   ├── prompt-engineering.md       # Prompt工程系统化
│   │   ├── agent-workflows.md          # ReAct, Multi-Agent
│   │   └── structured-output.md        # JSON Schema 实践
│   │
│   ├── module-b-smart-contracts/       # 智能合约深入
│   │   ├── solidity-security.md        # 合约安全审计清单
│   │   ├── gas-optimization.md         # Gas优化实战指南
│   │   ├── openzeppelin-guide.md       # OZ标准库使用
│   │   └── foundry-setup.md            # Foundry环境搭建
│   │
│   ├── module-c-ai-web3-pro/           # AIxWeb3进阶实验
│   │   ├── experiment-1.md             # 实验1: AI合约审计流水线
│   │   ├── experiment-2.md             # 实验2: 链上数据+AI分析
│   │   └── experiment-3.md             # 实验3: Oracle+AI决策
│   │
│   ├── module-d-l2-zk/                 # L2/ZK入门
│   │   ├── l2-overview.md              # Layer2概览
│   │   └── zkml-intro.md               # ZKML概念
│   │
│   ├── daily-checkin/                  # Week2 每日打卡
│   └── artifacts/                      # Week2 产物(代码、hash、截图)
│
├── module-a-ai-fundamentals/           # Week1原目录(保留)
├── module-b-web3-fundamentals/         # Week1原目录(保留)
├── module-c-cross-experiment/          # Week1原目录(保留)
├── docs/                               # Week1文档(保留)
├── artifacts/                          # Week1产物(保留)
├── README.md                           # 全局进度追踪
└── week2/README.md                     # 本文件
```

---

## 四、本周安全红线（继承自 Week 1）

- 私钥和助记词永远不暴露给 AI
- 所有上链操作必须在测试网完成
- 每笔交易必须人工确认
- AI生成的代码必须经过人工审查后才能部署

---

## 五、推进计划

### Day 1-2: Module A 问题地图 + Prompt Engineering
- [ ] 阅读 problem-map.md，确定本周优先解决的项
- [ ] Prompt参数对照实验（Temperature, Top-p, Max Tokens）
- [ ] Structured Output 实践

### Day 3-4: Module B Solidity 深入
- [ ] Gas 优化 checklist 编写
- [ ] OpenZeppelin ERC20 合约实现
- [ ] Foundry 测试环境搭建

### Day 5-6: Module C AI×Web3 进阶
- [ ] 选择1-2个实验动手实践
- [ ] 记录实验过程和边界情况

### Day 7: 总结归档
- [ ] 每日打卡整理
- [ ] Commit & Push
