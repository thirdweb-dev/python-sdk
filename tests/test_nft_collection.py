from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.types.nft import NFTMetadataInput
from thirdweb.contracts import NFTCollection
from thirdweb.core.sdk import ThirdwebSDK
from brownie import accounts
import pytest

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


def test_mint(nft_collection: NFTCollection):
    result = nft_collection.mint(
        NFTMetadataInput.from_json(
            {"name": "Python SDK NFT", "description": "Minted with the python SDK!"}
        )
    )

    assert result.id == 0
    assert result.data().metadata.name == "Python SDK NFT"

    metadata = nft_collection.get(0).metadata

    assert metadata.name == "Python SDK NFT"
    assert metadata.description == "Minted with the python SDK!"
    assert nft_collection.balance() == 1


def test_burn(nft_collection: NFTCollection):
    nft_collection.mint(NFTMetadataInput.from_json({"name": "Python SDK NFT"}))
    nft = nft_collection.get(0)

    assert nft_collection.total_supply() == 1
    assert nft.metadata.name == "Python SDK NFT"
    assert nft.owner == nft_collection._contract_wrapper.get_signer_address()

    nft_collection.burn(0)

    try:
        nft_collection.get(0)
        assert False
    except:
        assert True


def test_transfer(nft_collection: NFTCollection):
    nft_collection.mint(NFTMetadataInput.from_json({"name": "Python SDK NFT"}))

    assert nft_collection.balance() == 1
    assert nft_collection.balance_of(accounts[0].address) == 0

    nft_collection.transfer(accounts[0].address, 0)

    assert nft_collection.balance() == 0
    assert nft_collection.balance_of(accounts[0].address) == 1


def test_batch_mint_to(nft_collection: NFTCollection):
    results = nft_collection.mint_batch_to(
        accounts[0].address,
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

    assert len(results) == 2

    nft_1 = nft_collection.get(0)
    nft_2 = nft_collection.get(1)

    assert nft_1.owner == accounts[0].address
    assert nft_2.owner == accounts[0].address

    assert nft_1.metadata.name == "Python SDK NFT 1"
    assert nft_2.metadata.name == "Python SDK NFT 2"
    assert nft_1.metadata.description == "Minted with the python SDK!"
    assert nft_2.metadata.description == "Minted with the python SDK!"


@pytest.mark.usefixtures("primary_account")
def test_ownership(nft_collection: NFTCollection, primary_account):
    nft_collection.mint_batch_to(
        primary_account.address,
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

    assert nft_collection.get_owned_token_ids() == [0, 1]
    assert nft_collection.get_owned()[0].metadata.name == "Python SDK NFT 1"
