# improved .env methods of getting account
# NEVER use this method for account with real money
# .env file: export PRIVATE_KEY=b9e....
# brownie-config.yaml file: dotenv: .env  wallets: from_key: ${PRIVATE_KEY}
# when running $ brownie run scripts/deploy_env_account.py, it prints out my MetaMask Rinkeby account 1 address

from brownie import accounts, config


def deploy_simple_storage():
    account = accounts.add(config["wallets"]["from_key"])
    print(account)


def main():
    deploy_simple_storage()
