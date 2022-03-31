from thirdweb.contracts import Token
from thirdweb.core.sdk import ThirdwebSDK
from brownie import accounts
import pytest

from thirdweb.types.settings.metadata import TokenContractMetadata


@pytest.mark.usefixtures("sdk", "token_address")
@pytest.fixture()
def token(sdk: ThirdwebSDK, token_address: str) -> Token:
    token = sdk.get_token(token_address)
    return token


def test_token_provider(token: Token):
    """
    Should have correct provider and signer from SDK
    """

    assert token._contract_wrapper.get_provider() is not None
    assert token._contract_wrapper.get_signer() is not None


def test_metadata(token: Token):
    """
    Get token metadata
    """

    token.metadata.set(TokenContractMetadata(name="Test Token", symbol="TST"))

    metadata = token.metadata.get()

    assert metadata.name == "Test Token"
    assert metadata.symbol == "TST"


def test_mint_tokens(token: Token):
    """
    Should mint tokens
    """

    total_supply = token.total_supply()
    token.mint(20)
    new_supply = token.total_supply()

    assert new_supply.display_value == total_supply.display_value + 20


def test_transfer_tokens(token: Token):
    """
    Should mint tokens
    """

    current_balance = token.balance()
    other_balance = token.balance_of(accounts[1].address)
    token.transfer(accounts[1].address, 10)
    new_balance = token.balance()
    new_other_balance = token.balance_of(accounts[1].address)

    assert new_balance.display_value == current_balance.display_value - 10
    assert new_other_balance.display_value == other_balance.display_value + 10


# test vote functionality / delegations

# test batch minting

# test burning tokens

# test allowance
