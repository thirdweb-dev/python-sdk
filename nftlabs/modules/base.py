"""Base Module."""

from typing import Callable, Optional, cast
from eth_account.account import LocalAccount
from web3.types import TxReceipt

from ..storage import IpfsStorage
from ..options import SdkOptions

from web3 import Web3

from zero_ex.contract_wrappers import TxParams


class BaseModule:
    """
    Base module for all modules.
    """
    get_client: Optional[Callable[[], Web3]]
    """ Returns the client object. """
    get_storage: Optional[Callable[[], IpfsStorage]]
    """ Returns the storage object. """
    get_signer_address: Optional[Callable[[], str]]
    """ Returns the signer address. """
    get_private_key: Optional[Callable[[], str]]
    """ Returns the private key. """
    get_transact_opts: Optional[Callable[[], TxParams]]
    """ Returns the transaction options. """
    get_account: Optional[Callable[[], LocalAccount]]
    """ Returns the account object. """
    get_options: Optional[Callable[[], SdkOptions]]
    """ Returns the options object. """

    def __init__(self):
        self.get_client = None
        self.get_storage = None
        self.get_signer_address = None
        self.get_private_key = None
        self.get_transact_opts = None
        self.get_account = None
        self.get_options = None

    def execute_tx(self, tx) -> TxReceipt:
        """ 
        Execute a transaction and return the receipt.
        """
        client = self.get_client()
        nonce = client.eth.get_transaction_count(self.get_signer_address())
        tx['nonce'] = nonce
        del tx['from']
        signed_tx = self.__sign_tx(tx)
        tx_hash = client.eth.send_raw_transaction(signed_tx.rawTransaction)
        return cast(
            TxReceipt,
            client.eth.wait_for_transaction_receipt(
                tx_hash, timeout=self.get_options().tx_timeout_in_seconds)
        )

    def __sign_tx(self, tx):
        """ 
        Sign a transaction.
        """
        signed_tx = self.get_account().sign_transaction(tx)
        return signed_tx
