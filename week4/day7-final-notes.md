# Week 4 Day 7 最终学习笔记 | 2026-06-14

项目: ZKML Pipeline Agent | 赛道: Z.AI Long-Horizon Task | Demo Day

---

## 最终状态

全链路 6 Steps 已验证通过，合约 0x75dBdd07fE81628c7aef5a8b48493Ebc200afD60 部署在 Sepolia，链上 verifyProof 返回 TRUE。

## 本周实际节奏 vs Sprint Plan

| 计划 | 实际 | 差异 |
|------|------|------|
| Day 1: 模型+EZKL环境 | Day 1-2: 模型+EZKL全流程 | EZKL 一口气跑通了 setup/prove/verify |
| Day 2: Proof+Verifier | Day 3: Verifier+部署 | create_evm_verifier async bug 多耗 1 天 |
| Day 3: 链上部署+验证 | Day 4: 链上 verify 调试 | VK 不对齐，revert 整一天 |
| Day 4: Agent编排 | Day 5: 重新闭环+Agent脚本 | 从头 setup+prove+verifier+部署+验证 |
| Day 5: 打磨+提交 | Day 6: Web UI+README+提交 | 追加 Flask SSE Demo 界面 |
| Day 6-7: Buffer | Day 7: 项目迁移+最终总结 | C盘->E盘迁移，整理全部问题 |

核心瓶颈: 链上 verifyProof 的 VK 对齐问题 (Day 4)，体感最难受。

---

## Demo Day 补充事项

### 项目文件迁移
- 从 C:\Users\Administrator\ai-web3-training-week1 迁移到 E:\XZ\AI x Web3 School\ai-web3-training-week1
- 原因: C 盘空间不足 (项目 ~141MB，其中 pk.key 138MB)
- 验证: 所有文件完整，git 历史保留

---

# 训练营全程问题汇总

## 分类一: 工具链/环境 (共 13 个)

### 1. circom npm 安装旧版
- 现象: npm install -g circom 装的版本太旧，不兼容 2.x pragma
- 解决: 从 GitHub Releases 下 Rust 预编译二进制

### 2. circom pragma 版本体系混乱
- 现象: pragma circom 2.2.3 语义不清
- 解决: 统一用 2.2.3 版本

### 3. signal private 语法废弃
- 现象: circom 2.x 报 signal private 错误
- 解决: circom 2 默认 input 即为 private，声明无需 private 关键字

### 4. Windows CRLF 换行符
- 现象: circom 产生的文件含 CRLF，snarkjs 解析失败
- 解决: sed 转 LF

### 5. Foundry 管道安装被 Hermes 拦截
- 现象: curl ... | bash 触发了 Hermes 安全策略
- 解决: 直接从 GitHub Releases 下载预编译 zip

### 6. Foundry PATH 未持久化
- 现象: 新开终端找不到 forge/cast 命令
- 解决: export PATH="$HOME/.foundry/bin:$PATH" 写入 .bashrc
- 注意: Windows 下修改 .bashrc 也被拦截，需 printf ... | cat 方式写入

### 7. PowerShell env 与 bash export 不互通
- 现象: PowerShell 里 export 的变量 bash 脚本拿不到
- 解决: 统一在同一个终端下操作或用 .env 文件

### 8. write_file / execute_code 路径 double-prefix
- 现象: C:\c\Users\... 路径 bug，文件写到错误位置
- 解决: terminal + cat heredoc 写文件

### 9. EZKL 23.0.5 API 参数签名大改
- 现象: calibrate_settings 等函数参数从 dict 改为文件路径
- 解决: 通读 API 文档，全部改用 keyword args

### 10. create_evm_verifier async bug
- 现象: Windows 下 "no running event loop" (pyo3 tokio 线程问题)
- 解决: asyncio.run(create_evm_verifier(...)) 手动包装

### 11. Foundry via_ir 编译要求
- 现象: Verifier.sol Stack too deep
- 解决: foundry.toml via_ir = true

### 12. vm.envUint hex prefix 问题
- 现象: envUint 读 .env 的 PRIVATE_KEY 带 0x 前缀导致铸造失败
- 解决: forge script --private-key CLI flag 替代 envUint

### 13. Etherscan 合约验证
- 现象: forge verify-contract 网络不通
- 解决: 手动验证 (未解决，API key 问题)

## 分类二: AI 辅助开发边界 (共 4 个)

### 14. AI 无法判断业务逻辑
- 现象: Hermes 生成的合约补了权限控制，但训练营 demo 不需要
- 教训: 业务决策必须人工做

