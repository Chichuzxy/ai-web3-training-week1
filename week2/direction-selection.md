# Week 2 | 方向选择说明：Privacy & Security

**作者:** Chichuzxy  
**日期:** 2026-05-28  
**主方向:** Privacy & Security (隐私与安全)

---

## 一、领域扫描回顾

Week 2 启动时对 AI x Web3 五大领域做了初步扫描:

| # | 领域 | 核心痛点 | 初步判断 |
|---|------|----------|----------|
| 1 | Payment / Commerce | 跨境结算效率低、交易透明性不足 | AI 可做风控预测, Web3 做清算层, 但方案成熟度已高 |
| 2 | Identity / Reputation | 身份伪造、数据孤岛 | 有价值, 但和隐私高度重叠, 可作为子方向 |
| 3 | Wallet / Permission | 私钥管理复杂、多链兼容差 | 偏工程问题, AI 作用有限 |
| 4 | Privacy / Security | 敏感信息暴露、合约漏洞、AI 推理数据隐私 | AI+Web3 双重不可替代, 技术深度够 |
| 5 | Governance / Coordination | 投票操控、参与度低 | Week 1 短暂探索过, 但 AI 切入点不够硬 |

## 二、为什么选 Privacy & Security

### 2.1 问题足够真实

- 智能合约漏洞导致数十亿美元损失(如 Euler Finance 1.97 亿、Ronin 6.25 亿)
- 用户在 DApp 交互时, 地址行为模式可被链上分析工具反向追踪
- AI 模型训练需要大量数据, 但用户不愿(也不应该)将原始数据交给中心化服务器

### 2.2 AI 和 Web3 各自不可替代

判断标准: 去掉 AI 或去掉 Web3, 方案是否还能成立?

| 维度 | 如果去掉 AI | 如果去掉 Web3 | 结论 |
|------|------------|--------------|------|
| 合约审计 | 人工审计速度慢、覆盖率低, 无法实时检测 | 可以用中心化数据库存审计结果, 但信任成本高 | AI 不可替代(速度和覆盖面) |
| 隐私计算 | 不用 AI 就没有智能分析能力, 只剩加密管道 | 不用 Web3/ZK 就无法在不暴露数据的前提下验证结果 | 两者都不可替代 |
| 链上行为异常检测 | 规则引擎无法应对复杂模式, 漏报率高 | 检测结果可以中心化存储, 但公信力不足 | AI 不可替代(Web3 加分) |

核心结论: 在"用 ZK 证明 AI 推理正确性"这个交叉点上, AI 提供推理能力, Web3 (ZKP) 提供验证机制, 去掉任何一边都无法实现"可信且隐私的 AI 推理"。

### 2.3 技术深度适合训练营

- 涉及 Circom / ZK-SNARKs 电路编写 (有实操产出)
- 可以结合 Layer2 降低 gas 成本 (方案完整性强)
- ZKML 是前沿方向, 有论文和开源项目支撑 (参考资料充分)

## 三、主方向的具体聚焦

在 Privacy & Security 大类下, 我进一步聚焦到:

**ZKML: 零知识机器学习推理验证**

一句话定义: 让 AI 模型在链下完成推理, 然后用零知识证明在链上验证"推理过程确实正确", 而无需暴露模型参数或输入数据。

典型场景:
1. 用户向 AI Agent 提交敏感数据(如医疗记录), Agent 链下推理, 链上 ZK 证明推理正确
2. 合约安全审计 AI 给出漏洞报告, ZK 证明审计覆盖了所有关键路径
3. 链上信用评分: 用户不暴露交易历史, AI 在可信环境计算, ZK 证明评分结果

## 四、与其他方向的关系

```
Privacy & Security (主方向)
  ├── ZKML 推理验证 (核心)
  ├── 合约安全审计 (AI 辅助, 可作为应用层)
  └── Identity / Reputation (子方向: 隐私身份是 ZKML 的上游依赖)
```

Governance 和 Payment 放入 backlog, 后续如有需要可复用 ZKML 验证模块。

## 五、未选方向的 Backlog

| 方向 | 暂缓原因 | 复用可能性 |
|------|----------|-----------|
| Payment | 方案已成熟, 创新空间小 | ZKML 可用于隐私支付审计 |
| Governance | AI 切入点偏软, 难以量化 | ZK 投票可复用 ZKML 验证 |
| Identity | 与隐私高度重叠 | 作为 ZKML 场景的上游身份层 |
| Wallet | 偏工程, AI 作用有限 | 暂不考虑 |

---

## 参考项目/论文(持续补充)

- EZKL: https://github.com/zkonduit/ezkl (ZKML 推理框架)
- Modulus Labs: https://modulus.xyz (ZKML 基础设施)
- Giza: https://giza.tech (AI Agent + ZK 验证)
- circomlib: https://github.com/iden3/circomlib (Circom 标准电路库)
