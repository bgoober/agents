from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model


class Message(Model):
    message: str

# my  version of bob's agent identifier address
RECIPIENT_ADDRESS = "agent1qg60aduf2zq4k7us6kxmpxjpjwe6urttuywj3zrvm4ujt0p7duln5n22vqv"

alice = Agent(
    name="alice",
    port=8000,
    seed="birth hope jar nasty protect large company hotel that seven reduce believe theory valve verb practice joke planet joke mind innocent anchor shiver shell",
    endpoint=["http://127.0.0.1:8000/submit"],
)

fund_agent_if_low(alice.wallet.address())

# print your agent's identifier/address and its fetch network/wallet address
print("uAgent address/identifier: ", alice.address)
print("Fetch network/wallet address: ", alice.wallet.address())

@alice.on_interval(period=2.0)
async def send_message(ctx: Context):
    await ctx.send(RECIPIENT_ADDRESS, Message(message="hello there bob"))


@alice.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")


if __name__ == "__main__":
    alice.run()
