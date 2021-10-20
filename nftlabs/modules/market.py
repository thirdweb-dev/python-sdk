from web3 import Web3
from typing import List, Dict
from . import BaseModule
from ..types import Role, Listing as ListingType
from ..abi.market import Market
from market_types import ListArg, Filter
from ..abi.erc20 import ERC20
from ..abi.erc165 import ERC165
from ..abi.erc1155 import ERC1155
from ..abi.nft import NFT


class MarketModule(BaseModule):
    address: str
    __abi_module: Market

    def __init__(self, client: Web3, address: str):
        super().__init__()
        self.address = address
        self.__abi_module = Market(client, address)

    #todo: return types
    def list_item(self, arg: ListArg):
        from_address = self.get_signer_address()
        client = self.get_client()
        erc165 = ERC165(client, arg.asset_contract)
        isERC165 = erc165.supports_interface(client, arg.asset_contract)
        if isERC165:
            asset = NFT(client, arg.asset_contract)
            approved = asset.is_approved_for_all(
                arg.asset_contract, from_address)
            if not approved:
                asset.approve_for_all(from_address, arg.asset_contract)
                is_token_approved = (asset.get_approved(
                    arg.token_id).lower() == self.address.lower())
                if not is_token_approved:
                    asset.set_approval_for_all(arg.asset_contract, True)
        else:
            asset = ERC1155(client, arg.asset_contract)
            approved = asset.is_approved_for_all(
                arg.asset_contract, from_address)
            if not approved:
                asset.approve_for_all(from_address, arg.asset_contract)
                is_token_approved = (asset.get_approved(
                    arg.token_id).lower() == self.address.lower())
                if not is_token_approved:
                    asset.set_approval_for_all(self.address, True)

        tx = self.__abi_module.list.build_transaction(
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
        result = self.__abi_module.get_minted_batch_event(
            tx_hash=receipt.transactionHash.hex())

    def unlist_item(self, listing_id, quantity):
        tx = self.__abi_module.unlist.build_transaction(
            listing_id,
            quantity,
            self.get_transact_opts()
        )
        self.execute_tx(tx)

    def buy(self, listing_id: int, quantity: int):
        listing = get(listing_id)
        owner = self.get_signer_address()
        spender = self.address
        total_price = listing.price_per_token * quantity
        if listing.currency_contract is not None and listing.currency_contract != "0x0000000000000000000000000000000000000000":
            erc20 = ERC20(self.get_client(), listing.currency_contract)
            allowance = erc20.allowance(owner, spender)
            if allowance <= total_price:
                erc20.increase_allowance(
                    spender,
                    total_price,
                    self.get_transact_opts()
                )

        tx = self.__abi_module.buy.build_transaction(
            listing_id,
            quantity,
            self.get_transact_opts()
        )
        receipt = self.execute_tx(tx)
        result = self.__abi_module.get_minted_batch_event(
            tx_hash=receipt.transactionHash.hex())

    def set_market_fee_bps(self, amount: int):
        tx = self.__abi_module.set_market_fee_bps.build_transaction(
            amount,
            self.get_transact_opts())
        self.execute_tx(tx)

    def get(self, listing_id) -> List:
        self.__abi_module.get_listing.call(listing_id)

    def get_all(self, search_filter: Filter = None) -> List[ListingType]:
        if search_filter is None:
            self.__abi_module.get_all_listings.call()
        elif search_filter.asset_contract is not None:
            if search_filter.token_id is not None:
                self.__abi_module.get_listings_by_asset.call(
                    filer.asset_contract,
                    filer.token_id
                )
            else:
                self.__abi_module.get_listings_by_asset_contract.call(
                    filer.asset_contract
                )
        elif search_filter.seller is not None:
            self.__abi_module.get_listings_by_seller.call(
                filer.seller
            )
        else:
            self.__abi_module.get_all_listings.call()

    def total_supply(self) -> int:
        self.__abi_module.total_listings.call()
