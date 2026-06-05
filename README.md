# 🚀 AI x Web3 School - Training Project

**学员:** Chichuzxy
**当前周次:** Week 3｜Hackathon 启动 + 方向收敛
**主方向:** Privacy & Security -> ZKML 推理验证
**赛道:** Z.AI | Web3 x Long-Horizon Task
**开始日期:** May 21, 2026

---

## 📋 本周 (Week 3) 目标

收敛方向、补齐研究、组建队伍、为 Week 4 Hackathon 冲刺做好一切准备。

---

## 📁 项目结构

```
ai-web3-training-week1/
├── README.md                    # 本文件
├── .gitignore
│
├── module-a-ai-fundamentals/    # [Done] AI 基础
├── module-b-web3-fundamentals/  # [Done] Web3 基础
├── module-c-cross-experiment/   # [Done] 交叉实验
├── module-d-l2-zk/              # [Done] L2/ZK 模块
│
├── week2/                       # [Done] 问题地图 + 方向选择 + Proposal
│   ├── problem-map.md
│   ├── direction-selection.md
│   ├── proposal-zkml.md
│   ├── deep-dive-package.md
│   └── artifacts/circom-poc/
│
├── week3/                       # [Done] 缺口诊断 + 深度研究
│   ├── README.md
│   ├── proposal-memo.md         # Hackathon 1页 proposal
│   └── deep-research.md         # EZKL/Circom/Halo2 + risk memo
│
├── project/                     # Hackathon 项目骨架
│   ├── README.md                # 项目说明
│   ├── sprint-plan.md           # Week 4 每日任务
│   ├── hackathon-card.md        # Hackathon 方向卡
│   ├── team.md                  # 队伍信息
│   ├── glm-api-plan.md          # GLM-5.1 API 方案
│   └── .env.example
│
├── contracts/                   # [Done] Foundry 合约 + 测试
│   ├── foundry.toml
│   ├── src/
│   ├── test/
│   └── lib/forge-std/           # forge-std 标准库
│
├── docs/                        # 学习笔记
├── artifacts/                   # 交易记录 + PoW
├── agent-workflows/             # Agent 编排脚本
└── testing-foundry/             # Foundry 测试练习
```

---

## 🎯 Week 1 任务清单

### 模块 A｜AI 基础（优先级 ⭐⭐⭐）

- [ ] **搭建 Learning Agent** 
  - [ ] 配置 Hermes Agent（当前环境）
  - [ ] 记录模型/API 路径
  - [ ] 测试 Agent 生成小工具/页面

- [ ] **创建 GitHub Repo** ← 本项目就是！✅

- [ ] **Agent 实战练习**
  - [ ] 用 Agent 生成一个 CLI 工具或简单网页
  - [ ] 记录工具配置、学习日志
  - [ ] Commit 到 GitHub

- [ ] **Prompt 工程学习**
  - [ ] 理解 Context Window / System Prompt / Messages
  - [ ] 了解 Temperature / Max Tokens 参数
  - [ ] 总结 Prompt vs Workflow vs Agent 的区别

### 模块 B｜Web3 基础（优先级 ⭐⭐⭐⭐⭐）

- [ ] **钱包创建与安全**
  - [ ] 创建 MetaMask 测试钱包
  - [ ] 理解 Address / Mnemonic / Private Key 差异
  - [ ] **⚠️ 绝不提交私钥/助记词到 GitHub!**

- [ ] **测试网交互**
  - [ ] 切换至 Sepolia 测试网
  - [ ] 领取测试币（Faucet）
  - [ ] 发送一笔测试交易
  - [ ] 在 Etherscan 记录 TX Hash / Gas / Block Number

- [ ] **智能合约体验**（加分项）
  - [ ] 用 Remix 部署最简单合约（Counter.sol）
  - [ ] 完成一次读取和一次写入操作

- [ ] **理论对比**
  - [ ] 理解 EOA vs 智能账户 vs 多签的差异

### 模块 C｜最小交叉实验（优先级 ⭐⭐⭐⭐）

- [ ] **选择一条链路完成**（三选一即可）：
  1. **AI Coding → 合约部署**: AI 生成合约代码 → 人工 Review → 部署到测试网
  2. **Agent Workflow → 钱包确认**: AI 生成交易计划 → 你确认参数 → 手动签名发送
  3. **治理助手 → 人工审核**: AI 分析提案 → 整理要点 → 公开记录

- [ ] **记录实验全流程**：
  - [ ] AI 输出了什么？
  - [ ] 人工复核了什么？
  - [ ] 钱包确认了什么？
  - [ ] 链上执行结果？
  - [ ] 区块浏览器验证链接

- [ ] **画出流程图**
  ```
  AI 生成 → 人工复核 → 钱包确认 → 链上执行 → 区块浏览器验证
  ```

---

## 📝 交付物检查

