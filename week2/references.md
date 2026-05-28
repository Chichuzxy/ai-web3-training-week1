# Week 2 | 参考资料清单

**作者:** Chichuzxy  
**日期:** 2026-05-28  
**方向:** Privacy & Security / ZKML

---

## 一、ZKML 项目 (实操参考)

| 项目 | 链接 | 说明 |
|------|------|------|
| EZKL | https://github.com/zkonduit/ezkl | ONNX → ZK 电路，当前最易用的 ZKML 框架 |
| Modulus Labs | https://modulus.xyz | ZKML 基础设施，有详细技术博客 |
| Giza | https://giza.tech | AI Agent + ZK 验证，Casino (链上 AI 框架) |
| Giza Starknet Agent | https://github.com/gizatechxyz/Orion | Starknet 上的 ZKML 推理 |
| EZKL Examples | https://docs.ezkl.xyz | 官方教程，含线性回归、MNIST 等 |

## 二、ZK 证明系统 (理论 + 工具)

| 资源 | 链接 | 说明 |
|------|------|------|
| Circom 官方文档 | https://docs.circom.io | 电路编写语言，入门必读 |
| circomlib | https://github.com/iden3/circomlib | 标准电路库 (哈希、比较器等) |
| Halo2 文档 | https://zcash.github.io/halo2 | EZKL 底层证明系统 |
| SnarkJS | https://github.com/iden3/snarkjs | Groth16/Plonk 证明生成和验证 |
| ZK-SNARKs 入门 | https://zkp.science | 学术资源汇总 |

## 三、论文 (学术支撑)

| 论文 | 年份 | 核心内容 |
|------|------|----------|
| zkCNN: Zero Knowledge Proofs for Convolutional Neural Network | 2021 | 用 ZKP 验证 CNN 推理，开创性工作 |
| ZKML: Verifiable ML with Zero-Knowledge Proofs | 2023 | EZKL 团队技术报告 |
| Modulus Labs Research | 2023 | ZKML 性能优化方向 |
| Verifiable Computation for ML (vCNN) | 2022 | 验证卷积层计算的正确性 |
| On-Chain Machine Learning (DCML) | 2023 | 去中心化 ML 推理框架设计 |

## 四、Layer2 / 部署参考

| 资源 | 链接 | 说明 |
|------|------|------|
| Sepolia 测试网 | https://sepolia.etherscan.io | 主要部署目标 |
| Arbitrum Sepolia | https://sepolia.arbiscan.io | 备选 (gas 更低) |
| Foundry Book | https://book.getfoundry.sh | 合约开发和测试框架 |
| OpenZeppelin Contracts | https://docs.openzeppelin.com/contracts | 安全合约库 |

## 五、训练营相关

| 资源 | 说明 |
|------|------|
| AI x Web3 School 课件 | 训练营 Week 1-2 材料 |
| Week 1 Repo | https://github.com/Chichuzxy/ai-web3-training-week1 |
| Week 1 问题地图 | module-a-ai-patterns/problem-map.md |

---

## 阅读优先级

1. EZKL 官方文档 -- 直接指导 PoC 开发
2. Circom 入门文档 -- 理解电路编写基础
3. zkCNN 论文 -- 理解 ZKML 的核心思路
4. Modulus Labs 博客 -- 了解工业级 ZKML 方案
