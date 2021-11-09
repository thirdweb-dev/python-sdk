from typing import List

from thirdweb_web3 import Web3

from ..abi.erc20 import ERC20
from ..abi.erc1155 import ERC1155
from ..abi.market import Market, MarketListing
from ..abi.nft import NFT
from ..constants import ZeroAddress
from ..errors import AssetNotFoundException, UnsupportedAssetException
from ..modules.currency import CurrencyModule
from ..modules.nft import NftModule
from ..types.currency import CurrencyValue
from ..types.listing import Listing
from ..types.market import Filter, ListArg, MarketListing
from . import BaseModule


class MarketModule(BaseModule):
    """
    The market module allows you to manage listings.
    """

    address: str
    """
    Address of the market contract.
    """
    __abi_module: Market

    def __init__(self, address: str, client: Web3, ):
        """
        Initialize the Market Module.
        """

        super().__init__()
        self.address = address
        self.__abi_module = Market(client, address)

    def list(self, arg: ListArg) -> Listing:
        """
        WIP: This method is still in beta and will contain bugs.
        Status: Listing works but decoding the logs is breaking due to a bug
        in the web3 library (https://github.com/ethereum/web3.py/pull/1484).
        We're unable to return the new listing ID to the caller. Calling
        this method will return None for now.

        List an asset for sale.
        """
        if self.is_erc721(arg.asset_contract):
            self.__approve_erc_721(arg.asset_contract, arg.token_id)
        elif self.is_erc1155(arg.asset_contract):
            self.__approve_erc_1155(arg.asset_contract)
        else:
            raise UnsupportedAssetException()

        receipt = self.execute_tx(
            self.__abi_module._list.build_transaction(
                asset_contract=arg.asset_contract,
                token_id=arg.token_id,
                currency=arg.currency_contract,
                price_per_token=arg.price_per_token,
                quantity=arg.quantity,
                seconds_until_end=arg.seconds_until_end,
                seconds_until_start=arg.seconds_until_start,
                tokens_per_buyer=arg.tokens_per_buyer,
                tx_params=self.get_transact_opts()))
        result = self.__abi_module.get_new_listing_event(
            tx_hash=receipt.transactionHash.hex())
        listing = result[0]['args']['listing']
        return self.get(listing[0])

    def __approve_erc_1155(self, address: str) -> Listing:
        """
        BETA: This method is still in beta and might contain bugs.
        """
        from_address = self.get_signer_address()
        asset = ERC1155(self.get_client(), address)
        approved = asset.is_approved_for_all.call(
            from_address, self.address)
        if not approved:
            self.execute_tx(
                asset.set_approval_for_all.build_transaction(self.address, True, self.get_transact_opts()))

    def __approve_erc_721(self, address: str, token_id: int):
        from_address = self.get_signer_address()
        asset = NFT(self.get_client(), address)
        approved = asset.is_approved_for_all.call(
            from_address, self.address)
        if not approved:
            is_token_approved = asset.get_approved.call(
                token_id).lower() == self.address.lower()
            if not is_token_approved:
                self.execute_tx(asset.set_approval_for_all.build_transaction(
                    self.address, True, self.get_transact_opts()))

    def unlist(self, listing_id, quantity):
        """
        Unlist a certain quantity of tokens from a listing.
        """
        tx = self.__abi_module.unlist.build_transaction(
            listing_id,
            quantity,
            self.get_transact_opts()
        )
        self.execute_tx(tx)

    def unlist_all(self, listing_id: int):
        """
        Unlist all available tokens from a listing.
        """
        self.unlist(listing_id, self.get(listing_id).quantity)

    def buy(self, listing_id: int, quantity: int):
        """
        BETA: This method is still in beta and might contain bugs.

        Buy a listing.
        """
        item = self.get(listing_id)
        owner = self.get_signer_address()
        spender = self.address
        total_price = item.pricePerToken * quantity
        if item.currency is not None and item.currency != ZeroAddress:
            erc20 = ERC20(self.get_client(), item.currency)
            allowance = erc20.allowance.call(owner, spender)
            if allowance < total_price:
                tx = erc20.increase_allowance.build_transaction(spender,
                                                                total_price,
                                                                self.get_transact_opts())
                self.execute_tx(tx)

        tx = self.__abi_module.buy.build_transaction(
            listing_id,
            quantity,
            self.get_transact_opts()
        )
        receipt = self.execute_tx(tx)
        result = self.__abi_module.get_new_sale_event(
            tx_hash=receipt.transactionHash.hex())

    def set_market_fee_bps(self, amount: int):
        """
        Set the market fee in basis points.
        """
        tx = self.__abi_module.set_market_fee_bps.build_transaction(
            amount,
            self.get_transact_opts())
        self.execute_tx(tx)

    def get(self, listing_id) -> Listing:
        """
        Get a listing.
        """
        listing = MarketListing(
            **self.__abi_module.get_listing.call(listing_id))
        if listing.listingId != listing_id:
            raise AssetNotFoundException(identifier=listing_id)
        return self.__transform_result_to_listing(listing)

    def set_module_metadata(self, metadata: str):
        """
        Sets the metadata for the module
        """
        uri = self.get_storage().upload_metadata(
            metadata, self.address, self.get_signer_address())
        tx = self.__abi_module.set_contract_uri.build_transaction(
            uri,
            self.get_transact_opts())
        self.execute_tx(tx)

    def get_listing(self, listing_id: int) -> Listing:
        """
        Get a listing.
        """
        return self.get(listing_id)

    def get_all(self, filter: Filter = None) -> List[Listing]:
        """
        Returns all the listings.
        """
        if filter is None:
            return self.__abi_module.get_all_listings.call()
        elif filter.asset_contract is not None:
            if filter.token_id is not None:
                return self.__abi_module.get_listings_by_asset.call(
                    filter.asset_contract,
                    filter.token_id
                )
            else:
                return self.__abi_module.get_listings_by_asset_contract.call(
                    filter.asset_contract
                )
        elif filter.seller is not None:
            return self.__abi_module.get_listings_by_seller.call(
                filter.seller
            )
        else:
            return self.__abi_module.get_all_listings.call()

    def total_listings(self) -> int:
        """
        Returns the total supply of the market.
        """
        return self.__abi_module.total_listings.call()

    def get_abi_module(self) -> Market:
        return self.__abi_module

    def __transform_result_to_listing(self, listing: MarketListing) -> Listing:
        currency: CurrencyValue = None
        if listing.currency == ZeroAddress:
            pass
        else:
            currency_module = CurrencyModule(
                listing.currency, self.get_client())
            currency_module.get_client = self.get_client
            currency = currency_module.get_value(listing.pricePerToken)

        nft_module = NftModule(listing.assetContract, self.get_client())
        nft_module.get_storage = self.get_storage
        metadata = nft_module.get(listing.tokenId)

        return Listing(
            currency_contract=listing.currency,
            currency_metadata=currency,
            id=listing.listingId,
            price_per_token=listing.pricePerToken,
            quantity=listing.quantity,
            sale_end=listing.saleEnd,
            sale_start=listing.saleStart,
            seller=listing.seller,
            token_contract=listing.assetContract,
            token_id=listing.tokenId,
            token_metadata=metadata,
            tokens_per_buyer=listing.tokensPerBuyer,
        )
