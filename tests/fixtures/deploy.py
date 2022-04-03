from dataclasses import dataclass
from dotenv import load_dotenv
from brownie import (
    accounts,
    Forwarder,
    TWFactory,
    TWFee,
    TWRegistry,
    TokenERC20,
    TokenERC721,
    TokenERC1155,
)
from eth_account import Account
import pytest
import os


load_dotenv()


@dataclass
class ContractAddresses:
    factory: str
    registry: str
    fee: str
    token: str
    nft_collection: str
    edition: str


@pytest.fixture(scope="session")
def contract_addresses():
    accounts.add(os.environ.get("PRIVATE_KEY"))
    address = Account.from_key(os.environ.get("PRIVATE_KEY")).address
    account = accounts.at(address)
    accounts[0].transfer(account, 10000000000000000)

    trusted_forwarder = account.deploy(Forwarder)
    trusted_forwarder_address = trusted_forwarder.address

    thirdweb_registry = account.deploy(TWRegistry, trusted_forwarder_address)

    thirdweb_factory = account.deploy(
        TWFactory, trusted_forwarder_address, thirdweb_registry.address
    )

    thirdweb_fee = account.deploy(
        TWFee, trusted_forwarder_address, thirdweb_factory.address
    )

    token_erc_20 = account.deploy(TokenERC20, thirdweb_fee.address)
    token_erc_721 = account.deploy(TokenERC721, thirdweb_fee.address)
    token_erc_1155 = account.deploy(TokenERC1155, thirdweb_fee.address)

    return ContractAddresses(
        factory=thirdweb_factory.address,
        registry=thirdweb_registry.address,
        fee=thirdweb_fee.address,
        token=token_erc_20.address,
        nft_collection=token_erc_721.address,
        edition=token_erc_1155.address,
    )
