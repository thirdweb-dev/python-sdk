from thirdweb.contracts.token import Token
from thirdweb.core.sdk import ThirdwebSDK
from brownie import accounts, TokenERC20
import pytest


@pytest.mark.usefixtures("contracts")
@pytest.mark.usefixtures("sdk")
@pytest.fixture(scope="function")
def token(contracts, sdk: ThirdwebSDK) -> Token:
    (_, _, thirdweb_fee) = contracts
    contract = accounts[0].deploy(TokenERC20, thirdweb_fee.address)
    token = sdk.get_token(contract.address)
    return token


def test_mint_tokens(token: Token):
    """
    Should mint tokens
    """

    pass


def test_transfer_tokens(token: Token):
    """
    Should mint tokens
    """

    pass


def test_list_holders(token: Token):
    """
    Should list current holders
    """

    pass


def test_burn_tokens(token: Token):
    """
    Should burn tokens
    """

    pass
