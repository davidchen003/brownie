# NEVER use this method for account with real money
# .env file: export PRIVATE_KEY=b9e....
# brownie-config.yaml file: dotenv: .env
# when running $ brownie run scripts/deploy_env_account.py, it prints out my MetaMask Rinkeby account 1 address

from brownie import accounts
import os


def deploy_simple_storage():
    account = accounts.add(os.getenv("PRIVATE_KEY"))
    print(account)


def main():
    deploy_simple_storage()
