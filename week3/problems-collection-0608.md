# 踩坑合集 | 学习笔记 | 2026-06-08

项目全程遇到的问题和解决方案，按发生顺序整理。

---

## 一、工具链/环境类

### 1. Circom npm 装的是旧版 (Week 2)

`npm install -g circom` 装的是 circom1 (JS实现)，编译 circom2 代码报 Parse error。
解决：从 GitHub Releases 下载 circom2 v2.2.3 Rust 可执行文件。
教训：工具链第一步确认版本，npm 不一定是新版。

### 2. Circom pragma 版本号不对 (Week 2)

`pragma circom 0.5.46` 在 circom2.2.3 上报错。0.5.46 是 circom1 的版本体系。
解决：改为 `pragma circom 2.2.3`。

### 3. `signal private input` 语法已废弃 (Week 2)

circom2 中 `private` 不再是关键字。
解决：改为 `signal input a` —— input 默认就是 private。

### 4. Windows CRLF 换行符 (Week 2)

circom 解析器不认 `\r\n`，编译报错。
解决：`sed -i 's/\r$//' file.circom`，编辑器保存为 LF。

### 5. Foundry 安装被拦截 3 天 (Week 3, 6/4 - 6/5)

三道关卡：
- PowerShell `curl -L \| bash` 语法不兼容
- `irm` 官方脚本路径 404
- Hermes 安全策略拦截所有管道下载 (curl ... | bash)，分步下载 foundryup.sh 也不行

最终绕过：直接从 GitHub Releases 下载 Windows 预编译 zip (foundry_v1.7.1_win32_amd64.zip, 79MB)，解压出 forge.exe / cast.exe / anvil.exe / chisel.exe。

教训：Windows + Hermes 代理环境，管道安装大概率被拦。优选预编译二进制直接下载。

### 6. Foundry PATH 未持久化 (Week 3, 6/6)

装了但新终端找不到 forge。
解决：`export PATH="$HOME/.foundry/bin:$PATH"` 写入 .bashrc。

### 7. write_file 路径解析 bug (Week 3, 6/5)

相对路径 `/c/Users/...` 被解析成 `C:\c\Users\...`。
解决：一律用绝对路径 `C:/Users/...`。

### 8. 跨终端环境变量不互通 (Week 3, 6/7)

PowerShell 设 `$env:ZAI_API_KEY` 后，bash 终端里读不到。反过来 bash 的 `export` 在 PowerShell 中报 CommandNotFoundException。
解决：在同一个 bash 终端内 export，或用 .env + python-dotenv。

---

## 二、安全类

### 9. API Key 明文泄露 (Week 3, 6/7)

用户在聊天中两次明文贴出真实 API Key (Z.AI + 智谱)。
后果：Key 已暴露，需立即去后台 revoke 并重新生成。
教训：API Key 一律用环境变量注入，不硬编码、不贴聊天、不进 git。

---

## 三、项目管理类

### 10. 文档间描述矛盾 (Week 2)

problem-decomposition.md 写 Groth16，proposal-zkml.md 写 Halo2，互相矛盾。
解决：明确分工 —— PoC 用 Groth16 (Circom+SnarkJS)，生产用 Halo2 (EZKL)。所有文档统一措辞。

### 11. README 状态与实际不一致 (Week 3, 6/6)

week3/README 有 3 处过时标记：Foundry 标"未完成"(实际已装)、GLM API 标"未完成"(文件已写)、组队标"待确认"(已完成)。
解决：逐一交叉检查后同步。

### 12. 笔记只存聊天未落盘 (Week 3)

6/3、6/4、6/5 的学习笔记只在聊天中口述，未写入 week3/ 下的 md 文件。6/6 开始补充落盘。
教训：笔记立即落盘，不依赖聊天回查。

---

## 四、AI 辅助开发的边界

### 13. AI 对业务逻辑判断困难 (Week 2)

AI 建议加 onlyOwner，但 TraceRecorder 是"开放记录本"，不需要权限控制。
教训：AI 给技术建议，最终决策需人理解业务。

### 14. AI 审计误报率高 (Week 2)

4 个 AI 发现中 3 个有实际价值，1 个是低优先级。
教训：AI 审计是"发现"不是"诊断"，需人工过滤。

### 15. AI 对效率优化不够敏感 (Week 2)

AI 没发现事件参数中 oldMessage(string) 的冗余。
教训：AI 习惯"功能正确"判断，对"效率优化"不敏感。

---

## 五、当前仍未解决的

- EZKL Windows 兼容性未验证（计划 Colab 跑）
- GLM-5.1 API 联通测试未跑（待终端批准）
- Sepolia 测试币未领
- .env 实际文件未创建（只有 .env.example）
