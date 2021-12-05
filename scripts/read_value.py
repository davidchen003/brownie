from brownie import SimpleStorage, accounts, config


def read_contract():
    simple_storage = SimpleStorage[-1]  # get the most recently deployed SimpleStorage
    # simple_storage = SimpleStorage[-1] # get the 1st deployed
    # Brownie saved deployed contract info, including abi and address, in build/deployments folder

    print(f"retrived value: {simple_storage.retrieve()}")


def main():
    read_contract()
