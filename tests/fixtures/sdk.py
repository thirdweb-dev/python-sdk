from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.core.classes.registry import ContractRegistry
from thirdweb.core.classes.factory import ContractFactory
from web3.middleware import geth_poa_middleware
from thirdweb.core.sdk import ThirdwebSDK
from eth_account import Account
from dotenv import load_dotenv
from web3 import Web3
import pytest
import os

load_dotenv()


@pytest.mark.usefixtures("primary_account")
@pytest.fixture(scope="session")
def sdk(primary_account):
    signer = primary_account
    sdk = ThirdwebSDK("http://localhost:8545", signer)
    return sdk
