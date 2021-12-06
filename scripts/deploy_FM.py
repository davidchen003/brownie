from brownie import FundMe, MockV3Aggregator
from scripts.helpful_scripts import get_account, network, config


def deploy_fund_me():
    account = get_account()

    # if we are on a persistent network like Rinkeby, use the associated address specified in brownie-config.yaml
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    # otherwise, deploy mocks
    else:
        print(f"The active network is {network.show_active()}")
        print("Deploying Mocks ...")
        # deploy the mock contract ockV3Aggregator in contracts/test/
        # 18 as decimal, 2000 as initial value
        mock_aggregator = MockV3Aggregator.deploy(
            18, 2000000000000000000000, {"from": account}
        )
        price_feed_address = mock_aggregator.address
        print("Mocks deployed")

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
