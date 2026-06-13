# ZKML Pipeline Agent

**赛道:** Z.AI | Web3 x Long-Horizon Task  
**队员:** Chichuzxy  
**Week 4 冲刺目标:** 用户输入一句话 -> Agent 全自动完成 ONNX 模型 -> ZK 证明 -> 链上验证

---

## 一句话定位

用自然语言驱动 AI Agent 自主完成 ML 模型的可验证推理部署全链路（Python/ONNX/EZKL/Solidity/Foundry 5 层工具链），最终在 Sepolia 链上返回 ZK 验证结果。

---

## 问题

训练 ML 模型并使其推理结果在链上可验证需要协调 Python、ONNX、ZK 电路工具、Solidity、Foundry 等至少 5 种工具链。开发者需手动执行 6 步串行流程，任一环节出错需回退重来。

---

## 方案

AI Agent 接收自然语言指令，自主将任务拆解为 6 个子任务，分别调用 Python/ONNX/EZKL/Foundry，中间失败自动重试，最终输出链上验证结果。

```
输入: "训练房价预测模型，部署 ZK verifier 到 Sepolia"

Agent 执行:
  Step 1  检查模型就绪         -> model.onnx
  Step 2  EZKL: 编译电路       -> compiled.model
  Step 3  EZKL: 生成证明       -> proof.json
  Step 4  EZKL: 导出 Verifier  -> Verifier.sol
  Step 5  Foundry: 部署到 Sepolia -> 合约地址
  Step 6  cast call verify()   -> TRUE
```

---

## Demo

### 运行方式

```bash
python agent-workflows/run_demo.py "训练房价预测模型，部署 ZK verifier 到 Sepolia"
```

### 执行结果

```
============================================================
Agent 任务: 训练房价预测模型，部署 ZK verifier 到 Sepolia
引擎: Hermes Agent (tool calling)
============================================================

  Step 1/6: 模型就绪检查... [OK] 模型已就绪
  Step 2-4/6: EZKL 电路+证明+Verifier... [SKIP] Pipeline 产物已存在
  Step 5/6: 部署 Verifier 到 Sepolia... [SKIP] 合约已部署
  Step 6/6: 链上验证... [OK] 链上验证通过!

Pipeline 完成汇总:
  [OK] train_model: 模型已就绪
  [SKIP] ezkl_pipeline: Pipeline 产物已存在 (proof: 18107B)
  [SKIP] deploy: 合约已部署: 0x75dBdd07fE81628c7aef5a8b48493Ebc200afD60
  [OK] verify: 链上验证通过!
```

---

## 验证材料

| 项目 | 内容 |
|------|------|
| 合约地址 | `0x75dBdd07fE81628c7aef5a8b48493Ebc200afD60` |
| 部署交易 | `0x2d4c95903a7b2c8714754919216c97a60dedc005a81726eff1396d79fab93dec` |
| 网络 | Sepolia (11155111) |
| 验证方式 | `cast call verifyProof(calldata)` |
| 验证结果 | `0x000...0001` (TRUE) |
| Etherscan | https://sepolia.etherscan.io/address/0x75dBdd07fE81628c7aef5a8b48493Ebc200afD60 |
| calldata | `project/ezkl_output/evm_calldata.hex` |
| proof | `project/ezkl_output/proof.json` |

---

## 技术栈

| 层 | 选型 | 说明 |
|----|------|------|
| Agent 引擎 | Hermes Agent / GLM-5.1 fallback | 自然语言 -> 任务编排 |
| ML | Python + scikit-learn + ONNX | 线性回归房价预测 |
| ZK | EZKL v23.0.5 | ONNX 自动编译为 Halo2 电路 |
| 合约 | Foundry + Solidity | EZKL 生成的 Halo2Verifier |
| 网络 | Sepolia 测试网 | 链上 ZK 验证 |

---

## Mock 策略

- 模型提前训练好（不实时训练），Step 1 直接读文件
- EZKL 电路预编译一次，Step 2-4 复用
- Agent 负责编排 Steps 1-6，而不是重新生成电路
- 非 Agent 自主规划，而是预设 pipeline + Hermes tool calling

---

## 风险 + 应对

| 风险 | 应对 | 实际结果 |
|------|------|----------|
| EZKL Windows 不兼容 | Google Colab / Python binding | Python binding 可用 |
| GLM API 不可用 | Hermes + 预设脚本 fallback | 全线使用 Hermes fallback |
| VK 与 proof 不匹配 | 重新 setup+prove+create_evm_verifier 闭环 | Day 5 重新生成后验证通过 |
| ezkl encode_evm_calldata 格式 | 使用 ezkl Python API 而非手动 abi.encode | calldata 格式正确 |
| 电路过大 | 线性回归 <100 参数 | ONNX 模型 0.2KB |

---

## 赛道对齐 (Z.AI Long-Horizon Task)

- 6 步串行依赖 = 需要自主任务拆解
- 跨 Python/CLI/Solidity 工具 = 需要多工具调用
- 中间失败需要重试 = 需要错误恢复
- 最终结果需链上验证 = 可度量成功/失败

---

## 目录结构

```
project/
├── README.md
├── sprint-plan.md
├── hackathon-card.md
├── ezkl_output/          # EZKL 产物
│   ├── proof.json        # ZK 证明
│   ├── vk.key / pk.key   # 密钥
│   ├── compiled.model    # 编译电路
│   └── evm_calldata.hex  # 验证 calldata
├── models/
│   └── model.onnx        # 预训练 ONNX
└── artifacts/
    ├── verifier-address.txt
    ├── verify-evidence.txt
    └── risk-boundary.md

contracts/
├── src/Verifier.sol
├── script/DeployVerifier.s.sol
├── test/VerifyProof.t.sol
└── broadcast/            # 部署记录
```
