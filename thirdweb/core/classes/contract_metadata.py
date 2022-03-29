from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from web3.eth import TxReceipt


class ContractMetadata:
    _contract_wrapper: ContractWrapper
    _schema: object
    _storage: IpfsStorage

    def __init__(self, contract_wrapper: ContractWrapper, storage: IpfsStorage):
        self._contract_wrapper = contract_wrapper
        self._storage = storage

    def get(self):
        uri = self._contract_wrapper._contract_abi.contract_uri.call()
        data = self._storage.get(uri)
        return data

    def set(self, metadata) -> TxReceipt:
        uri = self._parse_and_upload_metadata(metadata)
        return self._contract_wrapper.send_transaction("set_contract_uri", [uri])

    def _parse_and_upload_metadata(self, metadata):
        return self._storage.upload_metadata(metadata)
