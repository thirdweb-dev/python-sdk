"""Interact with the market module of the app."""
from web3 import Web3
from typing import List, Dict
from . import BaseModule
from ..types import Role
from ..abi.market import Market
from ..types.market import ListArg, Filter, MarketListing
from ..types.listing import Listing
from ..abi.erc20 import ERC20
from ..abi.erc165 import ERC165
from ..abi.erc1155 import ERC1155
from ..abi.nft import NFT
nulladdress = "0x0000000000000000000000000000000000000000"

class MarketModule(BaseModule):
    """
    Market Methods
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

    def list(self, arg: ListArg):
        """
        List an asset for sale.
        """
        from_address = self.get_signer_address()
        client = self.get_client()
        erc165 = ERC165(client, arg.asset_contract)
        isERC721 = erc165.supports_interface.call( bytearray.fromhex("80ac58cd"))
        if isERC721:
            asset = NFT(client, arg.asset_contract)
            approved = asset.is_approved_for_all.call(  from_address, self.address)
            if not approved:
                is_token_approved = asset.get_approved.call(arg.token_id).lower() == self.address.lower()
                if not is_token_approved:
                    self.execute_tx(asset.set_approval_for_all.build_transaction(self.address, True, self.get_transact_opts()))
       
        else:
            asset = ERC1155(client, arg.asset_contract)
            approved = asset.is_approved_for_all.call(from_address, self.address)

            if not approved:
                asset.set_approval_for_all.call(self.address, True)

        tx = self.__abi_module._list.build_transaction(
            arg.asset_contract,
            arg.token_id,
            arg.currency_contract,
            arg.price_per_token,
            arg.quantity,
            arg.tokens_per_buyer,
            arg.seconds_until_start,
            arg.seconds_until_end,
            self.get_transact_opts()
        )

        receipt = self.execute_tx(tx)
        result = self.__abi_module.get_new_listing_event(tx_hash=receipt.transactionHash.hex())
        # listing_id = result[0]['args']['token_id']
        # return self.get(listing_id)

    def unlist(self, listing_id, quantity):
        """ 
        Unlist an asset for sale.
        """
        tx = self.__abi_module.unlist.build_transaction(
            listing_id,
            quantity,
            self.get_transact_opts()
        )
        self.execute_tx(tx)

    def unlist_all(self, listing_id: int):
        """ 
        Unlist an asset for sale.
        """
        self.unlist(listing_id, self.get(listing_id).quantity)

    def buy(self, listing_id: int, quantity: int):
        """
        Buy a listing.
        """
        item = self.get(listing_id)
        owner = self.get_signer_address()
        spender = self.address
        total_price = item.pricePerToken * quantity
        if item.currency is not None and item.currency != nulladdress:
            erc20 = ERC20(self.get_client(), item.currency)
            allowance = erc20.allowance.call(owner, spender)
            if allowance < total_price:
                tx = erc20.increase_allowance.build_transaction(    spender,
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

        """
        Get a listing.
        """
        return self.__abi_module.get_listing.call(listing_id)

    def get_all_listings(self, search_filter: Filter = None) -> List[Listing]:
        """ 
        Returns all the listings.
        """
        return self.get_all(search_filter)
    
    def get(self, listing_id) -> MarketListing:
        """
        Get a listing.
        """
        return MarketListing(**self.__abi_module.get_listing.call(listing_id))

    def set_module_metadata(metadata: str):
        """
        Sets the metadata for the module
        """
        uri = self.get_storage().upload_metadata(
            metadata, self.address, self.get_signer_address())

    def get_listing(self, listing_id: int) -> Listing:
        """
        Get a listing.
        """
        return self.get(listing_id)

    def get_all(self, search_filter: Filter = None) -> List[Listing]:
        """ 
        Returns all the listings.
        """
        if search_filter is None:
            return self.__abi_module.get_all_listings.call()
        elif search_filter.asset_contract is not None:
            if search_filter.token_id is not None:
                return self.__abi_module.get_listings_by_asset.call(
                    filer.asset_contract,
                    filer.token_id
                )
            else:
                return self.__abi_module.get_listings_by_asset_contract.call(
                    filer.asset_contract
                )
        elif search_filter.seller is not None:
            return self.__abi_module.get_listings_by_seller.call(
                filer.seller
            )
        else:
            return self.__abi_module.get_all_listings.call()

    def total_listings(self) -> int:
        """
        Returns the total supply of the market.
        """
        return self.__abi_module.total_listings.call()
