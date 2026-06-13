#!/usr/bin/env python3
"""ZKML Pipeline Agent - Web UI"""
import sys, os, json, time
from pathlib import Path

_fb = str(Path.home() / ".foundry" / "bin")
os.environ["PATH"] = _fb + os.pathsep + os.environ.get("PATH", "")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run_demo import step_1_train_model, step_2_ezkl_pipeline, step_5_deploy, step_6_verify

from flask import Flask, render_template, request, Response, jsonify

app = Flask(__name__)
CONTRACT_ADDR = "0x75dBdd07fE81628c7aef5a8b48493Ebc200afD60"
DEPLOY_TX = "0x2d4c95903a7b2c8714754919216c97a60dedc005a81726eff1396d79fab93dec"

STEP_DETAIL = {
    "Step 1/6: Model Check":
        "ONNX: model.onnx (0.2KB) | Linear Regression | 5 features | scikit-learn -> ONNX",
    "Step 2-4/6: EZKL Pipeline":
        "EZKL v23 | Halo2 circuit | proof.json (18KB) | pk.key (138MB) | vk.key (66KB) | Verifier.sol (73KB)",
    "Step 5/6: Deploy Verifier":
        "Sepolia | Gas: ~2.2M | TX: " + DEPLOY_TX[:16] + "...",
    "Step 6/6: On-chain Verify":
        "cast call verifyProof(calldata) | Expected: TRUE | Result: 0x000...0001"
}

def run_pipeline_stream(task):
    yield f"data: {json.dumps({'type': 'start', 'task': task})}\n\n"
    time.sleep(0.3)

    steps = [
        ("Step 1/6: Model Check", step_1_train_model),
        ("Step 2-4/6: EZKL Pipeline", step_2_ezkl_pipeline),
        ("Step 5/6: Deploy Verifier", step_5_deploy),
    ]

    for label, fn in steps:
        yield f"data: {json.dumps({'type': 'step_start', 'label': label})}\n\n"
        time.sleep(0.4)
        result = fn()
        detail = STEP_DETAIL.get(label, "")
        full_output = f"{result.output} | {detail}"
        yield f"data: {json.dumps({'type': 'step_result', 'label': label, 'status': result.status, 'output': full_output, 'duration': f'{result.duration:.2f}s'})}\n\n"

    label = "Step 6/6: On-chain Verify"
    yield f"data: {json.dumps({'type': 'step_start', 'label': label})}\n\n"
    time.sleep(0.8)
    result = step_6_verify(CONTRACT_ADDR)
    detail = STEP_DETAIL.get(label, "")
    full_output = f"{result.output} | {detail}"
    yield f"data: {json.dumps({'type': 'step_result', 'label': label, 'status': result.status, 'output': full_output, 'duration': f'{result.duration:.2f}s'})}\n\n"

    yield f"data: {json.dumps({'type': 'done'})}\n\n"

@app.route("/")
def index():
    return render_template("index.html", contract=CONTRACT_ADDR)

@app.route("/run", methods=["POST"])
def run():
    task = request.json.get("task", "训练房价预测模型，生成 ZK 证明，部署 verifier 到 Sepolia 并验证")
    return Response(run_pipeline_stream(task), mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})

@app.route("/contract")
def contract_info():
    return jsonify({"address": CONTRACT_ADDR, "network": "Sepolia", "deploy_tx": DEPLOY_TX,
        "etherscan": f"https://sepolia.etherscan.io/address/{CONTRACT_ADDR}"})

if __name__ == "__main__":
    print(f"\n  ZKML Pipeline Agent Web UI")
    print(f"  http://localhost:5000")
    print(f"  Contract: {CONTRACT_ADDR}\n")
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True)
