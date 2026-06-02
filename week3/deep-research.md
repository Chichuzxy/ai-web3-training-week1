# Week 3 | 深度研究摘要

**日期:** 2026-06-02
**主方向:** ZKML 推理验证

---

## 1. EZKL - ONNX to ZK Circuit

### 解决什么

EZKL 将 ONNX 模型自动编译为 Halo2 ZK 电路。开发者不需要手写 Circom——只需提供 .onnx 文件，EZKL 处理量化、电路生成、proof 生成、链上验证全流程。

支持三种证明场景:
- 公开模型 + 隐私输入
- 隐私模型 + 公开输入
- 全部公开（验证计算正确性）

### 边界

- 后端用 Halo2（无 trusted setup），proof 可链上 EVM 验证
- Python/CLI/JS 三端可用，Colab notebook 一键跑通
- v21.0.0 已通过 Trail of Bits 审计
- 提供远程 proving 服务（不需要本地 GPU）

### 缺什么

- 量化精度损失: ONNX float -> ZK 有限域整数，输出与 Python 推理结果有偏差
- 操作符覆盖: ONNX 120+ 算子，EZKL 支持约 50 个，复杂模型可能需要改写
- 激活函数成本: Sigmoid/Softmax/GELU 极贵，大模型（Transformer）基本跑不动
- 电路规模: 模型参数每增加一点，电路 constraints 线性增长

### 对 Proposal 的影响

Week 4 必须用小模型（线性回归/小型 MLP）。EZKL CLI 直接调用，不做 Python API 封装，降低集成复杂度。量化精度偏差不是 demo 阶段的 blocker——只需要证明"电路验证通过"即可。

---

## 2. Circom / SnarkJS - 手动电路工具链

### 解决什么

Circom 是 ZK 电路 DSL，SnarkJS 是配套的 proof 生成和验证工具。适合手写电路（如 hash、merkle tree、签名验证），不适合 ML 推理电路（手写 matmul 不现实）。

### 成熟度

- Circom 2.x (Rust 编译器) 仍在活跃维护，社区最大
- SnarkJS 相对停滞，但功能稳定
- Circomlib 提供大量标准模板（comparator、hash、signature）
- Groth16 是默认证明系统，proof 最小（~128 bytes），gas 最低

### 对 Proposal 的影响

PoC 阶段手写过 basicAdd.circom 验证了工具链可用。但 proposal 核心 pipeline 不走 Circom——用 EZKL 自动编译 ONNX。Circom 保留作为 fallback：如果 EZKL 编译失败，可以手写一个极简验证电路证明工具链可达性。

---

## 3. Halo2 vs Groth16

| 维度 | Groth16 | Halo2 |
|------|---------|-------|
| Trusted Setup | 需要，每电路一次 | 不需要（IPA + Pedersen） |
| Proof 大小 | ~128 bytes（最小） | ~几 KB（更大） |
| Gas 成本 | 最低 | 更高 |
| 递归验证 | 不支持 | 原生支持 |
| 工具链成熟度 | 高，Circom 生态最完整 | 中，EZKL / PSE 用 |
| 社区 | iden3/Polygon Hermez/大量项目 | Zcash / Scroll / Taiko |

### 谁何时用

- PoC / 最小 demo: Groth16，因为 proof 小、gas 低、工具链稳
- 生产 / 多证明聚合: Halo2，因为不需要为每个电路重新做 trusted setup，且支持递归

### 对 Proposal 的影响

EZKL 默认用 Halo2，proposal 跟着走就行。不纠结选哪个——EZKL 选了 Halo2，我们就用 Halo2。如果链上验证 gas 太高，可以换成 Arbitrum Sepolia（L2 便宜）。

---

## 风险 Memo

ZKML 方向成立依赖三个前提:

1. EZKL 能稳定将小型 ONNX 模型转为可用电路。如果版本不兼容或编译失败，fallback 是手写 Circom 极简电路证明工具链可达性（但丢掉了"ONNX 自动编译"的亮点）。

2. 电路规模不会超出 Sepolia gas 限制。应对: 用线性回归（<100 参数），部署到 L2 降低 gas。

3. GLM-5.1 能有效编排 6 步 pipeline。如果 API 不稳定或限流，fallback 用 Hermes 预定义脚本代替 agent 自主编排——仍能演示"可验证推理部署"核心价值，只是少了"自主拆解"。

最大失败点: EZKL 编译 ONNX 在 Windows 环境不兼容。应对: 提前在 Colab 跑通 EZKL 全流程，确认可用后再写本地集成。
