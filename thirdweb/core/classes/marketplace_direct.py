from typing import Optional
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.marketplace import DirectListing, NewDirectListing, Offer
from web3.eth import TxReceipt


class MarketplaceDirect(BaseContract):
    _storage: IpfsStorage

    def __init__(self, contract_wrapper: ContractWrapper, storage: IpfsStorage):
        super().__init__(contract_wrapper)
        self._storage = storage

    """
    READ FUNCTIONS
    """

    def get_listing(self, listing_id: int) -> DirectListing:
        pass

    def get_active_offer(self, listing_id: int, address: str) -> Optional[Offer]:
        pass

    """
    WRITE FUNCTIONS
    """

    def create_listing(self, listing: NewDirectListing) -> TxReceipt:
        pass

    def make_offer(
        self,
        listing_id: int,
        quantity_desired: int,
        currency_contract_address: str,
        price_per_token: int,
    ) -> TxReceipt:
        pass

    def accept_offer(self, listing_id: int, address_or_offerror: str) -> TxReceipt:
        pass

    def buyout_listing(
        self, listing_id: int, quantity_desired: int, receiver: Optional[str] = None
    ) -> TxReceipt:
        pass

    def update_listing(self, listing: DirectListing) -> TxReceipt:
        pass

    def cancel_listing(self, listing_id: int) -> TxReceipt:
        pass

    """
    INTERNAL FUNCTIONS
    """

    def _validate_listing(self, listing_id: int) -> DirectListing:
        pass

    def _map_listing(self, listing) -> DirectListing:
        pass

    def _is_still_valid_listing(
        self, listing: DirectListing, quantity: Optional[int] = None
    ) -> bool:
        pass
