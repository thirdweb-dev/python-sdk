import pytest
from thirdweb.abi import TokenERC721
from thirdweb.contracts.nft_collection import NFTCollection
from thirdweb.core.sdk import ThirdwebSDK
from web3 import Web3

from thirdweb.types.settings.metadata import NFTCollectionContractMetadata


@pytest.mark.usefixtures("sdk", "primary_account")
@pytest.fixture(scope="function")
def nft_collection(sdk: ThirdwebSDK, primary_account) -> NFTCollection:
    sdk.update_signer(primary_account)
    return sdk.get_nft_collection(
        sdk.deployer.deploy_nft_collection(
            NFTCollectionContractMetadata(
                name="SDK NFT Collection",
            )
        )
    )


# @pytest.fixture
# def sdk_mumbai():
#     RPC_URL = "https://rpc-mumbai.maticvigil.com"
#     provider = Web3(Web3.HTTPProvider(RPC_URL))
#     sdk = ThirdwebSDK(provider)
#     return sdk


# @pytest.mark.usefixtures("sdk_mumbai")
# def test_custom(sdk_mumbai: ThirdwebSDK):
#     custom = sdk_mumbai.unstable_get_custom_contract(
#         "0x87f80ba61BceC41108127991a706EDE2aBBef015"
#     )


@pytest.mark.usefixtures("sdk")
def test_custom_abi(sdk: ThirdwebSDK, nft_collection: NFTCollection):
    custom = sdk.unstable_get_custom_contract(
        nft_collection.get_address(), TokenERC721.abi()
    )
