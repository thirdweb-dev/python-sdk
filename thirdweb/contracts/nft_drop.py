from typing import Final, List, Optional
from thirdweb.abi import DropERC721
from thirdweb.constants.role import Role
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_platform_fee import ContractPlatformFee
from thirdweb.core.classes.contract_roles import ContractRoles
from thirdweb.core.classes.contract_royalty import ContractRoyalty
from thirdweb.core.classes.contract_sales import ContractPrimarySale
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.drop_claim_conditions import DropClaimConditions
from thirdweb.core.classes.erc_721 import ERC721
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import ContractType
from thirdweb.types.contracts.claim_conditions import ClaimVerification
from thirdweb.types.nft import (
    NFTMetadata,
    NFTMetadataInput,
    NFTMetadataOwner,
    QueryAllParams,
)
from thirdweb.types.sdk import SDKOptions
from thirdweb.types.settings.metadata import DropContractMetadata
from eth_account.account import LocalAccount
from web3 import Web3

from thirdweb.types.tx import TxResultWithId


class NFTDrop(ERC721[DropERC721]):
    _abi_type = DropERC721

    contract_type: Final[ContractType] = ContractType.NFT_DROP
    contract_roles: Final[List[Role]] = [Role.ADMIN, Role.MINTER, Role.TRANSFER]

    metadata: ContractMetadata[DropERC721, DropContractMetadata]
    roles: ContractRoles
    primary_sale: ContractPrimarySale[DropERC721]
    platform_fee: ContractPlatformFee[DropERC721]
    royalty: ContractRoyalty[DropERC721]
    claim_conditions: DropClaimConditions

    def __init__(
        self,
        provider: Web3,
        address: str,
        storage: IpfsStorage,
        signer: Optional[LocalAccount] = None,
        options: SDKOptions = SDKOptions(),
    ):
        abi = DropERC721(provider, address)
        contract_wrapper = ContractWrapper(abi, provider, signer, options)
        super().__init__(contract_wrapper, storage)

        self.metadata = ContractMetadata(
            contract_wrapper, storage, DropContractMetadata
        )
        self.roles = ContractRoles(contract_wrapper, self.contract_roles)
        self.primary_sale = ContractPrimarySale(contract_wrapper)
        self.platform_fee = ContractPlatformFee(contract_wrapper)
        self.royalty = ContractRoyalty(contract_wrapper, self.metadata)
        self.claim_conditions = DropClaimConditions(
            self._contract_wrapper, self.metadata, self._storage
        )

    def get_all_claimed(
        self, query_params: Optional[QueryAllParams] = None
    ) -> List[NFTMetadataOwner]:
        pass

    def get_all_unclaimed(
        self, query_params: Optional[QueryAllParams] = None
    ) -> List[NFTMetadata]:
        pass

    def total_claimed_supply(self) -> int:
        pass

    def total_unclaimed_supply(self) -> int:
        pass

    def create_batch(
        self, metadatas: List[NFTMetadataInput]
    ) -> List[TxResultWithId[NFTMetadata]]:
        pass

    def claim_to(
        self,
        destination_address: str,
        quantity: int,
        proofs: List[str] = [
            "0x0000000000000000000000000000000000000000000000000000000000000000"
        ],
    ) -> List[TxResultWithId[NFTMetadata]]:
        pass

    def claim(
        self,
        quantity: int,
        proofs: List[str] = [
            "0x0000000000000000000000000000000000000000000000000000000000000000"
        ],
    ) -> List[TxResultWithId[NFTMetadata]]:
        pass

    """
    INTERNAL FUNCTIONS
    """

    def _prepare_claim(
        self,
        quantity: int,
        proofs: List[str] = [
            "0x0000000000000000000000000000000000000000000000000000000000000000"
        ],
    ) -> ClaimVerification:
        pass
