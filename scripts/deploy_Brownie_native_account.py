### this is recommended secure way to store private key
# `$brownie accounts new MyMetaMask`, which prompted to enter private key (use my metamask Rinkeby account 1)
# then it prompts to enter password to access this private key (my "usual")

# you can see and other accounts by `$brownie accounts list`
# to delete an account: `$brownie accounts delete account_name`
# when running `$brownie run scripts/deploy_xxx.py`, it prompts for password
# Enter password for "MyMetaMask":
# then the script prints out the my MetaMask Rinkeby account 1 address

from brownie import accounts


def deploy_simple_storage():
    account = accounts.load("MyMetaMask")
    print(account)


def main():
    deploy_simple_storage()
