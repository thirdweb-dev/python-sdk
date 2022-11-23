from time import time
from typing import Any, cast
from thirdweb.constants.currency import NATIVE_TOKEN_ADDRESS, ZERO_ADDRESS
from thirdweb.constants.role import Role
from thirdweb.contracts.token import Token
from thirdweb.types.contracts.signature import PayloadToSign721
from thirdweb.types.currency import TokenAmount
from thirdweb.types.nft import NFTMetadataInput
from thirdweb.contracts import NFTCollection
from thirdweb.core.sdk import ThirdwebSDK
from brownie import accounts
import pytest

from thirdweb.types.settings.metadata import (
    NFTCollectionContractMetadata,
    TokenContractMetadata,
)


@pytest.mark.usefixtures("sdk", "primary_account")
@pytest.fixture(scope="function")
def nft_collection(sdk: ThirdwebSDK, primary_account) -> NFTCollection:
    sdk.update_signer(primary_account)
    nft_collection = sdk.get_nft_collection(
        sdk.deployer.deploy_nft_collection(
            NFTCollectionContractMetadata(
                name="OUCH VOUCH",
                symbol="VOUCH",
                primary_sale_recipient=cast(Any, sdk.get_signer()).address,
                seller_fee_basis_points=0,
            )
        )
    )

    nft_collection.roles.grant(Role.MINTER, sdk.get_signer().address)  # type: ignore
    nft_collection.roles.grant(Role.MINTER, accounts[0].address)

    return nft_collection


@pytest.mark.usefixtures("sdk", "secondary_account")
@pytest.fixture(scope="function")
def token(sdk: ThirdwebSDK, secondary_account) -> Token:
    token = sdk.get_token(
        sdk.deployer.deploy_token(
            TokenContractMetadata(
                name="Test Token",
                symbol="TEST",
                primary_sale_recipient=sdk.get_signer().address,  # type: ignore
            )
        )
    )

    token.mint_batch_to(
        [
            TokenAmount(to_address=accounts[0].address, amount=1000),
            TokenAmount(to_address=accounts[1].address, amount=1000),
            TokenAmount(to_address=sdk.get_signer().address, amount=1000),  # type: ignore
            TokenAmount(to_address=secondary_account.address, amount=1000),
        ]
    )

    return token


@pytest.fixture
def metadata() -> PayloadToSign721:
    return PayloadToSign721(
        to=accounts[0].address,
        price=1,
        currency_address=NATIVE_TOKEN_ADDRESS,
        metadata=NFTMetadataInput(name="OUCH VOUCH"),
        mint_end_time=int(time() + 60 * 60 * 24 * 1000 * 1000),
        mint_start_time=int(time()) - 1800,
        uid=None,
        primary_sale_recipient=ZERO_ADDRESS,
    )


def test_generate_valid_signature(
    nft_collection: NFTCollection, metadata: PayloadToSign721
):
    good_payload = nft_collection.signature.generate(metadata)
    valid = nft_collection.signature.verify(good_payload)
    assert valid


@pytest.mark.usefixtures("sdk", "primary_account", "secondary_account")
def test_claiming(
    sdk: ThirdwebSDK,
    nft_collection: NFTCollection,
    primary_account,
    secondary_account,
):
    payloads = []
    free_mint = PayloadToSign721(
        to=accounts[0].address,
        price=0,
        currency_address=NATIVE_TOKEN_ADDRESS,
        metadata=NFTMetadataInput(name="OUCH VOUCH"),
        mint_end_time=int(time() + 60 * 60 * 24 * 1000 * 1000),
        mint_start_time=int(time()) - 1800,
        uid=None,
        primary_sale_recipient=ZERO_ADDRESS,
    )

    for i in range(0, 10):
        payloads.append(free_mint)

    batch = [nft_collection.signature.generate(p) for p in payloads]
    sdk.update_signer(secondary_account)
    tx = nft_collection.signature.mint_batch(batch)
    sdk.update_signer(primary_account)

    assert len(tx) == 10
    assert tx[0].id == 0
    assert tx[3].id == 3

    assert nft_collection.get(tx[0].id).metadata.name == "OUCH VOUCH"
    assert nft_collection.balance_of(accounts[0].address) == 10

@pytest.mark.usefixtures("sdk", "primary_account", "secondary_account")
def test_custom_token(
    sdk: ThirdwebSDK,
    nft_collection: NFTCollection,
    token: Token,
    primary_account,
    secondary_account,
):
    old_balance = nft_collection.balance_of(accounts[0].address)
    metadata = PayloadToSign721(
        price=1,
        currency_address=token.get_address(),
        metadata=NFTMetadataInput(name="custom token test"),
        mint_end_time=int(time() + 60 * 60 * 24 * 1000 * 1000),
        mint_start_time=int(time()) - 1800,
        to=accounts[0].address,
        uid=None,
        primary_sale_recipient=ZERO_ADDRESS,
    )
    payload = nft_collection.signature.generate(metadata)

    sdk.update_signer(secondary_account)
    nft_collection.signature.mint(payload)

    new_balance = nft_collection.balance_of(accounts[0].address)

    assert new_balance == old_balance + 1
