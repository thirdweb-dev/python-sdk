from thirdweb.core.classes.factory import ContractFactory
from web3.middleware import geth_poa_middleware
from thirdweb.core.classes.registry import ContractRegistry
from thirdweb.core.sdk import ThirdwebSDK
from eth_account import Account
from dotenv import load_dotenv
from brownie import accounts
from web3 import Web3
import pytest
import os

load_dotenv()


@pytest.mark.usefixtures("contract_addresses")
@pytest.fixture(scope="session")
def sdk_local(contract_addresses):
    provider = Web3(Web3.HTTPProvider())
    signer = Account.from_key(os.environ.get("PRIVATE_KEY"))

    sdk = ThirdwebSDK(provider, signer)

    # Manually set factory and registry addresses
    factory = ContractFactory(
        contract_addresses.factory,
        sdk.get_provider(),
        sdk.get_signer(),
        sdk.get_options(),
    )
    sdk.deployer._set_factory(factory)

    registry = ContractRegistry(
        contract_addresses.registry,
        sdk.get_provider(),
        sdk.get_signer(),
        sdk.get_options(),
    )
    sdk.deployer._set_registry(registry)

    return sdk


# Injecting middleware to web3 provider for non local network as specified here
# https://stackoverflow.com/questions/70812529/the-field-extradata-is-97-bytes-but-should-be-32-it-is-quite-likely-that-you-a
@pytest.fixture()
def sdk_mumbai():
    provider = Web3(Web3.HTTPProvider("https://rpc-mumbai.maticvigil.com"))
    provider.middleware_onion.inject(geth_poa_middleware, layer=0)

    signer = Account.from_key(os.environ.get("PRIVATE_KEY"))
    sdk = ThirdwebSDK(provider, signer)

    return sdk
