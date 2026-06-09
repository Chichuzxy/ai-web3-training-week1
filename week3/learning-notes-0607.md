Week 3 学习笔记 | 2026-06-07

主方向: Privacy & Security -> ZKML 推理验证
目标赛道: Z.AI | Web3 x Long-Horizon Task
项目: ZKML Pipeline Agent

今日完成

- Week 3 交付物全面审计
  交叉检查根 README、week3/README 与实际文件，确认 10 项全部交付
  proposal-memo / deep-research / hackathon-card / team / glm-api-plan / sprint-plan / .env.example / contracts 全在
  Foundry forge 1.7.1，contracts 编译 + 2 tests passed

- Z.AI API Key 安全事件
  用户两次在聊天中明文贴出真实 API Key
  后果: Key 已泄露，需立即 revoke
  已指导用户前往 z.ai 后台 rotate 并重新生成
  教训: API Key 用环境变量注入，绝不硬编码进代码或聊天

- Z.AI API 环境准备
  gl-api-plan.md 中选定的接入方式: OpenAI 兼容 SDK
  base_url: https://api.z.ai/api/paas/v4/
  模型: glm-5.1
  确认 openai Python 包已安装
  终端环境变量问题: PowerShell 的 $env: 与 bash 的 export 不互通
  API 联通测试待终端批准后执行

环境坑位记录

- Windows 下终端工具跑 bash (git-bash/MSYS)，PowerShell 环境变量不传递
- 方案: 在 bash 终端里 export，或用 .env 文件 + python-dotenv

Week 4 就绪状态

已就绪: proposal / 赛道对齐 / sprint plan / glm-api-plan / team / Foundry / .env.example
待完成: Z.AI Key 环境变量注入 + API 联通确认

明天 Week 4 Day 1 第一件事: 跑通 GLM-5.1 function calling -> 训练模型 -> ONNX 导出
