Week 4 Day 1 学习笔记 | 2026-06-08

主方向: Privacy & Security -> ZKML 推理验证
赛道: Z.AI | Web3 x Long-Horizon Task
项目: ZKML Pipeline Agent

今日内容

项目全程踩坑复盘

整理了从 Week 2 到现在遇到的全部 15 个问题：

工具链/环境 (8)
  circom npm 装旧版 -> 从 GitHub 下新版 Rust 二进制
  circom pragma 版本体系混乱 -> 2.x 用 2.2.3
  signal private 语法废弃 -> circom2 默认 private
  Windows CRLF 换行符 -> sed 转 LF
  Foundry 管道安装被 Hermes 拦截 -> 直接下预编译 zip
  Foundry PATH 未持久化 -> 写入 .bashrc
  write_file 路径 /c/Users 解析异常 -> 用 C:/Users 绝对路径
  PowerShell env 与 bash export 不互通 -> 同终端 export 或 .env

安全教训 (1)
  API Key 明文贴聊天 -> 立即 revoke，只用环境变量注入

项目管理 (3)
  文档间 Groth16/Halo2 描述矛盾 -> 统一措辞
  README 状态与实际 3 处不一致 -> 交叉检查同步
  6/3-6/5 笔记只存聊天未落盘 -> 每次立即写文件

AI 辅助开发边界 (3)
  AI 无法判断业务逻辑 (如权限控制必要性)
  AI 审计误报率约 25%
  AI 对效率优化不敏感 (如冗余事件参数)

仍未解决 (4)
  EZKL Windows 兼容性
  GLM-5.1 API 联通测试 (卡在终端批准)
  Sepolia 测试币未领
  .env 实际文件未创建

明天推进
  GLM-5.1 API 联通 -> 模型训练 -> ONNX 导出 (Week 4 Day 1-2)
