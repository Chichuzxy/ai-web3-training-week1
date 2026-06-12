# ezkl_pipeline.py - EZKL 全流程 (ezkl 23.0.5 API)
# ZKML Pipeline Agent: Day 1-2

import ezkl
import json
import os
import numpy as np

MODEL_PATH = "project/models/model.onnx"
OUTPUT_DIR = "project/ezkl_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)
data = np.load("model_test_data.npz")

def check_file(path, label):
    assert os.path.exists(path), f"{label} NOT FOUND: {path}"
    print(f"  {label}: {path} ({os.path.getsize(path)} bytes)")

# Step 1-3: gen_settings + calibrate + compile (skip if compiled.model exists)
if not os.path.exists(f"{OUTPUT_DIR}/compiled.model"):
    print("=== Step 1: gen_settings ===")
    run_args = ezkl.PyRunArgs()
    run_args.input_visibility = "public"
    run_args.output_visibility = "public"
    run_args.param_visibility = "fixed"
    ezkl.gen_settings(MODEL_PATH, f"{OUTPUT_DIR}/settings.json", run_args)

    print("=== Step 2: calibrate_settings ===")
    cal_data = {"input_data": data["X_test"].reshape((-1, 5)).tolist()}
    cal_path = f"{OUTPUT_DIR}/cal_data.json"
    json.dump(cal_data, open(cal_path, "w"))
    ezkl.calibrate_settings(data=cal_path, model=MODEL_PATH,
        settings=f"{OUTPUT_DIR}/settings.json", target="resources")

    print("=== Step 3: compile_circuit ===")
    ezkl.compile_circuit(MODEL_PATH, f"{OUTPUT_DIR}/compiled.model",
        f"{OUTPUT_DIR}/settings.json")
    print("  compiled OK")
else:
    print("=== Steps 1-3: SKIP (compiled.model exists) ===")

# Step 4: gen_srs (returns None on success, check file)
if not os.path.exists(f"{OUTPUT_DIR}/kzg.srs"):
    print("=== Step 4: gen_srs ===")
    settings = json.load(open(f"{OUTPUT_DIR}/settings.json"))
    logrows = settings.get("run_args", {}).get("logrows", 15)
    ezkl.gen_srs(f"{OUTPUT_DIR}/kzg.srs", logrows)
    check_file(f"{OUTPUT_DIR}/kzg.srs", "SRS")
else:
    print("=== Step 4: SKIP (kzg.srs exists) ===")

# Step 5: setup
if not os.path.exists(f"{OUTPUT_DIR}/pk.key"):
    print("=== Step 5: setup ===")
    ezkl.setup(
        model=f"{OUTPUT_DIR}/compiled.model",
        vk_path=f"{OUTPUT_DIR}/vk.key",
        pk_path=f"{OUTPUT_DIR}/pk.key",
        srs_path=f"{OUTPUT_DIR}/kzg.srs"
    )
    check_file(f"{OUTPUT_DIR}/vk.key", "vk")
    check_file(f"{OUTPUT_DIR}/pk.key", "pk")
else:
    print("=== Step 5: SKIP (pk.key exists) ===")

# Step 6: gen_witness
print("=== Step 6: gen_witness ===")
sample_input = data["X_test"][:1].reshape((1, 5)).tolist()
witness_in = {"input_data": sample_input}
witness_path = f"{OUTPUT_DIR}/witness_input.json"
json.dump(witness_in, open(witness_path, "w"))
ezkl.gen_witness(data=witness_path, model=f"{OUTPUT_DIR}/compiled.model",
    output=f"{OUTPUT_DIR}/witness.json", vk_path=f"{OUTPUT_DIR}/vk.key",
    srs_path=f"{OUTPUT_DIR}/kzg.srs")
check_file(f"{OUTPUT_DIR}/witness.json", "witness")

# Step 7: prove
print("=== Step 7: prove ===")
ezkl.prove(witness=f"{OUTPUT_DIR}/witness.json", model=f"{OUTPUT_DIR}/compiled.model",
    pk_path=f"{OUTPUT_DIR}/pk.key", srs_path=f"{OUTPUT_DIR}/kzg.srs",
    proof_path=f"{OUTPUT_DIR}/proof.json")
check_file(f"{OUTPUT_DIR}/proof.json", "proof")

# Step 8: verify
print("=== Step 8: verify ===")
assert ezkl.verify(proof_path=f"{OUTPUT_DIR}/proof.json",
    settings_path=f"{OUTPUT_DIR}/settings.json",
    vk_path=f"{OUTPUT_DIR}/vk.key",
    srs_path=f"{OUTPUT_DIR}/kzg.srs"), "verify failed"
print("  PROOF VERIFIED OK")

# Step 9: create EVM Verifier
print("=== Step 9: create_evm_verifier ===")
import asyncio
os.makedirs("contracts/src", exist_ok=True)
async def _create_verifier():
    await ezkl.create_evm_verifier(
        vk_path=f"{OUTPUT_DIR}/vk.key",
        settings_path=f"{OUTPUT_DIR}/settings.json",
        sol_code_path="contracts/src/Verifier.sol",
        abi_path=f"{OUTPUT_DIR}/Verifier.abi",
        srs_path=f"{OUTPUT_DIR}/kzg.srs"
    )
asyncio.run(_create_verifier())
check_file("contracts/src/Verifier.sol", "Verifier.sol")

print("\n=== ALL DONE ===")
print(f"Proof: {OUTPUT_DIR}/proof.json")
print(f"Verifier: contracts/src/Verifier.sol")
