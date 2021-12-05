from brownie import accounts


def deploy_simple_storage():
    account = accounts[
        0
    ]  # which is the 1st account of the 10 Ganache account Brownie spins up
    print(account)


def main():
    deploy_simple_storage()
