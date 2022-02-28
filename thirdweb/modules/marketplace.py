"""
Interact with the Market module of the app.
"""
import time
from typing import List
from thirdweb import storage
from thirdweb.constants.erc_interfaces import InterfaceIdErc721

from thirdweb_web3 import Web3
from ..abi.erc165 import ERC165
from ..abi.erc20 import ERC20
from ..abi.erc1155 import ERC1155
from ..abi.marketplace import IMarketplaceListingParameters, Marketplace, IMarketplaceListing
from ..abi.nft import NFT
from ..constants import NativeAddress, ZeroAddress
from ..errors import AssetNotFoundException, AuctionAlreadyStartedException, AuctionHasNotEndedException, UnsupportedAssetException, WrongListingTypeException, ListingNotFoundException
from ..modules.currency import CurrencyModule
from ..modules.nft import NftModule
from ..types.currency import CurrencyValue
from ..types.listing import Listing
from ..types.marketplace import AuctionListing, DirectListing, NewAuctionListing, NewBid, NewListing, NewOffer, Offer
from . import BaseModule


class MarketplaceModule(BaseModule):
    """
    Interact with the Market module of the app.
    """
    address: str
    """
    Address of the module
    """
    """
    Address of the market contract.
    """
    __abi_module: Marketplace
    MAX_BPS: 10000

    def __init__(self, address: str, client: Web3, ):
        """
        :param address: The address of the market contract.
        :param client: The web3 client.

        Initialize the Market Module.

        """

        super().__init__()
        self.address = address
        self.__abi_module = Marketplace(client, address)

    def create_direct_listing(self, listing: NewListing) -> int:
        """
        Create a direct listing.

        :param listing: The listing to create.
        :return: The listing id.
        """
        self.__handle_token_approval(
            listing.assetContractAddress, listing.tokenId, self.address)

        tx = self.__abi_module.create_listing.build_transaction(IMarketplaceListingParameters(
            listing.assetContractAddress,
            listing.tokenId,
            listing.startTimeInSeconds,
            listing.listingDurationInSeconds,
            listing.quantity,
            listing.currencyContractAddress,
            listing.buyoutPricePerToken,
            listing.buyoutPricePerToken,
            0,
        ))
        receipt = self.execute_tx(tx)
        return receipt.logs[0]["args"]["listingId"]

    def create_auction_listing(self, listing: NewAuctionListing) -> int:
        """
        Create an auction listing.

        :param listing: The listing to create.
        :return: The listing id.
        """
        self.__validate_new_listing_param(listing)

        self.__handle_token_approval(
            listing.assetContractAddress, listing.tokenId, self.address)

        tx = self.__abi_module.create_listing.build_transaction(IMarketplaceListingParameters(
            listing.assetContractAddress,
            listing.tokenId,
            listing.startTimeInSeconds,
            listing.listingDurationInSeconds,
            listing.quantity,
            listing.currencyContractAddress,
            listing.reservePricePerToken,
            listing.buyoutPricePerToken,
            1,
        ))
        receipt = self.execute_tx(tx)
        return receipt["logs"][0]["args"]["listingId"]

    def make_direct_listing_offer(self, offer: NewOffer):
        if (offer.currency_contract_address == ZeroAddress or offer.currency_contract_address == NativeAddress):
            raise "You must use the wrapped native token address when making an offer with a native token"
        try:
            self.get_direct_listing(offer.listing_id)
        except:
            raise AssetNotFoundException(offer.listing_id)

        self.__set_allowance(offer.price_per_token * offer.quantity_desired,
                             offer.currency_contract_address, self.get_transact_opts())
        tx = self.__abi_module.offer.build_transaction(
            offer.listing_id, offer.quantity_desired, offer.currency_contract_address, offer.price_per_token)
        receipt = self.execute_tx(tx)

    def is_native_token(self, address: str):
        return (address == ZeroAddress) or (address == NativeAddress)

    def __set_allowance(self, amount: int, token_contract_address: str, opts: dict):
        """
        Set the allowance of the module to the spender.

        :param amount: The amount to set.
        :param spender: The spender address.
        :param opts: The transaction options.
        """
        if self.is_native_token(token_contract_address):
            opts["value"] = amount
        else:
            currency_module = ERC20(self.client, self.address)
            allowance = currency_module.allowance.call(
                self.get_signer_address(), self.address)
            if allowance < amount:
                tx = currency_module.increase_allowance.build_transaction(
                    self.address, amount - allowance, opts)
                self.execute_tx(tx)
        return opts

    def make_auction_listing_bid(self, bid: NewBid):
        listing = self.__validate_auction_listing(bid.listing_id)

        bid_buffer = self.get_bid_buffer_bps()
        winning_bid = self.get_winning_bid(bid.listing_id)
        if winning_bid is not None:
            is_winning_bidder = self.is_winning_bid(
                winning_bid.pricePerToken, bid.price_per_token, bid_buffer)
            if not is_winning_bidder:
                raise Exception("The bid price is not within the bid buffer")
        self.__set_allowance(bid.price_per_token * listing.quantity,
                             listing.currency_contract_address, self.get_transact_opts())
        tx = self.__abi_module.offer.build_transaction(
            bid.listing_id, listing.quantity, listing.currency_contract_address, bid.price_per_token)
        self.execute_tx(tx)

    def is_winning_bid(self, winning_price: int, new_bid_price: int, bid_buffer: int):
        buffer = (new_bid_price * self.MAX_BPS) / winning_price
        return (buffer > bid_buffer)

    def get_winning_bid(self, listing_id: int):
        """
        Get the winning bid for a listing.

        :param listing_id: The listing id.
        :return: The winning bid.
        """
        bid = self.__abi_module.winning_bid.call(listing_id)

        if bid[1] == ZeroAddress:
            return None

        if bid is None:
            return None
        return self.__map_offer(listing_id, bid)

    def get_direct_listing(self, listing_id: int):
        listing = self.__abi_module.listings.call(listing_id)
        if listing[0] != listing_id:
            raise AssetNotFoundException(listing_id)
        if listing[11] != 1:
            raise WrongListingTypeException(
                listing_id, "Auction", "Direct")

        return self.__map_direct_listing(listing)

    def __map_direct_listing(self, listing):
        nftcontract = NftModule(listing[3], self.get_client())
        return DirectListing(listing[0], assetContractAddress=listing[2], tokenId=listing[3], asset=nftcontract.get(listing[3]), startTimeInSeconds=listing[4], secondsUntilEnd=listing[5], quantity=listing[6], currencyContractAddress=listing[7], buyoutCurrencyValuePerToken=CurrencyModule(listing[7], self.get_client).get_value(listing[8]), buyoutPrice=listing[9], sellerAddress=listing[1], listing_type=[11])

    def __handle_token_approval(self, asset: str, token_id: int, from_address: str):
        erc165 = ERC165(self.get_client, asset)
        is_erc721 = erc165.supports_interface.call(InterfaceIdErc721)
        if is_erc721:
            erc721 = NFT(self.get_client, asset)
            approved = erc721.is_approved_for_all.call(
                from_address, self.address)
            if not approved:
                is_token_approved = (erc721.get_approved.call(
                    token_id).lower() == self.address.lower())
                if not is_token_approved:
                    tx = erc721.set_approval_for_all.build_transaction(
                        self.address, True)
                    self.execute_tx(tx)
        else:
            erc1155 = ERC1155(self.get_client, asset)
            approved = erc1155.is_approved_for_all.call(
                from_address, self.address)
            if not approved:
                tx = erc1155.set_approval_for_all.build_transaction(
                    self.address, True)
                self.execute_tx(tx)

    def __is_token_approved_for_marketplace(self, asset_contract: str, token_id: int, from_address: str):
        try:
            erc165 = ERC165(self.get_client, asset_contract)
            is_erc721 = erc165.supports_interface.call(InterfaceIdErc721)
            if is_erc721:
                erc721 = NFT(self.get_client, asset_contract)
                approved = erc721.is_approved_for_all.call(
                    from_address, self.address)
                if approved:
                    return True

                return (erc721.get_approved.call(token_id).lower() == self.address.lower())
            else:
                erc1155 = ERC1155(self.get_client, asset_contract)
                return erc1155.is_approved_for_all.call(from_address, self.address)
        except:
            print("Failed to check if token is approved")
            return False

    def __is_still_valid_direct_listing(self, listing: DirectListing, quantity: int) -> bool:
        approved = self.__is_token_approved_for_marketplace(
            listing.assetContractAddress, listing.tokenId, listing.sellerAddress)
        if not approved:
            return False

        erc165 = ERC165(self.get_client, listing.assetContractAddress)
        is_erc721 = erc165.supports_interface.call(InterfaceIdErc721)
        if is_erc721:
            erc721 = NFT(self.get_client, listing.assetContractAddress)
            return (erc721.owner_of.call(listing.tokenId).lower() == listing.sellerAddress.lower())
        else:
            erc1155 = ERC1155(self.get_client, listing.assetContractAddress)
            balance = erc1155.balance_of.call(
                listing.sellerAddress, listing.tokenId)
            return (balance >= listing.quantity)

    def __validate_new_listing_param(param: (NewListing or NewAuctionListing)):
        if (param.assetContractAddress is None):
            raise Exception("Asset contract address is required")
        if (param.tokenId is None):
            raise Exception("Token ID is required")
        if (param.startTimeInSeconds is None):
            raise Exception("Start time is required")
        if (param.listingDurationInSeconds is None):
            raise Exception("Listing duration is required")
        if (param.buyoutPricePerToken is None):
            raise Exception("Buyout price is required")
        if (param.quantity is None):
            raise Exception("Quantity is required")
        if (param.listing_type == "NewAuctionListing"):
            if (param.reservePricePerToken is None):
                raise Exception("Buyout currency value is required")

    def __validate_direct_listing(self, listing_id: int):
        return self.get_direct_listing(listing_id)

    def __validate_auction_listing(self, listing_id: int) -> AuctionListing:
        return self.get_auction_listing(listing_id)

    def __map_offer(self, listing_id: int, offer) -> Offer:
        return Offer(quantityDesired=offer[2],
                     pricePerToken=offer[4],
                     currencyContractAddress=offer[3],
                     buyerAddress=offer[1],
                     currencyValue=CurrencyModule(
                         offer[3], self.get_client).get_value(offer[4] * offer[2]),
                     listing_id=offer[0],
                     )

    def get_active_offer(self, listing_id: int, address: str) -> Offer:
        self.__validate_direct_listing(listing_id)
        offers = self.__abi_module.winning_bid.call(listing_id, address)
        if offers[1] == ZeroAddress:
            return None
        return self.__map_offer(listing_id, offers)

    def get_bid_buffer_bps(self):
        return self.__abi_module.bid_buffer_bps.call()

    def get_time_buffer_in_seconds(self):
        return self.__abi_module.time_buffer.call()

    def accept_direct_listing(self, listing_id: int, from_address: str):
        tx = self.__abi_module.accept_offer.build_transaction(
            listing_id, from_address)
        self.execute_tx(tx)

    def buyout_auction_listing(self, listing_id: int, from_address: str):
        listing = self.__validate_auction_listing(listing_id)
        self.make_auction_listing_bid(
            NewBid(listing_id, listing.buyoutPricePerToken))

    def buyout_direct_listing(self, listing_id: int, quantity: str):
        listing = self.__validate_direct_listing(listing_id)
        valid = self.__is_still_valid_direct_listing(listing, quantity)
        if not valid:
            raise Exception(
                "The asset on this listing has been moved from the listers wallet, this listing is now invalid")
        value = listing.buyoutPrice * quantity
        self.__set_allowance(value, listing.currencyContractAddress)
        tx = self.__abi_module.buy.build_transaction(listing_id, quantity)
        self.execute_tx(tx)

    def update_direct_listing(self, listing: DirectListing):
        tx = self.__abi_module.update_listing.build_transaction(
            listing.id, listing.quantity, listing.buyoutPrice, listing.buyoutPrice, listing.currencyContractAddress,  listing.startTimeInSeconds, listing.secondsUntilEnd)
        self.execute_tx(tx)

    def update_auction_listing(self, listing: AuctionListing):
        tx = self.__abi_module.update_listing.build_transaction(
            listing.id, listing.quantity, listing.reservePrice, listing.buyoutPrice, listing.currencyContractAddress, listing.startTimeInSeconds, listing.secondsUntilEnd)
        self.execute_tx(tx)

    def cancel_direct_listing(self, listing_id: int):
        listing = self.__validate_direct_listing(listing_id)
        listing.quantity = 0
        self.update_direct_listing(listing)

    def cancel_auction_listing(self, listing_id: int):
        listing = self.__validate_auction_listing(listing_id)
        listing.quantity = 0
        now = int(time.time())
        if now > listing.startTimeInSeconds:
            raise AuctionAlreadyStartedException(
                listing_id)
        tx = self.__abi_module.close_auction.build_transaction(listing_id)
        self.execute_tx(tx)

    def close_auction_listing(self, listing_id: int, close_for: str):
        if close_for is not None:
            close_for = self.get_signer_address()
        listing = self.__validate_auction_listing(listing_id)
        try:
            tx = self.__abi_module.close_auction.build_transaction(
                listing_id, close_for)
            self.execute_tx(tx)
        except Exception as e:
            raise AuctionHasNotEndedException(listing_id)

    def set_bid_buffer_bps(self, bid_buffer_bps: int):
        tx = self.__abi_module.set_auction_buffers.build_transaction(
            bid_buffer_bps, self.get_bid_buffer_bps())
        self.execute_tx(tx)

    def buyout_listing(self, listing_id: int, quantity: str):
        listing = self.__abi_module.listings.call(listing_id)
        if not listing[0] == listing_id:
            raise ListingNotFoundException(listing_id)
        if listing[11] == 0:
            if quantity is None:
                raise Exception("Quantity is required")
            return self.buyout_direct_listing(listing_id, quantity)
        return self.buyout_auction_listing(listing_id, quantity)

    def get_listing(self, listing_id: int) -> DirectListing or AuctionListing:
        listing = self.__abi_module.listings.call(listing_id)
        if not listing[0] == listing_id:
            raise ListingNotFoundException(listing_id)
        if listing[11] == 0:
            return self.__map_direct_listing(listing)
        elif listing[11] == 1:
            return self.__map_auction_listing(listing)
        else:
            raise Exception("Unkwown listing type : " + listing[11])

    def __map_auction_listing(self, listing):
        nftcontract = NftModule(listing[3], self.get_client())
        return AuctionListing(id=listing[0], assetContractAddress=listing[2], tokenId=listing[3], asset=nftcontract.get(listing[3]), startTimeInSeconds=listing[4], secondsUntilEnd=listing[5], quantity=listing[6], currencyContractAddress=listing[7], reservePrice=listing[8], buyoutCurrencyValuePerToken=CurrencyModule(listing[7], self.get_client).get_value(listing[9]), buyoutPrice=listing[9], sellerAddress=listing[1], listing_type=[11], reservePriceCurrencyValuePerToken=CurrencyModule(listing[7], self.get_client).get_value(listing[8]))

    def clean_listing(self, listing_id):
        try:
            listing = self.get_listing(listing_id)
        except:
            return None
        if listing.type == 1:
            return listing
        valid = self.__is_still_valid_direct_listing(listing)
        if not valid:
            return None
        return listing

    def get_all_listings(self):
        i = 0
        total_listings = self.__abi_module.total_listings.call()
        listings = []
        while i < total_listings:
            listing = self.clean_listing(i)
            if listing is not None:
                listings.append(listing)
            i += 1
        return listings
