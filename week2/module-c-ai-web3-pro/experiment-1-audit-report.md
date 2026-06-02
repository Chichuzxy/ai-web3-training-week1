# Module C 实验1 | AI 辅助智能合约审计流水线 -- TraceRecorder.sol

**日期:** 2026-05-29
**目标合约:** TraceRecorder.sol (Week 1 部署)
**审计方法:** LLM 结构化分析 + 人工复核

---

## 一、合约概况

```solidity
// 合约地址: 0xdA2E7bF7aD355562fb1faeAFa3B560337410651a (Sepolia)
// 功能: 记录 value + message + 操作者地址，通过事件追踪变更历史
contract TraceRecorder {
    uint256 public value;
    string public message;
    address public lastOperator;
    // ...
}
```

## 二、AI 审计结果

### 发现 1: 缺少访问控制

- 等级: HIGH
- 置信度: 0.95
- 描述: `setValue()` 和 `setMessage()` 函数没有权限限制，任何人都可以调用
- 修复建议: 添加 `onlyOwner` modifier，继承 OpenZeppelin 的 Ownable

```solidity
// 修复后
import "@openzeppelin/contracts/access/Ownable.sol";
contract TraceRecorder is Ownable {
    function setValue(uint256 newValue, string memory note) public onlyOwner {
        // ...
    }
}
```

### 发现 2: 状态变量存储布局可优化

- 等级: LOW
- 置信度: 0.85
- 描述: `value` (uint256, 32 bytes), `message` (string, 32 bytes slot), `lastOperator` (address, 20 bytes) 分散存储。address 可以和更小的类型打包
- 修复建议: 当前结构已经比较合理，如果要极致优化，可以把 lastOperator 替换为 mapping

### 发现 3: string 存储成本高

- 等级: INFO
- 置信度: 0.90
- 描述: `message` 是 string 类型，每次写入固定消耗 1 slot (20,000 gas 首次 / 2,900 gas 后续)，如果消息长度超过 31 字节会额外占用 slot
- 修复建议: 如果消息有固定格式，用 bytes32 替代 string

### 发现 4: 无暂停/紧急机制

- 等级: MEDIUM
- 置信度: 0.70
- 描述: 合约没有暂停功能，出现问题时无法临时冻结操作
- 修复建议: 可添加 Pausable 机制（但当前合约简单，此建议优先级较低）

## 三、人工复核

| AI 发现 | 判定 | 说明 |
|---------|------|------|
| 缺少访问控制 | 确认有效 | 取决于使用场景。如果是"开放记录本"则不需要；如果是"管理数据"则需要 Owner |
| 存储布局可优化 | 误报偏向 | 当前布局已经合理，再优化收益极小 |
| string 存储成本高 | 确认有效 | 但 TraceRecorder 本身不是高频写入场景，可接受 |
| 无暂停机制 | 低优先级 | 简单合约不需要过度设计 |

### 人工补充发现

**发现 A: 事件参数冗余**

`MessageChanged` 事件包含了 `oldMessage` (string)，在链上产生高 gas 成本。如果只需要追踪变更，可以用 `keccak256(oldMessage)` 替代完整字符串。

```solidity
event MessageChanged(
    address indexed operator,
    bytes32 indexed oldMessageHash,
    string newMessage
);
```

## 四、修复实施

### 修复后的合约: TraceRecorderV2.sol

已在 week2/artifacts/ 下保存修复版本:
- 添加 Ownable 权限控制
- 优化 MessageChanged 事件参数

## 五、对比总结

| 维度 | 原始版 | 修复版 |
|------|--------|--------|
| 权限控制 | 无 | onlyOwner |
| Gas (setMessage) | ~45,000 | ~38,000 (事件参数优化) |
| 事件可查询性 | 高 | 中 (oldMessage 改为 hash) |
| 安全性 | 低 | 中高 |

## 六、AI 审计方法总结

1. LLM Prompt 设计关键:
   - 要求输出结构化 JSON (vulnerability, severity, confidence, fix)
   - 提供明确的审计 checklist 作为 prompt 上下文
   - 要求区分 P0/P1/P2 优先级

2. AI 局限性:
   - 无法判断业务逻辑是否正确（比如"是否需要访问控制"取决于场景）
   - 对 gas 估算值不够精确
   - 容易给出过拟合的安全建议

3. 人工复核必不可少:
   - 判别误报（本实验中 1/4 为低价值发现）
   - 补充漏报（事件参数冗余 AI 未发现）