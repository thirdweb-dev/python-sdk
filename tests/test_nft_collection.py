from brownie import accounts
from thirdweb.contracts import NFTCollection
from thirdweb.core.sdk import ThirdwebSDK
import pytest

from thirdweb.types.nft import NFTMetadataInput
from thirdweb.types.settings.metadata import NFTCollectionContractMetadata

OTHER_ADDRESS = "0x9e31E40Dda94976A405D7BDe6c698DB60E95C87d"
NFT_COLLECTION_ADDRESS = "0x83FcE9255793F5f7DE9Fb4998a6100d5C81C1FE1"


@pytest.mark.usefixtures("sdk_mumbai")
@pytest.fixture()
def nft_collection(sdk_mumbai: ThirdwebSDK) -> NFTCollection:
    nft_collection = sdk_mumbai.get_nft_collection(NFT_COLLECTION_ADDRESS)
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


def test_batch_mint_to(nft_collection: NFTCollection):
    nft_collection.mint_batch_to(
        accounts[1].address,
        [
            NFTMetadataInput.from_json(
                {
                    "name": "Python SDK NFT 1",
                    "description": "Minted with the python SDK!",
                }
            ),
            NFTMetadataInput.from_json(
                {
                    "name": "Python SDK NFT 2",
                    "description": "Minted with the python SDK!",
                }
            ),
        ],
    )


# def test_metadata(nft_collection: NFTCollection):
#     nft_collection.metadata.set(
#         NFTCollectionContractMetadata.from_json({"name": "Python SDK Contract"})
#     )

#     metadata = nft_collection.metadata.get()

#     assert metadata.to_json()["name"] == "Python SDK Contract"
