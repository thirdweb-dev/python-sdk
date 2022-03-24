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

    assert sdk.get_provider().eth.chain_id == provider.eth.chain_id
    assert sdk.get_signer() is None
