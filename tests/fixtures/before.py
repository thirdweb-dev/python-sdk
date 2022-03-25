from eth_account import Account
from dotenv import load_dotenv
from web3.middleware import geth_poa_middleware
from web3 import Web3
import pytest
import os

from thirdweb.core.sdk import ThirdwebSDK

load_dotenv()

# TODO: Switch to local deployment once DEPLOYER is setup

# Injecting middleware to web3 provider for non local network as specified here
# https://stackoverflow.com/questions/70812529/the-field-extradata-is-97-bytes-but-should-be-32-it-is-quite-likely-that-you-a
@pytest.fixture()
def sdk():
    provider = Web3(Web3.HTTPProvider("https://rpc-mumbai.maticvigil.com"))
    provider.middleware_onion.inject(geth_poa_middleware, layer=0)
    signer = Account.from_key(os.environ.get("PRIVATE_KEY"))
    sdk = ThirdwebSDK(provider, signer)
    return sdk
