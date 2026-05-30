# Week 2 学习笔记 | 2026-05-30

**作者:** Chichuzxy
**主方向:** Privacy & Security → ZKML 推理验证

---

## 今日完成

完成 Week 2 最后 3 项缺失交付物，Week 2 全部 7 项交付物齐全。

### 新交付物

1. **AI x Web3 问题地图 (problem-map.md)**
   - 覆盖 6 个方向: Payment, Identity, Wallet, Privacy, Governance, DeFi
   - 每个方向标注: AI 不可替代什么、Web3 不可替代什么、反例、典型场景
   - 方向判断矩阵: 结构性需求、验证可能性、最小切入、风险边界、Week 3 承接

2. **方向 Backlog (direction-backlog.md)**
   - 记录 3 个未选方向及其不选原因: Wallet, Payment, Governance
   - 防止后续讨论中反复摇摆

3. **主方向深挖包 (deep-dive-package.md)**
   - 1 张全链路流程图 (用户 → Prover → Verifier → Consumer)
   - 1 个典型场景 (健康数据隐私诊断)
   - 3 个反例 (结果上链无证明、公开数据分析、纯 TEE 方案)
   - 1 组关键风险 (7 项风险矩阵 + 缓解优先级)
   - 1 个最小验证计划 (Circom PoC 7 步骤, 3 步已完成)

---

## 学习收获

### 1. 交付物不等于"写完文件"

Week 2 总交付要求是 7 项，不是 7 个文件。之前 direction-selection 里有个简表以为是问题地图，实际上它缺 5 方向完整分析和判断矩阵。深挖包也是一样: proposal 里有流程图碎片，但没有场景、反例、风险和验证计划的独立整理。

教训: 对着要求一项一项过，不要靠感觉。

### 2. 深挖包的"反例"价值最大

写反例的过程最能检验是否真正理解一个方向:
- 不是 ZKML: 结果上链但无 verify(proof)
- 不是 ZKML: 数据公开, 不需要隐私
- 不是 ZKML: 信任硬件而非密码学

只有能举出清晰的边界 case，才算真正掌握了判断框架。

### 3. Week 2 的真正产出

不是 7 个文档本身，而是:
- 判断能力: 一个方向中 AI 和 Web3 各自不可替代什么
- 拆解能力: 参与方、流程、自动化边界、验证机制、风险
- 表达能力: 用场景、反例、流程图把一个复杂方向讲清楚

---

## 当前 PoC 进度

Circom 基本电路 (basicAdd) 编译 + Proof 生成 + 本地验证: 已完成
产物: week2/artifacts/circom-poc/ (5 个文件)

下一步: Solidity Verifier 合约部署到 Sepolia 测试网

---

## Week 2 交付物总览

| # | 交付物 | 文件 | 状态 |
|---|--------|------|------|
| 1 | 问题地图 | problem-map.md | Done |
| 2 | 方向选择说明 | direction-selection.md | Done |
| 3 | 问题拆解 | problem-decomposition.md | Done |
| 4 | 初步 Proposal | proposal-zkml.md | Done |
| 5 | 参考资料清单 | references.md | Done |
| 6 | 主方向深挖包 | deep-dive-package.md | Done |
| 7 | 方向 backlog | direction-backlog.md | Done |
