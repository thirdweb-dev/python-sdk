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


@pytest.mark.usefixtures("contract_addresses", "primary_account")
@pytest.fixture(scope="session")
def sdk_local(contract_addresses, primary_account):
    provider = Web3(Web3.HTTPProvider())
    signer = primary_account

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

    # Grant factory operator role on registry
    operator_role = registry._contract_abi.operator_role.call()  # type: ignore
    registry.send_transaction("grant_role", [operator_role, contract_addresses.factory])

    # Add deployed contract implementatinos to factory
    factory.send_transaction("add_implementation", [contract_addresses.nft_collection])
    factory.send_transaction("add_implementation", [contract_addresses.edition])
    factory.send_transaction("add_implementation", [contract_addresses.token])
    factory.send_transaction("add_implementation", [contract_addresses.marketplace])
    factory.send_transaction("add_implementation", [contract_addresses.drop])

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
