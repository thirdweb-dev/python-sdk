from typing import Any, Dict, Generic, TypeVar
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.settings.metadata import ContractMetadata as TContractMetadata
from web3.eth import TxReceipt

Schema = TypeVar("Schema", bound=TContractMetadata)


class ContractMetadata(Generic[Schema]):
    _contract_wrapper: ContractWrapper
    _schema: Schema
    _storage: IpfsStorage

    def __init__(
        self, contract_wrapper: ContractWrapper, storage: IpfsStorage, schema: Schema
    ):
        self._contract_wrapper = contract_wrapper
        self._storage = storage
        self._schema = schema

    def get(self) -> Schema:
        uri = self._contract_wrapper._contract_abi.contract_uri.call()
        data = self._storage.get(uri)
        return self._schema.from_json(data)

    def set(self, metadata: Schema) -> TxReceipt:
        uri = self._parse_and_upload_metadata(metadata.to_json())
        return self._contract_wrapper.send_transaction("set_contract_uri", [uri])

    def _parse_and_upload_metadata(self, metadata: Dict[str, Any]) -> str:
        return self._storage.upload_metadata(metadata)
