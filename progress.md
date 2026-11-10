---
title: NanoBot 学习进度板
create_at: 2026-08-23
update_at: 2026-08-28
tags: [AI, Agent, NanoBot, Progress]
aliases: [NanoBot Progress]
---

# NanoBot 学习进度板

## 当前状态

| 项目 | 内容 |
|---|---|
| 当前模块 | M01：最小闭环 |
| 当前章节 | 第 03 章：AgentLoop（L01～L02 已完成） |
| 学习状态 | 已理解 create_task、协作式并发及 per-session serial / cross-session concurrent |
| 每周预算 | 6～8 小时 |
| 当前源码 | `main@9807e9cf37a5f5dcfad9dd86276dbda56e5363da` |
| 下一个动作 | 观察优先命令、活动 Session follow-up 与新 Turn 三个入站分支 |
| 好奇心停车场 | 回答引用机制由哪个模块负责；官方 Wiki 与源码如何对应 |

## 章节进度

### 模块 M01：最小闭环

- [x] 00 建立运行基线
- [x] 01 一次完整 Agent Turn
- [x] 02 MessageBus 与事件契约
- [ ] 03 AgentLoop（进行中：L01～L02 已完成）
- [ ] 04 AgentRunner
- [ ] 05 Mini Nanobot
- [ ] 复习一

### 模块 M02：上下文与状态

- [ ] 06 ContextBuilder
- [ ] 07 Templates、Skills 与 Runtime Context
- [ ] 08 Session Key 与 JSONL 持久化
- [ ] 09 Context Governance 与 Compaction
- [ ] 10 Memory 与 Dream
- [ ] 11 Hook、Streaming、Checkpoint 与 Turn Delivery
- [ ] 复习二

### 模块 M03：工具与边界

- [ ] 12 Tool Contract、Schema、Registry 与 Loader
- [ ] 13 Filesystem、Apply Patch、Search 与 File State
- [ ] 14 Shell、Exec Session、取消与 Sandbox
- [ ] 15 Web Search、Fetch 与 SSRF
- [ ] 16 MCP、Agent Plugin、Skills 与 CLI Apps
- [ ] 17 Subagent、Session Messaging 与 Runtime Control

### 模块 M04：长程能力

- [ ] 18 Sustained Goal 与 Long Task
- [ ] 19 Cron、Trigger、Heartbeat 与 Automation Turn
- [ ] 20 图片、附件与音频转录
- [ ] 复习三

### 模块 M05：模型运行时

- [ ] 21 Config Schema、Loader 与 Watcher
- [ ] 22 Model Preset、Runtime、Registry 与 Factory
- [ ] 23 Provider Base、OpenAI Compatible 与 Responses API
- [ ] 24 Specialized Provider、OAuth、Fallback 与 Conversation State

### 模块 M06：Channel 与 Gateway

- [ ] 25 BaseChannel 与事件契约
- [ ] 26 Channel Registry、Manager 与 Outbound Delivery
- [ ] 27 WebSocket Channel
- [ ] 28 Bot SDK Channel 家族
- [ ] 29 企业、设备、联邦与邮件 Channel 家族
- [ ] 30 Gateway、Process Runtime、Lease 与 Pairing
- [ ] 复习四

### 模块 M07：公开入口与显示层

- [ ] 31 Python SDK 与 OpenAI-compatible API
- [ ] 32 Command Router 与 CLI
- [ ] 33 WebUI Bootstrap 与 NanobotClient
- [ ] 34 Stream Projection、Session 与活动状态
- [ ] 35 Components、Workbench 与 Settings
- [ ] 36 构建、打包、部署、测试与安全总审计

### 模块 M08：掌握验证

- [ ] 37 架构内扩展
- [ ] 38 跨层故障诊断
- [ ] 39 架构答辩

## 阶段作品

- [ ] Mini Nanobot
- [ ] Session/Context 检视器
- [ ] 带安全边界的自定义 Tool
- [ ] 可恢复的长程自动化
- [ ] Provider 对照运行记录
- [ ] WebSocket 客户端
- [ ] Provider 能力矩阵
- [ ] Channel 能力矩阵
- [ ] SDK/API/CLI/WebUI 四入口追踪图
- [ ] 可提交质量的扩展功能
- [ ] 最终架构答辩文档

## 单章解锁检查

完成一章时填写；五项至少四项为真，才进入下一章。

- [x] 我能脱稿画出本章流程。
- [x] 我能解释涉及模块的责任边界。
- [x] 我能判断一个需求应修改哪个模块。
- [x] 我能运行或编写相关测试。
- [ ] 我能完成一个小修改并预测影响。

## 间隔复习队列

| 知识点 | 最近复习 | 等级 | 下一次复习 | 薄弱点 |
|---|---|---:|---|---|
| Ch00 CLI 启动链与入口分流 | 2026-08-27 | 1：模糊 | 2026-08-30 | 入口加载成本误绑定为渲染/进程成本 |
| Ch01 完整 Turn 主干 | 2026-08-28 | 2：清晰 | 2026-09-04（D+7） | 保留流式显示与持久化边界 |
| Ch02 MessageBus 与事件契约 | 2026-08-28 | 2：清晰 | 2026-09-04（D+7） | 术语：Channel 适配器、进程内异步队列 |

## 好奇心停车场

学习中发现但不属于当前章节的问题统一放在这里，复习周再处理。

- [ ] 回答引用机制由 Provider、Web Tool、Prompt 还是显示层负责？
- [ ] 为 0.3.0 Wiki 的功能说明建立源码映射。
- [ ] 异步测试前确认 dev extras 与 `pytest-asyncio` 已加载，消除 `asyncio_mode` 警告。

## 本周记录

| 日期 | 学习块 | 产物 | 下一步 |
|---|---:|---|---|
| 2026-08-24 | 首次运行与安装诊断 | 服务、本地模型和引用回答验证成功；分离安装、TTY 向导和 WebUI bundle 三层问题 | 完成一句话骨架，再做一次环境路径验证 |
| 2026-08-25 | Editable 安装、主动复习与 CLI 启动链 | 用包元数据证明源码关联；掌握 PATH、shebang、TTY 与 console script | 次日继续 Typer、TUI、Gateway 与公开入口 |
| 2026-08-26 | Typer、TUI、Gateway 与第 00 章验收 | 四入口关系图；`tests/cli/test_entry.py` 结果 `2 passed`；统一解锁 4/5 | D+1 主动回忆后开始第 01 章 |
| 2026-08-27 | Ch00 D+1 + Ch01 L01～L03 + Ch02 L01～L03 | 完成 Turn 主干；掌握异步队列、事件契约并验证队列唤醒 | 进入 Ch03 AgentLoop |
| 2026-08-28 | Ch03 L02 | 区分 session_key 的状态归属与 Session lock 的并发保护 | 追踪 AgentLoop 入站分支 |
