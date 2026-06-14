# AI x Web3 School 训练营 - Week 1 学习打卡

## 日期：2026-05-22 (Day 3)

---

## 一、今日完成的任务

### 1. Hermes Agent 配置与使用
- **环境**: Windows 桌面版 Hermes Agent
- **模型切换记录**:
  - qwen3.6-flash-2026-04-16（上午，遇到 API Key 401 错误，后修复）
  - qwen3.6-35b-a3b（下午）
  - qwen3.5-27b（下午 - 晚间主力模型）
  - glm-5.1（晚间 GitHub 推送阶段）
  - qwen3.6-plus-2026-04-02（当前）
- **工具链验证**: browser / search / terminal / file / session_search / delegate_task 等全部可用
- **Session 数量**: 今日约 33 个独立会话，累计数百次 tool call

### 2. Web3 基础任务回顾（专业课已完成，向 Agent 确认）
- **测试钱包**: MetaMask 已创建
  - 钱包地址: `0x147Fcf3EB8B9E305a5b4e16cbba90462F7126db9`
- **测试网**: Sepolia
  - 通过 faucet 领取过测试 ETH
  - 发送过测试交易
- **合约部署**: 使用 Remix IDE 连接 MetaMask 在 Sepolia 上部署过合约
- **区块浏览器**: 已在 Sepolia Etherscan 上验证过交易和合约

### 3. AI 工具实践
- 使用 ZhipuAI (智谱) Python SDK 跑过 API 调用测试
- 验证了 AI 生成代码 -> 人工复核 -> 本地运行的完整链路

### 4. Learning Agent 配置记录
- 确认当前 Hermes Agent 即为 Week 1 要求的 learning agent
- 记录了完整的配置信息（模型提供商、工具集、插件列表）
- 创建了实验报告和学习日志文档：
  - `ai-web3-training-week1-hermes-desktop-report.md`
  - `ai-web3-training-week1-hermes-learning-log.md`

### 5. GitHub Repo 管理
- Repo: https://github.com/Chichuzxy/ai-web3-training-week1
- 遇到问题: github.com HTTPS 连接不稳定，尝试通过 GitHub REST API 推送
- 状态: 报告文档已生成，待网络稳定后推送

---

## 二、今日学到的关键概念

### Agent vs Chatbot
- **Chatbot**: 只能输出文本，无外部操作能力
- **Agent**: 可以调用 tools (读文件、执行命令、搜索网络、操作浏览器等)，形成完整的"感知-决策-执行"循环

### Tool Use 机制
1. Plugin Discovery -> 发现可用工具
2. Register Providers -> 注册工具提供者
3. Tool Schema Injection -> 注入 schema 到 prompt
4. Model Returns Tool Call -> 模型决定使用哪个工具
5. Execute & Return Result -> 执行并返回结果
6. Iterate -> 根据结果继续对话或调用下一个工具

### 安全原则
- 私钥/助记词必须止步于人工，AI Agent 不能直接接触
- 所有链上操作必须在测试网进行
- 签名、转账、合约写入必须保留人工确认环节

---

## 三、遇到的问题与解决

| 问题 | 原因 | 解决方式 |
|------|------|----------|
| API 401 错误 | DashScope API Key 失效/过期 | 更换有效 API Key |
| GitHub 推送失败 | github.com HTTPS 连接不通 | 尝试 REST API 方式推送，待网络恢复 |
| 会话上下文丢失 | 新 session 无历史上下文 | 使用 session_search 回溯历史 |

---

## 四、交付物清单

- [x] Learning Agent 配置记录（本文档 + Hermes 实验报告）
- [x] GitHub Repo: https://github.com/Chichuzxy/ai-web3-training-week1
- [x] 测试网交易记录（钱包地址 + Sepolia 活动）
- [ ] 测试网交易哈希/合约地址截图（需从专业课本或 Etherscan 补充）
- [x] AI x Web3 交叉实验记录（ZhipuAI API 调用 -> 本地运行）
- [ ] 交叉实验完整链路文档（待完善）

---

## 五、明日计划

1. 确认 GitHub 推送状态，补充 repo 中的文档
2. 从 Etherscan 导出 Sepolia 交易记录和合约地址截图
3. 完成最小交叉实验的完整链路记录：
   - AI 生成 -> 人工复核 -> 钱包确认 -> 链上执行 -> 区块浏览器验证
4. 整理 Week 1 概念说明文档
5. 用自己话复述本周核心概念，请 Agent 审阅

---

## 六、今日统计

- **活跃时段**: 20:39 - 23:14 (约 2.5 小时)
- **会话数**: ~33 个
- **使用模型**: 5 个 (qwen3.6-flash, qwen3.6-35b, qwen3.5-27b, glm-5.1, qwen3.6-plus)
- **平台**: CLI (本地终端)
- **主要工具调用**: terminal, search_files, read_file, session_search, write_file, execute_code

---

*记录时间: 2026-05-22 23:14*
*记录方式: Hermes Agent 自动从 agent.log 和 session 历史中提取生成，人工确认后保存*
