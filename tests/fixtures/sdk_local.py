from brownie import accounts
from web3 import Web3
import pytest

from thirdweb.core.sdk import ThirdwebSDK


@pytest.fixture(scope="session")
def sdk():
    provider = Web3(Web3.HTTPProvider("http://localhost:8545"))
    signer = accounts[0]

    sdk = ThirdwebSDK(provider, signer)
    return sdk
