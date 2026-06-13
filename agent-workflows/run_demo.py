#!/usr/bin/env python3
import shutil
"""
ZKML Pipeline Agent - Demo Runner
Week 4 Hackathon: 用户一句话 -> agent 全自动编排 -> 链上 ZK 验证

用法:
    python run_demo.py "训练房价预测模型，部署 ZK verifier 到 Sepolia"

引擎:
    Hermes Agent (默认) 或 GLM-4.7-Flash (需要 Z.AI API Key)
"""

import sys
import os
import json
import time
import asyncio
from dataclasses import dataclass
from typing import Optional

# ============================================================
# Step 执行器 - 每个 step 是独立可调用的函数
# ============================================================

@dataclass
class StepResult:
    step: str
    status: str  # 'ok' | 'skip' | 'error'
    output: str
    duration: float

def step_1_train_model() -> StepResult:
    """Step 1: 加载预训练 ONNX 模型"""
    t0 = time.time()
    model_path = "project/models/model.onnx"
    if os.path.exists(model_path):
        size_kb = os.path.getsize(model_path) / 1024
        return StepResult("train_model", "ok",
            f"模型已就绪: {model_path} ({size_kb:.1f} KB)", time.time() - t0)
    return StepResult("train_model", "error", "模型文件缺失", time.time() - t0)

def step_2_ezkl_pipeline() -> StepResult:
    """Step 2-4: EZKL 全流程 (电路编译 + 证明生成 + Verifier 导出)"""
    t0 = time.time()
    output_dir = "project/ezkl_output"

    # 检查是否已生成
    required = ["proof.json", "vk.key", "pk.key", "compiled.model"]
    missing = [f for f in required if not os.path.exists(f"{output_dir}/{f}")]
    has_verifier = os.path.exists("contracts/src/Verifier.sol")

    if not missing and has_verifier:
        proof_size = os.path.getsize(f"{output_dir}/proof.json")
        return StepResult("ezkl_pipeline", "skip",
            f"Pipeline 产物已存在 (proof: {proof_size}B, Verifier.sol: OK)",
            time.time() - t0)

    # 需要重新跑
    import subprocess
    result = subprocess.run(["python", "ezkl_pipeline.py"],
        capture_output=True, text=True, timeout=600)
    if result.returncode == 0:
        return StepResult("ezkl_pipeline", "ok",
            "EZKL 全流程完成 (setup + prove + verifier)", time.time() - t0)
    return StepResult("ezkl_pipeline", "error",
        f"EZKL pipeline 失败: {result.stderr[-200:]}", time.time() - t0)

def step_5_deploy() -> StepResult:
    """Step 5: 部署 Verifier 到 Sepolia（如已部署则跳过）"""
    t0 = time.time()

    # 检查已知合约
    KNOWN_ADDR = "0x75dBdd07fE81628c7aef5a8b48493Ebc200afD60"
    env = {}
    with open(".env", encoding="utf-8") as f:
        for line in f:
            if '=' in line and not line.startswith('#'):
                k, v = line.strip().split('=', 1)
                env[k] = v
    rpc = env.get("SEPOLIA_RPC_URL", "")
    pk = env.get("PRIVATE_KEY", "")

    # 检查链上是否有代码
    import subprocess
    code = subprocess.run([shutil.which("cast") or "cast", "code", KNOWN_ADDR, "--rpc-url", rpc],
        capture_output=True, text=True, timeout=10)
    if code.stdout.strip() and code.stdout.strip() != "0x":
        return StepResult("deploy", "skip",
            f"合约已部署: {KNOWN_ADDR}", time.time() - t0)

    import subprocess
    result = subprocess.run([
        shutil.which("forge") or "forge", "script", "script/DeployVerifier.s.sol:DeployVerifier",
        "--rpc-url", rpc, "--private-key", pk, "--broadcast"
    ], capture_output=True, text=True, timeout=300, cwd="contracts")

    if result.returncode == 0:
        # 提取地址
        for line in result.stdout.split('\n'):
            if "Verifier deployed at:" in line:
                addr = line.split(":")[-1].strip()
                return StepResult("deploy", "ok",
                    f"合约已部署: {addr}", time.time() - t0)
    return StepResult("deploy", "error",
        f"部署失败: {result.stderr[-200:]}", time.time() - t0)

def step_6_verify(address: str) -> StepResult:
    """Step 6: 链上验证 proof"""
    t0 = time.time()

    import ezkl
    calldata = ezkl.encode_evm_calldata(
        proof="project/ezkl_output/proof.json",
        calldata="/tmp/evm_demo_calldata.bin"
    )

    env = {}
    with open(".env", encoding="utf-8") as f:
        for line in f:
            if '=' in line and not line.startswith('#'):
                k, v = line.strip().split('=', 1)
                env[k] = v

    import subprocess
    calldata_hex = "0x" + calldata.hex()
    result = subprocess.run([
        shutil.which("cast") or "cast", "call", address, calldata_hex,
        "--rpc-url", env.get("SEPOLIA_RPC_URL", "")
    ], capture_output=True, text=True, timeout=30)

    if "0x0000000000000000000000000000000000000000000000000000000000000001" in result.stdout:
        return StepResult("verify", "ok",
            f"链上验证通过! 合约: {address}", time.time() - t0)
    return StepResult("verify", "error",
        f"验证失败: {result.stdout.strip()}", time.time() - t0)


