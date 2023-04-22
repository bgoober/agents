from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model


class Message(Model):
    message: str


bob = Agent(
    name="bob",
    port=8001,
    seed="tool model void slim mixed brave muffin inform swim loyal envelope front mind feed hold timber like shove cube donor paddle walk opinion elder",
    endpoint=["http://127.0.0.1:8001/submit"],
)

fund_agent_if_low(bob.wallet.address())

# print your agent's identifier/address and its fetch network/wallet address
print("uAgent address/identifier: ", bob.address)
print("Fetch network/wallet address: ", bob.wallet.address())

@bob.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")

    # send the response
    await ctx.send(sender, Message(message="hello there alice"))


if __name__ == "__main__":
    bob.run()
