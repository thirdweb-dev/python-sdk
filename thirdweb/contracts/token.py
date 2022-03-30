from typing import Final, List, Optional, Union
from thirdweb.abi import TokenERC20
from web3 import Web3
from web3.eth import TxReceipt
from eth_account.account import LocalAccount
from thirdweb.common.currency import parse_units
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.erc_20 import ERC20
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.currency import CurrencyValue, TokenAmount

from thirdweb.types.sdk import SDKOptions
from thirdweb.types.settings.metadata import TokenContractMetadata


class Token(ERC20):
    contract_type: Final[str] = "token"
    contract_roles: Final[List[str]] = ["admin", "minter", "transfer"]

    schema = TokenContractMetadata
    metadata: ContractMetadata[TokenContractMetadata]

    def __init__(
        self,
        provider: Web3,
        address: str,
        storage: IpfsStorage,
        signer: Optional[LocalAccount],
        options: SDKOptions = SDKOptions(),
    ):
        abi = TokenERC20(provider, address)
        contract_wrapper = ContractWrapper(abi, provider, signer, options)
        super().__init__(contract_wrapper, storage)

        self.metadata = ContractMetadata(contract_wrapper, storage, self.schema)

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

        return self._get_value(self._get_abi().get_votes.call(account))

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

        return self._get_abi().delegates.call(account)

    """
    WRITE FUNCTIONS
    """

    def mint(self, amount: int) -> TxReceipt:
        """
        Mint tokens to the connected wallet.

        :param amount: amount of tokens to mint
        :returns: transaction receipt of the mint
        """

        return self.mint_to(self._contract_wrapper.get_signer_address(), amount)

    def mint_to(self, to: str, amount: int) -> TxReceipt:
        """
        Mint tokens to a specified wallet.

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

        :param args: list of wallet addresses and amounts to mint
        :returns: transaction receipt of the mint
        """

        # TODO: Implement - Relies on MULTICALL
        raise NotImplementedError

    def delegate_to(self, delegatee_address: str) -> TxReceipt:
        """
        Delegate the connected wallets tokens to a specified wallet.

        :param delegatee_address: wallet address to delegate tokens to
        :returns: transaction receipt of the delegation
        """

        return self._contract_wrapper.send_transaction("delegate", [delegatee_address])
