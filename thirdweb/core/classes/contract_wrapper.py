from typing import Any, Generic, Tuple, List, Optional, cast
from eth_typing import Address

from web3 import Web3
from web3.datastructures import AttributeDict
from web3.contract import Contract
from thirdweb.common.error import NoSignerException
from web3._utils.events import EventLogErrorFlags
from thirdweb.common.sign import EIP712Domain, sign_typed_data_internal
from thirdweb.constants.events import EventStatus, EventType

from thirdweb.core.classes.provider_handler import ProviderHandler
from web3.eth import TxReceipt
from eth_account.account import LocalAccount
from zero_ex.contract_wrappers.tx_params import TxParams
from thirdweb.types.contract import TContractABI
from thirdweb.types.events import SignatureEvent, TxEvent

from thirdweb.types.sdk import SDKOptions


class ContractWrapper(Generic[TContractABI], ProviderHandler):
    """
    The contract wrapper wraps an instance of a specific thirdweb contract ABI
    and exposed functions for interacting with the contract.
    """

    _contract_abi: TContractABI

    def __init__(
        self,
        contract_abi: TContractABI,
        provider: Web3,
        signer: Optional[LocalAccount] = None,
        options: SDKOptions = SDKOptions(),
    ):
        """
        Initializes the contract wrapper.

        :param contract_abi: ABI of the thirdweb contract to use
        :param provider: web3 provider instance to use
        :param signer: optional account to use for signing transactions
        """

        super().__init__(provider, signer, options)
        self._contract_abi = contract_abi

    def get_chain_id(self) -> int:
        """
        Get the chain ID of the active provider

        :returns: chain ID of the active provider
        """

        provider = self.get_provider()
        return provider.eth.chain_id

    def get_signer_address(self) -> str:
        """
        Get the address of the active signer

        :returns: address of the active signer
        """

        signer = self.get_signer()

        if signer is None:
            raise NoSignerException

        return signer.address

    def get_contract_interface(self) -> Contract:
        """
        Get the contract interface of the contract wrapper.

        :returns: contract interface of the contract wrapper
        """

        return self.get_provider().eth.contract(
            address=cast(Address, self._contract_abi.contract_address),
            abi=self._contract_abi.abi(),
        )

    def get_events(self, event: str, receipt: TxReceipt) -> Tuple[AttributeDict]:
        """
        Get the events from a transaction receipt.

        :param event: name of the event to get
        :param receipt: transaction receipt to get the events from
        """

        return (
            self.get_contract_interface()
            .events[event]()
            .processReceipt(receipt, errors=EventLogErrorFlags.Discard)
        )

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
        tx = getattr(self._contract_abi, fn).build_transaction(
            *args, tx_params=TxParams(gas_price=provider.eth.gas_price)
        )
        tx["nonce"] = nonce

        signed_tx = signer.sign_transaction(tx)
        tx_hash = provider.eth.send_raw_transaction(signed_tx.rawTransaction)

        self.emit_transaction_event(EventStatus.SUBMITTED, tx_hash.hex())

        receipt = provider.eth.wait_for_transaction_receipt(tx_hash)

        self.emit_transaction_event(EventStatus.COMPLETED, tx_hash.hex())

        return receipt

    def multi_call(self, encoded: List[str]) -> TxReceipt:
        """
        Execute a multicall and return the result.

        :param encoded: list of encoded function calls to execute
        """

        return self.send_transaction("multicall", [encoded])

    def emit_transaction_event(self, status: EventStatus, tx_hash: str):
        self.emit(EventType.TRANSACTION, TxEvent(status, tx_hash))  # type: ignore

    def sign_typed_data(
        self, signer: LocalAccount, domain: EIP712Domain, types: Any, message: Any
    ) -> bytes:
        self.emit(
            EventType.SIGNATURE,  # type: ignore
            SignatureEvent(EventStatus.SUBMITTED, message, ""),
        )

        signature = sign_typed_data_internal(
            self.get_provider(), signer, domain, types, message
        )

        self.emit(
            EventType.SIGNATURE,  # type: ignore
            SignatureEvent(EventStatus.COMPLETED, message, signature),
        )

        return signature
