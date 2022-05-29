"""Interface for interacting with a marketplace contract"""

from time import time
from thirdweb.common.error import ListingNotFoundException
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.core.classes.contract_events import ContractEvents
from thirdweb.core.classes.contract_platform_fee import ContractPlatformFee
from thirdweb.types.marketplace import (
    AuctionListing,
    ContractListing,
    DirectListing,
    ListingType,
    MarketplaceFilter,
)
from thirdweb.types.settings.metadata import MarketplaceContractMetadata
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_roles import ContractRoles
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.core.classes.marketplace_auction import MarketplaceAuction
from thirdweb.core.classes.marketplace_direct import MarketplaceDirect
from thirdweb.types.contract import ContractType
from eth_account.account import LocalAccount
from thirdweb.types.sdk import SDKOptions
from thirdweb.constants.role import Role, get_role_hash
from typing import Any, Final, List, Optional, Union, cast
from thirdweb.abi import Marketplace as MarketplaceABI
from web3.eth import TxReceipt
from web3 import Web3


class Marketplace(BaseContract[MarketplaceABI]):
    """
    Create your own whitelabel marketplace that enables users to buy and sell any digital assets.

    ```python
    from thirdweb import ThirdwebSDK

    # You can customize this to a supported network or your own RPC URL
    network = "mumbai"

    # Now we can create a new instance of the SDK
    sdk = ThirdwebSDK(network)

    # If you want to send transactions, you can instantiate the SDK with a private key instead:
    #   sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, network)

    contract = sdk.get_marketplace("{{contract_address}}")
    ```
    """

    _abi_type = MarketplaceABI
    _storage: IpfsStorage

    contract_type: Final[ContractType] = ContractType.MARKETPLACE
    contract_roles: Final[List[Role]] = [Role.ADMIN, Role.LISTER, Role.ASSET]

    metadata: ContractMetadata[MarketplaceABI, MarketplaceContractMetadata]
    roles: ContractRoles
    platform_fee: ContractPlatformFee[MarketplaceABI]
    direct: MarketplaceDirect
    auction: MarketplaceAuction
    events: ContractEvents[MarketplaceABI]

    def __init__(
        self,
        provider: Web3,
        address: str,
        storage: IpfsStorage,
        signer: Optional[LocalAccount] = None,
        options: SDKOptions = SDKOptions(),
    ):
        abi = MarketplaceABI(provider, address)
        contract_wrapper = ContractWrapper(abi, provider, signer, options)
        super().__init__(contract_wrapper)

        self._storage = storage
        self.metadata = ContractMetadata(
            contract_wrapper, storage, MarketplaceContractMetadata
        )
        self.platform_fee = ContractPlatformFee(contract_wrapper)
        self.direct = MarketplaceDirect(contract_wrapper, storage)
        self.auction = MarketplaceAuction(contract_wrapper, storage)
        self.events = ContractEvents(contract_wrapper)

    """
    READ FUNCTIONS
    """

    def get_listing(self, listing_id: int) -> Union[DirectListing, AuctionListing]:
        """
        Get a listing from the marketplace by ID

        :param listing_id: ID of the listing to get
        :return: Listing object
        """
        listing_args = self._contract_wrapper._contract_abi.listings.call(listing_id)
        listing = ContractListing(*listing_args)

        if listing.asset_contract == ZERO_ADDRESS:
            raise ListingNotFoundException(listing_id)

        if ListingType(listing.listing_type) == ListingType.AUCTION:
            return self.auction._map_listing(listing)
        if ListingType(listing.listing_type) == ListingType.DIRECT:
            return self.direct._map_listing(listing)

        raise Exception(f"Unkown listing type {listing.listing_type}")

    def get_active_listings(self) -> List[Union[DirectListing, AuctionListing]]:
        """
        Get all the currently active listings from the marketplace.

        ```python
        listings = contract.get_active_listings()
        price_of_first = listings[0].price
        ```

        :return: List of listings
        """
        raw_listings = self._get_all_listings_no_filter()

        listings: List[Union[DirectListing, AuctionListing]] = []
        for listing in raw_listings:
            if ListingType(listing.type) == ListingType.AUCTION and cast(
                AuctionListing, listing
            ).end_time_in_epoch_seconds > int(time()):
                listings.append(listing)
            elif (
                ListingType(listing.type) == ListingType.DIRECT and listing.quantity > 0
            ):
                listings.append(listing)

        return listings

    def get_all_listings(
        self, filter: MarketplaceFilter = None
    ) -> List[Union[DirectListing, AuctionListing]]:
        """
        Get all the listings that have ever been made on this marketplace.

        ```python
        listings = contract.get_all_listings()
        price_of_first = listings[0].price
        ```

        :param filter: Filter to apply to the listings
        :return: List of listings
        """
        raw_listings = self._get_all_listings_no_filter()

        if filter is not None:
            if filter.seller:
                raw_listings = [
                    listing
                    for listing in raw_listings
                    if listing.seller_address == filter.seller
                ]
            if filter.token_contract:
                if filter.token_id:
                    raw_listings = [
                        listing
                        for listing in raw_listings
                        if listing.asset_contract_address == filter.token_contract
                        and listing.token_id == filter.token_id
                    ]
                else:
                    raw_listings = [
                        listing
                        for listing in raw_listings
                        if listing.asset_contract_address == filter.token_contract
                    ]

            max_id = min(filter.start + filter.count, self.get_total_count())
            raw_listings = [raw_listings[i] for i in range(filter.start, max_id)]

        return [listing for listing in raw_listings if listing is not None]

    get_all = get_all_listings

    def get_total_count(self) -> int:
        """
        Get the total number of listings on this marketplace.

        :return: Total number of listings
        """
        return self._contract_wrapper._contract_abi.total_listings.call()

    def is_restricted_to_lister_role_only(self) -> bool:
        """
        Check whether only wallets with the lister role can make listings.

        :return: True if only lister wallets can make listings
        """
        anyone_can_list = self._contract_wrapper._contract_abi.has_role.call(
            get_role_hash(Role.LISTER), ZERO_ADDRESS
        )
        return not anyone_can_list

    def get_bid_buffer_bps(self) -> int:
        """
        Get the bid buffer basis points for this marketplace.

        :return: Bid buffer basis points
        """
        return self._contract_wrapper._contract_abi.bid_buffer_bps.call()

    def get_time_buffer_in_seconds(self) -> int:
        """
        Get the time buffer for this marketplace in seconds

        :return: Time buffer in seconds
        """
        return self._contract_wrapper._contract_abi.time_buffer.call()

    """
    WRITE FUNCTIONS
    """

    def buyout_listing(
        self,
        listing_id: int,
        quantity_desired: Optional[int] = None,
        receiver: Optional[str] = None,
    ) -> TxReceipt:
        """
        Buyout a listing by listing ID

        ```python
        listing_id = 0
        quantity_desired = 1

        contract.buyout_listing(listing_id, quantity_desired)
        ```

        :param listing_id: ID of the listing to buyout
        :param quantity_desired: Quantity to buyout
        :param receiver: Address to send the asset to
        :return: Transaction receipt of buyout
        """
        raw_listing = self._contract_wrapper._contract_abi.listings.call(listing_id)
        listing = ContractListing(*raw_listing)

        if listing.listing_id != listing_id:
            raise ListingNotFoundException(listing_id)

        if ListingType(listing.listing_type) == ListingType.DIRECT:
            if quantity_desired is None:
                raise Exception("quantity_desired is required for direct listings")

            return self.direct.buyout_listing(listing_id, quantity_desired, receiver)
        elif ListingType(listing.listing_type) == ListingType.AUCTION:
            return self.auction.buyout_listing(listing_id)

        raise Exception(f"Unkown listing type {listing.listing_type}")

    def set_bid_buffer_bps(self, buffer_bps: int) -> TxReceipt:
        """
        Set the bid buffer basis points for this marketplace.

        ```python
        buffer_bps = 500
        contract.set_bid_buffer_bps(buffer_bps)
        ```

        :param buffer_bps: Bid buffer basis points
        :return: Transaction receipt
        """
        self.roles.verify([Role.ADMIN], self._contract_wrapper.get_signer_address())

        time_buffer = self.get_time_buffer_in_seconds()
        return self._contract_wrapper.send_transaction(
            "set_auction_buffers", [time_buffer, buffer_bps]
        )

    def set_time_buffer_in_seconds(self, buffer_in_seconds: int) -> TxReceipt:
        """
        Set the time buffer of the marketplace.

        ```python
        buffer_in_seconds = 60
        contract.set_time_buffer_in_seconds(buffer_in_seconds)
        ```

        :param buffer_in_seconds: Time buffer in seconds
        :return: Transaction receipt
        """
        self.roles.verify([Role.ADMIN], self._contract_wrapper.get_signer_address())

        bid_buffer_bps = self.get_bid_buffer_bps()
        return self._contract_wrapper.send_transaction(
            "set_auction_buffers", [buffer_in_seconds, bid_buffer_bps]
        )

    def allow_listing_from_specific_asset_only(
        self, contract_address: str
    ) -> TxReceipt:
        """
        Restrict marketplace so only specific asset can be listed.

        :param contract_address: Address of the asset contract
        """
        encoded = []
        interface = self._contract_wrapper.get_contract_interface()
        members = self.roles.get(Role.ASSET)

        if ZERO_ADDRESS in members:
            encoded.append(
                interface.encodeABI(
                    "revoke_role", [get_role_hash(Role.ASSET), ZERO_ADDRESS]
                )
            )

        encoded.append(
            interface.encodeABI(
                "grant_role", [get_role_hash(Role.ASSET), contract_address]
            )
        )

        return self._contract_wrapper.multi_call(encoded)

    def allow_listing_from_any_asset(self) -> TxReceipt:
        """
        Allow asset to be listed on the marketplace.

        :return: Transaction receipt
        """

        encoded = []
        interface = self._contract_wrapper.get_contract_interface()
        members = self.roles.get(Role.ASSET)

        for member in members:
            encoded.append(
                interface.encodeABI("revoke_role", [get_role_hash(Role.ASSET), member])
            )

        encoded.append(
            interface.encodeABI("grant_role", [get_role_hash(Role.ASSET), ZERO_ADDRESS])
        )

        return self._contract_wrapper.multi_call(encoded)

    """
    INTERNAL FUNCTIONS
    """

    def _get_all_listings_no_filter(
        self,
    ) -> List[Union[DirectListing, AuctionListing]]:
        total_listings = self._contract_wrapper._contract_abi.total_listings.call()

        listings = []
        for i in range(total_listings):
            try:
                listing = self.get_listing(i)

                if ListingType(listing.type) == ListingType.AUCTION:
                    listings.append(listing)
                else:
                    valid = self.direct._is_still_valid_listing(cast(Any, listing))

                    if valid:
                        listings.append(listing)
            except:
                pass

        return [listing for listing in listings if listing is not None]
