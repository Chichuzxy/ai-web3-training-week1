# Module B | Solidity 深入 -- 合约安全审计清单

**目标：** 掌握智能合约常见漏洞和审计方法论。

---

## 一、常见漏洞分类

### Reentrancy（重入攻击）
- **原理:** 外部调用者利用回调递归进入合约
- **影响:** ⭐⭐⭐⭐⭐ 最高级别
- **防御:** Checks-Effects-Interactions 模式 / ReentrancyGuard
- **历史案例:** The DAO (2016), Parity Wallet (2017)

### Overflow/Underflow（溢出/下溢）
- **原理:** 算术运算超出数据类型范围
- **影响:** ⭐⭐⭐（Solidity 0.8+ 自动检查，旧版本危险）
- **防御:** Solidity >= 0.8.0 自带溢出保护

### Access Control（权限控制缺失）
- **原理:** 关键函数没有限制调用者
- **影响:** ⭐⭐⭐⭐
- **防御:** OpenZeppelin Ownable / AccessControl

### Oracle Manipulation（预言机操纵）
- **原理:** 利用价格预言机的可操纵性
- **影响:** ⭐⭐⭐⭐
- **防御:** 使用 Chainlink 等去中心化 oracle

---

## 二、审计 Checklist

### [P0] 代码逻辑审查
- [ ] 所有状态变量修改都放在事件触发之前（防止重入）
- [ ] 关键函数有 require/pause 保护
- [ ] no code path returns without proper state update

### [P0] 权限审查
- [ ] owner 函数只有管理员可调用
- [ ] transferOwnership 有 timelock
- [ ] 无隐藏 backdoor

### [P1] Gas 相关审查
- [ ] 无限循环风险（特别是遍历 mapping 或 array）
- [ ] 预估 gas 是否在 block limit 内

### [P1] 数字安全审查
- [ ] 浮点精度问题（用固定小数点替代 float）
- [ ] 前端验证 vs 后端验证的完整性

### [P2] 设计层面审查
- [ ] 是否有合理的升级机制
- [ ] pause/emergency withdraw 功能
- [ ] 参数是否可被外部操纵

---

## 三、实践练习

### 练习 1: Audit TraceRecorder.sol
对之前的 TraceRecorder 合约做一轮审计:
- 找出不安全的设计决策
- 提出改进方案
- 记录审计过程到 week2 artifacts

### 练习 2: 实现带 ReentrancyGuard 的 SafeTransfer
```solidity
// TODO: Week 2 实践
// 要求: 
// 1. 使用 modifiers 实现重入保护
// 2. 遵循 Checks-Effects-Interactions 模式
```

---

*创建于 Week 2 | 继承 Week 1 安全红线意识*
