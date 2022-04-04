from thirdweb.core.classes.contract_platform_fee import ContractPlatformFee
from thirdweb.types.marketplace import AuctionListing, DirectListing
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
from thirdweb.constants.role import Role
from typing import Final, List, Optional, Union
from thirdweb.abi import Marketplace as MarketplaceABI
from web3.eth import TxReceipt
from web3 import Web3


class Marketplace(BaseContract):
    _abi_type: MarketplaceABI
    _storage: IpfsStorage

    contract_type: Final[ContractType] = ContractType.MARKETPLACE
    contract_roles: Final[List[Role]] = [Role.ADMIN, Role.LISTER, Role.ASSET]

    schema = MarketplaceContractMetadata
    metadata: ContractMetadata[MarketplaceABI, MarketplaceContractMetadata]
    roles: ContractRoles
    platform_fee: ContractPlatformFee[MarketplaceABI]
    direct: MarketplaceDirect
    auction: MarketplaceAuction

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
        self.platform_fee = ContractPlatformFee(contract_wrapper)
        self.direct = MarketplaceDirect(contract_wrapper, storage)
        self.auction = MarketplaceAuction(contract_wrapper, storage)

    """
    READ FUNCTIONS
    """

    def get_listing(self, listing_id: int) -> Union[DirectListing, AuctionListing]:
        pass

    def get_active_listings(self) -> List[Union[DirectListing, AuctionListing]]:
        pass

    def get_all_listings(self) -> List[Union[DirectListing, AuctionListing]]:
        pass

    get_all = get_all_listings

    def get_total_count(self) -> int:
        pass

    def is_restricted_to_lister_role_only(self) -> bool:
        pass

    def get_bid_buffer_bps(self) -> int:
        pass

    def get_time_buffer_in_seconds(self) -> int:
        pass

    """
    WRITE FUNCTIONS
    """

    def buyout_listing(
        self, listing_id: int, quantity_desired: int, receiver: Optional[str] = None
    ) -> TxReceipt:
        pass

    def set_bid_buffer_bps(self, buffer_bps: int) -> TxReceipt:
        pass

    def set_time_buffer_in_seconds(self, buffer_in_seconds: int) -> TxReceipt:
        pass

    def allow_listing_from_specific_asset_only(
        self, contract_address: str
    ) -> TxReceipt:
        pass

    def allow_listing_from_any_asset(self) -> TxReceipt:
        pass

    """
    INTERNAL FUNCTIONS
    """

    def _get_all_listings_no_filter(self) -> List[Union[DirectListing, AuctionListing]]:
        pass
