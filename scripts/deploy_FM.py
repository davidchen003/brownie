from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def deploy_fund_me():
    account = get_account()

    # if we are on a persistent network like Rinkeby, use the associated address specified in brownie-config.yaml
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    # otherwise, deploy mocks to a local Ganache network already running (if none, spins up its own Ganache network)
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
        # .get("verify") makes our life easier (than ["verify"]) if we forget to add "verify" in brownie-config.yaml
    )
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
