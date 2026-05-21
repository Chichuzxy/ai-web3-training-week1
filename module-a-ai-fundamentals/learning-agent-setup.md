# 🤖 模块 A｜AI 基础：Learning Agent 配置记录

**更新日期:** May 21, 2026  
**学员:** Chichu

---

## 🎯 学习目标（模块 A）

理解 LLM 如何基于上下文生成；掌握上下文窗口、系统指令、提示词和工具调用的边界；学会用 AI coding/learning agent 完成实际任务。

### 核心概念速览
| 概念 | 作用 | 类比 Web3 |
|------|------|----------|
| **Context Window** | 模型能"记住"的最大 token 数 | 区块大小限制 |
| **System Prompt** | 设定 AI 的角色和行为准则 | 智能合约规则 |
| **Messages** | 对话历史（user/assistant/tool） | Transaction 记录 |
| **Temperature** | 控制输出的随机性 (0~2) | Gas Price - 越高越"激进" |
| **Max Tokens** | 单次回复的长度限制 | Block Gas Limit |

---

## 🔧 当前使用的 Agent 环境

### 1. Hermes Agent 配置（主开发环境）

```yaml
Provider: custom (Qwen3.5-122B-A10B)
Model: qwen3.5-122b-a10b
Base URL: [本地部署 / Custom Provider]
Mode: chat_completions

Toolsets Enabled:
  - terminal (执行 shell 命令)
  - file (读写文件)
  - browser (网页交互)
  - memory (持久化记忆)
  - skills (技能加载)
  - delegate_task (子代理委托)
```

**Hermes Home 路径:**
```
C:\Users\Administrator\AppData\Local\hermes
```

**配置文件位置:**
```
C:\Users\Administrator\AppData\Local\hermes\config.yaml
C:\Users\Administrator\AppData\Local\hermes\.env  # API Keys 只在这里
```

### 2. 其他可探索的 Agent 工具（后续对比学习）

| 工具 | 定位 | 适合场景 |
|------|------|---------|
| **Claude Code** | 代码专项 Agent | 复杂 refactoring、PR Review |
| **OpenAI Codex** | 编程助手 | 快速生成代码片段 |
| **LangGraph** | Workflow 编排 | 多步骤任务链 |
| **OpenAI Agents SDK** | Agent 框架 | 自定义 Agent 逻辑 |

---

## 📝 实战记录

### Task 1: 初始化训练营项目 Repo ✅

**目标:** 用 Agent 完成一个完整的 Git 项目初始化流程

**Prompt (输入给 Agent):**
```
帮我初始化第一个训练营项目的 Repo，就模块 A？
```

**Agent Actions:**
1. ✅ 搜索历史会话，确认"模块 A"的具体定义
2. ✅ 创建项目目录结构（6 个子目录）
3. ✅ 编写详细 README.md（包含任务清单、安全守则等）
4. ✅ 初始化 Git 仓库

**关键知识点:**
- Agent 会主动 `session_search` 来保持语境连贯
- 使用 `terminal` 工具执行真实命令
- 使用 `write_file` 创建内容文件
- 遇到不确定时会先 `clarify` 询问用户

**结果验证:**
```bash
cd ai-web3-training-week1
ls -la
# ✓ 看到 .git, README.md, module-a-ai-fundamentals/, 等
```

---

## 💬 典型 Prompt 模板（供参考）

### 概念解释类
```
请用通俗语言解释 [概念名]，并给我一个 Web3 或 AI 领域的实际例子。
最好有类比，让我更容易理解。
```

### 代码生成类
```
我需要写一个 [功能描述] 的代码。
要求：
- 可直接运行
- 附带关键注释
- 优先用测试网 / 本地环境
- 避免硬编码敏感信息
```

### 调试排错类
```
我遇到了以下错误：
[粘贴错误信息]

请帮我：
1. 分析可能的原因
2. 给出排查步骤
3. 提供修复方案
```

---

## 🔄 Agent 工作流观察（Hermes）

### 标准对话流程
```
用户输入 → Agent 接收 → 
  ↓
检查技能和上下文（是否需要加载 skill? 是否有相关记忆？）
  ↓
决定是否调用工具（terminal / file / browser / search...）
  ↓
工具返回结果 → Agent 处理 → 生成最终回复
  ↓
保存到 session DB → 未来可被 session_search 召回
```

### 工具使用优先级判断
根据 `AGENTS.md` 和项目经验：
1. **单个操作 + 无逻辑** → 直接用工具（如 `read_file`, `terminal`）
2. **3+ 步操作 + 中间处理** → 用 `execute_code`（Python 脚本批量处理）
3. **复杂推理 + 多分支** → 让 Agent 自己决定工具调用顺序
4. **耗时任务（>1 分钟）** → 用 `terminal(background=True)` 或 `delegate_task`

---

## ⚠️ 重要安全提醒

**AI Agent ≠ 自主操作钱包!**

| 可以自动化的 | 必须人工确认的 |
|-------------|---------------|
| 生成代码 / 脚本 | 私钥 / 助记词管理 |
| 解释交易含义 | 签名 / 授权操作 |
| 查询链上数据 | 转账 / 合约写入 |
| 整理学习日志 | 主网交互 |

**原则:** AI 输出 → 人工复核 → 钱包确认 → 链上执行 → 区块浏览器验证

---

## 📚 学习笔记

### Q: Prompt vs Workflow vs Agent，三者区别是什么？

**A:** 

| 层级 | 特点 | 示例 |
|------|------|------|
| **Prompt** | 单次请求，一次性回答 | "帮我写一个 Hello World 程序" |
| **Workflow** | 固定流程，按顺序执行多个步骤 | "先生成代码 → 再运行测试 → 最后写文档" |
| **Agent** | 自主决策，可根据情况选择工具 | "我要完成这个项目，先查文档，再写代码，遇到问题就搜索..." |

**类比 Web3:**
- **Prompt** = 一次简单的转账交易
- **Workflow** = 一个固定的 Smart Contract 调用链
- **Agent** = DAO（可以自主决策、调用各种工具）

---

## 🎯 下一步行动

- [ ] 尝试让 Agent 生成一个小工具（CLI 或网页）
- [ ] 记录不同 Temperature 参数对输出质量的影响
- [ ] 对比 Hermes Agent vs Claude Code 在同一个任务上的表现
- [ ] 整理自己的 Prompt Library（存到 `prompts-library.md`）

---

**最后更新:** May 21, 2026  
**维护者:** Chichu
