from thirdweb.contracts import NFTCollection
from thirdweb.core.sdk import ThirdwebSDK
import pytest

from thirdweb.types.nft import NFTMetadataInput

OTHER_ADDRESS = "0x9e31E40Dda94976A405D7BDe6c698DB60E95C87d"
NFT_COLLECTION_ADDRESS = "0xED8121008B1aD8327297Afa820041a5B3523f3E7"


@pytest.mark.usefixtures("sdk")
@pytest.fixture()
def nft_collection(sdk: ThirdwebSDK) -> NFTCollection:
    nft_collection = sdk.get_nft_collection(NFT_COLLECTION_ADDRESS)
    return nft_collection


def test_provider(nft_collection: NFTCollection):
    assert nft_collection._contract_wrapper.get_provider() is not None
    assert nft_collection._contract_wrapper.get_signer() is not None


def test_mint(nft_collection: NFTCollection):
    balance = nft_collection.balance()

    nft_collection.mint(
        NFTMetadataInput.from_json(
            {"name": "Python SDK NFT", "description": "Minted with the python SDK!"}
        )
    )

    token_id = nft_collection.get_total_count() - 1
    metadata = nft_collection.get(token_id).metadata

    assert metadata.name == "Python SDK NFT"
    assert metadata.description == "Minted with the python SDK!"
    assert nft_collection.balance() == balance + 1


def test_burn(nft_collection: NFTCollection):
    token_id = nft_collection.get_total_count() - 1
    nft_collection.mint(NFTMetadataInput.from_json({"name": "Python SDK NFT"}))

    nft_collection.burn(token_id)


def test_transfer(nft_collection: NFTCollection):
    my_balance = nft_collection.balance()
    other_balance = nft_collection.balance_of(OTHER_ADDRESS)

    token_id = nft_collection.get_total_count() - 1
    nft_collection.mint(NFTMetadataInput.from_json({"name": "Python SDK NFT"}))

    nft_collection.transfer(OTHER_ADDRESS, token_id)
