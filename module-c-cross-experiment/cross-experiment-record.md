# 最小交叉实验记录

**实验人:** Chichu  
**日期:** 2026-05-24  
**实验目标:** 跑通 "AI 生成 -> 人工复核 -> 钱包确认 -> 链上执行 -> 区块浏览器验证" 完整链路

---

## 实验链路

### 第 1 步: AI 生成

- **工具:** Hermes Agent (AI 队友)
- **任务:** 让 AI 生成一个最小可部署的 Solidity 合约 (TraceRecorder)
- **AI 输出:** `artifacts/TraceRecorder.sol` -- 一个包含状态变量读写和事件记录的练习合约
- **AI 角色:** 辅助编写合约代码、解释 Solidity 语法、整理项目结构

### 第 2 步: 人工复核

- **复核内容:**
  - [x] 检查合约代码逻辑是否正确 (setValue/setMessage/readAll)
  - [x] 确认构造函数参数: initValue=0, initMessage="TraceRecorder initialized"
  - [x] 确认无权限漏洞 (本合约设计为开放调用, 适合学习)
  - [x] 确认未暴露私钥或助记词
- **复核结论:** 代码符合预期, 可以在测试网部署

### 第 3 步: 钱包确认

- **工具:** MetaMask (浏览器扩展钱包)
- **操作:** 通过 Remix IDE 连接 MetaMask, 选择 Sepolia 测试网
- **确认内容:**
  - [x] 确认部署网络为 Sepolia (非主网)
  - [x] 确认 Gas 费用合理
  - [x] MetaMask 弹窗中点击确认, 完成签名

### 第 4 步: 链上执行

- **合约地址:** `0xdA2E7bF7aD355562fb1faeAFa3B560337410651a`
- **部署交易哈希:** `0x727688e97b6c4f7ae3223482e6fd9d81b27effa974b0f7d91dab4be370c22671`
- **网络:** Sepolia Testnet
- **状态:** 部署成功

### 第 5 步: 区块浏览器验证

- **Etherscan 合约页面:** https://sepolia.etherscan.io/address/0xdA2E7bF7aD355562fb1faeAFa3B560337410651a
- **Etherscan 交易页面:** https://sepolia.etherscan.io/tx/0x727688e97b6c4f7ae3223482e6fd9d81b27effa974b0f7d91dab4be370c22671
- **验证结果:** 合约已成功部署, 可在浏览器中查看源码和交易详情

---

## 实验总结

### 链路跑通情况

| 环节 | 状态 | 说明 |
|------|------|------|
| AI 生成 | 完成 | Hermes Agent 生成 TraceRecorder 合约代码 |
| 人工复核 | 完成 | 检查代码逻辑、参数、安全性 |
| 钱包确认 | 完成 | MetaMask 签名确认部署交易 |
| 链上执行 | 完成 | 合约部署到 Sepolia 测试网 |
| 区块浏览器验证 | 完成 | Etherscan 可查证合约和交易 |

### 关键收获

1. **AI 的角色是辅助, 不是替代:** AI 负责写代码和解释, 但签名和确认必须由人完成
2. **私钥安全是底线:** 整个流程中 AI 从未接触私钥, MetaMask 独立管理密钥
3. **测试网是必经之路:** 所有操作在 Sepolia 完成, 零成本验证流程
4. **区块浏览器是真相来源:** 链上数据可在 Etherscan 独立验证, 不依赖任何一方说法

### 边界与风险

- 本合约无权限控制, 不适合生产环境
- AI 生成的合约仍需人工审计, 不能完全信任
- 当前实验为单次部署, 未覆盖合约升级、交互等复杂场景
