from thirdweb.contracts import NFTCollection
from thirdweb.core.sdk import ThirdwebSDK
import pytest

OTHER_ADDRESS = "0x9e31E40Dda94976A405D7BDe6c698DB60E95C87d"
NFT_COLLECTION_ADDRESS = "0x522B1fE8BDF70fB0c3a4931aCB94fBa6C232c74f"


@pytest.mark.usefixtures("sdk")
@pytest.fixture()
def nft_collection(sdk: ThirdwebSDK) -> NFTCollection:
    nft_collection = sdk.get_nft_collection(NFT_COLLECTION_ADDRESS)
    return nft_collection


def test_nft_collection_provider(nft_collection: NFTCollection):
    assert nft_collection._contract_wrapper.get_provider() is not None
    assert nft_collection._contract_wrapper.get_signer() is not None
