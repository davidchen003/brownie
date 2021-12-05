from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    account = accounts[
        0
    ]  # which is the 1st account of the 10 Ganache account Brownie spins up
    simple_storage = SimpleStorage.deploy({"from": account})
    # print(SimpleStorage)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)  # number of block(s) to wait
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def main():
    deploy_simple_storage()
