from time import time
import pytest
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.constants.role import Role
from thirdweb.contracts.nft_drop import NFTDrop

from thirdweb.core.sdk import ThirdwebSDK
from thirdweb.types.contracts.claim_conditions import ClaimConditionInput
from thirdweb.types.nft import NFTMetadataInput
from thirdweb.types.settings.metadata import NFTDropContractMetadata


@pytest.mark.usefixtures("sdk", "primary_account")
@pytest.fixture(scope="function")
def nft_drop(sdk: ThirdwebSDK, primary_account) -> NFTDrop:
    sdk.update_signer(primary_account)
    nft_drop = sdk.get_nft_drop(
        sdk.deployer.deploy_nft_drop(
            NFTDropContractMetadata(
                name="SDK NFT Drop",
                primary_sale_recipient=sdk.get_signer().address,  # type: ignore
                seller_fee_basis_points=500,
                fee_recipient=ZERO_ADDRESS,
                platform_fee_basis_points=10,
                platform_fee_recipient=ZERO_ADDRESS,
            )
        )
    )
    nft_drop.roles.grant(Role.MINTER, sdk.get_signer().address)  # type: ignore
    return nft_drop


def test_create_batch(nft_drop: NFTDrop):
    metadatas = []
    for i in range(10):
        metadatas.append(NFTMetadataInput(name=f"NFT {i}"))

    nft_drop.create_batch(metadatas)
    nfts = nft_drop.get_all()

    assert len(nfts) == 10

    for i, nft in enumerate(nfts):
        assert nft.metadata.name == f"NFT {i}"


"""

def test_claim_defaults(nft_drop: NFTDrop):
    assert nft_drop.total_claimed_supply == 0

    nft_drop.create_batch([NFTMetadataInput(name="NFT")])
    nft_drop.claim_conditions.set([ClaimConditionInput()])

    assert nft_drop.claim_conditions.can_claim(1) is True

    nft_drop.claim(1)

    assert nft_drop.total_claimed_supply == 1


def test_unclaimable(nft_drop: NFTDrop):
    nft_drop.claim_conditions.set(
        [ClaimConditionInput(start_time=int(time()) + 60 * 60 * 24 * 1000 * 1000)]
    )

    assert nft_drop.claim_conditions.can_claim(1) is False

"""
