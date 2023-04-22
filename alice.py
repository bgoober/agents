
# import the Agent class and the Context class
from uagents import Agent, Context

# create an agent named "alice"
alice = Agent(name="alice")

@alice.on_interval(period=2.0)
async def say_hello(ctx: Context):
    ctx.logger.info(f'hello, my name is {ctx.name}')

if __name__ == "__main__":
    alice.run()
