from cosmpy.aerial.wallet import LocalWallet
from cosmpy.crypto.keypairs import PrivateKey
from cosmpy.aerial.client import LedgerClient, NetworkConfig

# To create a random private key:
# private_key = PrivateKey()

# wallet = LocalWallet(private_key)

# create the wallet in 1 line instead of the 2 lines above
wallet = LocalWallet(PrivateKey())

address = wallet.address()

print(address)

# this generates a new private key, wallet, and address every time since no mnemonic is saved

# define the blockchain network to connect to, in this case fetch mainnet
ledger = LedgerClient(NetworkConfig.fetch_mainnet())

# query all balances for the address
balances = ledger.query_bank_all_balances(address)
print(f"balances are: {balances}")

# query just the afet balance for the address
balance = ledger.query_bank_balance(address, denom='afet')
print(f"afet balance is: {balance}")

# staking summary for address
staking_summary = ledger.query_staking_summary(address)
print(staking_summary)