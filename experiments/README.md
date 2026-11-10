# 学习实验

这里保存可以脱离 nanobot 主仓库运行的最小实验，例如消息队列、Mini Agent、状态机和
协议转换器。

需要直接修改 nanobot 源码的实验应放在源码仓库的短期 `study/chXX-topic` 分支中；本目录
只记录实验目标、预期、结果和必要的独立代码，避免复制上游源码。

实验目录建议命名：

```text
chXX-short-topic/
├── README.md
├── src/
└── tests/
```

## 已完成实验

- [Ch02 MessageBus 队列唤醒](ch02_message_bus_wakeup.py)：验证空队列等待、发布后唤醒、
  对象引用传递与最终队列大小。
