"""
Interact with the Market module of the app.
"""
from typing import List

from thirdweb_web3 import Web3

from ..abi.erc20 import ERC20
from ..abi.erc1155 import ERC1155
from ..abi.marketplace import IMarketplaceListingParameters, Marketplace, IMarketplaceListing
from ..abi.nft import NFT
from ..constants import ZeroAddress
from ..errors import AssetNotFoundException, UnsupportedAssetException
from ..modules.currency import CurrencyModule
from ..modules.nft import NftModule
from ..types.currency import CurrencyValue
from ..types.listing import Listing
from ..types.marketplace import NewAuctionListing, NewBid, NewListing, NewOffer
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
        self._handle_token_approval(
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
        # TODO validate

        self._handle_token_approval(
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
        if (offer.currency_contract_address == ZeroAddress or offer.currency_contract_address == "0xeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee"):
            raise "You must use the wrapped native token address when making an offer with a native token"
        try:
            self.get_direct_listing(offer.listing_id)  # TODO
        except:
            raise AssetNotFoundException(offer.listing_id)

        self.set_allowance(offer.price_per_token * offer.quantity_desired,
                           offer.currency_contract_address, self.get_transact_opts())  # TODO
        tx = self.__abi_module.offer.build_transaction(
            offer.listing_id, offer.quantity_desired, offer.currency_contract_address, offer.price_per_token)
        receipt = self.execute_tx(tx)

    def make_auction_listing_bid(self, bid: NewBid):
        # TODO validate

        bid_buffer = self.get_bid_buffer_bps()  # TODO
        winning_bid = self.get_winning_bid(listing_id)  # TODO
        if winning_bid is not None:
            is_winning_bidder = self.is_winning_bidder(
                winning_bid.price_per_token, bid.price_per_token, bid_buffer)  # TODO
            if not is_winning_bidder:
                raise Exception(
                    "The bid price is not within the bid buffer")  # TODO add specific error
        self.set_allowance(bid.price_per_token * listing.quantity, 


    def _handle_token_approval(self, asset: str, token_id: int, from_address: str):
        return  # TODO: implement
