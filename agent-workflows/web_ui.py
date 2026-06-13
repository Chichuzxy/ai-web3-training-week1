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

DETAILS = {
    "Step 1/6: Model Check": "ONNX model: project/models/model.onnx (0.2 KB) | Model type: Linear Regression | Features: 5 (house price prediction) | Framework: scikit-learn -> ONNX",
    "Step 2-4/6: EZKL Pipeline": "EZKL v23.0.5 | Circuit: Halo2 | Proof: proof.json (18 KB) | Setup: pk.key (138 MB) + vk.key (66 KB) | SRS: kzg.srs (4 MB, logrows=15) | Verifier: Verifier.sol (73 KB)",
    "Step 5/6: Deploy Verifier": "Network: Sepolia (Chain ID: 11155111) | Contract: Halo2Verifier | Gas: ~2.2M | Deploy TX: " + DEPLOY_TX[:20] + "...",
    "Step 6/6: On-chain Verify": "Method: cast call verifyProof(calldata) | calldata: evm_calldata.hex (6858 bytes) | Expected: 0x000...0001 (TRUE)"
}

def run_pipeline_stream(task):
    yield f"data: {json.dumps({'type': 'start', 'task': task})}\n\n"
    yield f"data: {json.dumps({'type': 'info', 'text': 'Engine: Hermes Agent (tool calling)'})}\n\n"
    yield f"data: {json.dumps({'type': 'info', 'text': 'Network: Sepolia Testnet (Chain ID: 11155111)'})}\n\n"
    yield f"data: {json.dumps({'type': 'info', 'text': 'Contract: ' + CONTRACT_ADDR})}\n\n"

    steps = [
        ("Step 1/6: Model Check", step_1_train_model),
        ("Step 2-4/6: EZKL Pipeline", step_2_ezkl_pipeline),
        ("Step 5/6: Deploy Verifier", step_5_deploy),
    ]

    for label, fn in steps:
        yield f"data: {json.dumps({'type': 'step_start', 'label': label})}\n\n"
        time.sleep(0.5)  # demo pacing
        result = fn()
        detail = DETAILS.get(label, "")
        yield f"data: {json.dumps({'type': 'step_result', 'label': label, 'status': result.status, 'output': result.output, 'detail': detail, 'duration': f'{result.duration:.2f}s'})}\n\n"

    # Step 6
    label = "Step 6/6: On-chain Verify"
    yield f"data: {json.dumps({'type': 'step_start', 'label': label})}\n\n"
    time.sleep(1.0)  # dramatic pause
    result = step_6_verify(CONTRACT_ADDR)
    detail = DETAILS.get(label, "")
    yield f"data: {json.dumps({'type': 'step_result', 'label': label, 'status': result.status, 'output': result.output, 'detail': detail, 'duration': f'{result.duration:.2f}s'})}\n\n"

    yield f"data: {json.dumps({'type': 'done', 'contract': CONTRACT_ADDR, 'tx': DEPLOY_TX})}\n\n"

@app.route("/")
def index():
    return render_template("index.html", contract=CONTRACT_ADDR)

@app.route("/run", methods=["POST"])
def run():
    task = request.json.get("task", "")
    return Response(run_pipeline_stream(task), mimetype="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"})

@app.route("/contract")
def contract_info():
    return jsonify({"address": CONTRACT_ADDR, "network": "Sepolia", "deploy_tx": DEPLOY_TX, "etherscan": f"https://sepolia.etherscan.io/address/{CONTRACT_ADDR}"})

if __name__ == "__main__":
    print(f"\n  ZKML Pipeline Agent Web UI")
    print(f"  http://localhost:5000")
    print(f"  Contract: {CONTRACT_ADDR}\n")
    app.run(debug=True, host="0.0.0.0", port=5000, threaded=True)
