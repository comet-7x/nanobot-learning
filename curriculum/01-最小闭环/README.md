---
title: NanoBot 模块 M01：最小闭环
create_at: 2026-08-26
update_at: 2026-08-27
tags: [MOC, AI, Agent, NanoBot, Module]
module: 01
status: in-progress
---

# M01：最小闭环

## 模块目标

从可复现运行基线出发，先看见一次完整 Agent Turn，再依次打开 MessageBus、AgentLoop、
AgentRunner，最后独立完成 Mini Nanobot。

```mermaid
flowchart LR
    C00["Ch00 运行基线"] --> C01["Ch01 一次完整 Turn"]
    C01 --> C02["Ch02 MessageBus"]
    C02 --> C03["Ch03 AgentLoop"]
    C03 --> C04["Ch04 AgentRunner"]
    C04 --> C05["Ch05 Mini Nanobot"]
    C05 --> R1["复习一"]
```

## 章节顺序

| 顺序 | 章节 | 状态 | 核心产物 |
|---:|---|---|---|
| 01 | [Ch00 建立运行基线](00-建立运行基线/README.md) | 已完成 | 可复现基线、入口地图 |
| 02 | [Ch01 一次完整 Agent Turn](01-一次完整AgentTurn/README.md) | 已完成 | 端到端 Turn 图 |
| 03 | [Ch02 MessageBus 与事件契约](02-MessageBus与事件契约/README.md) | 已完成 | 最小异步消息总线 |
| 04 | [Ch03 AgentLoop](03-AgentLoop/README.md) | 进行中：L01 已完成 | 入站分支地图 |
| 05 | Ch04 AgentRunner | 未开始 | Runner 状态机 |
| 06 | Ch05 Mini Nanobot | 未开始 | 150～300 行 Mini Agent |
| 07 | 复习一 | 未开始 | 脱稿重画与故障定位 |

返回[课程顺序总索引](../README.md)。
