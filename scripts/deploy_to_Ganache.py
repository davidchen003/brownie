from brownie import accounts, config, SimpleStorage


def deploy_simple_storage():
    account = accounts[
        0
    ]  # which is the 1st account of the 10 Ganache account Brownie spins up
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)


def main():
    deploy_simple_storage()
