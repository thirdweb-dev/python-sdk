from thirdweb.contracts import Edition
from thirdweb.core.sdk import ThirdwebSDK
import pytest

from thirdweb.types.nft import EditionMetadata, EditionMetadataInput, NFTMetadataInput

OTHER_ADDRESS = "0x9e31E40Dda94976A405D7BDe6c698DB60E95C87d"
EDITION_ADDRESS = "0x1df918F9181dbc00DBFd164028FdB97a03F2de69"


@pytest.mark.usefixtures("sdk_mumbai")
@pytest.fixture()
def edition(sdk_mumbai: ThirdwebSDK) -> Edition:
    edition = sdk_mumbai.get_edition(EDITION_ADDRESS)
    return edition


def test_edition_provider(edition: Edition):
    assert edition._contract_wrapper.get_provider() is not None
    assert edition._contract_wrapper.get_signer() is not None


def test_mint(edition: Edition):
    edition.mint(
        EditionMetadataInput(
            NFTMetadataInput.from_json(
                {"name": "Python SDK NFT", "description": "Minted with the python SDK!"}
            ),
            100,
        )
    )

    token_id = edition.get_total_count() - 1
    metadata = edition.get(token_id).metadata

    assert metadata.name == "Python SDK NFT"
    assert metadata.description == "Minted with the python SDK!"


def test_transfer(edition: Edition):
    token_id = edition.get_total_count()

    edition.mint(
        EditionMetadataInput(
            NFTMetadataInput.from_json(
                {"name": "Python SDK NFT", "description": "Minted with the python SDK!"}
            ),
            100,
        )
    )

    my_balance = edition.balance(token_id)
    other_balance = edition.balance_of(OTHER_ADDRESS, token_id)

    edition.transfer(OTHER_ADDRESS, token_id, 50)

    assert edition.balance_of(OTHER_ADDRESS, token_id) == other_balance + 50
    assert edition.balance(token_id) == my_balance - 50