- [ ] Learning Agent / Coding Agent 配置记录 (`module-a/learning-agent-setup.md`)
- [ ] 模型/API 路径说明 (README 中注明)
- [ ] GitHub Repo 创建 + README + 至少 3 个 Commits
- [ ] 至少一次 agent 协助学习或编码日志 (`docs/learning-log.md`)
- [ ] 测试网交易哈希 + 区块浏览器链接 (`artifacts/tx-hashes.txt`)
- [ ] 最小交叉实验说明文档 (`module-c/experiment-log.md`)

---

## 🔐 安全守则（重要！）

**⚠️ NEVER COMMIT TO GITHUB:**
- ❌ 私钥 (Private Key)
- ❌ 助记词 (Mnemonic / Seed Phrase)  
- ❌ API Keys（可用 `.env` 文件+`.gitignore`）
- ❌ 密码 / Token

**✅ DO USE:**
- ✅ 测试网 (Sepolia, Goerli, Mumbai...)
- ✅ `.env` 环境变量
- ✅ Git ignore 敏感文件

---

## 🛠️ 技术栈

| 领域 | 工具 |
|------|------|
| **AI Agent** | Hermes Agent (当前), Claude Code, OpenAI Agents SDK |
| **区块链** | Ethereum, Sepolia Testnet |
| **钱包** | MetaMask |
| **开发工具** | Git, GitHub, Remix IDE |
| **区块浏览器** | Etherscan (Sepolia) |

---

## 📚 参考资源

### 模块 A｜AI 基础
- [What is a Large Language Model?](https://huggingface.co/course/chapter1/1)
- [Anthropic Claude API Docs](https://docs.anthropic.com/)
- [Hermes Agent Docs](https://hermes-agent.nousresearch.com/docs)
- [LangGraph Tutorial](https://langchain-ai.github.io/langgraph/)

### 模块 B｜Web3 基础
- [Ethereum Docs](https://ethereum.org/developers/docs/)
- [MetaMask Setup](https://metamask.io/download/)
- [Sepolia Faucet](https://sepoliafaucet.com/)
- [Remix IDE](https://remix.ethereum.org/)

### 模块 C｜交叉实验
- [AI x Web3 Best Practices](https://www.google.com/search?q=ai+web3+security+best+practices)
- [Safe Multisig Wallet](https://safe.global/)

---

## 🚦 进度追踪

### Week 1 完成进度

**模块 A | AI 基础**
- [x] 初始化项目 Repo + README
- [x] 完成 Learning Agent 配置记录
- [x] Prompt 库整理
- [x] Agent 生成 Demo: eth-checksum-cli.py, gas-price-checker.py
- [x] Prompt 参数实验记录
- [x] Day 1-3 打卡 (05-22)
- [x] Day 4-5 打卡 (05-23)

**模块 B | Web3 基础**
- [x] 合约已部署到 Sepolia 测试网 (TraceRecorder.sol)
- [x] 合约地址: `0xdA2E7bF7aD355562fb1faeAFa3B560337410651a`
- [x] 部署交易: `0x727688e97b6c4f7ae3223482e6fd9d81b27effa974b0f7d91dab4be370c22671`
- [x] 合约源码已归档至 artifacts/
- [x] 测试网交易记录文档
- [x] Gas 数据补充完成 (4 笔交易对比分析)

**模块 C | 最小交叉实验**
- [x] 完成 AI 生成合约 -> 人工复核 -> 钱包确认 -> 链上部署 -> 区块浏览器验证
- [x] 交叉实验文档已创建

### Next Steps
- [x] 合约读写验证记录 (已完成)
- [x] 模块 C 最小交叉实验 (已完成)
- Week 2: Deep Dive into Smart Contracts + Advanced AI Patterns

### Week 2 | 已完成
| 交付物 | 文件 | 状态 |
|--------|------|------|
| 问题地图 | week2/problem-map.md | done |
| 方向选择说明 | week2/direction-selection.md | done |
| 问题拆解 | week2/problem-decomposition.md | done |
| 初步 Proposal | week2/proposal-zkml.md | done |
| 参考资料 | week2/references.md | done |
| 主方向深挖包 | week2/deep-dive-package.md | done |
| 方向 backlog | week2/direction-backlog.md | done |
| Circom PoC | week2/artifacts/circom-poc/ | done |

### Week 3 | 已完成 ✅
| 任务 | 状态 |
|------|------|
| 缺口诊断 | done |
| 赛道对齐 (Z.AI) | done |
| 1 页 proposal memo | done |
| 深度研究 (EZKL/Circom/Halo2) | done |
| Risk memo | done |
| Hackathon 方向卡 | done |
| 组队 + 角色分工 | done |
| Repo skeleton + sprint plan | done |
| GLM API 集成调研 | done |
| Foundry 安装 + contracts 初始化 | done |

主方向: Privacy & Security -> ZKML 推理验证
目标赛道: Z.AI | Web3 x Long-Horizon Task
项目名: ZKML Pipeline Agent

---

## 💡 备注

ZKML 全链路 (训练->ONNX->电路->部署->推理->验证) 作为 Long-Horizon Task 天然对齐 Z.AI 赛道。
Week 3 目标: 把 proposal 收敛成 Week 4 可冲刺的 MVP 范围。
