from typing import List, cast
from thirdweb.abi import TokenERC721
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.types.nft import NFTMetadata, NFTMetadataOwner
from web3.eth import TxReceipt


class ERC721(BaseContract):
    def __init__(self, contract_wrapper: ContractWrapper):
        super().__init__(contract_wrapper)

    """
    READ FUNCTIONS
    """

    def get(self, token_id: int) -> NFTMetadataOwner:
        pass

    def get_all(self) -> List[NFTMetadataOwner]:
        pass

    def get_total_count(self) -> int:
        pass

    def get_owned(self, address: str) -> List[NFTMetadataOwner]:
        pass

    def owner_of(self, token_id: int) -> str:
        pass

    def total_supply(
        self,
    ) -> int:
        pass

    def balance_of(self, address: str) -> int:
        pass

    def balance(
        self,
    ) -> int:
        pass

    def is_transfer_restricted(
        self,
    ) -> bool:
        pass

    def is_approved(self, address: str, operator: str) -> bool:
        pass

    """
    WRITE FUNCTIONS
    """

    def transfer(self, to: str, token_id: int) -> TxReceipt:
        pass

    def burn(self, token_id: int) -> TxReceipt:
        pass

    def set_approval_for_all(self, operator: str, approved: bool) -> TxReceipt:
        pass

    """
    PRIVATE FUNCTIONS
    """

    def _get_abi(self) -> TokenERC721:
        return cast(TokenERC721, self._contract_wrapper._contract_abi)

    def _get_token_metadata(self, token_id: int) -> NFTMetadata:
        pass
