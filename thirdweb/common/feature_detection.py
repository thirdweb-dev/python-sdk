import base58
from hexbytes import HexBytes
from web3.contract import ContractFunctions
from web3 import Web3
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from cbor2 import decoder
import json


def matches_interface(
    contract: ContractFunctions, interface_to_match: ContractFunctions
) -> bool:
    contract_functions = [fn for fn in contract]
    interface_fn = [fn for fn in interface_to_match]

    overlap = set(contract_functions).intersection(interface_fn)
    return set(interface_fn) == set(overlap)


def fetch_contract_metadata(metadata_uri: str, storage: IpfsStorage) -> str:
    metadata = storage.get(metadata_uri)
    return metadata["output"]["abi"]


def fetch_contract_metadata_from_address(
    address: str, provider: Web3, storage: IpfsStorage
) -> str:
    metadata_uri = resolve_contract_uri_from_address(address, provider)
    if not metadata_uri:
        raise Exception(f"Failed to resolve metadata for contract at {address}")

    return fetch_contract_metadata(metadata_uri, storage)


def resolve_contract_uri_from_address(address: str, provider: Web3) -> str:
    bytecode = provider.eth.get_code(address)
    return extract_ipfs_hash_from_bytecode(bytecode)


def extract_ipfs_hash_from_bytecode(bytecode: HexBytes) -> str:
    try:
        cbor_length = bytecode[-2] * 0x100 + bytecode[-1]
        cbor_data = bytecode[-cbor_length - 2 : -2]
        ipfs_data = decoder.loads(cbor_data)["ipfs"]
        ipfs_hash = base58.b58encode(ipfs_data).decode("utf-8")
        return f"ipfs://{ipfs_hash}"
    except Exception as e:
        print("Failed to extract IPFS hash from bytecode")
    return ""
