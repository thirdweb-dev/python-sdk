from web3 import Web3
from typing import List, Dict
from . import BaseModule
from ..types import Role, Listing as ListingType
from ..abi.market import Market
#_types



# from ..errors import NoSignerException
# from ..abi.erc20 import ERC20


class MarketModule(BaseModule):
    address: str
    __abi_module: Market
    def __init__(self, client: Web3, address: str):
        super().__init__()
        self.address = address
        self.__abi_module = Market(client, address)
    
    #todo: return types
    def list_item(self, arg: ListArg):
        if arg.properties is None:
            arg.properties = {}
        else:
            final_properties = copy.copy(arg.properties)
        tx = self.__abi_module.list.build_transaction(
            arg.asset_contract, 
            arg.token_id, 
            arg.currency, 
            arg.price_per_token,
            arg.quantity, 
            arg.tokens_per_buyer, 
            arg.seconds_until_start, 
            arg.seconds_until_end,
            self.get_transact_opts()
        )
        self.execute_tx(tx)
    
    def unlist_item(self, listing_id, quantity):
        tx = self.__abi_module.unlist.build_transaction(
            listing_id, 
            quantity,
            self.get_transact_opts()
            )
        self.execute_tx(tx)
    
    def add_to_listing(self, listing_id, quantity):
        tx = self.__abi_module.add_to_listing.build_transaction(
            listing_id, 
            quantity,
            self.get_transact_opts()
            )
        self.execute_tx(tx)

    def updateListingParams(self, args: ListUpdate):
        tx = self.__abi_module.updateListingParams(
            args.listing_id,
            args.price_per_token,
            args.currency,
            args.tokens_per_buyer,
            args.seconds_until_start,
            args.seconds_until_end
        )
        self.execute_tx(tx)
    
    def buy(self, listing_id: int, quantity: int):
        tx = self.__abi_module.buy.build_transaction(
            listing_id, 
            quantity, 
            buyer,
            self.get_transact_opts()
            )
        self.execute_tx(tx)

    def set_market_fee_bps(self, amount: int):
        tx = self.__abi_module.set_market_fee_bps.build_transaction(
            amount, 
            self.get_transact_opts())
        self.execute_tx(tx)
    
    def get(self, listing_id) -> List:
        self.__abi_module.get_listing.call(listing_id)
    
    def get_all(self) -> List[ListingType]:
        self.__abi_module.get_all_listings.call()
        
    def get_all_by_seller(self, seller: str) -> List[ListingType]:
        self.__abi_module.get_listings_by_seller.call(seller)
    
    def get_all_by_asset_contract(self, asset_contract: str) -> List[ListingType]:
        self.__abi_module.get_listings_by_asset_contract.call(asset_contract)
    
    def get_all_by_asset(self, asset: str) -> List[ListingType]:
        self.__abi_module.get_listings_by_asset.call(asset)


    def grant_role(self, role: Role, address: str):
        role_hash = role.get_hash()
        tx = self.__abi_module.grant_role.build_transaction(
            role_hash,
            address,
            self.get_transact_opts()
        )

        self.execute_tx(tx)

    def revoke_role(self, role: Role, address: str):
        role_hash = role.get_hash()
        tx = self.__abi_module.revoke_role.build_transaction(
            role_hash,
            address,
            self.get_transact_opts()
        )
        self.execute_tx(tx)

    def total_supply(self) -> int:
        self.__abi_module.total_listings.call()


