from typing import Final, Optional

from web3 import Web3
from thirdweb.common.feature_detection import implements_interface
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_roles import ContractRoles
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import ContractType
from eth_account.account import LocalAccount

from thirdweb.types.sdk import SDKOptions
from thirdweb.types.settings.metadata import ContractMetadataSchema


class CustomContract(BaseContract):
    contract_type: Final[ContractType] = ContractType.CUSTOM

    metadata: ContractMetadata[ThirdwebContract, ContractMetadataSchema]

    def __init__(
        self,
        provider: Web3,
        address: str,
        storage: IpfsStorage,
        signer: Optional[LocalAccount] = None,
        options: SDKOptions = SDKOptions(),
    ):
        abi = ThirdwebContract(provider, address)
        contract_wrapper = ContractWrapper(abi, provider, signer, options)
        super().__init__(contract_wrapper)

        self._storage = storage
        self.metadata = ContractMetadata(
            contract_wrapper, storage, ContractMetadataSchema
        )

        self.roles = self.detect_roles()
        self.royalties = self.detect_royalties()
        self.sales = self.detect_primary_sales()
        self.platform_fee = self.detect_platform_fee()

    def detect_roles(self):
        pass

    def detect_royalties(self):
        pass

    def detect_primary_sales(self):
        pass

    def detect_platform_fee(self):
        pass
