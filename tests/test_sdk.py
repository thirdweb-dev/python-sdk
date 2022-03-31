from thirdweb.core.sdk import ThirdwebSDK
from brownie import accounts
import pytest


@pytest.mark.usefixtures("sdk")
def test_sdk_initialization(sdk: ThirdwebSDK):
    signer = sdk.get_signer()
    provider = sdk.get_provider()

    assert provider.eth.default_account == signer
    assert signer is not None and signer.address == accounts[0].address


# test SDK provider switching

# test SDK signer switching

# test SDK contract caching

# test SDK provider and signer switching on contract
