# GLM-5.1 API 集成计划

**日期:** 2026-06-02
**赛道:** Z.AI | Web3 x Long-Horizon Task
**模型:** GLM-5.1 (Z.AI 旗舰模型)

---

## 模型能力速览

| 指标 | 数值 |
|------|------|
| Context 长度 | 200K tokens |
| 最大输出 | 128K tokens |
| 持续执行 | 最长 8 小时自主工作 |
| Thinking Mode | 支持 |
| Function Calling | 支持 |
| MCP 工具 | 支持 |
| Streaming | 支持 |
| 兼容 OpenAI SDK | 是 |

核心亮点: 不是单轮对话变聪明，而是能在 8 小时内持续自主规划 -> 执行 -> 验证 -> 优化，适合多步骤串行工程任务。

---

## API 接入方式

### 方式 1: OpenAI 兼容 SDK (推荐，最快接入)

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_ZAI_API_KEY",
    base_url="https://api.z.ai/api/paas/v4/"
)

response = client.chat.completions.create(
    model="glm-5.1",
    messages=[{"role": "user", "content": "训练房价预测模型，部署 ZK verifier"}],
    thinking={"type": "enabled"},
    max_tokens=4096
)
```

### 方式 2: Z.AI 官方 SDK

```bash
pip install zai-sdk
```

```python
from zai import ZaiClient

client = ZaiClient(api_key="YOUR_API_KEY")
response = client.chat.completions.create(
    model="glm-5.1",
    messages=[{"role": "user", "content": "..."}]
)
```

### 方式 3: cURL

```bash
curl -X POST "https://api.z.ai/api/paas/v4/chat/completions" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "glm-5.1", "messages": [{"role": "user", "content": "..."}]}'
```

---

## Week 4 集成方案

### 方案 A: GLM-5.1 直接编排 + Function Calling (理想方案)

```
GLM-5.1 作为主 agent，通过 function calling 调用:
  - train_model(data) -> model.onnx
  - ezkl_compile(onnx_path) -> circuit + keys
  - ezkl_prove(input) -> proof
  - deploy_verifier(contract_path) -> address
  - verify_onchain(address, proof) -> tx_hash

GLM-5.1 负责: 拆解任务 + 决定调用顺序 + 检查中间结果 + 失败重试
```

需要: Z.AI API Key + 定义 function schemas

### 方案 B: Hermes 预设脚本 + GLM-5.1 仅作规划 (fallback)

```
Hermes 运行预设的 pipeline.py（6 个 step 已定义）
GLM-5.1 只负责: 理解用户输入 -> 生成执行计划 -> 传给 pipeline
pipeline.py 逐个执行 step，失败返回错误信息给 GLM-5.1 重新规划
```

需要: Hermes Agent + pipeline.py + GLM-5.1 API Key

### 方案 C: 纯 Hermes 预设编排 (最小 fallback)

```
Hermes + 预设 pipeline.py
不调用 GLM-5.1，用户手动指定参数
仍能演示 "可验证推理部署" 链路，但失去 "自主拆解"
```

需要: Hermes Agent + pipeline.py

---

## 待办

- [ ] 获取 Z.AI API Key (https://z.ai/manage-apikey/apikey-list)
- [ ] 确认 Coding Plan 订阅或按量计费方案
- [ ] 测试 GLM-5.1 Function Calling 是否稳定
- [ ] 写 function schemas: train_model / ezkl_compile / ezkl_prove / deploy_verifier
- [ ] 端到端测试: 一句话 -> agent 调用 6 个 function -> 链上验证通过

---

## 费用估算

| 方案 | 费用 | 说明 |
|------|------|------|
| Coding Plan | $18/月 | 含 GLM-5.1 + 编码工具兼容 |
| 按量计费 | 看 token 用量 | GLM-5.1 定价见 https://docs.z.ai/guides/overview/pricing |

Week 4 demo 预计 token 用量不高（6 步编排 + 少量重试），按量可能 <$5。

---

## Function Calling Schema (草案)

```json
[
  {
    "name": "train_model",
    "description": "Train a simple ML model and export to ONNX format",
    "parameters": {
      "type": "object",
      "properties": {
        "model_type": {"type": "string", "enum": ["linear_regression", "mlp"]},
        "output_path": {"type": "string", "description": "Path for ONNX file"}
      }
    }
  },
  {
    "name": "ezkl_compile",
    "description": "Compile ONNX model to ZK circuit using EZKL",
    "parameters": {
      "type": "object",
      "properties": {
        "onnx_path": {"type": "string"},
        "settings_path": {"type": "string"}
      }
    }
  },
  {
    "name": "ezkl_prove",
    "description": "Generate ZK proof for given input using EZKL",
    "parameters": {
      "type": "object",
      "properties": {
        "input_data": {"type": "array", "items": {"type": "number"}},
        "proof_path": {"type": "string"}
      }
    }
  },
  {
    "name": "deploy_verifier",
    "description": "Deploy Solidity verifier contract to Sepolia using Foundry",
    "parameters": {
      "type": "object",
      "properties": {
        "contract_path": {"type": "string"},
        "rpc_url": {"type": "string"},
        "private_key": {"type": "string"}
      }
    }
  },
  {
    "name": "verify_onchain",
    "description": "Call verify() on deployed contract with proof",
    "parameters": {
      "type": "object",
      "properties": {
        "contract_address": {"type": "string"},
        "proof_path": {"type": "string"}
      }
    }
  }
]
```
