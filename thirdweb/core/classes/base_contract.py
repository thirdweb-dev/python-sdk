from typing import Generic, Optional
from web3 import Web3
from eth_account.account import LocalAccount

from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.types.contract import TContractABI


class BaseContract(Generic[TContractABI]):
    """
    Base contract class to define usage of the contract wrapper and enable
    easy provider and signer switching across all contracts
    """

    _contract_wrapper: ContractWrapper[TContractABI]

    def __init__(self, contract_wrapper: ContractWrapper[TContractABI]):
        self._contract_wrapper = contract_wrapper

    def on_provider_updated(self, provider: Web3):
        """
        Updates the contract provider when the SDK provider is updated

        :param provider: web3 provider instance to use
        """

        self._contract_wrapper._update_provider(provider)

    def on_signer_updated(self, signer: Optional[LocalAccount] = None):
        """
        Updates the contract signer when the SDK signer is updated

        :param signer: optional account to use for signing transactions
        """

        self._contract_wrapper._update_signer(signer)

    def get_address(self) -> str:
        """
        Get the address of the contract
        """

        return self._contract_wrapper._contract_abi.contract_address
