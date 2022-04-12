from tkinter.tix import IMAGE
from eth_account.account import LocalAccount
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.core.sdk import ThirdwebSDK
from thirdweb.contracts import Token
from brownie import accounts
import pytest

from thirdweb.types.settings.metadata import TokenContractMetadata


@pytest.mark.usefixtures("sdk", "primary_account")
@pytest.fixture(scope="function")
def token(sdk: ThirdwebSDK, primary_account) -> Token:
    sdk.update_signer(primary_account)
    return sdk.get_token(
        sdk.deployer.deploy_token(
            TokenContractMetadata(
                name="SDK Token",
                symbol="SDK",
                primary_sale_recipient=ZERO_ADDRESS,
            )
        )
    )


def test_metadata(token: Token):
    """
    Get token metadata
    """

    metadata = token.metadata.get()

    assert metadata.name == "SDK Token"
    assert metadata.symbol == "SDK"
    assert metadata.primary_sale_recipient == ZERO_ADDRESS


def test_mint_tokens(token: Token):
    """
    Should mint tokens
    """

    original_supply = token.total_supply().display_value
    token.mint(20)
    new_supply = token.total_supply().display_value

    assert new_supply == original_supply + 20


def test_transfer_tokens(token: Token):
    """
    Should mint tokens
    """

    token.mint(20)

    assert token.balance().display_value == 20
    assert token.balance_of(accounts[0].address).display_value == 0

    token.transfer(accounts[0].address, 10)

    assert token.balance().display_value == 10
    assert token.balance_of(accounts[0].address).display_value == 10


# test vote functionality / delegations

# test batch minting

# test burning tokens

# test allowance
