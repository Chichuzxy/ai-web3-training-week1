# Module A | AI Patterns

**从 LLM 到 Agent Workflow + Tool Use 的进阶之路**

---

## 学习路线

### Part 1: Prompt Engineering 系统化
- [ ] Context Window / System Prompt / Messages 深度理解
- [ ] Temperature / Top-p / Max Tokens 调参实验
- [ ] Few-shot vs Zero-shot 对比
- [ ] Structured Output (JSON Schema)

### Part 2: Agent Workflow
- [ ] ReAct Pattern (Reasoning + Acting)
- [ ] Plan-and-Solve
- [ ] Multi-Agent 架构模式
- [ ] Hermes Agent 配置实战

### Part 3: Tool Use
- [ ] Tool Definition Schema
- [ ] Function Calling 完整流程
- [ ] Error Handling + Retry Logic
- [ ] Chaining Tools for Complex Tasks

---

## 问题地图 (Problem Map)

以下是我从 Week 1 实践过程中遇到的问题和思考，整理成这张地图作为后续学习的指引。

### 认知盲区层
| 问题 | 来源 | 解决方向 |
|------|------|----------|
| 为什么 Gas Price 会波动？测试网和主网的区别是什么？ | week1 Gas 数据记录 | 了解 EIP-1559、Base Fee、Priority Fee |
| Prompt 长度影响什么？什么时候需要 split context？ | prompt-parameter-experiments.md | Context Window 管理策略 |
| AI 生成的合约代码真的安全吗？怎么验证？ | cross-experiment-record.md | 智能合约审计基础 |

### 技能缺口层
| 缺口 | 优先级 | 学习计划 |
|------|--------|----------|
| Foundry 工作流 | P0 | 搭建 Foundry 环境，写第一个测试 |
| OpenZeppelin 标准库 | P0 | 实现一个 ERC20 代币合约 |
| RAG 入门 | P1 | 用 embedding 做简单文档检索 |
| Chainlink Oracle | P1 | 链下数据上链的实践 |

### 工程实践层
| 实践项 | 当前状态 | 下一步 |
|--------|----------|--------|
| CI/CD for smart contracts | 未开始 | GitHub Actions + Hardhat/Foundry tests |
| Git flow for repos | 基础 commit/push | Branch strategy + PR workflow |
| Logging & Observability | 无 | 合约事件日志 + 前端查询 |

---

## 参考资源

- [Anthropic Claude API Documentation](https://docs.anthropic.com/)
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
- [LangGraph Tutorial](https://langchain-ai.github.io/langgraph/)
- [Solidity by Example](https://solidity-by-example.org/)
- [SWC Registry (Smart Contract Weakness Classification)](https://swcregistry.io/)
