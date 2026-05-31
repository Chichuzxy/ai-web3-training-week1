# Week 2 | AI x Web3 问题地图 & Proposal

**日期:** 2026-05-28 ~ 2026-05-30
**主方向:** Privacy & Security -> ZKML (零知识证明机器学习)
**前置:** Week 1 完成

---

## Bootcamp Week 2 核心任务

构建 AI x Web3 问题地图，选定一个主方向做深挖，产出 Proposal。

关键判断标准: AI 的角色和 Web3 机制是否都不可替代。

---

## 交付物 (7 项)

| # | 交付物 | 文件 | 状态 |
|---|--------|------|------|
| 1 | 问题地图 | problem-map.md | done |
| 2 | 方向选择说明 | direction-selection.md | done |
| 3 | 问题拆解 | problem-decomposition.md | done |
| 4 | 初步 Proposal | proposal-zkml.md | done |
| 5 | 参考资料 | references.md | done |
| 6 | 主方向深挖包 | deep-dive-package.md | done |
| 7 | 方向 backlog | direction-backlog.md | done |

---

## 目录结构

```
week2/
├── README.md                    # 本文件
├── problem-map.md               # [1] 问题地图 (6 方向 x AI/Web3 不可替代性判断)
├── direction-selection.md       # [2] 方向选择 -> ZKML
├── problem-decomposition.md     # [3] 核心问题五层拆解
├── proposal-zkml.md             # [4] ZKML 初步 Proposal
├── references.md                # [5] 参考资料清单
├── deep-dive-package.md         # [6] 主方向深挖包: 流程图/场景/反例/风险/验证计划
├── direction-backlog.md         # [7] 方向 backlog (未选方向 + 不选原因)
│
├── artifacts/
│   └── circom-poc/              # Circom PoC 产物 (电路/证明/验证密钥)
│       ├── basicAdd.circom
│       ├── input.json
│       ├── proof.json
│       ├── public.json
│       └── verification_key.json
│
└── circom-debug-log.md          # Circom 调试记录 (版本/语法/CRLF)
```

---

## 主方向: Privacy & Security -> ZKML

核心问题: 如何不暴露模型权重的前提下，让链上合约验证 AI 推理结果？

不可替代性分析:
- AI 侧: ZK 电路需要 ML 模型推理逻辑 -> AI 不可替代
- Web3 侧: 验证结果存于不可篡改的链上 -> Web3 不可替代
- 交叉点: ZK 证明将 AI 推理的可信度锚定到链上

更多细节见 proposal-zkml.md + deep-dive-package.md。

---

## 安全红线

- 私钥/助记词永不暴露给 AI
- 所有链上操作仅限测试网
- 每笔交易须人工确认
- AI 生成代码须人工审查后部署