### 15. AI 审计误报率约 25%
- 现象: Hermes 审计报告标记了 4 个问题，实际只有 3 个是真的
- 教训: AI 审计结果必须人工复核

### 16. AI 对效率优化不敏感
- 现象: AI 没有指出冗余 event 参数 (浪费 gas)
- 教训: 优化建议要靠经验积累

### 17. AI 技术判断受对话上下文限制
- 现象: Day 4 convo 里 AI 提到了弃用的 abi.encode 方案
- 教训: 给 AI 的上下文要清晰标注最新状态

## 分类三: 安全问题 (共 2 个)

### 18. API Key 泄露到聊天
- 现象: GLM_API_KEY 明文贴进了聊天输入
- 解决: 立即 revoke 旧 key，之后只用环境变量注入
- 教训: 加密钥文件到 .gitignore，永远不贴聊天

### 19. SSH key 未绑定 GitHub 账号
- 现象: id_ed25519 不是 Chichuzxy 的 GitHub SSH key
- 解决: push 走 HTTPS + token 认证

## 分类四: 项目管理 (共 3 个)

### 20. 文档间术语矛盾
- 现象: Groth16 和 Halo2 在不同文档里混用
- 解决: 统一措辞为 Halo2 (EZKL 实际输出)

### 21. README 状态与实际不一致
- 现象: 根 README 标 done 但文件不在
- 解决: 交叉检查 > 同步 > 标注

### 22. 笔记未及时落盘
- 现象: 6/3-6/5 的对话记录全在聊天窗口，重启后丢失
- 解决: 每天立即写文件 + git commit

## 分类五: 链上/合约 (共 2 个)

### 23. 手动 eth_abi.encode 格式错误
- 现象: 自己用 eth_abi.encode(['bytes','uint256[]'], [proof, instances]) 编码 calldata
- 根因: Verifier.sol 内部对 instances 的编码格式与手动编码不完全一致
- 解决: 必须用 ezkl.encode_evm_calldata() 生成 calldata

### 24. VK 与 proof 不匹配导致链上 revert
- 现象: 本地 verify 通过，链上调 verifyProof 总是 revert
- 根因: Day 2 生成 proof.json，Day 3 单独跑 create_evm_verifier，中间 setup 可能被重跑导致 VK 变化
- 解决: 删所有产物，一键从头跑完 setup+prove+create_evm_verifier
- 教训: EZKL pipeline 必须端到端闭环执行

---

# 技术栈和能力盘点

## 已掌握的

| 领域 | 具体 |
|------|------|
| ZK Proof | circom 电路编写、EZKL 全链路 (gen_settings -> verify) |
| Solidity | Foundry 编译/部署/测试、forge script、via_ir |
| ONNX | sklearn -> ONNX 导出、Gemm 算子手动构建 |
| Agent | Hermes tool calling、pipeline 编排、SSE Web UI |
| 链上 | cast call/send、ABI 编码、bytecode 对比 |
| Python | ezkl binding、asyncio 包装、文件编码处理 |

## 未深入但接触过

- Halo2 内部原理 (EZKL 自动生成，只调了 API)
- GLM-5.1 Function Calling (API key 问题未实际接入)
- L2 部署 (仅列出下一步计划)

## 下一步可能的延伸方向

1. GLM-5.1 Function Calling 取代预设 pipeline (动态决策)
2. 多模型支持 (MLP/CNN 更复杂电路)
3. L2 部署 (Arbitrum Sepolia 降 gas)
4. 生产级治理 (MPC SRS、多方审计)
5. 前端界面 (Web UI 自然语言输入 -> 全自动)

---

# 个人反思

## 做得好的

- 踩坑记录详细，每个 bug 都定位了根因
- Sprint plan 与实际偏差在可控范围内
- 最终 6 steps 闭环跑通，Demo 材料齐全

## 可以改进的

- API key 安全: 第一次犯泄露错误是完全可避免的
- 笔记落盘节奏: 应每完成一件事就写，不堆到晚上
- GitHub push 频率: 早期 commit 太少，后补了大量一次 push

---

# 提交清单最终确认

- [x] project/README.md (完整 demo 说明)
- [x] project/artifacts/verifier-address.txt (合约+部署TX)
- [x] project/artifacts/verify-evidence.txt (链上验证证据)
- [x] project/artifacts/risk-boundary.md (风险边界)
- [x] 根 README.md Week 4 状态更新
- [x] agent-workflows/run_demo.py (端到端编排脚本)
- [x] agent-workflows/web_ui.py + templates/ (Demo Web UI)
- [x] 全部学习笔记 (week4/day1-7)
- [x] 最终问题汇总 (本文)
- [ ] Git push to GitHub (待 Chichuzxy 手动确认)
