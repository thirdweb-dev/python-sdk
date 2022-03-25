from thirdweb.contracts import Token
from thirdweb.core.sdk import ThirdwebSDK
import pytest

OTHER_ADDRESS = "0x9e31E40Dda94976A405D7BDe6c698DB60E95C87d"
TOKEN_ADDRESS = "0xA53885ABB6F74EAd52078624D28B6b09BD668B83"


@pytest.mark.usefixtures("sdk")
@pytest.fixture()
def token(sdk: ThirdwebSDK) -> Token:
    token = sdk.get_token(TOKEN_ADDRESS)
    return token


def test_token_provider(token: Token):
    """
    Should have correct provider and signer from SDK
    """

    assert token._contract_wrapper.get_provider() is not None
    assert token._contract_wrapper.get_signer() is not None


def test_get_metadata(token: Token):
    """
    Get token metadata
    """

    metadata = token.get()
    assert metadata.name == "Vote Token"
    assert metadata.decimals == 18


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
    other_balance = token.balance_of(OTHER_ADDRESS)
    token.transfer(OTHER_ADDRESS, 10)
    new_balance = token.balance()
    new_other_balance = token.balance_of(OTHER_ADDRESS)

    assert new_balance.display_value == current_balance.display_value - 10
    assert new_other_balance.display_value == other_balance.display_value + 10


# test vote functionality / delegations

# test batch minting

# test burning tokens

# test allowance
