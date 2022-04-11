from typing import Any, List
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.contract_roles import ContractRoles
from thirdweb.abi import TokenERC1155
from thirdweb.types.tx import TxResultWithId
from thirdweb.types.contracts.signature import (
    PayloadToSign1155,
    PayloadWithUri1155,
    SignedPayload1155,
)


class ERC1155SignatureMinting:
    _contract_wrapper: ContractWrapper[TokenERC1155]
    _storage: IpfsStorage

    roles: ContractRoles

    def __init__(
        self,
        contract_wrapper: ContractWrapper[TokenERC1155],
        roles: ContractRoles,
        storage: IpfsStorage,
    ):
        self._contract_wrapper = contract_wrapper
        self._storage = storage
        self.roles = roles

    def mint(self, signed_payload: SignedPayload1155) -> TxResultWithId:
        pass

    def mint_batch(
        self, signed_payloads: List[SignedPayload1155]
    ) -> List[TxResultWithId]:
        pass

    def verify(self, signed_payload: SignedPayload1155) -> bool:
        pass

    def generate(self, mint_request: PayloadToSign1155) -> SignedPayload1155:
        pass

    def generate_batch(
        self, payloads_to_sign: List[PayloadToSign1155]
    ) -> List[SignedPayload1155]:
        pass

    """
    INTERNAL FUNCTIONS
    """

    def map_payload_to_contract_struct(mint_request: PayloadWithUri1155) -> Any:
        pass
