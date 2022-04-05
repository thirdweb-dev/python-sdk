from re import M
from typing import Any, Dict, Optional

from brownie import ZERO_ADDRESS
from eth_utils import is_address
from thirdweb.abi import Marketplace
from thirdweb.abi.erc165 import ERC165
from thirdweb.abi.ierc1155 import IERC1155
from thirdweb.abi.ierc721 import IERC721
from thirdweb.common.currency import (
    fetch_currency_value,
    is_native_token,
    normalize_price_value,
    set_erc20_allowance,
)
from thirdweb.common.error import ListingNotFoundException, WrongListingTypeException
from thirdweb.common.marketplace import (
    handle_token_approval,
    is_token_approved_for_marketplace,
    map_offer,
    validate_new_listing_param,
)
from thirdweb.common.nft import fetch_token_metadata_for_contract
from thirdweb.constants.contract import INTERFACE_ID_IERC1155, INTERFACE_ID_IERC721
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.marketplace import (
    ContractListing,
    ContractOffer,
    DirectListing,
    ListingType,
    NewDirectListing,
    Offer,
)
from web3.eth import TxReceipt


class MarketplaceDirect(BaseContract[Marketplace]):
    _storage: IpfsStorage

    def __init__(self, contract_wrapper: ContractWrapper, storage: IpfsStorage):
        super().__init__(contract_wrapper)
        self._storage = storage

    """
    READ FUNCTIONS
    """

    def get_listing(self, listing_id: int) -> DirectListing:
        raw_listing = self._contract_wrapper._contract_abi.listings.call(listing_id)
        listing = ContractListing(*raw_listing)

        if listing.asset_contract == ZERO_ADDRESS:
            raise ListingNotFoundException(listing_id)

        if listing.listing_type != ListingType.DIRECT:
            raise WrongListingTypeException(
                listing_id,
                "Auction",
                "Direct",
            )

        return self._map_listing(listing)

    def get_active_offer(self, listing_id: int, address: str) -> Optional[Offer]:
        self._validate_listing(listing_id)

        if not is_address(address):
            raise Exception("Address must be a valid address")

        raw_ofers = self._contract_wrapper._contract_abi.offers.call(
            listing_id, address
        )
        offers = ContractOffer(*raw_ofers)

        if offers.offeror == ZERO_ADDRESS:
            return None

        return map_offer(self._contract_wrapper.get_provider(), listing_id, offers)

    """
    WRITE FUNCTIONS
    """

    def create_listing(self, listing: NewDirectListing) -> TxReceipt:
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

        return self._contract_wrapper.send_transaction(
            "create_listing",
            [
                {
                    "asset_contract": listing.asset_contract_address,
                    "token_id": listing.token_id,
                    "buyout_price_per_token": normalized_price_per_token,
                    "currency_to_accept": listing.currency_contract_address,
                    "quantity_to_list": listing.quantity,
                    "reserve_price_per_token": normalized_price_per_token,
                    "seconds_until_end_time": listing.listing_duration_in_seconds,
                    "start_time": listing.start_time_in_seconds,
                }
            ],
        )

    def make_offer(
        self,
        listing_id: int,
        quantity_desired: int,
        currency_contract_address: str,
        price_per_token: int,
    ) -> TxReceipt:
        if is_native_token(currency_contract_address):
            raise Exception(
                "You must used the wrapped native token address when making an offer"
            )

        normalized_price = normalize_price_value(
            self._contract_wrapper.get_provider(),
            price_per_token,
            currency_contract_address,
        )

        try:
            self.get_listing(listing_id)
        except:
            raise ListingNotFoundException(listing_id)

        overrides: Dict[Any, Any] = {}
        set_erc20_allowance(
            self._contract_wrapper,
            quantity_desired * normalized_price,
            currency_contract_address,
            overrides,
        )

        # TODO: Add OVERRIDES
        return self._contract_wrapper.send_transaction(
            "offer",
            [listing_id, quantity_desired, currency_contract_address, normalized_price],
        )

    def accept_offer(self, listing_id: int, address_or_offerror: str) -> TxReceipt:
        self._validate_listing(listing_id)

        raw_offer = self._contract_wrapper._contract_abi.offers.call(
            listing_id, address_or_offerror
        )
        offer = ContractOffer(*raw_offer)

        return self._contract_wrapper.send_transaction(
            "accept_offer",
            [listing_id, address_or_offerror, offer.currency, offer.price_per_token],
        )

    def buyout_listing(
        self, listing_id: int, quantity_desired: int, receiver: Optional[str] = None
    ) -> TxReceipt:
        listing = self._validate_listing(listing_id)
        valid = self._is_still_valid_listing(listing, quantity_desired)

        if not valid:
            raise Exception(
                "The asset on this listing has been moved from the lister's wallet, this listing is now invalid"
            )

        buy_for = receiver if receiver else self._contract_wrapper.get_signer_address()

        overrides: Dict[Any, Any] = {}
        set_erc20_allowance(
            self._contract_wrapper,
            listing.buyout_price * quantity_desired,
            listing.currency_contract_address,
            overrides,
        )

        # TODO: Add OVERRIDES
        return self._contract_wrapper.send_transaction(
            "buy",
            [
                listing_id,
                buy_for,
                quantity_desired,
                listing.currency_contract_address,
                listing.buyout_price * quantity_desired,
            ],
        )

    def update_listing(self, listing: DirectListing) -> TxReceipt:
        return self._contract_wrapper.send_transaction(
            "update_listing",
            [
                listing.id,
                listing.quantity,
                listing.buyout_price,
                listing.buyout_price,
                listing.currency_contract_address,
                listing.start_time_in_seconds,
                listing.seconds_until_end,
            ],
        )

    def cancel_listing(self, listing_id: int) -> TxReceipt:
        return self._contract_wrapper.send_transaction(
            "cancel_direct_listing", [listing_id]
        )

    """
    INTERNAL FUNCTIONS
    """

    def _validate_listing(self, listing_id: int) -> DirectListing:
        try:
            return self.get_listing(listing_id)
        except:
            raise ListingNotFoundException(listing_id)

    def _map_listing(self, listing: ContractListing) -> DirectListing:
        return DirectListing(
            id=listing.listing_id,
            asset_contract_address=listing.asset_contract,
            token_id=listing.token_id,
            buyout_price=listing.buyout_price_per_token,
            currency_contract_address=listing.currency,
            buyout_currency_value_per_token=fetch_currency_value(
                self._contract_wrapper.get_provider(),
                listing.currency,
                listing.buyout_price_per_token,
            ),
            quantity=listing.quantity,
            start_time_in_seconds=listing.start_time,
            asset=fetch_token_metadata_for_contract(
                listing.asset_contract,
                self._contract_wrapper.get_provider(),
                listing.token_id,
                self._storage,
            ),
            seconds_until_end=listing.end_time,
            seller_address=listing.token_owner,
        )

    def _is_still_valid_listing(
        self, listing: DirectListing, quantity: Optional[int] = None
    ) -> bool:
        approved = is_token_approved_for_marketplace(
            self._contract_wrapper.get_provider(),
            self.get_address(),
            listing.asset_contract_address,
            listing.token_id,
            listing.seller_address,
        )

        if not approved:
            return False

        provider = self._contract_wrapper.get_provider()
        erc165 = ERC165(provider, listing.asset_contract_address)
        is_erc721 = erc165.supports_interface.call(INTERFACE_ID_IERC721)
        is_erc1155 = erc165.supports_interface.call(INTERFACE_ID_IERC1155)

        if is_erc721:
            ierc721 = IERC721(provider, listing.asset_contract_address)
            return (
                ierc721.owner_of.call(listing.token_id).lower()
                == listing.seller_address.lower()
            )
        elif is_erc1155:
            ierc1155 = IERC1155(provider, listing.asset_contract_address)
            balance = ierc1155.balance_of.call(listing.seller_address, listing.token_id)
            return balance > (quantity if quantity is not None else listing.quantity)
        else:
            return False
