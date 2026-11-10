---
title: NanoBot 课程顺序索引
create_at: 2026-08-26
update_at: 2026-08-27
tags: [MOC, AI, Agent, NanoBot, Curriculum]
---

# NanoBot 课程顺序索引

这里是“应该按什么顺序学习”的唯一入口。日期只记录学习发生时间，不再决定文件顺序。

## 编号规则

```text
M01-Ch00-L01
│   │    └── Lesson：章内小节，从 01 开始
│   └────── Chapter：全课程章节，00～39
└────────── Module：能力模块，01～08
```

目录与文件使用数字前缀自然排序：

```text
curriculum/
└── 01-最小闭环/
    └── 00-建立运行基线/
        ├── README.md
        ├── 01-安装与首次运行.md
        ├── 02-安装脚本TTY与WebUI构建.md
        └── ...
```

## 模块与章节顺序

| 模块 | 阶段（v2） | 章节 | 状态 |
|---|---|---|---|
| [M01 最小闭环](01-最小闭环/README.md) | Phase 1 | Ch00～Ch05 + 复习一 | 进行中：Ch00～Ch02 完成，Ch03 L01～L02 完成 |
| M02 上下文与状态 | Phase 2 | Ch06～Ch11 + 复习二 | 未开始（Ch08/09/11 为主线，Ch06/07/10 按需） |
| M03 工具与边界 | Phase 4 | Ch12～Ch17 | 未开始（按需） |
| M04 长程能力 | Phase 4 | Ch18～Ch20 + 复习三 | 未开始（按需） |
| M05 模型运行时 | Phase 4 | Ch21～Ch24 | 未开始（按需） |
| M06 输入输出与常驻运行 | Phase 4 | Ch25～Ch30 + 复习四 | 未开始（按需） |
| M07 公开入口与显示层 | Phase 4 | Ch31～Ch36 | 未开始（按需） |
| M08 掌握验证 | Phase 4 | Ch37～Ch39 | 未开始（按需） |

## 全部章节顺序

| 模块 | 按顺序学习的章节 |
|---|---|
| M01 最小闭环 | Ch00 建立运行基线 → Ch01 一次完整 Agent Turn → Ch02 MessageBus 与事件契约 → Ch03 AgentLoop → Ch04 AgentRunner → Ch05 Mini Nanobot |
| M02 上下文与状态 | Ch06 ContextBuilder → Ch07 Templates、Skills 与 Runtime Context → Ch08 Session Key 与 JSONL 持久化 → Ch09 Context Governance 与 Compaction → Ch10 Memory 与 Dream → Ch11 Hook、Streaming、Checkpoint 与 Turn Delivery |
| M03 工具与边界 | Ch12 Tool Contract、Schema、Registry 与 Loader → Ch13 Filesystem、Apply Patch、Search 与 File State → Ch14 Shell、Exec Session、取消与 Sandbox → Ch15 Web Search、Fetch 与 SSRF → Ch16 MCP、Agent Plugin、Skills 与 CLI Apps → Ch17 Subagent、Session Messaging 与 Runtime Control |
| M04 长程能力 | Ch18 Sustained Goal 与 Long Task → Ch19 Cron、Trigger、Heartbeat 与 Automation Turn → Ch20 图片、附件与音频转录 |
| M05 模型运行时 | Ch21 Config Schema、Loader 与 Watcher → Ch22 Model Preset、Runtime、Registry 与 Factory → Ch23 Provider Base、OpenAI Compatible 与 Responses API → Ch24 Specialized Provider、OAuth、Fallback 与 Conversation State |
| M06 输入输出与常驻运行 | Ch25 BaseChannel 与事件契约 → Ch26 Channel Registry、Manager 与 Outbound Delivery → Ch27 WebSocket Channel → Ch28 Bot SDK Channel 家族 → Ch29 企业、设备、联邦与邮件 Channel 家族 → Ch30 Gateway、Process Runtime、Lease 与 Pairing |
| M07 公开入口与显示层 | Ch31 Python SDK 与 OpenAI-compatible API → Ch32 Command Router 与 CLI → Ch33 WebUI Bootstrap 与 NanobotClient → Ch34 Stream Projection、Session 与活动状态 → Ch35 Components、Workbench 与 Settings → Ch36 构建、打包、部署、测试与安全总审计 |
| M08 掌握验证 | Ch37 架构内扩展 → Ch38 跨层故障诊断 → Ch39 架构答辩 |

## 使用方式

1. 从当前模块 README 找到标记为“下一章”的章节。
2. 进入章节 README，按 L01、L02、L03 顺序学习。
3. 日期视图只用于回顾学习历史，见[学习日志索引](../notes/学习日志索引.md)。
4. 完成小节后更新章节 README；完成章节后更新[进度板](../progress.md)。

详细目标与阶段安排以[学习路线 v2](../roadmap.md)为准。
