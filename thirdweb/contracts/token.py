"""Interface for interacting with a token contract"""

from typing import Final, List, Optional
from thirdweb.abi import TokenERC20
from web3 import Web3
from web3.eth import TxReceipt
from eth_account.account import LocalAccount
from thirdweb.common.currency import parse_units
from thirdweb.constants.role import Role
from thirdweb.core.classes.contract_events import ContractEvents
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_platform_fee import ContractPlatformFee
from thirdweb.core.classes.contract_roles import ContractRoles
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.erc_20 import ERC20
from thirdweb.core.classes.erc_20_signature_minting import ERC20SignatureMinting
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import ContractType
from thirdweb.types.currency import CurrencyValue, Price, TokenAmount

from thirdweb.types.sdk import SDKOptions
from thirdweb.types.settings.metadata import TokenContractMetadata


class Token(ERC20):
    """
    Create a standard crypto token or cryptocurrency.

    ```python
    from thirdweb import ThirdwebSDK
    from eth_account import Account

    # You can customize this to a supported network or your own RPC URL
    network = "mumbai"

    # This will create a random account to use for signing transactions
    signer = Account.create()

    sdk = ThirdwebSDK(network, signer)
    contract = sdk.get_token("{{contract_address}}")
    ```
    """

    _abi_type = TokenERC20

    contract_type: Final[ContractType] = ContractType.TOKEN
    contract_roles: Final[List[Role]] = [Role.ADMIN, Role.MINTER, Role.TRANSFER]

    metadata: ContractMetadata[TokenERC20, TokenContractMetadata]
    roles: ContractRoles
    platform_fee: ContractPlatformFee
    signature: ERC20SignatureMinting
    events: ContractEvents[TokenERC20]

    def __init__(
        self,
        provider: Web3,
        address: str,
        storage: IpfsStorage,
        signer: Optional[LocalAccount] = None,
        options: SDKOptions = SDKOptions(),
    ):
        abi = TokenERC20(provider, address)
        contract_wrapper = ContractWrapper(abi, provider, signer, options)
        super().__init__(contract_wrapper, storage)

        self.metadata = ContractMetadata(
            contract_wrapper, storage, TokenContractMetadata
        )
        self.roles = ContractRoles(contract_wrapper, self.contract_roles)
        self.platform_fee = ContractPlatformFee(contract_wrapper)
        self.signature = ERC20SignatureMinting(
            contract_wrapper, self.roles, self._storage
        )
        self.events = ContractEvents(contract_wrapper)

    """
    READ FUNCTIONS
    """

    def get_vote_balance(self) -> CurrencyValue:
        """
        Get the connected wallets voting power in this token.

        :returns: vote balance of the connected wallet
        """

        return self.get_vote_balance_of(self._contract_wrapper.get_signer_address())

    def get_vote_balance_of(self, account: str) -> CurrencyValue:
        """
        Get the voting power of the specified wallet in this token.

        :param account: wallet address to check the balance of
        :returns: vote balance of the specified wallet
        """

        return self._get_value(
            self._contract_wrapper._contract_abi.get_votes.call(account)
        )

    def get_delegation(self) -> str:
        """
        Get the connected wallets delegatee address for this token.

        :returns: delegation address of the connected wallet
        """

        return self.get_delegation_of(self._contract_wrapper.get_signer_address())

    def get_delegation_of(self, account: str) -> str:
        """
        Get a specified wallets delegatee for this token.

        :param account: wallet address to check the delegation of
        :returns: delegation address of the specified wallet
        """

        return self._contract_wrapper._contract_abi.delegates.call(account)

    """
    WRITE FUNCTIONS
    """

    def mint(self, amount: Price) -> TxReceipt:
        """
        Mint tokens to the connected wallet.

        :param amount: amount of tokens to mint
        :returns: transaction receipt of the mint
        """

        return self.mint_to(self._contract_wrapper.get_signer_address(), amount)

    def mint_to(self, to: str, amount: Price) -> TxReceipt:
        """
        Mint tokens to a specified wallet.

        ```python
        contract.mint_to("{{wallet_address}}", 1)
        ```

        :param to: wallet address to mint tokens to
        :param amount: amount of tokens to mint
        :returns: transaction receipt of the mint
        """

        amount_with_decimals = parse_units(amount, self.get().decimals)
        return self._contract_wrapper.send_transaction(
            "mint_to", [to, amount_with_decimals]
        )

    def mint_batch_to(self, args: List[TokenAmount]) -> TxReceipt:
        """
        Mint tokens to a list of wallets.

        ```python
        from thirdweb.types.currency import TokenAmount

        args = [
            TokenAmount("{{wallet_address}}", 1),
            TokenAmount("{{wallet_address}}", 2),
        ]

        contract.mint_batch_to(args)
        ```

        :param args: list of wallet addresses and amounts to mint
        :returns: transaction receipt of the mint
        """

        encoded = []
        interface = self._contract_wrapper.get_contract_interface()
        for arg in args:
            encoded.append(
                interface.encodeABI(
                    "mintTo",
                    [arg.to_address, parse_units(arg.amount, self.get().decimals)],
                )
            )
        return self._contract_wrapper.multi_call(encoded)

    def delegate_to(self, delegatee_address: str) -> TxReceipt:
        """
        Delegate the connected wallets tokens to a specified wallet.

        :param delegatee_address: wallet address to delegate tokens to
        :returns: transaction receipt of the delegation
        """

        return self._contract_wrapper.send_transaction("delegate", [delegatee_address])
