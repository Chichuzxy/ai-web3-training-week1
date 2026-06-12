# Week 4 Day 4 学习笔记 | 2026-06-11

项目: ZKML Pipeline Agent | 赛道: Z.AI Long-Horizon Task

## 今日完成

### 链上 verifyProof 调试

目标: 用 proof.json + instances 调已部署的 Verifier 合约 (0xE99Fb0F146DcBCAd66589C7BF9963B785EE5D495)

过程:
  1. 本地验证 proof 有效: ezkl.verify() -> True
  2. ABI 编码 calldata: eth_abi.encode(['bytes','uint256[]'], [proof, instances])
  3. cast call -> revert
  4. 合约 bytecode 对比: forge inspect deployedBytecode vs cast code -> EXACT MATCH
  5. 重新生成 proof + 本地验证 -> True，链上仍 revert

根因定位:
  Day 2 生成 proof.json，Day 3 单独跑 create_evm_verifier
  中间 ezkl_pipeline.py 被重新执行的话，gen_witness + prove 会被重跑
  如果 setup 也被重跑过，vk.key 就会变，导致 Verifier.sol 里的 VK 与 proof 不匹配

解决方案:
  删 pk.key / vk.key / proof.json / Verifier.sol
  一键跑 ezkl_pipeline.py（setup -> prove -> create_evm_verifier 连续执行）
  重新编译 + 部署 + verifyProof

### 验证方法沉淀

| 需求 | 方法 |
|------|------|
| 本地 proof 验证 | ezkl.verify(proof_path=, settings_path=, vk_path=, srs_path=) |
| 合约 bytecode 获取 | forge inspect Contract:Name deployedBytecode --via-ir |
| 链上 bytecode 获取 | cast code --rpc-url <URL> <address> |
| ABI 编码 | eth_abi.encode(['bytes','uint256[]'], [proof_bytes, instances]) |
| selector 计算 | eth_utils.keccak(text='verifyProof(bytes,uint256[])')[:4] |
| 合约调用 trace | cast call --trace <address> <calldata> |

### 技术要点

EZKL verify API (23.0.5 vs 旧版):
  - 旧版: ezkl.verify(proof_path, vk_path, settings_path) 位置参数
  - 23.0.5: ezkl.verify(proof_path=, settings_path=, vk_path=, srs_path=) keyword args
  - 必须同时传 srs_path，否则解析失败

Halo2Verifier:
  - 1426 行 Solidity assembly
  - verifyProof(bytes,uint256[]) returns bool
  - 每次验证 gas ~149k (revert 时) 到 ~270k (完整)

## 仍未解决

- 链上 verifyProof: 需重新走完整闭环
- GLM-5.1 API 接入
- Pipeline 配置 + 端到端自动化

## 下一步 (Day 5)

- 重跑 ezkl_pipeline.py 从头闭环
- 重新编译 + 部署 Verifier 到 Sepolia
- 链上 verifyProof 确认通过
- 接入 GLM-5.1 API + function calling
- Demo 截图 / 录屏
