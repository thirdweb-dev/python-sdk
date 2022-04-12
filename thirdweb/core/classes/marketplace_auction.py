from time import time
from typing import Any, Dict, Optional, cast
from thirdweb.abi import Marketplace
from thirdweb.abi.marketplace import IMarketplaceListingParameters
from thirdweb.common.currency import (
    fetch_currency_metadata,
    fetch_currency_value,
    format_units,
    normalize_price_value,
    set_erc20_allowance,
)
from thirdweb.common.error import (
    AuctionAlreadyStartedException,
    ListingNotFoundException,
    WrongListingTypeException,
)
from thirdweb.common.marketplace import (
    handle_token_approval,
    is_winning_bid,
    map_offer,
    validate_new_listing_param,
)
from thirdweb.common.nft import fetch_token_metadata_for_contract
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.currency import Price
from thirdweb.types.marketplace import (
    AuctionListing,
    ContractListing,
    ContractOffer,
    ListingType,
    NewAuctionListing,
    Offer,
)
from web3.eth import TxReceipt


class MarketplaceAuction(BaseContract[Marketplace]):
    _storage: IpfsStorage

    def __init__(self, contract_wrapper: ContractWrapper, storage: IpfsStorage):
        super().__init__(contract_wrapper)
        self._storage = storage

    """
    READ FUNCTIONS
    """

    def get_listing(self, listing_id: int) -> AuctionListing:
        """
        Get an auction listing from the marketplace by ID

        :param listing_id: The ID of the listing to get
        :return: The auction listing
        """
        raw_listing = self._contract_wrapper._contract_abi.listings.call(listing_id)
        listing = ContractListing(*raw_listing)

        if listing.listing_id != listing_id:
            raise ListingNotFoundException(listing_id)

        if ListingType(listing.listing_type) != ListingType.AUCTION:
            raise WrongListingTypeException(
                listing_id,
                "Auction",
                "Auction",
            )

        return self._map_listing(listing)

    def get_winning_bid(self, listing_id: int) -> Optional[Offer]:
        """
        Get the winning bid on an auction listing

        :param listing_id: The ID of the listing to get the winning bid for
        :return: The winning bid
        """
        self._validate_listing(listing_id)
        raw_offers = self._contract_wrapper._contract_abi.winning_bid.call(listing_id)
        offers = ContractOffer(*raw_offers)

        if offers.offeror == ZERO_ADDRESS:
            return None

        return map_offer(self._contract_wrapper.get_provider(), listing_id, offers)

    def get_winner(self, listing_id) -> str:
        """
        Get the winner of an auction that has already ended.

        :param listing_id: The ID of the listing to get the winner for
        :return: The winning bidder
        """
        interface = self._contract_wrapper.get_contract_interface()
        closed_auctions = interface.events.AuctionClosed().getLogs()

        auctions = [
            auction.get("args").get("listing_id") == listing_id
            for auction in closed_auctions
        ]

        if len(auctions) == 0:
            raise Exception(
                f"Could not find auction with listing ID {listing_id} in close auctions"
            )

        return auctions[0].get("winning_bidder")

    """
    WRITE FUNCTIONS
    """

    def create_listing(self, listing: NewAuctionListing) -> int:
        """
        Create a new auction listing

        :param listing: The listing to create
        :return: The ID of the listing
        """
        validate_new_listing_param(listing)

        handle_token_approval(
            self._contract_wrapper.get_provider(),
            self._contract_wrapper.get_signer(),
            self.get_address(),
            listing.asset_contract_address,
            listing.token_id,
            self._contract_wrapper.get_signer_address(),
        )

        normalized_price_per_token = normalize_price_value(
            self._contract_wrapper.get_provider(),
            listing.buyout_price_per_token,
            listing.currency_contract_address,
        )

        normalized_reserve_price = normalize_price_value(
            self._contract_wrapper.get_provider(),
            listing.reserve_price_per_token,
            listing.currency_contract_address,
        )

        receipt = self._contract_wrapper.send_transaction(
            "create_listing",
            [
                IMarketplaceListingParameters(
                    assetContract=listing.asset_contract_address,
                    tokenId=listing.token_id,
                    startTime=listing.start_time_in_seconds,
                    secondsUntilEndTime=listing.listing_duration_in_seconds,
                    quantityToList=listing.quantity,
                    currencyToAccept=listing.currency_contract_address,
                    reservePricePerToken=normalized_reserve_price,
                    buyoutPricePerToken=normalized_price_per_token,
                    listingType=1,
                ),
            ],
        )

        events = self._contract_wrapper.get_events("ListingAdded", receipt)
        return cast(Any, events[0].get("args")).get("listingId")

    def buyout_listing(self, listing_id: int) -> TxReceipt:
        """
        Buyout an auction listing

        :param listing_id: The ID of the listing to buyout
        :return: The transaction receipt
        """
        listing = self._validate_listing(listing_id)

        currency_metadata = fetch_currency_metadata(
            self._contract_wrapper.get_provider(), listing.currency_contract_address
        )

        return self.make_bid(
            listing_id, format_units(listing.buyout_price, currency_metadata.decimals)
        )

    def make_bid(self, listing_id: int, price_per_token: Price) -> TxReceipt:
        """
        Make a bid on an auction listing

        :param listing_id: The ID of the listing to bid on
        :param price_per_token: The price per token to bid
        :return: The transaction receipt
        """
        listing = self._validate_listing(listing_id)
        normalized_price = normalize_price_value(
            self._contract_wrapper.get_provider(),
            price_per_token,
            listing.currency_contract_address,
        )

        bid_buffer = self._contract_wrapper._contract_abi.bid_buffer_bps.call()
        winning_bid = self.get_winning_bid(listing_id)

        if winning_bid is not None:
            is_winner = is_winning_bid(
                winning_bid.price_per_token, normalized_price, bid_buffer
            )

            if not is_winner:
                "Bid price is too low based on the current winning bid and the bid buffer"
        else:
            token_price = normalized_price
            reserve_price = listing.reserve_price

            if not token_price >= reserve_price:
                "Bid price is too low based on reserve price"

        quantity = listing.quantity
        value = normalized_price * quantity

        overrides: Dict[Any, Any] = {}
        set_erc20_allowance(
            self._contract_wrapper, value, listing.currency_contract_address, overrides
        )

        return self._contract_wrapper.send_transaction(
            "offer",
            [
                listing_id,
                listing.quantity,
                listing.currency_contract_address,
                normalized_price,
            ],
        )

    def cancel_listing(self, listing_id: int) -> TxReceipt:
        """
        Cancel an auction listing

        :param listing_id: The ID of the listing to cancel
        :return: The transaction receipt
        """
        listing = self._validate_listing(listing_id)

        now = int(time())
        start_time = listing.start_time_in_epoch_seconds

        raw_offers = self._contract_wrapper._contract_abi.winning_bid.call(listing_id)
        offers = ContractOffer(*raw_offers)

        if now > start_time and offers.offeror != ZERO_ADDRESS:
            raise AuctionAlreadyStartedException(listing_id)

        return self._contract_wrapper.send_transaction(
            "close_auction", [listing_id, self._contract_wrapper.get_signer_address()]
        )

    def close_listing(
        self, listing_id: int, close_for: Optional[str] = None
    ) -> TxReceipt:
        if not close_for:
            close_for = self._contract_wrapper.get_signer_address()

        listing = self._validate_listing(listing_id)

        try:
            return self._contract_wrapper.send_transaction(
                "close_auction", [listing_id, close_for]
            )
        except Exception as err:
            raise Exception(err)

    def update_listing(self, listing: AuctionListing) -> TxReceipt:
        """
        Update a listing on the marketplace

        :param listing: The listing to update
        :return: The transaction receipt
        """

        return self._contract_wrapper.send_transaction(
            "update_listing",
            [
                listing.id,
                listing.quantity,
                listing.reserve_price,
                listing.buyout_price,
                listing.currency_contract_address,
                listing.start_time_in_epoch_seconds,
                listing.end_time_in_epoch_seconds,
            ],
        )

    """
    INTERNAL FUNCTIONS
    """

    def _validate_listing(self, listing_id: int) -> AuctionListing:
        try:
            return self.get_listing(listing_id)
        except:
            raise ListingNotFoundException(listing_id)

    def _map_listing(self, listing: ContractListing) -> AuctionListing:
        return AuctionListing(
            id=listing.listing_id,
            asset_contract_address=listing.asset_contract,
            buyout_price=listing.buyout_price_per_token,
            currency_contract_address=listing.currency,
            buyout_currency_value_per_token=fetch_currency_value(
                self._contract_wrapper.get_provider(),
                listing.currency,
                listing.buyout_price_per_token,
            ),
            token_id=listing.token_id,
            quantity=listing.quantity,
            start_time_in_epoch_seconds=listing.start_time,
            asset=fetch_token_metadata_for_contract(
                listing.asset_contract,
                self._contract_wrapper.get_provider(),
                listing.token_id,
                self._storage,
            ),
            reserve_price_currency_value_per_token=fetch_currency_value(
                self._contract_wrapper.get_provider(),
                listing.currency,
                listing.reserve_price_per_token,
            ),
            reserve_price=listing.reserve_price_per_token,
            end_time_in_epoch_seconds=listing.end_time,
            seller_address=listing.token_owner,
        )
