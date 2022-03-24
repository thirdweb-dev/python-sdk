from typing import Optional
from web3 import Web3
from eth_account.account import LocalAccount

from thirdweb.core.classes.contract_wrapper import ContractWrapper


class BaseContract:
    """
    Base contract class to define usage of the contract wrapper and enable
    easy provider and signer switching across all contracts
    """

    __contract_wrapper: ContractWrapper

    def __init__(self, contract_wrapper: ContractWrapper):
        self.__contract_wrapper = contract_wrapper

    def on_provider_updated(self, provider: Web3):
        """
        Updates the contract provider when the SDK provider is updated

        :param provider: web3 provider instance to use
        """

        self.__contract_wrapper.update_provider(provider)

    def on_signer_updated(self, signer: Optional[LocalAccount]):
        """
        Updates the contract signer when the SDK signer is updated

        :param signer: optional account to use for signing transactions
        """

        self.__contract_wrapper.update_signer(signer)

    def get_address(self):
        """
        Get the address of the contract
        """

        self.__contract_wrapper.__contract_abi.address
