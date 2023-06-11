from cosmpy.aerial.wallet import LocalWallet
from cosmpy.crypto.keypairs import PrivateKey

# To create a random private key:
# private_key = PrivateKey()

# wallet = LocalWallet(private_key)

# create the wallet in 1 line instead of the 2 lines above
wallet = LocalWallet(PrivateKey())

address = wallet.address()

print(address)

# this generates a new private key, wallet, and address every time since no mnemonic is saved