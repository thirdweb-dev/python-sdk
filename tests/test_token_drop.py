from tkinter.tix import IMAGE
from eth_account.account import LocalAccount
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.core.sdk import ThirdwebSDK
from thirdweb.contracts import TokenDrop
from brownie import accounts
import pytest

from thirdweb.types.settings.metadata import TokenContractMetadata


@pytest.mark.usefixtures("sdk", "primary_account")
@pytest.fixture(scope="function")
def token_drop(sdk: ThirdwebSDK, primary_account) -> TokenDrop:
    sdk.update_signer(primary_account)
    return sdk.get_token(
        sdk.deployer.deploy_token_drop(
            TokenContractMetadata(
                name="SDK Token",
                symbol="SDK",
                primary_sale_recipient=ZERO_ADDRESS,
            )
        )
    )