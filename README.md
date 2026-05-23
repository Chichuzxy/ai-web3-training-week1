# 🚀 AI x Web3 School - Week 1 Training Project

**学员:** Chichu  
**周次:** Week 1｜AI 与 Web3 基础知识  
**开始日期:** May 21, 2026

---

## 📋 本周目标

建立 AI × Web3 的共同语言 + 第一轮真实操作能力。

重点不是把 AI 和 Web3 各自讲成完整大课，而是完成：
- ✅ AI 工具实践
- ✅ 测试网交互  
- ✅ 最小 AI × Web3 交叉实验
- ✅ 知道哪些动作可以自动化、哪些必须人工确认

---

## 📁 项目结构

```
ai-web3-training-week1/
├── module-a-ai-fundamentals/    # 模块 A｜AI 基础：从 LLM 到 Agent Workflow
│   ├── learning-agent-setup.md  # Learning Agent 配置记录
│   ├── prompts-library.md       # Prompt 库（常用提示词模板）
│   └── demo/                    # Agent 生成的 Demo 项目
├── module-b-web3-fundamentals/  # 模块 B｜Web3 基础：账户、钱包、签名与链上执行
│   ├── wallet-setup.md          # 钱包创建说明
│   ├── testnet-tx-record.md     # 测试网交易记录
│   └── smart-contract-demo/     # 简单合约示例
├── module-c-cross-experiment/   # 模块 C｜最小交叉实验：AI 输出到链上执行
│   ├── workflow-diagram.md      # 流程图（AI→人工复核→钱包确认→链上执行）
│   └── experiment-log.md        # 实验过程记录
├── docs/                        # 学习笔记和概念卡片
│   ├── concepts.md              # 核心概念速记
│   └── glossary.md              # 术语表
├── artifacts/                   # Proof of Work 证据
│   ├── screenshots/             # 截图证明
│   └── tx-hashes.txt            # 交易哈希汇总
└── README.md                    # 本项目说明（本文件）
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

### Today (May 21, 2026)
- [x] 初始化项目 Repo
- [x] 完成模块 A 的 Learning Agent 配置
- [ ] 完成模块 B 的钱包创建和测试网交易
  - [x] 合约已部署到 Sepolia 测试网
  - [x] 记录合约地址: `0xc56a...7948`
  - [x] 记录部署交易: `0xf414...f937`
  - [ ] 补充合约源码和读写验证
- [ ] 设计并完成模块 C 的最小交叉实验

### Next Steps
- Week 2: Deep Dive into Smart Contracts + Advanced AI Patterns
- Week 3: Building Real AI × Web3 Applications
- Week 4: Final Project Showcase

---

## 💡 队友备注

这是 Chichu 的第一个训练营项目，主要用于：
1. 记录 AI Agent 使用经验
2. 积累 Web3 开发技能  
3. 完成每周的 proof-of-work 交付
4. 为后续更复杂的项目打基础

**下一步行动建议：**
- 先跑通模块 A 的 Learning Agent 设置
- 然后做模块 B 的基础实操（这个最重要！）
- 最后尝试模块 C 的交叉实验

有问题随时喊我！一起搞定这周的任务 🤝
