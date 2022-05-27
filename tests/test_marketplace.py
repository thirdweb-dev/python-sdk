from time import time
from thirdweb.core.sdk import ThirdwebSDK
from thirdweb.contracts import Marketplace, NFTCollection, Edition, Token
from brownie import accounts
import pytest
from thirdweb.types.currency import TokenAmount
from thirdweb.types.marketplace import NewAuctionListing, NewDirectListing

from thirdweb.types.nft import EditionMetadataInput, NFTMetadataInput
from thirdweb.types.settings.metadata import (
    EditionContractMetadata,
    MarketplaceContractMetadata,
    NFTCollectionContractMetadata,
    TokenContractMetadata,
)


@pytest.mark.usefixtures("sdk", "primary_account")
@pytest.fixture(scope="function")
def marketplace(sdk: ThirdwebSDK, primary_account) -> Marketplace:
    sdk.update_signer(primary_account)
    return sdk.get_marketplace(
        sdk.deployer.deploy_marketplace(
            MarketplaceContractMetadata(
                name="Test Marketplace",
                platform_fee_basis_points=0,
            )
        )
    )


@pytest.mark.usefixtures("sdk")
@pytest.fixture(scope="function")
def nft_collection(sdk: ThirdwebSDK) -> NFTCollection:
    nft_collection = sdk.get_nft_collection(
        sdk.deployer.deploy_nft_collection(
            NFTCollectionContractMetadata(
                name="Test NFT",
                seller_fee_basis_points=200,
                fee_recipient=sdk.get_signer().address,  # type: ignore
                primary_sale_recipient=sdk.get_signer().address,  # type: ignore
            )
        )
    )

    nft_collection.mint_batch(
        [
            NFTMetadataInput(name="Test 0"),
            NFTMetadataInput(name="Test 1"),
            NFTMetadataInput(name="Test 2"),
            NFTMetadataInput(name="Test 3"),
        ]
    )

    return nft_collection


@pytest.mark.usefixtures("sdk")
@pytest.fixture()
def edition(sdk: ThirdwebSDK) -> Edition:
    edition = sdk.get_edition(
        sdk.deployer.deploy_edition(
            EditionContractMetadata(
                name="Test Edition",
                seller_fee_basis_points=100,
                primary_sale_recipient=sdk.get_signer().address,  # type: ignore
            )
        )
    )

    edition.mint_batch(
        [
            EditionMetadataInput(
                metadata=NFTMetadataInput(name="Test 0"), supply=100000
            ),
            EditionMetadataInput(
                metadata=NFTMetadataInput(name="Test 1"), supply=100000
            ),
        ]
    )

    return edition


@pytest.mark.usefixtures("sdk")
@pytest.fixture(scope="function")
def token(sdk: ThirdwebSDK) -> Token:
    token = sdk.get_token(
        sdk.deployer.deploy_token(
            TokenContractMetadata(
                name="Test Token",
                symbol="TEST",
                primary_sale_recipient=sdk.get_signer().address,  # type: ignore
            )
        )
    )

    token.mint_batch_to(
        [
            TokenAmount(to_address=accounts[0].address, amount=1000),
            TokenAmount(to_address=accounts[1].address, amount=1000),
            TokenAmount(to_address=sdk.get_signer().address, amount=1000),  # type: ignore
        ]
    )

    return token


def create_direct_listing(
    marketplace: Marketplace,
    token_address: str,
    contract_address: str,
    token_id: int,
    quantity: int = 1,
) -> int:
    return marketplace.direct.create_listing(
        NewDirectListing(
            asset_contract_address=contract_address,
            buyout_price_per_token=0.1,  # type: ignore
            currency_contract_address=token_address,
            start_time_in_seconds=int(time()) - 1800,
            listing_duration_in_seconds=60 * 60 * 24 * 365 * 100,
            token_id=token_id,
            quantity=quantity,
        )
    )


def create_auction_listing(
    marketplace: Marketplace,
    token_address: str,
    contract_address: str,
    token_id: int,
    quantity: int = 1,
):
    return marketplace.auction.create_listing(
        NewAuctionListing(
            asset_contract_address=contract_address,
            buyout_price_per_token=0.1,  # type: ignore
            currency_contract_address=token_address,
            start_time_in_seconds=int(time()) - 1800,
            listing_duration_in_seconds=60 * 60 * 24 * 365 * 100,
            token_id=token_id,
            quantity=quantity,
            reserve_price_per_token=0.05,  # type: ignore
        )
    )


def test_listings(
    sdk: ThirdwebSDK,
    marketplace: Marketplace,
    nft_collection: NFTCollection,
    token: Token,
):
    listing_id = create_direct_listing(
        marketplace, token.get_address(), nft_collection.get_address(), 0
    )

    assert listing_id == 0

    listing_id = create_auction_listing(
        marketplace, token.get_address(), nft_collection.get_address(), 1
    )

    assert listing_id == 1

    assert len(marketplace.get_all()) == 2

    listing_1 = marketplace.direct.get_listing(0)
    listing_2 = marketplace.auction.get_listing(1)

    assert listing_1.buyout_currency_value_per_token.display_value == 0.1
    assert listing_2.reserve_price_currency_value_per_token.display_value == 0.05

    assert len(marketplace.get_active_listings()) == 2
    assert nft_collection.owner_of(0) == sdk.get_signer().address  # type: ignore

    marketplace.buyout_listing(0, quantity_desired=1, receiver=accounts[0].address)

    assert len(marketplace.get_active_listings()) == 1
    assert nft_collection.owner_of(0) == accounts[0].address


def test_make_offer(
    sdk: ThirdwebSDK,
    marketplace: Marketplace,
    nft_collection: NFTCollection,
    token: Token,
):
    listing_id = create_direct_listing(
        marketplace, token.get_address(), nft_collection.get_address(), 0
    )

    assert listing_id == 0

    marketplace.direct.make_offer(
        0,
        quantity_desired=1,
        currency_contract_address=token.get_address(),
        price_per_token=0.1,
    )
