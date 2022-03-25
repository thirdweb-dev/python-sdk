import pytest
import os

from eth_account import Account
from web3 import Web3

from thirdweb.core.sdk import ThirdwebSDK


@pytest.mark.usefixtures("sdk")
def test_sdk_initialization(sdk: ThirdwebSDK):
    signer = sdk.get_signer()
    provider = sdk.get_provider()

    assert provider.eth.chain_id == 80001
    assert signer is not None
    assert signer.address == "0xa05271523BD00593eb4CC6DCbDcbd045361a9a03"
