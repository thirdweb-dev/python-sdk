from thirdweb.contracts import Edition
from thirdweb.core.sdk import ThirdwebSDK
import pytest

from thirdweb.types.nft import EditionMetadata, EditionMetadataInput, NFTMetadataInput

OTHER_ADDRESS = "0x9e31E40Dda94976A405D7BDe6c698DB60E95C87d"
EDITION_ADDRESS = "0x1df918F9181dbc00DBFd164028FdB97a03F2de69"


@pytest.mark.usefixtures("sdk")
@pytest.fixture()
def edition(sdk: ThirdwebSDK) -> Edition:
    edition = sdk.get_edition(EDITION_ADDRESS)
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
