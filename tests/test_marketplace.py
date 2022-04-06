from tkinter.tix import IMAGE
from eth_account.account import LocalAccount
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.core.sdk import ThirdwebSDK
from thirdweb.contracts import Marketplace
from brownie import accounts
import pytest


@pytest.mark.usefixtures("sdk")
@pytest.fixture(scope="function")
def marketplace(sdk: ThirdwebSDK) -> Marketplace:
    marketplace_address = sdk.deployer.deploy_marketplace(
        {
            "name": "SDK Marketplace",
            "symbol": "SDK",
        }
    )
    marketplace = sdk.get_marketplace(marketplace_address)
    return marketplace


def test_deploy(marketplace: Marketplace):
    marketplace.get_all()
