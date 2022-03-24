import pytest
from brownie import accounts
from web3 import Web3

from thirdweb.core.sdk import ThirdwebSDK


@pytest.fixture
def initialize_sdk():
    pass


def test_sdk_initialization(initialize_sdk):
    provider = Web3(Web3.HTTPProvider("https://polygon-rpc.com/"))
    sdk = ThirdwebSDK(provider, None)

    assert True
