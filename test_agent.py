from uagents import Agent

alice1 = Agent(name="alice")

print("uAgent address: ", alice1.address)
print("Fetch network address: ", alice1.wallet.address())
