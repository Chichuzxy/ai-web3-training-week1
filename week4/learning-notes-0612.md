# Week 4 Day 5 学习笔记 | 2026-06-12

项目: ZKML Pipeline Agent | 赛道: Z.AI Long-Horizon Task

## 今日完成

### 1. 链上 verifyProof 突破（从头闭环）

Day 4 遗留问题: 链上 verifyProof 一直 revert，本地验证却通过。

Day 5 根因定位:
  手动 eth_abi.encode(['bytes','uint256[]'], [proof, instances]) 编码的
  instances 格式与 Verifier.sol 内部期望格式不一致。
  ezkl 23.0.5 必须用 encode_evm_calldata() 生成 calldata。

操作步骤:
  1. 删除 pk.key / vk.key / proof.json / Verifier.sol（清空所有产物）
  2. 修复 ezkl_pipeline.py: create_evm_verifier 用 asyncio.run() 包装
  3. 一键跑 python ezkl_pipeline.py（setup -> prove -> create_evm_verifier）
  4. forge build + forge script deploy --broadcast
  5. ezkl.encode_evm_calldata() 生成正确 calldata
  6. cast call -> 0x01 (TRUE)

新合约: 0x75dBdd07fE81628c7aef5a8b48493Ebc200afD60 (Sepolia)

### 2. Agent 编排脚本

文件: agent-workflows/run_demo.py

6 步端到端 pipeline:
  Step 1 - 模型就绪检查 -> model.onnx (OK)
  Step 2-4 - EZKL 全流程 -> proof + Verifier.sol (SKIP, 已存在)
  Step 5 - 部署检查 -> 合约已部署 (SKIP)
  Step 6 - 链上验证 -> verifyProof returns TRUE

引擎选择:
  - Hermes Agent: 当前环境，免费，tool calling
  - GLM-4.7-Flash: Z.AI 免费模型，接入代码已写好
  - GLM-5.1: 付费，Z.AI 赛道旗舰

### 3. GLM API 测试

- GLM_API_KEY 已过期（401），但不影响 demo
- Hermes 本身即可完成全部编排

## 关键教训

| 坑 | 解决 |
|----|------|
| 手动 ABI 编码 instances 格式不对 | 必须用 ezkl.encode_evm_calldata() |
| create_evm_verifier Windows async bug | asyncio.run() 包装 |
| setup + prove + verifier 分开跑 VK 不对齐 | 必须一次脚本从头跑完 |

## 提交状态

- [x] Verifier 部署 + 链上验证通过
- [x] Agent 编排脚本 (run_demo.py)
- [ ] 根 README Week 4 状态更新
- [ ] Demo 截图/录屏
- [ ] 最终 push 到 GitHub
