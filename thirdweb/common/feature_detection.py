from typing import cast

from eth_typing import Address
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from web3.contract import ContractFunctions
from web3 import Web3
from thirdweb.core.classes.ipfs_storage import IpfsStorage

from thirdweb.types.contract import TContractABI
from thirdweb.types.settings.metadata import CustomContractMetadata


def matches_interface(
    contract: ContractFunctions, interface_to_match: ContractFunctions
) -> bool:
    contract_functions = [fn for fn in contract]
    interface_fn = [fn for fn in interface_to_match]

    overlap = set(contract_functions).intersection(interface_fn)
    return set(interface_fn) == set(overlap)


def fetch_contract_metadata(metadata_uri: str, storage: IpfsStorage) -> str:
    metadata = storage.get(metadata_uri)
    abi = storage._get(metadata["abiUri"]).json()
    return abi  # type: ignore
