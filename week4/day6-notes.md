# Week 4 Day 6 学习笔记 (2026-06-13)

## 完成事项

### 1. 合约地址确认 + 链上验证
- 最终合约: `0x75dBdd07fE81628c7aef5a8b48493Ebc200afD60`
- 部署 TX: `0x2d4c95903a7b2c8714754919216c97a60dedc005a81726eff1396d79fab93dec`
- 验证结果: verifyProof() = TRUE
- 淘汰旧合约 `0xE99F...` (Day 3, VK 不匹配)

### 2. run_demo.py 修复
- 编码: `.env` 含中文注释, `open()` 加 `encoding="utf-8"`
- PATH: PowerShell 找不到 cast/forge, 脚本顶部手动加 `~/.foundry/bin`
- 变量: `step_5_deploy()` 缺少 `pk = env.get("PRIVATE_KEY")`

### 3. Web UI (Flask + SSE)
- 双栏布局: 左侧 pipeline 日志 + 右侧项目信息
- SSE 实时推送每步结果
- 每步显示技术细节 (EZKL 版本/proof 大小/SRS 参数)
- 节奏停顿让 Demo 视频更长 (~8s)

### 4. 提交材料
- project/README.md 重写
- project/artifacts/verify-evidence.txt (新增)
- project/artifacts/risk-boundary.md (新增)
- 根 README.md Week 4 状态更新
- 清理临时文件 + 删除重复 Verifier.sol

### 5. Demo 录屏
- Web UI pipeline 全流程 + Etherscan 合约页面

---

## 踩坑记录

| 坑 | 原因 | 解决 |
|----|------|------|
| UnicodeDecodeError: gbk | .env 中文注释, Windows 默认 GBK | open(encoding="utf-8") |
| FileNotFoundError: cast | PowerShell PATH 不含 ~/.foundry/bin | 脚本顶部加 PATH |
| NameError: pk not defined | 只读了 RPC_URL 没读 PRIVATE_KEY | 补 pk = env.get("PRIVATE_KEY") |
| HTML JS 报错 | sed 替换 template literal 语法破坏 | 用 Python 做字符串替换 |

---

## 技术要点

### EZKL 全流程
gen_settings -> calibrate -> compile -> gen_srs -> setup -> gen_witness -> prove -> verify -> create_evm_verifier
- 9 步一次性跑完, VK 与 proof 绑定
- encode_evm_calldata() 生成 calldata, 不能手动 eth_abi.encode

### Flask SSE
```python
def stream():
    yield f"data: {json.dumps(event)}\n\n"
return Response(stream(), mimetype="text/event-stream")
```
前端 fetch + ReadableStream 逐行解析

### Foundry on Windows
- 二进制在 ~/.foundry/bin/ (cast.exe, forge.exe)
- 只在 git-bash PATH 中, PowerShell 不可见
