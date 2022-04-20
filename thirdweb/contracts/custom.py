from typing import Final, Optional

from web3 import Web3
from thirdweb.abi.i_thirdweb_platform_fee import IThirdwebPlatformFee
from thirdweb.abi.i_thirdweb_primary_sale import IThirdwebPrimarySale
from thirdweb.common.feature_detection import implements_interface
from thirdweb.constants.role import ALL_ROLES
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_platform_fee import ContractPlatformFee
from thirdweb.core.classes.contract_roles import ContractRoles
from thirdweb.core.classes.contract_royalty import ContractRoyalty
from thirdweb.core.classes.contract_sales import ContractPrimarySale
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import ContractType
from eth_account.account import LocalAccount
from thirdweb.abi import ThirdwebContract, AccessControlEnumerable, IThirdwebRoyalty

from thirdweb.types.sdk import SDKOptions
from thirdweb.types.settings.metadata import (
    ContractMetadataSchema,
    CustomContractMetadata,
)


class CustomContract(BaseContract[ThirdwebContract]):
    contract_type: Final[ContractType] = ContractType.CUSTOM

    metadata: ContractMetadata[ThirdwebContract, ContractMetadataSchema]

    def __init__(
        self,
        provider: Web3,
        address: str,
        abi: str,
        storage: IpfsStorage,
        signer: Optional[LocalAccount] = None,
        options: SDKOptions = SDKOptions(),
    ):
        contract_abi = ThirdwebContract(provider, address)
        contract_wrapper = ContractWrapper(contract_abi, provider, signer, options)
        super().__init__(contract_wrapper)

        self._storage = storage
        self.metadata = ContractMetadata(
            contract_wrapper, storage, CustomContractMetadata
        )

        self.roles = self.detect_roles()
        self.royalties = self.detect_royalties()
        self.sales = self.detect_primary_sales()
        self.platform_fee = self.detect_platform_fee()

    def detect_roles(self):
        if implements_interface(self._contract_wrapper, AccessControlEnumerable):
            return ContractRoles(self._contract_wrapper, ALL_ROLES)
        return None

    def detect_royalties(self):
        if implements_interface(self._contract_wrapper, IThirdwebRoyalty):
            metadata = ContractMetadata(
                self._contract_wrapper,
                self._storage,
                CustomContractMetadata,
            )
            return ContractRoyalty(self._contract_wrapper, metadata)
        return None

    def detect_primary_sales(self):
        if implements_interface(self._contract_wrapper, IThirdwebPrimarySale):
            return ContractPrimarySale(self._contract_wrapper)
        return None

    def detect_platform_fee(self):
        if implements_interface(self._contract_wrapper, IThirdwebPlatformFee):
            return ContractPlatformFee(self._contract_wrapper)
        return None
