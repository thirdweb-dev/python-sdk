from thirdweb.contracts.token import Token
from thirdweb.core.sdk import ThirdwebSDK
from brownie import accounts, TokenERC20
import pytest


@pytest.mark.usefixtures("contracts")
@pytest.mark.usefixtures("sdk")
@pytest.fixture
def token(contracts, sdk: ThirdwebSDK) -> Token:
    (_, _, thirdweb_fee) = contracts
    contract = accounts[0].deploy(TokenERC20, thirdweb_fee.address)
    token = sdk.get_token(contract.address)
    return token


def test_get_token(token: Token):
    assert token.get_address() is not None
