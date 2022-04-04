from typing import cast
from thirdweb.abi.t_w_registry import TWRegistry
from thirdweb.contracts import Token
from thirdweb.core.classes.factory import ContractFactory
from thirdweb.core.classes.registry import ContractRegistry
from thirdweb.core.sdk import ThirdwebSDK
from brownie import accounts
import pytest

from thirdweb.types.settings.metadata import TokenContractMetadata


@pytest.mark.usefixtures("sdk")
@pytest.fixture()
def token(sdk: ThirdwebSDK) -> Token:
    token_address = sdk.deployer.deploy_token(
        {
            "name": "Testing token from SDK",
            "symbol": "TEST",
            "description": "Test contract from tests",
            "image": "https://pbs.twimg.com/profile_images/1433508973215367176/XBCfBn3g_400x400.jpg",
            "primary_sale_recipient": accounts[0].address,
        }
    )
    token = sdk.get_token(token_address)
    return token


# def test_metadata(token: Token):
#     """
#     Get token metadata
#     """

#     metadata = token.metadata.get()

#     assert metadata.name == "Test Token"
#     assert metadata.symbol == "TST"


def test_mint_tokens(token: Token):
    """
    Should mint tokens
    """

    total_supply = token.total_supply()
    token.mint(20)
    new_supply = token.total_supply()

    assert new_supply.display_value == total_supply.display_value + 20


# def test_transfer_tokens(token: Token):
#     """
#     Should mint tokens
#     """

#     current_balance = token.balance()
#     other_balance = token.balance_of(accounts[1].address)
#     token.transfer(accounts[1].address, 10)
#     new_balance = token.balance()
#     new_other_balance = token.balance_of(accounts[1].address)

#     assert new_balance.display_value == current_balance.display_value - 10
#     assert new_other_balance.display_value == other_balance.display_value + 10


# test vote functionality / delegations

# test batch minting

# test burning tokens

# test allowance
