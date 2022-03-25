from typing import List, cast
from thirdweb.abi import TokenERC1155
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.types.nft import EditionMetadata, NFTMetadata, NFTMetadataOwner
from web3.eth import TxReceipt


class ERC1155(BaseContract):
    def __init__(self, contract_wrapper: ContractWrapper):
        super().__init__(contract_wrapper)

    """
    READ FUNCTIONS
    """

    def get(self, token_id: int) -> EditionMetadata:
        pass

    def get_all(self) -> List[EditionMetadata]:
        pass

    def get_total_count(self) -> int:
        pass

    def get_owned(self, address: str) -> List[EditionMetadata]:
        pass

    def total_supply(
        self,
    ) -> int:
        pass

    def balance_of(self, address: str, token_id: int) -> int:
        pass

    def balance(self, token_id: int) -> int:
        pass

    def is_transfer_restricted(self) -> bool:
        pass

    def is_approved(self, address: str, operator: str) -> bool:
        pass

    """
    WRITE FUNCTIONS
    """

    def transfer(self, to: str, token_id: int, amount: int) -> TxReceipt:
        pass

    def burn(self, token_id: int, amount: int) -> TxReceipt:
        pass

    def set_approval_for_all(self, operator: str, approved: bool) -> TxReceipt:
        pass

    """
    PRIVATE FUNCTIONS
    """

    def _get_abi(self) -> TokenERC1155:
        return cast(TokenERC1155, self._contract_wrapper._contract_abi)

    def _get_token_metadata(self, token_id: int) -> NFTMetadata:
        pass
