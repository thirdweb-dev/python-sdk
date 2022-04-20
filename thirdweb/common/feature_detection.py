from typing import cast

from eth_typing import Address
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from web3.contract import Contract
from web3 import Web3
from thirdweb.core.classes.ipfs_storage import IpfsStorage

from thirdweb.types.contract import TContractABI
from thirdweb.types.settings.metadata import CustomContractMetadata


def implements_interface(
    contract_wrapper: ContractWrapper[TContractABI], interface_to_match
) -> bool:
    target_interface = Web3.eth.contract(
        address=cast(Address, contract_wrapper._contract_abi.contract_address),
        abi=interface_to_match().abi(),
    )
    return matches_interface(
        contract_wrapper.get_contract_interface(), target_interface
    )


# TODO: Implement interface matching
def matches_interface(contract: Contract, interface_to_match: Contract) -> bool:
    contract_fn = contract.functions
    interface_fn = interface_to_match.functions

    return True


def fetch_contract_metadata(metadata_uri: str, storage: IpfsStorage) -> str:
    metadata = CustomContractMetadata.from_json(storage.get(metadata_uri))
    abi = storage.get(metadata["abiUri"])
    return abi  # type: ignore
