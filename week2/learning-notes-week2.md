# Week 2 学习笔记 | AI x Web3

**作者:** Chichuzxy
**主方向:** Privacy & Security -> ZKML 推理验证
**时间:** 2026-05-28 ~ 05-30

---

## 一、核心认知

### 1. "去掉AI / 去掉Web3"双重检验法

判断一个方向值不值得做：分别去掉AI和Web3，看方案是否还成立。

- 合约审计：去掉AI -> 人工审计太慢、太贵 -> AI不可替代
- 隐私计算：去掉Web3 -> 无法在不暴露数据前提下验证 -> Web3不可替代
- 选Privacy & Security的理由就是两端都是硬依赖，没有一方是"锦上添花"

### 2. Groth16 vs Halo2 不是二选一，是分阶段

直觉上想统一用一个证明系统。实用做法：

- PoC阶段用 Groth16：工具链成熟（Circom+SnarkJS）、gas低、社区资料多
- 生产阶段用 Halo2：无需可信设置（trusted setup）、安全性更高
- 两个阶段的分工要在所有文档中统一措辞，否则互相矛盾

### 3. ZK电路的完整链路

不是"写个电路就跑"。标准流程：

编译(.circom -> .r1cs) -> Powers of Tau(可信设置) -> 生成密钥 -> Witness -> Proof -> Verify

每一步有独立工具和命令，遗漏一步就跑不通。

### 4. 问题拆解的五个维度

参与方 x 流程阶段 x 自动化边界 x 验证机制 x 风险 = 完整拆解。

4个参与方（User/Prover/Verifier/Consumer）、4个阶段，每阶段判断需不需要人工确认。

### 5. AI辅助审计的定位

AI不是替代人工审计，而是"加速器"和"扫描器"：

- AI快速扫描代码模式（访问控制、存储布局、常见漏洞）
- 但无法判断业务逻辑是否合理（"是否需要访问控制"取决于使用场景）
- 人工复核必不可少：判别误报（本实验1/4为低价值发现）、补充漏报

### 6. 交付物不等于"写完文件"

Week 2总共7项交付，不是7个文件。之前 direction-selection 里有个简表以为是问题地图，实际缺5个方向的完整分析和判断矩阵。深挖包也类似：proposal里有流程图碎片，但没有场景、反例、风险和验证计划的独立整理。

教训：对着要求一项一项过，不要靠感觉。

### 7. Week 2真正产出的不是文档

是三个能力的建立：

- 判断能力：一个方向中AI和Web3各自不可替代什么
- 拆解能力：参与方、流程、自动化边界、验证机制、风险
- 表达能力：用场景、反例、流程图把一个复杂方向讲清楚

---

## 二、踩坑记录

### 坑1: npm版circom是旧版

- 现象：`npm install -g circom` 安装的是circom1（JS实现），编译circom2代码报 Parse error
- 解决：从GitHub Releases下载circom2 v2.2.3 Rust版可执行文件
- 教训：工具链第一步就是确认版本，不要默认npm的即为最新

### 坑2: pragma版本号不匹配

- 现象：`pragma circom 0.5.46;` 在circom2.2.3上报错
- 解决：改为 `pragma circom 2.2.3;`
- 原因：0.5.46是circom1的版本号，circom2用2.x体系

### 坑3: `signal private input` 语法已废弃

- 现象：circom2中private不再是关键字
- 解决：改为 `signal input a;` —— circom2中input默认就是private

### 坑4: Windows CRLF换行符

- 现象：circom解析器不认`\r\n`
- 解决：`sed -i 's/\r$//' basicAdd.circom`
- 后续：编辑circom文件时确保保存为LF

### 坑5: 文档间描述矛盾

- 现象：problem-decomposition.md写Groth16，proposal-zkml.md写Halo2
- 解决：明确分工——PoC用Groth16，生产用Halo2，所有文档统一措辞

### 坑6: AI对业务逻辑判断困难

- 现象：AI建议添加onlyOwner，但TraceRecorder是"开放记录本"，不需要权限控制
- 教训：AI只能给技术建议，最终决策需要人理解业务场景

### 坑7: AI审计误报率高

- 现象：4个AI发现，3个有实际价值，1个是低优先级
- 教训：AI审计是"发现"而非"诊断"，需要人类过滤

### 坑8: 事件参数优化容易被忽略

- 现象：AI没发现MessageChanged事件中oldMessage(string)的冗余
- 教训：AI习惯于"功能正确"判断，对"效率优化"不够敏感

---

## 三、想法和疑问

### 想法

1. ZKML的信任模型微妙点：用户信任ZK数学，但Prover可能用错误的模型推理。需要模型哈希链上承诺来约束
2. Layer2部署Verifier合约能大幅降低gas，但L2的sequencer去中心化程度是trade-off
3. 当前Circom对大模型（CNN/Transformer）支持有限，PoC只能用小模型。电路复杂度随模型参数数量线性增长
4. AI审计流水线可以自动化：将审计结果存入数据库，定期重新扫描合约更新
5. 可以结合形式化验证：AI扫描 + 形式化证明，提高安全性

### 疑问

1. EZKL自动将ONNX转ZK电路，生成的电路效率如何？会不会比手写Circom大很多？
2. Halo2的可信设置"可选"具体怎么运作？和Groth16的强制可信设置区别在哪？
3. ZK电路验证的是"计算正确性"，但如果Prover用了一个看起来对但实际有后门的模型版本怎么办？
4. 电路规模对proof生成时间的影响有多大？普通笔记本能跑多大的模型？
5. AI审计的准确率能提升到多少？如何量化效率提升？
6. AI审计报告如何集成到CI/CD流程？

---

## 四、Week 2 产出总览

| # | 交付物 | 文件 |
|---|--------|------|
| 1 | 问题地图（6方向xAI/Web3不可替代性判断） | problem-map.md |
| 2 | 方向选择说明 | direction-selection.md |
| 3 | 问题拆解（五维度） | problem-decomposition.md |
| 4 | 初步Proposal | proposal-zkml.md |
| 5 | 参考资料清单 | references.md |
| 6 | 主方向深挖包（流程图/场景/反例/风险/验证计划） | deep-dive-package.md |
| 7 | 方向backlog | direction-backlog.md |

附带产出：
- Circom PoC产物（artifacts/circom-poc/，5个文件）
- AI辅助合约审计报告（experiment-1-audit-report.md）
- Circom调试记录（circom-debug-log.md）

当前PoC进度：basicAdd电路编译+Proof生成+本地验证已完成。下一步：Solidity Verifier合约部署到Sepolia测试网。
