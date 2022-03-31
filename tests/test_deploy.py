from brownie import (
    accounts,
    Forwarder,
    TWFactory,
    TWFee,
    TWRegistry,
    DropERC721,
    DropERC1155,
    TokenERC20,
    TokenERC721,
    TokenERC1155,
)
import pytest


def test_deploy():
    trusted_forwarder = accounts[0].deploy(Forwarder)
    trusted_forwarder_address = trusted_forwarder.address

    thirdweb_registry = accounts[0].deploy(TWRegistry, trusted_forwarder_address)

    thirdweb_factory = accounts[0].deploy(
        TWFactory, trusted_forwarder_address, thirdweb_registry.address
    )

    thirdweb_fee = accounts[0].deploy(
        TWFee, trusted_forwarder_address, thirdweb_factory.address
    )

    token_erc_20 = accounts[0].deploy(TokenERC20, thirdweb_fee.address)
    token_erc_721 = accounts[0].deploy(TokenERC721, thirdweb_fee.address)
    token_erc_1155 = accounts[0].deploy(TokenERC1155, thirdweb_fee.address)
