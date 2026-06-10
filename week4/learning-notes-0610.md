# Week 4 Day 3 学习笔记 | 2026-06-10

## 今日完成

### EVM Verifier 生成（突破 Windows 阻塞）
- ezkl 23.0.5 `create_evm_verifier` 在 Windows 下有 tokio async bug: "no running event loop"
- **解决**: 用 `asyncio.run(create_evm_verifier(...))` 绕过
- 生成 Verifier.sol (1426行, 72KB) + Verifier.abi

### Foundry 编译 + 链上部署
- 编译坑: Verifier.sol 有 "Stack too deep" 错误, 需 `via_ir = true`
- Deploy.s.sol: `vm.startBroadcast()` + `--private-key 0x$PRIVATE_KEY` 解决 envUint 的 hex prefix 问题
- 合约成功部署到 Sepolia

### 部署信息
- 合约地址: `0xE99Fb0F146DcBCAd66589C7BF9963B785EE5D495`
- 部署交易: `0xeecc08bf26fc1ede7eb379024161560eb321bb0a363a759ef0c82f4c29420fe7`
- Gas 消耗: ~2.26M
- Sepolia鏈接: https://sepolia.etherscan.io/address/0xe99fb0f146dcbcad66589c7bf9963b785ee5d495

### 踩坑记录
| 坑 | 解决 |
|----|------|
| ezkl async/no event loop | asyncio.run() |
| Stack too deep | foundry.toml via_ir = true |
| vm.envUint hex prefix | --private-key CLI flag |
| Etherscan 验证 | 网络不通(api.etherscan.io), 待手动 |

## 下一步 (Day 4)
- 链上 verifyProof: 用 proof + instances 调合约验证
- Z.AI GLM-5.1 API 接入 + function calling
- 端到端: 一句话 -> 全流程自动化
