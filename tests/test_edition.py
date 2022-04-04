from brownie import accounts
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.contracts import Edition
from thirdweb.core.sdk import ThirdwebSDK
import pytest

from thirdweb.types.nft import EditionMetadataInput, NFTMetadataInput


@pytest.mark.usefixtures("sdk")
@pytest.fixture()
def edition(sdk: ThirdwebSDK) -> Edition:
    edition_address = sdk.deployer.deploy_edition(
        {
            "name": "SDK Edition",
            "symbol": "SDK",
            "primary_sale_recipient": ZERO_ADDRESS,
            "seller_fee_basis_points": 1000,
            "fee_recipient": ZERO_ADDRESS,
            "platform_fee_basis_points": 10,
            "platform_fee_recipient": ZERO_ADDRESS,
        }
    )
    edition = sdk.get_edition(edition_address)
    return edition


def test_mint(edition: Edition):
    edition.mint(
        EditionMetadataInput(
            NFTMetadataInput.from_json(
                {"name": "Python SDK NFT", "description": "Minted with the python SDK!"}
            ),
            100,
        )
    )

    metadata = edition.get(0).metadata

    assert metadata.name == "Python SDK NFT"
    assert metadata.description == "Minted with the python SDK!"
    assert edition.balance(0) == 100


def test_transfer(edition: Edition):
    edition.mint(
        EditionMetadataInput(
            NFTMetadataInput.from_json(
                {"name": "Python SDK NFT", "description": "Minted with the python SDK!"}
            ),
            100,
        )
    )

    my_balance = edition.balance(0)
    other_balance = edition.balance_of(accounts[0].address, 0)

    edition.transfer(accounts[0].address, 0, 50)

    assert edition.balance_of(accounts[0].address, 0) == other_balance + 50
    assert edition.balance(0) == my_balance - 50
