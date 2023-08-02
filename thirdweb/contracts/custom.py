from typing import Any, Final, Optional, cast
from eth_typing import Address
from thirdweb.core.classes.contract_events import ContractEvents

from web3 import Web3
from web3.contract import ContractFunctions, ContractFunction
from thirdweb.abi.token_erc1155 import TokenERC1155
from thirdweb.abi.token_erc20 import TokenERC20
from thirdweb.abi.token_erc721 import TokenERC721
from thirdweb.common.error import NoSignerException
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
    IContractMetadata,
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
    from thirdweb.types import SDKOptions

    # Get your secret key from the thirdweb api keys dashboard
    secret_key = "..."

    # You can customize this to a supported network or your own RPC URL
    network = "mumbai"

    # Now we can create a new instance of the SDK
    sdk = ThirdwebSDK(network, options=SDKOptions(secret_key=secret_key))

    # If you want to send transactions, you can instantiate the SDK with a private key instead:
    #   sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, network, options=SDKOptions(secret_key=secret_key))

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
    events: ContractEvents

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

        self.metadata = self._detect_metadata()
        self.roles = self._detect_roles()
        self.royalties = self._detect_royalties()
        self.sales = self._detect_primary_sales()
        self.platform_fee = self._detect_platform_fee()

        self.erc20 = self._detect_erc_20()
        self.erc721 = self._detect_erc_721()
        self.erc1155 = self._detect_erc_1155()

        self.events = ContractEvents(contract_wrapper)

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

        if func.abi["stateMutability"] == "view" or func.abi["stateMutability"] == "pure":
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

    def _detect_metadata(self):
        contract_wrapper = self._get_contract_wrapper(IContractMetadata)
        return ContractMetadata(
            contract_wrapper,
            self._storage,
            CustomContractMetadata,
        )

    def _detect_roles(self):
        contract_wrapper = self._get_contract_wrapper(IPermissionsEnumerable)
        return ContractRoles(contract_wrapper, ALL_ROLES)

    def _detect_royalties(self):
        contract_wrapper = self._get_contract_wrapper(IRoyalty)
        metadata = ContractMetadata(
            contract_wrapper,
            self._storage,
            CustomContractMetadata,
        )
        return ContractRoyalty(contract_wrapper, metadata)

    def _detect_primary_sales(self):
        contract_wrapper = self._get_contract_wrapper(IPrimarySale)
        return ContractPrimarySale(contract_wrapper)

    def _detect_platform_fee(self):
        contract_wrapper = self._get_contract_wrapper(IPlatformFee)
        return ContractPlatformFee(contract_wrapper)

    def _detect_erc_20(self):
        contract_wrapper = self._get_contract_wrapper(TokenERC20)
        return ERC20(contract_wrapper, self._storage)

    def _detect_erc_721(self):
        contract_wrapper = self._get_contract_wrapper(TokenERC721)
        return ERC721(contract_wrapper, self._storage)

    def _detect_erc_1155(self):
        contract_wrapper = self._get_contract_wrapper(TokenERC1155)
        return ERC1155(contract_wrapper, self._storage)

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
