from typing import Any, List, Optional

from web3 import Web3
from thirdweb.common.error import NoSignerException
from thirdweb.core.classes.provider_handler import ProviderHandler
from thirdweb.types.contract import ContractABI
from web3.eth import TxReceipt
from eth_account.account import LocalAccount

from thirdweb.types.sdk import SDKOptions


class ContractWrapper(ProviderHandler):
    __contract_abi: ContractABI

    def __init__(
        self,
        contract_abi: ContractABI,
        provider: Web3,
        signer: Optional[LocalAccount],
        options: SDKOptions = SDKOptions(),
    ):
        super().__init__(provider, signer, options)
        self.__contract_abi = contract_abi

    def get_chain_id(self):
        """
        Get the chain ID of the active provider

        :returns: chain ID of the active provider
        """

        provider = self.get_provider()
        return provider.eth.chain_id

    def get_signer_address(self):
        """
        Get the address of the active signer

        :returns: address of the active signer
        """

        signer = self.get_signer()

        if signer is None:
            raise NoSignerException

        return signer.address

    def send_transaction(self, fn: str, args: List[Any]) -> TxReceipt:
        """
        Send and execute a transaction and return the receipt.

        :param fn: name of the function you want to call on the contract
        :param args: list of arguments to pass to the function
        """

        provider = self.get_provider()
        signer = self.get_signer()

        if signer is None:
            raise NoSignerException

        nonce = provider.eth.get_transaction_count(signer.address)
        tx = getattr(self.__contract_abi, fn).build_transaction(*args)
        tx["nonce"] = nonce
        del tx["from"]

        signed_tx = signer.sign_transaction(tx)
        tx_hash = provider.eth.send_raw_transaction(signed_tx.raw_transaction)

        return provider.eth.wait_for_transaction_receipt(tx_hash)
