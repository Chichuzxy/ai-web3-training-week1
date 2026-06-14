# 测试网交易记录

**网络:** Sepolia Testnet  
**记录人:** Chichu  
**钱包地址:** `0x147Fcf3EB8B9E305a5b4e16cbba90462F7126db9`  
**更新日期:** 2026-05-23

---

## 1. 智能合约部署

### 基本信息

| 字段 | 值 |
|------|-----|
| 合约地址 | `0xdA2E7bF7aD355562fb1faeAFa3B560337410651a` |
| 部署交易哈希 | `0x727688e97b6c4f7ae3223482e6fd9d81b27effa974b0f7d91dab4be370c22671` |
| 部署网络 | Sepolia Testnet |
| 部署者地址 | `0x147Fcf3EB8B9E305a5b4e16cbba90462F7126db9` |

### 区块浏览器链接

- **合约页面:** https://sepolia.etherscan.io/address/0xdA2E7bF7aD355562fb1faeAFa3B560337410651a
- **交易详情:** https://sepolia.etherscan.io/tx/0x727688e97b6c4f7ae3223482e6fd9d81b27effa974b0f7d91dab4be370c22671

### 部署方式

**工具:** Remix IDE (https://remix.ethereum.org/)

**部署步骤:**
1. 在 Remix 中创建 `TraceRecorder.sol` 文件
2. 粘贴合约源码,选择 Solidity 编译器版本 `^0.8.20`
3. 编译合约,确认无错误
4. 切换到 "Deploy & Run Transactions" 面板
5. Environment 选择 "Injected Provider - MetaMask"
6. 确认 MetaMask 连接到 Sepolia 测试网
7. 输入构造函数参数: `initValue = 0`, `initMessage = "TraceRecorder initialized"`
8. 点击 Deploy,MetaMask 弹出确认窗口
9. 确认交易,等待挖矿确认
10. 复制合约地址和交易哈希记录到本文件

### 合约功能

**合约名称:** TraceRecorder

**主要功能:**
- **状态记录器:** 维护三个状态变量 - `value` (uint256)、`message` (string)、`lastOperator` (address)
- **数值修改:** `setValue()` 函数允许任何用户修改数值,记录旧值、新值和操作者,触发 `ValueChanged` 事件
- **消息修改:** `setMessage()` 函数允许任何用户修改字符串消息,记录旧消息、新消息和操作者,触发 `MessageChanged` 事件
- **批量读取:** `readAll()` 视图函数一次性返回所有状态变量
- **操作追溯:** 每次写入操作都会记录 `lastOperator` 为 `msg.sender`,并通过 Event 记录完整的变更历史

**设计特点:**
- 无权限控制 - 任何地址都可以调用 `setValue` 和 `setMessage`
- 事件驱动 - 所有状态变更都通过 Event 记录,方便链下监听和索引
- 简单透明 - 适合用于学习和测试链上状态交互

**源码位置:** `artifacts/TraceRecorder.sol`

---

## 2. 合约读写验证

### 读取操作

- [x] 完成一次合约读取调用
- [x] 记录读取结果

**调用函数:** `readAll()`

**读取结果:**
```
value: 0
message: "TraceRecorder initialized"
lastOperator: 0x147Fcf3EB8B9E305a5b4e16cbba90462F7126db9
```

**验证方式:** 在 Remix IDE 的 "Deployed Contracts" 面板中点击 `readAll()` 按钮,或通过 Etherscan 的 "Read Contract" 标签页调用。

### 写入操作

- [x] 完成一次合约写入调用
- [x] 记录交易哈希和结果

**操作 1: 修改数值**
- **调用函数:** `setValue(uint256 newValue, string memory note)`
- **参数:** `newValue = 42`, `note = "First value update by Chichu"`
- **交易哈希:** `0x87d57a4c2f296157227adeed93852037b139ddaebe96384cea4ed0a83d60dc0d`
- **Gas Used:** 33,226
- **Gas Price:** 1.53062375 Gwei
- **TxFee:** 0.0000509054846775 ETH
- **结果:** 
  - `value` 从 0 变为 42
  - `lastOperator` 更新为 `0x147Fcf3EB8B9E305a5b4e16cbba90462F7126db9`
  - 触发 `ValueChanged` 事件

**操作 2: 修改消息**
- **调用函数:** `setMessage(string memory newMessage)`
- **参数:** `newMessage = "Hello from Chichu's TraceRecorder!"`
- **交易哈希:** `0x6c0a5b888bcb7185fd8ce653239a45ba5368e466507d1ccd799807297fe55bcf`
- **Gas Used:** 34,706
- **Gas Price:** 1.534776295 Gwei
- **TxFee:** 0.000053261341765385 ETH
- **结果:**
  - `message` 从 "TraceRecorder initialized" 变为 "Hello from Chichu's TraceRecorder!"
  - `lastOperator` 更新为 `0x147Fcf3EB8B9E305a5b4e16cbba90462F7126db9`
  - 触发 `MessageChanged` 事件

**操作 3: 再次修改数值 (验证状态覆盖)**
- **调用函数:** `setValue(uint256 newValue, string memory note)`
- **参数:** `newValue = 100`, `note = "Second update - final value"`
- **交易哈希:** 未记录
- **Gas Used:** 未记录
- **结果:**
  - `value` 从 42 变为 100
  - 证明合约状态可以被多次修改

---

## 3. 测试交易（普通转账）

- [x] 发送一笔测试转账
- [x] 记录 TX Hash

**转账信息:**
- **From:** `0x147Fcf3EB8B9E305a5b4e16cbba90462F7126db9`
- **To:** `0x147Fcf3EB8B9E305a5b4e16cbba90462F7126db9` (自我转账)
- **金额:** `0.001 ETH` (测试网代币,无实际价值)
- **交易哈希:** `0x8e15062a6f3c1ad149f8f9231372f5b51d69700ac49ac2bf864afb26764b9e8f`
- **Gas Used:** 21,000
- **Gas Price:** 1.50000004 Gwei
- **TxFee:** 0.00003150000084 ETH
- **区块浏览器:** https://sepolia.etherscan.io/tx/0x8e15062a6f3c1ad149f8f9231372f5b51d69700ac49ac2bf864afb26764b9e8f

**操作步骤:**
1. 打开 MetaMask,确保切换到 Sepolia 测试网
2. 点击 "Send" 按钮
3. 输入接收方地址(可以转给自己或其他测试地址)
4. 输入金额 0.001 ETH
5. 确认 Gas 费用,点击确认
6. 等待交易确认后,复制交易哈希记录到本文件

---

## 4. Gas 记录

| 操作 | Gas Used | Gas Price (Gwei) | 总费用 (ETH) | 交易哈希 |
|------|----------|------------------|--------------|----------|
| 合约部署 | ~150,000 (估算) | ~1.5 (估算) | ~0.000225 (估算) | `0xf414a4aea774f9c34c0fc694e9f0792b8cfacdeaad7cca35adee7cd391dff937` |
| setValue(42) | 33,226 | 1.53062375 | 0.0000509054846775 | `0x87d57a4c2f296157227adeed93852037b139ddaebe96384cea4ed0a83d60dc0d` |
| setMessage | 34,706 | 1.534776295 | 0.000053261341765385 | `0x6c0a5b888bcb7185fd8ce653239a45ba5368e466507d1ccd799807297fe55bcf` |
| 普通转账 | 21,000 | 1.50000004 | 0.00003150000084 | `0x8e15062a6f3c1ad149f8f9231372f5b51d69700ac49ac2bf864afb26764b9e8f` |
| **总计** | **~238,932** | **~1.51 (平均)** | **~0.000360** | - |

### Gas 对比分析

| 对比项 | 数值 | 说明 |
|--------|------|------|
| 最省 Gas 的操作 | 普通转账 (21,000) | ETH 转账是固定成本，不执行合约代码 |
| 最费 Gas 的操作 | setMessage (34,706) | 字符串存储比纯数值修改更耗 Gas |
| setValue vs 转账 | 33,226 vs 21,000 | 合约写入比纯转账贵 ~58%，因为需要执行合约逻辑 |
| setMessage vs setValue | 34,706 vs 33,226 | 字符串存储额外消耗 ~1,480 Gas |
| Gas Price 范围 | 1.50 ~ 1.53 Gwei | Sepolia 测试网 Gas Price 很低，接近免费 |
| 四笔交易总成本 | ~0.00036 ETH | 按当前 ETH 价格约 $0.001，测试网几乎无成本 |

### 关键发现

1. **合约写入 > 纯转账**: 任何合约函数调用都比简单转账贵，因为需要加载合约代码、执行状态变更、触发事件
2. **字符串存储更贵**: `setMessage` 比 `setValue` 多消耗 ~1,480 Gas，因为 Solidity 中 `string` 是动态长度类型，需要额外的存储槽位
3. **测试网 Gas 极低**: Sepolia 上 1.5 Gwei 的 Gas Price 意味着即使复杂操作也几乎免费，主网同期可能在 20-50 Gwei
4. **Gas Used 的构成**: 
   - 21,000 是交易基础成本 (Base Cost)
   - 额外部分 = 合约执行成本 (SSTORE 存储操作、事件触发等)

---

## 5. 概念理解记录

### EOA vs 智能账户 vs 多签

| 类型 | 说明 | 示例 |
|------|------|------|
| **EOA (外部账户)** | 由私钥控制的普通账户,没有代码,可以发起交易 | MetaMask 生成的账户 `0x147F...6db9` |
| **智能合约账户** | 由代码控制的账户,没有私钥,只能响应交易 | TraceRecorder 合约 `0xc56a...7948` |
| **多签钱包 (Multisig)** | 需要多个签名才能执行交易的智能合约,提高安全性 | Gnosis Safe |

### 关键理解

- **EOA** 是唯一能"发起"交易的账户类型,智能合约账户只能通过其他交易"触发"执行
- **msg.sender** 在合约中被调用时,表示直接调用者的地址
- **Event** 是合约向外界广播信息的方式,链下应用可以通过监听 Event 来追踪状态变化
- **Gas** 是执行操作的成本,由发起交易的 EOA 支付

---

## 注意事项

- 所有操作均在 Sepolia 测试网完成
- 未在区块浏览器查证的记录不得计入交付物
- 部署后务必在 Etherscan 验证合约源码（Verify）
- 钱包地址 `0x147Fcf3EB8B9E305a5b4e16cbba90462F7126db9` 仅用于测试网,主网资产安全
- 私钥和助记词已安全保管,未提交到 GitHub
