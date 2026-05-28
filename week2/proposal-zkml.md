# Week 2 | Proposal: ZKML 隐私推理验证系统

**作者:** Chichuzxy  
**日期:** 2026-05-28  
**状态:** 初稿

---

## 一、项目概述

构建一个 ZKML PoC 系统，实现: 用户提交敏感数据 → AI 链下推理 → ZK 证明推理正确 → 链上验证结果，全程不暴露模型参数和原始数据。

## 二、技术架构

```
[用户] --加密数据--> [Prover 链下服务]
                        |
                        | 1. 加载模型 (ONNX)
                        | 2. 推理 → 结果 R
                        | 3. 生成 ZK proof P (EZKL/Circom)
                        |
                        v
                   [Verifier 合约] (Sepolia / Layer2)
                        |
                        | 验证 proof P
                        |
                        v
                   [结果已验证] ← Consumer 读取
```

## 三、技术选型

| 组件 | 选择 | 理由 |
|------|------|------|
| AI 模型 | 简单线性回归 / 小型 MLP | Circom 对大模型支持有限，先跑通 PoC |
| 模型格式 | ONNX | EZKL 原生支持 |
| ZK 框架 | EZKL (主) + Circom (辅助) | EZKL 自动将 ONNX 转 ZK 电路，降低手写成本 |
| 证明系统 | Halo2 (EZKL 默认) | 无需可信设置，比 Groth16 更安全 |
| 部署链 | Sepolia 测试网 | 免费 gas，训练营标准 |
| 合约框架 | Foundry | 测试快，Solidity 原生 |
| 前端 | 可选 (后期) | PoC 阶段用 CLI 即可 |

## 四、PoC 实现步骤

### Phase 1: 模型准备
1. 用 Python 训练一个简单模型 (如房价预测、疾病风险评分)
2. 导出为 ONNX 格式
3. 验证模型推理结果 (纯 Python 对照)

### Phase 2: ZK 电路
1. 用 EZKL 将 ONNX 模型转为 ZK 电路
2. 生成 proving key 和 verifying key
3. 本地测试: 输入数据 → 生成 proof → 本地验证

### Phase 3: 链上验证
1. 用 Foundry 编写 Solidity Verifier 合约
2. 部署到 Sepolia 测试网
3. 提交 proof → 合约验证 → 确认通过

### Phase 4: 端到端测试
1. 模拟完整流程: 用户输入 → 链下推理 → proof 生成 → 链上验证
2. 记录 gas 消耗、proof 生成时间
3. 截图 + 交易哈希存档

## 五、预期产出

| 产出 | 格式 | 说明 |
|------|------|------|
| 模型代码 | Python + ONNX | 训练脚本 + 导出模型 |
| ZK 电路 | EZKL 配置 | 电路文件 + keys |
| Verifier 合约 | Solidity | Foundry 项目 |
| 测试记录 | Markdown | gas、时间、截图 |
| Proposal 本文 | Markdown | 本文件 |

## 六、时间估算

| 阶段 | 预计时间 |
|------|----------|
| Phase 1 模型准备 | 1-2 天 |
| Phase 2 ZK 电路 | 2-3 天 |
| Phase 3 链上部署 | 1 天 |
| Phase 4 端到端 | 1 天 |
| **合计** | **5-7 天** |

## 七、风险与应对

| 风险 | 应对 |
|------|------|
| EZKL 生成的电路太大，proof 生成超时 | 用更小的模型，或减少层数 |
| Verifier 合约部署 gas 超限 | 换 Layer2 测试网 (如 Arbitrum Sepolia) |
| EZKL 版本不兼容 | 锁定版本，参考官方 example |
| 训练好的模型精度不够 | PoC 不要求高精度，能跑通即可 |

## 八、安全原则 (继承自训练营规范)

- 所有链上操作仅在 Sepolia 测试网
- 私钥不暴露给 AI
- 每笔交易人工确认
- 合约代码人工审查后再部署
