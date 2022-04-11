from typing import Any, List
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.contract_roles import ContractRoles
from thirdweb.abi import TokenERC20
from thirdweb.types.tx import TxResultWithId
from thirdweb.types.contracts.signature import (
    PayloadToSign20,
    PayloadWithUri20,
    SignedPayload20,
)


class ERC20SignatureMinting:
    _contract_wrapper: ContractWrapper[TokenERC20]
    _storage: IpfsStorage

    roles: ContractRoles

    def __init__(
        self,
        contract_wrapper: ContractWrapper[TokenERC20],
        roles: ContractRoles,
        storage: IpfsStorage,
    ):
        self._contract_wrapper = contract_wrapper
        self._storage = storage
        self.roles = roles

    def mint(self, signed_payload: SignedPayload20) -> TxResultWithId:
        pass

    def mint_batch(
        self, signed_payloads: List[SignedPayload20]
    ) -> List[TxResultWithId]:
        pass

    def verify(self, signed_payload: SignedPayload20) -> bool:
        pass

    def generate(self, mint_request: PayloadToSign20) -> SignedPayload20:
        pass

    def generate_batch(
        self, payloads_to_sign: List[PayloadToSign20]
    ) -> List[SignedPayload20]:
        pass

    """
    INTERNAL FUNCTIONS
    """

    def map_payload_to_contract_struct(mint_request: PayloadWithUri20) -> Any:
        pass
