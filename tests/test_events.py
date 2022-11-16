from time import time
from typing import Optional
from brownie import accounts
import pytest
from thirdweb.constants.currency import NATIVE_TOKEN_ADDRESS, ZERO_ADDRESS
from thirdweb.constants.events import EventStatus, EventType
from thirdweb.contracts.nft_collection import NFTCollection
from thirdweb.core.sdk import ThirdwebSDK
from thirdweb.types.contracts.signature import PayloadToSign721
from thirdweb.types.events import EventQueryOptions, SignatureEvent, TxEvent
from thirdweb.types.nft import NFTMetadataInput
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


def test_transaction_events(nft_collection: NFTCollection):
    event_status: Optional[EventStatus] = None

    def listener(event: TxEvent):
        nonlocal event_status
        print(event)
        if event_status is None:
            assert event.status == EventStatus.SUBMITTED
        elif event_status == EventStatus.SUBMITTED:
            assert event.status == EventStatus.COMPLETED

        event_status = event.status

    nft_collection.events.add_transaction_listener(listener)

    nft_collection.set_approval_for_all(ZERO_ADDRESS, True)
    assert event_status is not None


def test_signature_events(nft_collection: NFTCollection):
    event_status: Optional[EventStatus] = None

    def listener(event: SignatureEvent):
        nonlocal event_status
        print(event)
        if event_status is None:
            assert event.status == EventStatus.SUBMITTED
        elif event_status == EventStatus.SUBMITTED:
            assert event.status == EventStatus.COMPLETED

        event_status = event.status

    nft_collection._contract_wrapper.on(EventType.SIGNATURE, listener)  # type: ignore

    nft_collection.signature.generate(
        PayloadToSign721(
            to=accounts[0].address,
            price=1,
            currency_address=NATIVE_TOKEN_ADDRESS,
            metadata=NFTMetadataInput(name="Signature"),
            mint_end_time=int(time() + 60 * 60 * 24 * 1000 * 1000),
            mint_start_time=int(time()),
            uid=None,
            primary_sale_recipient=ZERO_ADDRESS,
        )
    )
    assert event_status is not None


@pytest.mark.usefixtures("primary_account")
def test_collection_events(nft_collection: NFTCollection, primary_account, secondary_account):
    nft_collection.mint(NFTMetadataInput(name="Minted"))
    events = nft_collection.events.get_events("TokensMinted", EventQueryOptions(filters={"mintedTo": primary_account.address}))
    assert len(events) == 1
    assert events[0].get("event") == "TokensMinted"

    events = nft_collection.events.get_events("TokensMinted", EventQueryOptions(filters={"mintedTo": secondary_account.address}))
    assert len(events) == 0