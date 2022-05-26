from time import time
from typing import Any, cast
from thirdweb.constants.currency import NATIVE_TOKEN_ADDRESS, ZERO_ADDRESS
from thirdweb.constants.role import Role
from thirdweb.contracts.edition import Edition
from thirdweb.contracts.token import Token
from thirdweb.types.contracts.signature import PayloadToSign1155
from thirdweb.types.currency import TokenAmount
from thirdweb.types.nft import NFTMetadataInput
from web3.constants import MAX_INT
from thirdweb.core.sdk import ThirdwebSDK
from brownie import accounts
import pytest

from thirdweb.types.settings.metadata import (
    EditionContractMetadata,
    TokenContractMetadata,
)


@pytest.mark.usefixtures("sdk", "primary_account")
@pytest.fixture()
def edition(sdk: ThirdwebSDK, primary_account) -> Edition:
    sdk.update_signer(primary_account)
    edition = sdk.get_edition(
        sdk.deployer.deploy_edition(
            EditionContractMetadata(
                name="SDK Edition",
                symbol="SDK",
                primary_sale_recipient=ZERO_ADDRESS,
                fee_recipient=ZERO_ADDRESS,
                platform_fee_basis_points=10,
                platform_fee_recipient=ZERO_ADDRESS,
            )
        )
    )

    edition.roles.grant(Role.MINTER, sdk.get_signer().address)  # type: ignore
    edition.roles.grant(Role.MINTER, accounts[0].address)

    return edition


@pytest.mark.usefixtures("sdk")
@pytest.fixture(scope="function")
def token(sdk: ThirdwebSDK) -> Token:
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
        ]
    )

    return token


@pytest.fixture
def metadata() -> PayloadToSign1155:
    return PayloadToSign1155(
        to=accounts[0].address,
        price=1,
        currency_address=NATIVE_TOKEN_ADDRESS,
        metadata=NFTMetadataInput(name="OUCH VOUCH"),
        mint_end_time=int(time() + 60 * 60 * 24 * 1000 * 1000),
        mint_start_time=int(time()) - 1800,
        uid=None,
        quantity=1,
        token_id=int(MAX_INT, 0),
        primary_sale_recipient=ZERO_ADDRESS,
    )


def test_generate_valid_signature(edition: Edition, metadata: PayloadToSign1155):
    good_payload = edition.signature.generate(metadata)
    valid = edition.signature.verify(good_payload)
    assert valid


@pytest.mark.usefixtures("sdk", "primary_account", "secondary_account")
def test_claiming(
    sdk: ThirdwebSDK,
    edition: Edition,
    primary_account,
    secondary_account,
):
    payloads = []
    free_mint = PayloadToSign1155(
        to=accounts[0].address,
        price=0,
        token_id=int(MAX_INT, 0),
        quantity=1,
        currency_address=NATIVE_TOKEN_ADDRESS,
        metadata=NFTMetadataInput(name="OUCH VOUCH"),
        mint_end_time=int(time() + 60 * 60 * 24 * 1000 * 1000),
        mint_start_time=int(time()) - 1800,
        uid=None,
        primary_sale_recipient=ZERO_ADDRESS,
    )

    for i in range(0, 10):
        payloads.append(free_mint)

    batch = [edition.signature.generate(p) for p in payloads]
    sdk.update_signer(secondary_account)
    tx = edition.signature.mint_batch(batch)
    sdk.update_signer(primary_account)

    assert len(tx) == 10
    assert tx[0].id == 0
    assert tx[3].id == 3

    assert edition.get(tx[0].id).metadata.name == "OUCH VOUCH"
