# Week 4 Day 1-2 学习笔记 | 2026-06-09

主方向: Privacy & Security -> ZKML 推理验证
赛道: Z.AI | Web3 x Long-Horizon Task
项目: ZKML Pipeline Agent

## 今日完成

### 模型训练 + ONNX 导出 (Day 1)

- 用 sklearn 训练线性回归模型 (5 特征, 500 样本, 归一化)
- 遇到 skl2onnx 导出的 LinearRegressor 算子 EZKL 不认
- 解决: 手动构建 ONNX 图，用 Gemm 原始算子 (MatMul + Add)
- model.onnx: 1 节点, 291 字节，推理结果与 sklearn 完全对齐

### EZKL 全链路 (Day 1-2)

- ezkl 23.0.5 Windows 预编译包直接 pip install 成功
- 跑通全流程: gen_settings -> calibrate -> compile -> gen_srs -> setup -> gen_witness -> prove -> verify
- Proof: project/ezkl_output/proof.json (18160 bytes)
- 本地验证通过 (verify OK)

踩坑记录:
  - ezkl 23.0.5 API 大改: calibrate_settings/gen_witness 参数从 dict 改为文件路径
  - get_srs/prove 等函数参数名变了 (需要 keyword args)
  - gen_srs 返回 None 而非 True/False
  - create_evm_verifier 在 Windows 下有 async Rust 线程 bug (pyo3 panic)
  - 数据归一化后才能通过 calibration (原始数据范围太大会报分解错误)

### 环境建设

- .env 文件已创建 (.gitignore 已配置)
- pk.key (138MB) + kzg.srs (4MB) 加入 .gitignore
- SSH config 修复: github.com 优先用 id_ed25519
- Git 推送到 GitHub 仍然卡在 SSH 认证 (id_ed25519 不在 Chichuzxy 账号上)

### 已验证的技术栈

| 组件 | 状态 |
|------|------|
| sklearn + ONNX (Gemm) | done |
| EZKL gen_settings | done |
| EZKL calibrate | done |
| EZKL compile_circuit | done |
| EZKL setup (pk + vk) | done |
| EZKL prove | done |
| EZKL verify (local) | done |
| EZKL create_evm_verifier | blocked (Win async bug) |

## 仍未解决

- EVM Verifier 合约: ezkl Windows async bug，需 Colab 生成
- Z.AI / GLM-5.1 API 联通测试: 待新 API Key (旧 key 已泄露作废)
- Git push: id_ed25519 未通过 GitHub 认证
- Sepolia 测试币未领
- Foundry 合约编译 + 部署

## 下一步 (Day 3)

- Z.AI API Key 获取 -> GLM-5.1 联通测试 -> Function Calling
- Verifier.sol 在 Colab 生成 -> 传输到本地
- Foundry 编译 Verifier -> Sepolia 部署
