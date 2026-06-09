# Week 3 学习笔记 | 2026-06-06

主方向: Privacy & Security -> ZKML 推理验证
目标赛道: Z.AI | Web3 x Long-Horizon Task
项目: ZKML Pipeline Agent

---

## 今日完成

- 交叉诊断 README 与实际状态，发现并修复 3 处不一致
  - week3 标记 Foundry "未完成" -> 实际已安装
  - week3 标记 GLM API "未完成" -> glm-api-plan.md 已存在
  - week3 标记组队 "待确认" -> team.md 已完整
- Foundry PATH 写入 .bashrc（export PATH="$HOME/.foundry/bin:$PATH"）
- 验证根 README + week3/README 全部状态同步
- Foundry 环境确认: forge 1.7.1, contracts 编译 + 2 tests pass

## Week 3 状态

全部 10 项交付物完成:
1. 缺口诊断
2. 更新后的根 README
3. 1 页 proposal memo
4. 2-3 份深度研究摘要 (EZKL/Circom-SnarkJS/Halo2-Groth16)
5. 1 份 risk memo
6. Hackathon 方向卡
7. Repo skeleton + sprint plan
8. Foundry 项目初始化 (forge 1.7.1, 2 tests passed)
9. GLM API 集成调研 (glm-api-plan.md)
10. 组队信息 (team.md)

## 下一步 (Week 4)

- 申请 GLM-5.1 API Key (z.ai)
- Day 1: 训练模型 + EZKL 环境搭建
- Day 2: Proof 生成 + Verifier 合约
- Day 3: Sepolia 部署 + 链上验证
- Day 4: Agent 编排 + 端到端
- Day 5: 打磨 + 提交
