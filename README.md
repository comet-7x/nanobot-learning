# nanobot-learning

一套以源码为中心、持续 44 周的 [nanobot](https://github.com/HKUDS/nanobot)
学习项目。目标不是浏览完仓库，而是能够解释、修改、验证并维护一个完整的 Python Agent
Runtime。

当前学习基线：nanobot `0.3.0`，commit
[`9807e9cf`](https://github.com/HKUDS/nanobot/tree/9807e9cf37a5f5dcfad9dd86276dbda56e5363da)。

## 从这里开始

- [学习导读](quickstart.md)
- [课程顺序索引](curriculum/README.md)
- [44 周详细路线](roadmap.md)
- [学习进度板](progress.md)
- [源码学习协议](learning-protocol.md)
- [源码地图与版本锚点](source-map.md)
- [M01 · Ch00：建立运行基线](curriculum/01-最小闭环/00-建立运行基线/README.md)

## 仓库结构

```text
.
├── curriculum/     # 按模块、章节、小节编号组织的正式课程
├── experiments/    # 学习实验说明与独立实验代码
├── notes/          # 按日期回看的学习日志索引
├── reviews/        # D+1、D+7、D+30 与阶段复习
├── templates/      # 章节、日志、复习和能力矩阵模板
├── quickstart.md   # 总导读
├── roadmap.md      # 44 周课程
├── progress.md     # 唯一进度事实来源
└── source-map.md   # 上游版本与源码导航
```

正式材料使用 `MXX-ChXX-LXX` 稳定编号，例如 `M01-Ch00-L03`。目录按模块和章节分层，
小节文件使用 `01-`、`02-` 前缀排序；学习日期保留在文档元数据中。

## 学习边界

- 本仓库只保存学习材料和独立实验，不复制 nanobot 源码。
- nanobot 的 `main` 分支用于跟随上游；代码实验使用短期 `study/chXX-topic` 分支。
- 每章记录学习时对应的上游 commit，避免源码变化造成认知漂移。
- 所有正式实验由学习者先说明预期，再亲手执行并记录结果。

本项目也可以作为 Obsidian 笔记目录使用；仓库内统一采用标准 Markdown 链接，因此在
GitHub 和 Obsidian 中都可以导航。

## 关联仓库

- 上游源码：[HKUDS/nanobot](https://github.com/HKUDS/nanobot)
- 个人知识库：[comet-7x/My-NoteBook](https://github.com/comet-7x/My-NoteBook)
