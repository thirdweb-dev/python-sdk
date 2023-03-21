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

def extract_minimal_proxy_implementation_address(bytecode: HexBytes) -> str:
    #  EIP-1167 clone minimal proxy - https://eips.ethereum.org/EIPS/eip-1167
    if bytecode.hex().startswith("0x363d3d373d3d3d363d73"):
        implementation_address = bytecode.hex()[22:22 + 40]
        return "0x" + implementation_address
    
    # Minimal Proxy with receive() from 0xSplits - https://github.com/0xSplits/splits-contracts/blob/c7b741926ec9746182d0d1e2c4c2046102e5d337/contracts/libraries/Clones.sol
    if bytecode.hex().startswith("0x36603057343d5230"):
        implementation_address = bytecode.hex()[122:122 + 40]
        return "0x" + implementation_address
    
    # 0age's minimal proxy - https://medium.com/coinmonks/the-more-minimal-proxy-5756ae08ee48
    if bytecode.hex().startswith("0x3d3d3d3d363d3d37363d73"):
        implementation_address = bytecode.hex()[24:24 + 40]
        return "0x" + implementation_address
    
    # vyper's minimal proxy (uniswap v1) - https://etherscan.io/address/0x09cabec1ead1c0ba254b09efb3ee13841712be14#code
    if bytecode.hex().startswith("0x366000600037611000600036600073"):
        implementation_address = bytecode.hex()[32:32 + 40]
        return "0x" + implementation_address

    return ""


def resolve_contract_uri_from_address(address: str, provider: Web3) -> str:
    bytecode = provider.eth.get_code(provider.toChecksumAddress(address))
    if bytecode.hex() == "0x":
        raise Exception(f"Contract at '{address}' does not exist")
    
    try:
        implementation_address = extract_minimal_proxy_implementation_address(bytecode)
        if implementation_address:
            checksum_implementation_address = provider.toChecksumAddress(implementation_address)
            return resolve_contract_uri_from_address(checksum_implementation_address, provider)
    except:
        pass

    try:
        proxy_storage = provider.eth.get_storage_at(
            provider.toChecksumAddress(address), 
            # hex: 0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc
            24440054405305269366569402256811496959409073762505157381672968839269610695612
        )
        implementation_address = "0x" + proxy_storage.hex().replace("0x", "").lstrip("0")
        if implementation_address != "0x":
            return resolve_contract_uri_from_address(
                implementation_address,
                provider,
            )
    except:
        pass

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
