---
title: NanoBot 源码地图与版本锚点
create_at: 2026-08-23
update_at: 2026-11-10
tags: [AI, Agent, NanoBot, Source-Map]
aliases: [NanoBot Source Map]
---

# NanoBot 源码地图与版本锚点

## 当前学习基线

| 项目 | 值 |
|---|---|
| Upstream | `https://github.com/HKUDS/nanobot` |
| 本地源码 | `/Users/comet/WorkSpace/Project/Python/nanobot`（`.venv` 已建，`import nanobot` 可用） |
| 分支 | `main` |
| Commit | `62c05e7f7e6573900af439047fe1579a03deea26` |
| 项目版本 | `v0.4.1-32` |
| 锚定日期 | `2026-11-10` |

固定版本源码链接前缀：

`https://github.com/HKUDS/nanobot/blob/62c05e7f7e6573900af439047fe1579a03deea26/`

## 一次 Turn 的源码地图

```mermaid
flowchart LR
    Channel["Channel"] --> Inbound["InboundMessage"]
    Inbound --> Bus["MessageBus"]
    Bus --> Loop["AgentLoop"]
    Loop --> Context["ContextBuilder"]
    Loop --> Session["SessionManager"]
    Loop --> Runner["AgentRunner"]
    Runner <--> Provider["LLMProvider"]
    Runner <--> Tools["ToolRegistry"]
    Runner --> Loop
    Loop --> Outbound["OutboundMessage"]
    Outbound --> Bus
    Bus --> Channel

    Memory["Memory / Dream"] -. "长期状态" .-> Context
    Runtime["Config / Model Runtime"] -. "模型与限制" .-> Loop
```

## 核心导航

| 责任 | 入口文件 | 学习章节 |
|---|---|---:|
| 消息事件与队列 | `nanobot/bus/events.py`, `nanobot/bus/queue.py` | 01～02 |
| Channel-facing Turn | `nanobot/agent/loop.py` | 01、03 |
| Model-facing Tool Loop | `nanobot/agent/runner.py` | 01、04 |
| 上下文装配 | `nanobot/agent/context.py` | 06～07 |
| Session 持久化 | `nanobot/session/manager.py` | 08～09 |
| 长期记忆 | `nanobot/agent/memory.py` | 10 |
| Hook 与投递 | `nanobot/agent/hook.py`, `turn_hooks.py`, `turn_delivery.py` | 11 |
| Tool 契约与发现 | `nanobot/agent/tools/base.py`, `registry.py`, `loader.py` | 12 |
| 文件与 Shell | `nanobot/agent/tools/filesystem.py`, `shell.py`, `sandbox.py` | 13～14 |
| Web 与 SSRF | `nanobot/agent/tools/web.py`, `nanobot/security/network.py` | 15 |
| MCP 与插件 | `nanobot/agent/tools/mcp.py`, `nanobot/agent/plugins.py` | 16 |
| Subagent 与持续目标 | `nanobot/agent/subagent.py`, `tools/spawn.py`, `tools/long_task.py` | 17～18 |
| 自动化 | `nanobot/cron/`, `nanobot/triggers/` | 19 |
| 配置 | `nanobot/config/schema.py`, `loader.py`, `watcher.py` | 21 |
| Provider | `nanobot/providers/base.py`, `registry.py`, `factory.py` | 22～24 |
| Channel | `nanobot/channels/base.py`, `manager.py`, `registry.py` | 25～29 |
| WebSocket | `nanobot/channels/websocket/runtime.py` | 27 |
| Gateway | `nanobot/gateway/runtime.py`, `nanobot/cli/gateway_runtime.py` | 30 |
| SDK 与 API | `nanobot/sdk/`, `nanobot/api/server.py` | 31 |
| CLI 与命令 | `nanobot/cli/`, `nanobot/command/` | 32 |
| WebUI 连接层 | `webui/src/lib/nanobot-client.ts` | 33 |
| WebUI 状态投影 | `webui/src/hooks/useNanobotStream.ts` | 34 |
| WebUI 页面 | `webui/src/App.tsx`, `webui/src/components/` | 35 |

## 架构约束导航

- 项目架构：`docs/architecture.md`
- 核心保持小型：`.agent/design.md`
- Workspace、SSRF、Sandbox：`.agent/security.md`
- 原子写、Prompt、Windows 等陷阱：`.agent/gotchas.md`
- 贡献规范：`CONTRIBUTING.md`

## 版本更新记录

每次切换学习基线时追加，不覆盖历史。

| 日期 | 旧 Commit | 新 Commit | 影响章节 | 处理结果 |
|---|---|---|---|---|
| 2026-08-23 | — | `9807e9cf` | 初始基线 | 创建路线 |
| 2026-11-10 | `9807e9cf`（0.3.0） | `62c05e7f`（v0.4.1-32） | Ch01~Ch03 已学章节；Ch04 起按新基线学 | 见下方漂移清单 |

## 0.3.0 → v0.4.1 核心漂移清单（2026-11-10 核对）

已学章节的概念笔记仍然有效，以下方法名/结构变化需要在对应章节学习时以新基线为准：

| 位置 | 旧（0.3.0） | 新（v0.4.1） | 影响 |
|---|---|---|---|
| `agent/loop.py` | `_dispatch(msg)` | `_dispatch_one(msg)` | Ch03 L01/L02 笔记中的方法名 |
| `agent/loop.py` | 七阶段内联在 `_process_message` | 抽出 `_run_turn_stage(ctx, name, fn)` 统一包装（restore/compact/command/build/run/save/respond 不变） | Ch01/Ch03 行号失效，阶段名不变 |
| `agent/loop.py` | `_build_initial_messages` | `_build_transcript_input`（TranscriptInput） | Ch01 调用链 |
| `agent/runner.py` | `_build_goal_continue_message` | `_build_continuation_message` | Ch04 学习时注意 |
| `agent/runner.py` | — | 新增 `_emit_checkpoint`、`_append_model_error_placeholder` | Ch04/Ch11 新机制 |
| `bus/` | `progress.py` 存在 | `progress.py` 删除，新增 `delivery.py`、`notification_delivery.py` | Ch02 出站事件结构 |
| `bus/queue.py` | 114 行变化 | 队列实现重构 | Ch02 概念不变，实现细节以新基线为准 |

未变化（已核对）：`consume_inbound`、`_effective_session_key`、`_get_session_lock`、
`AgentRunSpec`/`AgentRunResult`、`AgentRunner.run/_run_core/_request_model/_execute_tools`、
七阶段名称与顺序。
