from thirdweb.abi.contract_metadata_registry import ContractMetadataRegistry
from thirdweb.constants.addresses import get_contract_address_by_chain_id
from thirdweb.constants.chains import ChainId
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from web3.contract import ContractFunctions
from web3 import Web3
from thirdweb.core.classes.ipfs_storage import IpfsStorage

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


# TODO: Implement fetch contract metadata
def fetch_contract_metadata_from_address(
    address: str, provider: Web3, storage: IpfsStorage
) -> str:
    metadata_uri = resolve_contract_uri_from_address(address, provider)
    return fetch_contract_metadata(metadata_uri, storage)


def resolve_contract_uri_from_address(address: str, provider: Web3) -> str:
    chain_id = provider.eth.chainId
    metadata_registry_address = get_contract_address_by_chain_id(
        ChainId(chain_id),
        "contract_metadata_registry",
    )
    contract_metadata_registry = ContractMetadataRegistry(
        provider, metadata_registry_address
    )
    return contract_metadata_registry.get_metadata_uri.call(address)
