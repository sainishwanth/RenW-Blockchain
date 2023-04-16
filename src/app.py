from web3 import Web3
import scrape
import json
import pandas as pd

ganache_instance = 'http://127.0.0.1:7546'
web3 = Web3(Web3.HTTPProvider(ganache_instance))

web3.eth.default_account = web3.eth.accounts[0]

abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"uint256","name":"_listingIndex","type":"uint256"}],"name":"buyListing","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"_Name","type":"string"},{"internalType":"string","name":"_projectName","type":"string"},{"internalType":"uint256","name":"_amount","type":"uint256"},{"internalType":"uint256","name":"_quantity","type":"uint256"}],"name":"createListing","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getRandomNumber","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getTime","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"listing","outputs":[{"internalType":"string","name":"PersonName","type":"string"},{"internalType":"uint256","name":"stockID","type":"uint256"},{"internalType":"uint256","name":"PersonID","type":"uint256"},{"internalType":"uint256","name":"CompanyID","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint8","name":"count","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"quantity","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"stock","outputs":[{"internalType":"string","name":"CompanyName","type":"string"},{"internalType":"string","name":"ProjectName","type":"string"},{"internalType":"uint256","name":"CompanyID","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"quantity","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"users","outputs":[{"internalType":"string","name":"UserName","type":"string"},{"internalType":"uint256","name":"UserID","type":"uint256"},{"internalType":"uint256","name":"amount","type":"uint256"},{"internalType":"uint256","name":"stocksOwned","type":"uint256"}],"stateMutability":"view","type":"function"}]')
contract_address_Temp = "0xff33e96ce852E4BA3f53a2d4492483d962775D1C"
print(web3.is_connected())
contract_address = web3.to_checksum_address(contract_address_Temp)
contract = web3.eth.contract(address=contract_address, abi=abi)
tx_hash = contract.functions.createListing("Wipro", "Solana", 1000, 10).transact()
count = 0
web3.eth.wait_for_transaction_receipt(tx_hash)
lst = []

def BuyContract(i):
    contract.functions.buyListing(i).transact()


def ViewAllContracts():
    global lst
    countHere = 0
    for i in range(10):
        lst.append(contract.functions.listing(countHere).call())


while True:
    choice = int(input("1.View All Sales\n2.Buy\nEnter a Choice: "))
    if (choice == 1):
        ViewAllContracts()
        df = pd.DataFrame(lst)
        print(df)
    elif (choice == 2):
        num = int(input("Enter the contract Number "))
        BuyContract(num)
        Buyer = "0x2E13C205A8037D48452eA8009C83C9Ef71B47b22"
        Seller = "0x892672011bf69eBfBFAfc4907993a85cB1CFb515"
        key = "0xc183d5b67196193196132000d65cca805c571da6deb9a065f7b1e85c3230fd61"
        if Buyer != Seller:
            nonce = web3.eth.get_transaction_count(Buyer)

            tx = {
                'nonce': nonce,
                'to': Seller,
                'value': web3.to_wei(1, 'ether'),
                'gas': 2000000,
                'gasPrice': web3.to_wei('10', 'gwei')
            }

            signed_tx = web3.eth.account.sign_transaction(tx, key)
            tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
## Dummy Ether Accounts with Ganache
#accounts_dict = {'0x0334e662AD19863FfD9caB2296C68815f525aeE0': '0x1e8e3a5f6015c3f40d73e9b01bf55a5025fddbdb88e7fef6f925d5e4f5750c27',
#                 '0x489851e9Be7Ac9e730d13630f511c299C75c0580': '0xd1ed76f7319f7cc97c433a5b9acb025c8edecd397a40d870dcbf7fb9eb88b597',
#                 '0x5AE351b51Cd647F835Ba3399A65Db9f95d19E85C': '0xcf1211753756be7c466fe054df46bcb83be6ef099d256547ebc451788793e17e',
#                 '0x4746EA1B4b9938a7a3A3bc5ed27c462932e4Fe37': '0x956d9cc55f66b7bce36c981e87b0f7a5b7fe16ebe1c763a8b042d9c0a8b82100',
#                 '0x7531a388b432Def291EF3D37FE044e2C71De1dF0': '0x4886d18e1e30dcd342eb4d32bc0405caf53e78dbcf32b4927804d63e108a9731'}
#
#Buyer: int = int(input("Enter Buyer Account Number: "))
#Seller: int = int(input("Enter the Seller Number: "))

if Buyer != Seller:
    acc1 = list(accounts_dict)[Buyer]
    acc2 = list(accounts_dict)[Seller]
    print(acc1, acc2)
    key = accounts_dict[acc1]
    nonce = web3.eth.get_transaction_count(acc1)

    tx = {
        'nonce': nonce,
        'to': acc2,
        'value': web3.to_wei(1, 'ether'),
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei')
    }

    signed_tx = web3.eth.account.sign_transaction(tx, key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)