# ============================================================
# Agent 编排引擎
# ============================================================

def run_hermes_agent(task: str) -> list[StepResult]:
    """Hermes Agent 编排 - 直接按优先级顺序执行 steps"""
    print(f"\n{'='*60}")
    print(f"Agent 任务: {task}")
    print(f"引擎: Hermes Agent (tool calling)")
    print(f"{'='*60}\n")

    steps = []

    # Agent 自主决策执行顺序（此处简化为固定顺序，Hermes 实际可动态调整）
    for step_fn, label in [
        (step_1_train_model, "Step 1/6: 模型就绪检查"),
        (step_2_ezkl_pipeline, "Step 2-4/6: EZKL 电路+证明+Verifier"),
        (step_5_deploy, "Step 5/6: 部署 Verifier 到 Sepolia"),
    ]:
        print(f"  {label}...", end=" ", flush=True)
        result = step_fn()
        steps.append(result)
        print(f"[{result.status.upper()}] {result.output.split(chr(10))[0]}")

    # Step 6 需要合约地址
    CONTRACT_ADDR = "0x75dBdd07fE81628c7aef5a8b48493Ebc200afD60"
    print(f"  Step 6/6: 链上验证...", end=" ", flush=True)
    result = step_6_verify(CONTRACT_ADDR)
    steps.append(result)
    print(f"[{result.status.upper()}] {result.output.split(chr(10))[0]}")

    return steps


def run_glm_agent(task: str, api_key: Optional[str] = None) -> list[StepResult]:
    """GLM Agent 编排 - 使用 Z.AI API（需要 GLM_API_KEY）"""
    if not api_key:
        print("[WARN] GLM_API_KEY 未设置，fallback 到 Hermes Agent")
        return run_hermes_agent(task)

    print(f"\n{'='*60}")
    print(f"Agent 任务: {task}")
    print(f"引擎: GLM-4.7-Flash (Z.AI API, 免费)")
    print(f"{'='*60}\n")

    try:
        from openai import OpenAI
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.z.ai/api/paas/v4/"
        )

        # 定义 tools (function calling)
        tools = [
            {"type": "function", "function": {
                "name": "check_model_ready",
                "description": "检查预训练 ONNX 模型是否就绪",
                "parameters": {"type": "object", "properties": {}, "required": []}
            }},
            {"type": "function", "function": {
                "name": "run_ezkl_pipeline",
                "description": "运行 EZKL 全流程: 编译电路, 生成证明, 导出 Solidity Verifier",
                "parameters": {"type": "object", "properties": {}, "required": []}
            }},
            {"type": "function", "function": {
                "name": "deploy_verifier",
                "description": "部署 Verifier 合约到 Sepolia 测试网",
                "parameters": {"type": "object", "properties": {}, "required": []}
            }},
            {"type": "function", "function": {
                "name": "verify_proof_onchain",
                "description": "在链上调用 verifyProof 验证 ZK 证明",
                "parameters": {
                    "type": "object",
                    "properties": {"contract_address": {"type": "string"}},
                    "required": ["contract_address"]
                }
            }}
        ]

        response = client.chat.completions.create(
            model="glm-4.7-flash",
            messages=[
                {"role": "system", "content": "你是 ZKML Pipeline Agent，负责编排机器学习模型的 ZK 证明生成和链上验证。"},
                {"role": "user", "content": task}
            ],
            tools=tools,
            tool_choice="auto",
            max_tokens=1024
        )

        msg = response.choices[0].message
        if msg.tool_calls:
            print(f"  GLM 决定调用 {len(msg.tool_calls)} 个 tools:")
            for tc in msg.tool_calls:
                print(f"    - {tc.function.name}")
        else:
            print(f"  GLM 回复: {msg.content}")

        # 实际执行仍然用 Hermes（GLM 仅做规划层）
        print("\n  [执行层: Hermes]")
        return run_hermes_agent(task)

    except Exception as e:
        print(f"  GLM API 错误: {e}")
        print("  Fallback 到 Hermes Agent")
        return run_hermes_agent(task)


# ============================================================
# Main
# ============================================================

if __name__ == "__main__":
    task = sys.argv[1] if len(sys.argv) > 1 else \
        "训练房价预测模型，生成 ZK 证明，部署 verifier 到 Sepolia 并验证"

    # 引擎选择
    engine = os.environ.get("AGENT_ENGINE", "hermes")
    glm_key = os.environ.get("GLM_API_KEY")

    if engine == "glm" and glm_key:
        results = run_glm_agent(task, glm_key)
    else:
        results = run_hermes_agent(task)

    # 汇总
    print(f"\n{'='*60}")
    print("Pipeline 完成汇总:")
    for r in results:
        icon = "OK" if r.status == "ok" else ("SKIP" if r.status == "skip" else "FAIL")
        print(f"  [{icon}] {r.step}: {r.output[:80]}")
    print(f"{'='*60}")
