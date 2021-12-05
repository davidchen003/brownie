from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    # print(SimpleStorage)
    stored_value = simple_storage.retrieve()
    print(f"initial value: {stored_value}")
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)  # number of block(s) to wait
    updated_stored_value = simple_storage.retrieve()
    print(f"updated value: {updated_stored_value}")


def get_account():
    if network.show_active() == "development":
        return accounts[0]  # 1st of the 10 accounts of Ganache
    else:
        return accounts.add(
            config["wallets"]["from_key"]
        )  # private key in .env & brownie-config.yaml (which is MetaMask Rinkeby account 1)


def main():
    deploy_simple_storage()
