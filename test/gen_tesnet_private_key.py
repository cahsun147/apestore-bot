from web3 import Web3

RPC_URL     = "https://sepolia.base.org" 
w3 = Web3(Web3.HTTPProvider(RPC_URL))

account = w3.eth.account.create()

print("Alamat:", account.address)
print("Private key:", account.key.hex())


# account = Web3().eth.account.create()
# print("Alamat:", account.address)
# print("Private key:", account.key.hex())