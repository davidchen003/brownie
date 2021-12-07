from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]  # 1st of the 10 accounts of Ganache
    else:
        return accounts.add(
            config["wallets"]["from_key"]
        )  # private key in .env & brownie-config.yaml (which is MetaMask Rinkeby account 1)


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks ...")
    # deploy the mock contract ockV3Aggregator in contracts/test/
    # 18 as decimal, 2000 ETH as initial value
    if len(MockV3Aggregator) <= 0:  # if there is not another mock already deployed
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mocks deployed")
