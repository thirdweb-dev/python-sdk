from typing import Optional
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.marketplace import AuctionListing, Offer
from web3.eth import TxReceipt


class MarketplaceAuction(BaseContract):
    _storage: IpfsStorage

    def __init__(self, contract_wrapper: ContractWrapper, storage: IpfsStorage):
        super().__init__(contract_wrapper)
        self._storage = storage

    """
    READ FUNCTIONS
    """

    def get_listing(self, listing_id: int) -> AuctionListing:
        pass

    def get_winning_bid(self, listing_id: int) -> Optional[Offer]:
        pass

    def get_winner(listing_id) -> str:
        pass

    """
    WRITE FUNCTIONS
    """

    def create_listing(self, listing: AuctionListing) -> TxReceipt:
        pass

    def buyout_listing(self, listing_id: int) -> TxReceipt:
        pass

    def make_bid(self, listing_id: int, price_per_token: int) -> TxReceipt:
        pass

    def cancel_listing(self, listing_id: int) -> TxReceipt:
        pass

    def close_listing(self, listing_id: int) -> TxReceipt:
        pass

    def update_listing(self, listing_id: AuctionListing) -> TxReceipt:
        pass

    """
    INTERNAL FUNCTIONS
    """

    def _validate_listing(self, listing_id: int) -> AuctionListing:
        pass

    def _map_listing(self, listing) -> AuctionListing:
        pass
