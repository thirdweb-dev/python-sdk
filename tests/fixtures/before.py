from brownie import accounts, TWRegistry, TWFactory, TWFee
from web3 import Web3
import pytest

from thirdweb.core.sdk import ThirdwebSDK


@pytest.fixture(scope="session")
def contracts():
    TRUSTED_FORWARDER_ADDRESS = "0xc82BbE41f2cF04e3a8efA18F7032BDD7f6d98a81"

    thirdweb_registry = accounts[0].deploy(TWRegistry, TRUSTED_FORWARDER_ADDRESS)
    thirdweb_factory = accounts[0].deploy(
        TWFactory, TRUSTED_FORWARDER_ADDRESS, thirdweb_registry.address
    )
    thirdweb_fee = accounts[0].deploy(
        TWFee, TRUSTED_FORWARDER_ADDRESS, thirdweb_factory.address
    )

    return (thirdweb_registry, thirdweb_factory, thirdweb_fee)


@pytest.fixture()
def sdk():
    provider = Web3(Web3.HTTPProvider("http://localhost:8545"))
    sdk = ThirdwebSDK(provider, accounts[0])
    return sdk
