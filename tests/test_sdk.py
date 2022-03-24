from brownie import accounts
from dotenv import load_dotenv
import pytest
import os

from eth_account import Account
from web3 import Web3

from thirdweb.core.sdk import ThirdwebSDK

load_dotenv()


@pytest.fixture
def sdk() -> ThirdwebSDK:
    provider = Web3(Web3.HTTPProvider("https://polygon-rpc.com/"))
    account = Account.from_key(os.environ.get("PRIVATE_KEY"))
    return ThirdwebSDK(provider, account)


def test_sdk_initialization(sdk: ThirdwebSDK):
    signer = sdk.get_signer()
    provider = sdk.get_provider()

    assert provider.eth.chain_id == 137
    assert signer is not None
    assert signer.address == "0xa05271523BD00593eb4CC6DCbDcbd045361a9a03"
