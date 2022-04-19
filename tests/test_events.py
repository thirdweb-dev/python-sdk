import pytest
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.contracts.nft_collection import NFTCollection
from thirdweb.core.sdk import ThirdwebSDK
from thirdweb.types.settings.metadata import NFTCollectionContractMetadata


@pytest.mark.usefixtures("sdk", "primary_account")
@pytest.fixture(scope="function")
def nft_collection(sdk: ThirdwebSDK, primary_account) -> NFTCollection:
    sdk.update_signer(primary_account)
    return sdk.get_nft_collection(
        sdk.deployer.deploy_nft_collection(
            NFTCollectionContractMetadata(
                name="SDK NFT Collection",
                primary_sale_recipient=ZERO_ADDRESS,
                seller_fee_basis_points=10000,
                fee_recipient=ZERO_ADDRESS,
                platform_fee_basis_points=10,
                platform_fee_recipient=ZERO_ADDRESS,
            )
        )
    )


def test_emit_events(nft_collection: NFTCollection):
    pass
