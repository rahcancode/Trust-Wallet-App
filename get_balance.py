from web3 import Web3

# Connect to BNB Smart Chain
bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))

# Check if the connection is successful
if not web3.isConnected():
    print("Failed to connect to BNB Smart Chain")
    exit()

# Define the wallet address and the block number
wallet_address = "0x0C3022a9434e134288AAbc7fac56F421B43E92db"
block_number = 33078495

# Define the contract address and ABI for Binance-Peg BSC-USD token
token_address = "0x55d398326f99059ff775485246999027b3197955"  # Binance-Peg BSC-USD token address
token_abi = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function",
    }
]

# Create contract instance
contract = web3.eth.contract(address=token_address, abi=token_abi)

# Query the balance at the specified block number
try:
    balance = contract.functions.balanceOf(wallet_address).call(block_identifier=block_number)
    # Convert the balance from wei to the token's decimal format (18 decimals)
    balance_in_bsc_usd = web3.fromWei(balance, 'ether')
    print(f"The balance of the wallet at block {33078495} is: {balance_in_bsc_usd} BSC-USD")
except Exception as e:
    print(f"An error occurred: {e}")
