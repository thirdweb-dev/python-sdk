from thirdweb.core.classes.contract_wrapper import ContractWrapper
from web3.contract import Contract


def implements_interface(contract_wrapper: ContractWrapper, interface_to_match) -> bool:
    return matches_interface(
        contract_wrapper.get_contract_interface(), interface_to_match
    )


# TODO: Implement interface matching
def matches_interface(contract: Contract, interface_to_match) -> bool:
    contract_fn = contract.functions
    interface_fn = interface_to_match.functions

    return True
