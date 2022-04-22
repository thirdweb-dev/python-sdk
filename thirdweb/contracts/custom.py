from typing import Final, Optional, cast
from eth_typing import Address

from web3 import Web3
from web3.contract import ContractFunctions
from thirdweb.abi.i_signature_mint import ISignatureMint
from thirdweb.abi.i_thirdweb_platform_fee import IThirdwebPlatformFee
from thirdweb.abi.i_thirdweb_primary_sale import IThirdwebPrimarySale
from thirdweb.abi.i_token_erc1155 import ITokenERC1155
from thirdweb.abi.i_token_erc20 import ITokenERC20
from thirdweb.abi.i_token_erc721 import ITokenERC721
from thirdweb.common.feature_detection import matches_interface
from thirdweb.constants.role import ALL_ROLES
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_platform_fee import ContractPlatformFee
from thirdweb.core.classes.contract_roles import ContractRoles
from thirdweb.core.classes.contract_royalty import ContractRoyalty
from thirdweb.core.classes.contract_sales import ContractPrimarySale
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.erc_1155 import ERC1155
from thirdweb.core.classes.erc_20 import ERC20
from thirdweb.core.classes.erc_721 import ERC721
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
    functions: ContractFunctions

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

        contract = provider.eth.contract(address=cast(Address, address), abi=abi)
        self.functions = contract.functions

        self._storage = storage
        self.metadata = ContractMetadata(
            contract_wrapper, storage, CustomContractMetadata
        )

        self.roles = self.detect_roles()
        self.royalties = self.detect_royalties()
        self.sales = self.detect_primary_sales()
        self.platform_fee = self.detect_platform_fee()

        self.token = self.detect_erc_20()
        self.nft = self.detect_erc_721()
        self.edition = self.detect_erc_1155()

        # self.signature_mint = self.detect_signature_mint()

    def detect_roles(self):
        interface_to_match = self._get_interface_functions(
            AccessControlEnumerable.abi()
        )

        if matches_interface(self.functions, interface_to_match):
            contract_wrapper = self._get_contract_wrapper(AccessControlEnumerable)
            return ContractRoles(contract_wrapper, ALL_ROLES)
        return None

    def detect_royalties(self):
        interface_to_match = self._get_interface_functions(IThirdwebRoyalty.abi())

        if matches_interface(self.functions, interface_to_match):
            contract_wrapper = self._get_contract_wrapper(IThirdwebRoyalty)
            metadata = ContractMetadata(
                contract_wrapper,
                self._storage,
                CustomContractMetadata,
            )
            return ContractRoyalty(contract_wrapper, metadata)
        return None

    def detect_primary_sales(self):
        interface_to_match = self._get_interface_functions(IThirdwebPrimarySale.abi())

        if matches_interface(self.functions, interface_to_match):
            contract_wrapper = self._get_contract_wrapper(IThirdwebPrimarySale)
            return ContractPrimarySale(contract_wrapper)
        return None

    def detect_platform_fee(self):
        interface_to_match = self._get_interface_functions(IThirdwebPlatformFee.abi())

        if matches_interface(self.functions, interface_to_match):
            contract_wrapper = self._get_contract_wrapper(IThirdwebPlatformFee)
            return ContractPlatformFee(contract_wrapper)
        return None

    def detect_erc_20(self):
        interface_to_match = self._get_interface_functions(ITokenERC20.abi())

        if matches_interface(self.functions, interface_to_match):
            contract_wrapper = self._get_contract_wrapper(ITokenERC20)
            return ERC20(contract_wrapper, self._storage)
        return None

    def detect_erc_721(self):
        interface_to_match = self._get_interface_functions(ITokenERC721.abi())

        if matches_interface(self.functions, interface_to_match):
            contract_wrapper = self._get_contract_wrapper(ITokenERC721)
            return ERC721(contract_wrapper, self._storage)
        return None

    def detect_erc_1155(self):
        interface_to_match = self._get_interface_functions(ITokenERC1155.abi())

        if matches_interface(self.functions, interface_to_match):
            contract_wrapper = self._get_contract_wrapper(ITokenERC1155)
            return ERC1155(contract_wrapper, self._storage)
        return None

    def detect_signature_mint(self):
        interface_to_match = self._get_interface_functions(ISignatureMint.abi())

        if matches_interface(self.functions, interface_to_match):
            contract_wrapper = self._get_contract_wrapper(ISignatureMint)
            return ERC1155(contract_wrapper, self._storage)
        return None

    """
    INTERNAL FUNCTIONS
    """

    def _get_interface_functions(self, abi: str) -> ContractFunctions:
        return (
            self._contract_wrapper.get_provider()
            .eth.contract(
                address=cast(
                    Address, self._contract_wrapper._contract_abi.contract_address
                ),
                abi=abi,
            )
            .functions
        )

    def _get_contract_wrapper(self, abi) -> ContractWrapper:
        contract_abi = abi(
            self._contract_wrapper.get_provider(),
            self._contract_wrapper._contract_abi.contract_address,
        )

        return ContractWrapper(
            contract_abi,
            self._contract_wrapper.get_provider(),
            self._contract_wrapper.get_signer(),
        )
