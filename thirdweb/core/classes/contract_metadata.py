from typing import Any, Dict, Generic
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import TContractSchema, TMetadataABI
from web3.eth import TxReceipt


class ContractMetadata(Generic[TMetadataABI, TContractSchema]):
    _contract_wrapper: ContractWrapper[TMetadataABI]
    _schema: TContractSchema
    _storage: IpfsStorage

    def __init__(
        self,
        contract_wrapper: ContractWrapper[TMetadataABI],
        storage: IpfsStorage,
        contract_schema: TContractSchema,
    ):
        self._contract_wrapper = contract_wrapper
        self._storage = storage
        self._schema = contract_schema

    def get(self) -> TContractSchema:
        """
        Get the metadata associated with this contract.

        :returns: metadata associated with this contract
        """

        abi = self._contract_wrapper._contract_abi
        uri = abi.contract_uri.call()
        data = self._storage.get(uri)
        return self._schema.from_json(data)

    def set(self, metadata: TContractSchema) -> TxReceipt:
        """
        Set the metadata associated with this contract.

        :param metadata: metadata to set
        :returns: transaction receipt of setting the metadata
        """

        uri = self._parse_and_upload_metadata(metadata.to_json())
        return self._contract_wrapper.send_transaction("set_contract_uri", [uri])

    def _parse_and_upload_metadata(self, metadata: Dict[str, Any]) -> str:
        return self._storage.upload_metadata(metadata)
