# Module D | L2 + ZK 入门概览

**目标：** 理解 Layer 2 扩容方案和零知识证明的基本概念，为后续深度学习打基础。

---

## 一、Layer 2 为什么存在？

Ethereum 主网的问题:
- Gas 费用高（高峰期 >50 Gwei）
- TPS 低（约 15-30 tx/s）
- 用户体验差（等待确认时间长）

Layer 2 的核心思路：**在主网之外做计算，把结果回传主网验证**

---

## 二、L2 主要方案对比

| 方案 | 原理 | 代表项目 | 优缺点 |
|------|------|----------|--------|
| **Rollup** | 批量执行交易，压缩数据上链 | Arbitrum, Optimism, zkSync | 高 throughput, 安全性强 |
| **State Channels** | 链下交互，最终结算上链 | Lightning Network, Raiden | 极速但流动性受限 |
| **Sidechain** | 独立区块链，与主网并行 | Polygon PoS | 独立共识，安全性弱于 L2 |
| **Validium** | Rollup + off-chain data availability | Loopring | 成本最低但牺牲可用性 |

### 重点: Validium vs Rollup
- Rollup: 数据放在 L1（安全高，gas 仍有一定成本）
- Validium: 数据放链外（gas 极低，但依赖数据可用性节点）

---

## 三、ZK（零知识证明）快速理解

### 一句话定义
ZKP = 我能证明我知道某个东西，而不需要透露这个是什么

### 直观类比
- **传统密码:** "你知道我的密码" → 必须告诉我密码本身
- **ZKP:** "你知道我的密码" → 我出题你回答，我对答案，无需知道密码内容

### ZK 在 Web3 中的应用
1. **zkRollup** - 隐私性强的交易批处理
2. **zkML** - 证明 AI 模型推理正确但不暴露模型/数据
3. **身份认证** - 证明你满足条件(如年龄>18)而不暴露身份信息

---

## 四、Week 2 学习目标

- [ ] 能清晰解释 Rollup vs Sidechain 的区别
- [ ] 理解 Validity Proof 和 Fraud Proof 的差异
- [ ] 能用通俗语言给非技术人员讲 ZKP
- [ ] 选一个 L2 测试网做一次交互体验

---

*创建于 Week 2 | 仅作入门概览，深度内容待后续模块*
