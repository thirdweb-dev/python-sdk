from typing import cast
from thirdweb.abi.t_w_registry import TWRegistry
from thirdweb.contracts import Token
from thirdweb.core.classes.factory import ContractFactory
from thirdweb.core.classes.registry import ContractRegistry
from thirdweb.core.sdk import ThirdwebSDK
from brownie import accounts
import pytest

from thirdweb.types.settings.metadata import TokenContractMetadata


@pytest.mark.usefixtures("sdk", "contract_addresses")
@pytest.fixture()
def token(sdk: ThirdwebSDK, contract_addresses) -> Token:
    factory = cast(ContractFactory, sdk.deployer._get_factory())
    registry = cast(ContractRegistry, sdk.deployer._get_registry())

    factory.send_transaction("add_implementation", [contract_addresses.token])
    operator_role = registry._contract_abi.operator_role.call()  # type: ignore
    registry.send_transaction("grant_role", [operator_role, contract_addresses.factory])

    token_address = sdk.deployer.deploy_token(
        {
            "name": "Test Token",
            "symbol": "TST",
            "description": "Test token from tests",
            "primary_sale_recipient": accounts[0].address,
        }
    )
    token = sdk.get_token(token_address)
    return token


# def test_metadata(token: Token):
#     """
#     Get token metadata
#     """

#     token.metadata.set(TokenContractMetadata(name="Test Token", symbol="TST"))

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
