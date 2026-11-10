"""Minimal experiment for MessageBus inbound queue wake-up behavior."""

import asyncio

from nanobot.bus.events import InboundMessage
from nanobot.bus.queue import MessageBus


async def consume_one(bus: MessageBus) -> InboundMessage:
    print("consumer: waiting")
    message = await bus.consume_inbound()
    print(f"consumer: received {message.content!r}")
    return message


async def main() -> None:
    bus = MessageBus()
    original = InboundMessage(
        channel="learning",
        sender_id="comet",
        chat_id="ch02",
        content="hello queue",
    )

    consumer_task = asyncio.create_task(consume_one(bus))
    await asyncio.sleep(0)  # Let the consumer reach the empty queue first.

    print(f"consumer waiting before publish: {not consumer_task.done()}")
    await bus.publish_inbound(original)

    received = await consumer_task
    print(f"received is original object: {received is original}")
    print(f"final inbound size: {bus.inbound_size}")


if __name__ == "__main__":
    asyncio.run(main())
