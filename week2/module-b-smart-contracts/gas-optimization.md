# Module B | Solidity 深入 -- Gas 优化实战指南

**目标：** 从 Week 1 的基础部署，进阶到 Gas 优化的系统方法论。

---

## 一、Gas 消耗分层理解

### Layer 1: 基础交易费
所有交易的基础成本 = 21,000 gas

### Layer 2: SSTORE（状态存储）
| 操作 | Gas Cost | 说明 |
|------|----------|------|
| 存储槽从 0 → 非零 | 20,000 | 最贵的一次写入 |
| 存储槽从非零 → 其他非零 | 2,900 | 覆盖已有值 |
| 存储槽从非零 → 0 |  refund 4,800 | 清理释放refund |

### Layer 3: 事件触发
每次 emit event ≈ 75 + log_topic(375) × 级别 gas

---

## 二、Gas 优化 Checklist

### [P0] 存储布局优化
- [ ] 使用 packing: 把多个小类型变量塞进一个存储槽
- [ ] 示例: `uint8 a; uint8 b;` 只占 1 slot (2字节) 而非 2 slots
- [ ] Storage slot 对齐边界: 将相同大小的变量放一起

### [P0] 避免不必要的 SSTORE
- [ ] View/Pure 函数不耗 gas（读操作）
- [ ] 批量更新代替逐条更新
- [ ] 考虑用 mapping 替代 struct（取决于访问模式）

### [P1] 循环优化
- [ ] 遍历前确认数组/列表长度
- [ ] 避免在循环内做昂贵的 SSTORE
- [ ] 考虑 off-chain 索引 instead of on-chain 全量查询

### [P1] 数据类型选择
- [ ] 能用 uint8 就用，不要全部用 uint256
- [ ] address 比 bytes32 更便宜
- [ ] calldata 参数比 memory 参数省 gas

### [P2] 高级技巧
- [ ] immutable variables（部署后不可变，省 runtime gas）
- [ ] constant 变量（编译期替换，runtime 0 gas）
- [ ] short-circuit logic（利用 && / || 短路特性）

---

## 三、实践练习

### 练习 1: TraceRecorder 合约的 Gas Hot Spots
打开合约地址 `0xdA2E7bF7aD355562fb1faeAFa3B560337410651a`，对比:
- setValue() vs setMessage() 的 gas 消耗差异
- 分析为什么字符串存储比数值存储更贵

### 练习 2: 实现一个 Gas Optimized Counter
```solidity
// TODO: Week 2 实践
// 要求: 
// 1. 使用 packed storage (多个uint8共用slot)
// 2. 支持 batch increment
// 3. 对比优化前后的 gas 消耗
```

### 练习 3: Event vs Return 成本对比
设计实验，比较同一数据通过 event 输出和通过 function return 输出的 gas 差异

---

*创建于 Week 2 | 基于 Week 1 Gas 数据分析深化*
