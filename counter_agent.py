# counter agent example

# import Agent and Context classes from uagents library
from uagents import Agent, Context

# create the Agent object, called agent, and name it "counter"
counter_agent = Agent(name = "counter")

# print your agent's identifier/address and its fetch network/wallet address
print("uAgent address/identifier: ", counter_agent.address)
print("Fetch network/wallet address: ", counter_agent.wallet.address())

# decorate the next function with an on_interval task
@counter_agent.on_interval(period=2.0)
async def increment_count(ctx: Context):

    # create a count object in the agent's storage, called "count", and if it doesn't exist yet set it to 0
    count = ctx.storage.get("count") or 0

    # print the count
    ctx.logger.info(f"The count is {count}")

    # set the count in storage to count + 1
    ctx.storage.set("count", count + 1)

    # get the count again from storage
    count = ctx.storage.get("count")

    # print the new count
    ctx.logger.info(f"The count is now {count}")

# run the agent if the script is being run as the main module, instead of imported to another script
if __name__ == "__main__":
    counter_agent.run()