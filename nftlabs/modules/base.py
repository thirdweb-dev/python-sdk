from typing import Callable, Optional
from eth_account.account import LocalAccount, Account

from ..storage import IpfsStorage

from web3 import Web3
from web3.eth import wait_for_transaction_receipt

from eth_account.account import sign_transaction_dict

from zero_ex.contract_wrappers import TxParams

class BaseModule:
    get_client: Callable[[], Web3]
    get_storage: Callable[[], IpfsStorage]
    get_signer_address: Callable[[], str]
    get_private_key: Callable[[], str]
    get_transact_opts: Callable[[], TxParams]

    get_account: Optional[Callable[[], LocalAccount]]

    def __init__(
            self,
            get_client: Callable[[], Web3],
            get_storage: Callable[[], IpfsStorage],
            get_signer_address: Callable[[], str],
            get_private_key: Callable[[], str],
            get_transact_opts: Callable[[], TxParams]
    ):
        self.get_client = get_client
        self.get_storage = get_storage
        self.get_signer_address = get_signer_address
        self.get_private_key = get_private_key
        self.get_transact_opts = get_transact_opts
        self.get_account = None

    def execute_tx(self, tx):
        client = self.get_client()
        nonce = client.eth.get_transaction_count(self.get_signer_address()) + 1
        tx['nonce'] = nonce
        del tx['from']
        signed_tx = self.__sign_tx(tx)
        tx_hash = client.eth.send_raw_transaction(signed_tx.rawTransaction)
        print('tx_hash', tx_hash.hex())
        receipt = client.eth.wait_for_transaction_receipt(tx_hash, timeout=20)
        return receipt

    def __sign_tx(self, tx):
        signed_tx = self.get_account().sign_transaction(tx)
        return signed_tx


