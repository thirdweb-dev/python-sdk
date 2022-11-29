from typing import Any, Final, Optional, cast
from eth_typing import Address

from web3 import Web3
from web3.contract import ContractFunctions, ContractFunction
from thirdweb.abi.i_token_erc1155 import ITokenERC1155
from thirdweb.abi.i_token_erc20 import ITokenERC20
from thirdweb.abi.i_token_erc721 import ITokenERC721
from thirdweb.abi.token_erc721 import TokenERC721
from thirdweb.common.error import NoSignerException
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
from zero_ex.contract_wrappers.tx_params import TxParams
from thirdweb.types.contract import ContractType
from eth_account.account import LocalAccount
from thirdweb.abi import (
    IPermissionsEnumerable,
    IRoyalty,
    IPrimarySale,
    IPlatformFee,
)

from thirdweb.types.sdk import SDKOptions
from thirdweb.types.settings.metadata import (
    CustomContractMetadata,
)


class CustomContract(BaseContract[Any]):
    """
    An SDK interface for a custom contract instance.

    ```python
    from thirdweb import ThirdwebSDK

    # You can customize this to a supported network or your own RPC URL
    network = "mumbai"

    # Now we can create a new instance of the SDK
    sdk = ThirdwebSDK(network)

    # If you want to send transactions, you can instantiate the SDK with a private key instead:
    #   sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, network)

    contract = sdk.get_contract("{{contract_address}}")

    # If your contract follows the ERC721 standard, contract.nft will be present
    nfts = contract.nft.get_all()

    # You can call any contract read function as follows
    balance = contract.functions.balance().call()

    # And you can also use write functions like this
    address = "0x..."
    uri = "ipfs://..."
    contract.send_transaction("mint", [address, uri])
    ```
    """

    contract_type: Final[ContractType] = ContractType.CUSTOM

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
        # Temporarily use this ABI (none of the specific functions are used) so any ABi will use
        # Until we refactor the contract wrapper to require a web3py ABI instead of a generated one
        contract_abi = TokenERC721(provider, address)
        contract_wrapper = ContractWrapper(contract_abi, provider, signer, options)
        super().__init__(contract_wrapper)

        contract = provider.eth.contract(address=cast(Address, address), abi=abi)
        self.functions = contract.functions

        self._storage = storage

        self.roles = self._detect_roles()
        self.royalties = self._detect_royalties()
        self.sales = self._detect_primary_sales()
        self.platform_fee = self._detect_platform_fee()

        self.token = self._detect_erc_20()
        self.nft = self._detect_erc_721()
        self.edition = self._detect_erc_1155()

    def call(self, fn: str, *args) -> Any:
        func = cast(ContractFunction, getattr(self.functions, fn, None))
        if func is None:
            raise Exception(
                f"Function {fn} not found on contract {self.get_address()}. "
                + "Check your dashboard for the list of available functions."
            )

        # We need this to set params properly on func + throws good errors
        func.args = args
        func.kwargs = {}
        func._set_function_info()

        if len(func.abi["inputs"]) != len(args):
            signature = (
                "("
                + ", ".join(
                    [(i["name"] + ": " + i["type"]) for i in func.abi["inputs"]]
                )
                + ")"
            )
            raise Exception(
                f"Function {fn} expects {len(func.arguments)} arguments, "
                f"but {len(args)} were provided.\nExpected function signature: {signature}"
            )

        if func.abi["stateMutability"] == "view":
            return func(*args).call()
        else:
            provider = self._contract_wrapper.get_provider()
            signer = self._contract_wrapper.get_signer()

            if signer is None:
                raise NoSignerException

            nonce = provider.eth.get_transaction_count(signer.address)  # type: ignore

            tx = func(*args).buildTransaction(
                TxParams(gas_price=provider.eth.gas_price).as_dict()
            )
            tx["nonce"] = nonce

            signed_tx = signer.sign_transaction(tx)  # type: ignore
            tx_hash = provider.eth.send_raw_transaction(signed_tx.rawTransaction)

            return provider.eth.wait_for_transaction_receipt(tx_hash)

    """
    INTERNAL FUNCTIONS
    """

    def _detect_roles(self):
        interface_to_match = self._get_interface_functions(IPermissionsEnumerable.abi())

        if matches_interface(self.functions, interface_to_match):
            contract_wrapper = self._get_contract_wrapper(IPermissionsEnumerable)
            return ContractRoles(contract_wrapper, ALL_ROLES)
        return None

    def _detect_royalties(self):
        interface_to_match = self._get_interface_functions(IRoyalty.abi())

        if matches_interface(self.functions, interface_to_match):
            contract_wrapper = self._get_contract_wrapper(IRoyalty)
            metadata = ContractMetadata(
                contract_wrapper,
                self._storage,
                CustomContractMetadata,
            )
            return ContractRoyalty(contract_wrapper, metadata)
        return None

    def _detect_primary_sales(self):
        interface_to_match = self._get_interface_functions(IPrimarySale.abi())

        if matches_interface(self.functions, interface_to_match):
            contract_wrapper = self._get_contract_wrapper(IPrimarySale)
            return ContractPrimarySale(contract_wrapper)
        return None

    def _detect_platform_fee(self):
        interface_to_match = self._get_interface_functions(IPlatformFee.abi())

        if matches_interface(self.functions, interface_to_match):
            contract_wrapper = self._get_contract_wrapper(IPlatformFee)
            return ContractPlatformFee(contract_wrapper)
        return None

    def _detect_erc_20(self):
        interface_to_match = self._get_interface_functions(ITokenERC20.abi())

        if matches_interface(self.functions, interface_to_match):
            contract_wrapper = self._get_contract_wrapper(ITokenERC20)
            return ERC20(contract_wrapper, self._storage)
        return None

    def _detect_erc_721(self):
        interface_to_match = self._get_interface_functions(ITokenERC721.abi())

        if matches_interface(self.functions, interface_to_match):
            contract_wrapper = self._get_contract_wrapper(ITokenERC721)
            return ERC721(contract_wrapper, self._storage)
        return None

    def _detect_erc_1155(self):
        interface_to_match = self._get_interface_functions(ITokenERC1155.abi())

        if matches_interface(self.functions, interface_to_match):
            contract_wrapper = self._get_contract_wrapper(ITokenERC1155)
            return ERC1155(contract_wrapper, self._storage)
        return None

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
