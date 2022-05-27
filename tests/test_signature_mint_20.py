from time import time
from thirdweb.constants.currency import NATIVE_TOKEN_ADDRESS, ZERO_ADDRESS
from thirdweb.constants.role import Role
from thirdweb.contracts.token import Token
from thirdweb.types.contracts.signature import PayloadToSign20, PayloadToSign20
from thirdweb.types.currency import TokenAmount
from thirdweb.core.sdk import ThirdwebSDK
from brownie import accounts
import pytest

from thirdweb.types.settings.metadata import (
    TokenContractMetadata,
)


@pytest.mark.usefixtures("sdk", "primary_account")
@pytest.fixture(scope="function")
def token(sdk: ThirdwebSDK, primary_account) -> Token:
    sdk.update_signer(primary_account)

    token = sdk.get_token(
        sdk.deployer.deploy_token(
            TokenContractMetadata(
                name="Token Sigmint",
                symbol="TSIG",
                primary_sale_recipient=sdk.get_signer().address,  # type: ignore
            )
        )
    )

    custom_token = sdk.get_token(
        sdk.deployer.deploy_token(
            TokenContractMetadata(
                name="Test",
                symbol="TEST",
                primary_sale_recipient=sdk.get_signer().address,  # type: ignore
            )
        )
    )

    custom_token.mint_batch_to(
        [
            TokenAmount(to_address=accounts[0].address, amount=1000),
            TokenAmount(to_address=accounts[1].address, amount=1000),
            TokenAmount(to_address=sdk.get_signer().address, amount=1000),  # type: ignore
        ]
    )

    return custom_token


@pytest.fixture
def metadata() -> PayloadToSign20:
    return PayloadToSign20(
        to=accounts[0].address,
        price=0,
        currency_address=NATIVE_TOKEN_ADDRESS,
        primary_sale_recipient=ZERO_ADDRESS,
        quantity=1,
        mint_end_time=int(time() + 60 * 60 * 24),
        mint_start_time=int(time()) - 1800,
        uid=None,
    )


def test_generate_valid_signature(token: Token, metadata: PayloadToSign20):
    good_payload = token.signature.generate(metadata)
    valid = token.signature.verify(good_payload)
    assert valid

    token.signature.mint(good_payload)


@pytest.mark.usefixtures("sdk", "primary_account", "secondary_account")
def test_claiming(
    sdk: ThirdwebSDK,
    token: Token,
    primary_account,
    secondary_account,
):
    payloads = []
    free_mint = PayloadToSign20(
        to=accounts[0].address,
        price=0,
        currency_address=NATIVE_TOKEN_ADDRESS,
        quantity=1,
        primary_sale_recipient=ZERO_ADDRESS,
        mint_end_time=int(time() + 60 * 60 * 24),
        mint_start_time=int(time()) - 1800,
        uid=None,
    )

    for i in range(0, 10):
        payloads.append(free_mint)

    balance = token.balance_of(accounts[0].address)
    assert balance.display_value == 1000

    batch = [token.signature.generate(p) for p in payloads]
    sdk.update_signer(secondary_account)
    tx = token.signature.mint_batch(batch)
    sdk.update_signer(primary_account)

    balance = token.balance_of(accounts[0].address)
    assert balance.display_value == 1010
