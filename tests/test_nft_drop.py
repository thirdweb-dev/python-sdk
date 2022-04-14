from time import time
from brownie import accounts
import pytest
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.constants.role import Role
from thirdweb.contracts.nft_drop import NFTDrop

from thirdweb.core.sdk import ThirdwebSDK
from thirdweb.types.contracts.claim_conditions import (
    ClaimConditionInput,
    SnapshotAddressInput,
)
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


"""
def test_create_batch(nft_drop: NFTDrop):
    metadatas = []
    for i in range(10):
        metadatas.append(NFTMetadataInput(name=f"NFT {i}"))

    nft_drop.create_batch(metadatas)
    nfts = nft_drop.get_all()

    assert len(nfts) == 10

    for i, nft in enumerate(nfts):
        assert nft.metadata.name == f"NFT {i}"

    assert nft_drop.get_total_count() == 10
    assert len(nft_drop.get_all_claimed()) == 0
    assert len(nft_drop.get_all_unclaimed()) == 10


def test_claim_defaults(nft_drop: NFTDrop):
    assert nft_drop.total_claimed_supply() == 0
    assert nft_drop.balance() == 0

    nft_drop.create_batch([NFTMetadataInput(name="NFT")])
    nft_drop.claim_conditions.set(
        [ClaimConditionInput(start_time=int(time()) + 60 * 60 * 24 * 1000 * 1000)]
    )

    assert nft_drop.claim_conditions.can_claim(1) is False

    nft_drop.claim_conditions.set([ClaimConditionInput()])

    assert nft_drop.claim_conditions.can_claim(1) is True

    nft_drop.claim(1)

    assert nft_drop.total_claimed_supply() == 1
    assert nft_drop.balance() == 1



@pytest.mark.usefixtures("primary_account", "secondary_account")
def test_snapshot(nft_drop: NFTDrop, primary_account, secondary_account):
    nft_drop.claim_conditions.set(
        [
            ClaimConditionInput(start_time=int(time() / 2), price=1).set_snapshot(
                [
                    primary_account.address,
                    secondary_account.address,
                    accounts[1].address,
                ]
            ),
            ClaimConditionInput().set_snapshot([primary_account.address]),
        ]
    )

    metadata = nft_drop.metadata.get()
    merkles = metadata.merkle

    # TODO: Test if merkle roots are correct

    roots = [c.merkle_root_hash for c in nft_drop.claim_conditions.get_all()]
    assert len(roots) == 2


"""


@pytest.mark.usefixtures("sdk", "primary_account", "secondary_account")
def test_snapshot_claim(
    nft_drop: NFTDrop, sdk: ThirdwebSDK, primary_account, secondary_account
):
    assert nft_drop.balance() == 0

    metadatas = []
    for i in range(10):
        metadatas.append(NFTMetadataInput(name=f"NFT {i}"))
    nft_drop.create_batch(metadatas)
    nft_drop.claim_conditions.set(
        [
            ClaimConditionInput(
                start_time=int(time()) / 2,
                snapshot=[
                    SnapshotAddressInput(
                        address=primary_account.address, max_claimable=10
                    )
                ],
            )
        ]
    )

    print("ACTIVE: ", nft_drop.claim_conditions.get_active())

    # assert nft_drop.claim_conditions.can_claim(1) is True
    # assert nft_drop.claim_conditions.can_claim(1, secondary_account.address) is False

    try:
        sdk.update_signer(secondary_account)
        nft_drop.claim(1)
        assert False
    except:
        pass

    sdk.update_signer(primary_account)
    nft_drop.claim(1)

    assert nft_drop.balance() == 1
