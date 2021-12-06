from brownie import network, config, accounts


def get_account():
    if network.show_active() == "development":
        return accounts[0]  # 1st of the 10 accounts of Ganache
    else:
        return accounts.add(
            config["wallets"]["from_key"]
        )  # private key in .env & brownie-config.yaml (which is MetaMask Rinkeby account 1)
