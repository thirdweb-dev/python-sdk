from typing import Generic
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.types.contract import TPrimarySaleABI
from web3.eth import TxReceipt


class ContractPrimarySale(Generic[TPrimarySaleABI]):
    _contract_wrapper: ContractWrapper[TPrimarySaleABI]

    def __init__(self, contract_wrapper: ContractWrapper[TPrimarySaleABI]):
        self._contract_wrapper = contract_wrapper

    def get_recipient(self) -> str:
        """
        Get the primary sale recipient of this contract.

        :returns: the address of the primary sale recipient.
        """

        return self._contract_wrapper._contract_abi.primary_sale_recipient.call()

    def set_recipient(self, recipient: str) -> TxReceipt:
        """
        Set the primary sale recipient of this contract

        :param recipient: the address of the primary sale recipient.
        :returns: the transaction receipt.
        """

        return self._contract_wrapper.send_transaction(
            "set_primary_sale_recipient", [recipient]
        )
