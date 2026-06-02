# 学习笔记 2026-05-28

## 核心认知

### 1. "去掉AI / 去掉Web3"双重检验法
判断一个方向值不值得做的核心方法：分别去掉AI和Web3，看方案是否还成立。
- 合约审计：去掉AI → 人工审计太慢 → AI不可替代
- 隐私计算：去掉Web3 → 无法在不暴露数据前提下验证 → Web3不可替代
- 这就是选Privacy & Security的理由 —— 两端都是硬依赖

### 2. Groth16 vs Halo2 不是二选一，是分阶段
直觉上会想统一用一个证明系统。实用做法：
- PoC阶段用Groth16：工具链成熟（Circom+SnarkJS）、gas低、社区资料多
- 生产阶段用Halo2：无需可信设置（trusted setup）、安全性更高
- 两个阶段的分工要写清楚，否则文档之间互相矛盾

### 3. ZK电路的完整链路比想象中长
不是"写个电路就跑"。标准流程：
编译(.circom → .r1cs) → Powers of Tau(可信设置) → 生成密钥 → Witness → Proof → Verify
每个步骤有独立工具和命令，遗漏任何一步都跑不通。

### 4. 问题拆解的粒度
参与方 × 流程阶段 × 自动化边界 × 验证机制 × 风险 = 完整的问题拆解。
4个参与方（User/Prover/Verifier/Consumer）、4个阶段、每阶段判断需不需要人工确认。

## 踩坑记录

### 坑1: npm版circom是旧版
- 现象：`npm install -g circom` 安装的是circom1（JS实现），编译circom2代码报 Parse error
- 解决：从GitHub Releases下载circom2 v2.2.3 Rust版可执行文件
- 教训：工具链的第一步就是确认版本，不要默认npm的就是最新版

### 坑2: pragma版本号不匹配
- 现象：`pragma circom 0.5.46;` 在circom2.2.3上报错
- 解决：改为 `pragma circom 2.2.3;`
- 原因：0.5.46是circom1的版本号体系，circom2用2.x

### 坑3: `signal private input` 语法已废弃
- 现象：circom2中private不再是关键字
- 解决：改为 `signal input a;` —— circom2中input默认就是private
- 教训：circom1→circom2有不少breaking changes

### 坑4: Windows CRLF换行符
- 现象：circom解析器不认\r\n
- 解决：`sed -i 's/\r$//' basicAdd.circom`
- 后续：写circom文件时要确保编辑器保存为LF

### 坑5: 文档间描述矛盾
- 现象：problem-decomposition.md写Groth16，proposal-zkml.md写Halo2
- 解决：明确分工 —— PoC用Groth16，生产用Halo2，所有文档统一措辞
- 教训：多份文档互相引用时，关键决策点必须对齐

## 想法和疑问

### 想法
1. ZKML的信任模型有个微妙点：用户信任ZK数学，但Prover可能用错误的模型推理。需要模型哈希链上承诺来约束。
2. Layer2部署Verifier合约能大幅降低gas，但L2的sequencer去中心化程度是个trade-off。
3. 当前Circom对大模型（CNN/Transformer）支持有限，PoC只能用小模型。这个限制是因为电路复杂度随模型参数数量线性增长。

### 疑问
1. EZKL自动将ONNX转ZK电路，生成的电路效率如何？会不会比手写Circom电路大很多？
2. Halo2的可信设置"可选"具体怎么运作？和Groth16的强制可信设置区别在哪？
3. ZK电路验证的是"计算正确性"，但如果Prover用了一个看起来对但实际有后门的模型版本怎么办？
4. 电路规模对proof生成时间的影响有多大？普通笔记本能跑多大的模型？

## 产出文件

| 文件 | 用途 |
|------|------|
| direction-selection.md | 为什么选Privacy & Security / ZKML |
| problem-decomposition.md | 参与方、流程、验证机制、风险拆解 |
| proposal-zkml.md | 技术方案：ONNX + EZKL + Halo2 |
| references.md | ZKML项目、论文、工具清单 |
| circom-debug-log.md | Circom踩坑全记录 + 最终产物 |
| artifacts/circom-poc/ | 电路源码、proof、verification_key |