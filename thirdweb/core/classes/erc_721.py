from typing import List, Optional, cast
from thirdweb.abi import TokenERC721
from thirdweb.common.error import NotFoundException
from thirdweb.common.nft import fetch_token_metadata
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.nft import NFTMetadata, NFTMetadataOwner, QueryAllParams
from thirdweb.types.sdk import SDKOptions
from web3.eth import TxReceipt


class ERC721(BaseContract):
    _storage: IpfsStorage

    def __init__(
        self,
        contract_wrapper: ContractWrapper,
        storage: IpfsStorage,
    ):
        super().__init__(contract_wrapper)
        self._storage = storage

    """
    READ FUNCTIONS
    """

    def get(self, token_id: int) -> NFTMetadataOwner:
        owner = self.owner_of(token_id)
        metadata = self._get_token_metadata(token_id)
        return NFTMetadataOwner(metadata, owner)

    def get_all(
        self, query_params: QueryAllParams = QueryAllParams()
    ) -> List[NFTMetadataOwner]:
        max_id = min(query_params.start + query_params.count, self.get_total_count())
        return [self.get(token_id) for token_id in range(query_params.start, max_id)]

    def get_total_count(self) -> int:
        return self._get_abi().next_token_id_to_mint.call()

    def get_owned(self, address: str = "") -> List[NFTMetadataOwner]:
        owner = address if address else self._contract_wrapper.get_signer_address()
        balance = self._get_abi().balance_of.call(owner)
        token_ids = [
            self._get_abi().token_of_owner_by_index.call(owner, i)
            for i in range(balance)
        ]
        return [self.get(token_id) for token_id in token_ids]

    def owner_of(self, token_id: int) -> str:
        return self._get_abi().owner_of.call(token_id)

    def total_supply(
        self,
    ) -> int:
        return self._get_abi().next_token_id_to_mint.call()

    def balance(
        self,
    ) -> int:
        return self.balance_of(self._contract_wrapper.get_signer_address())

    def balance_of(self, address: str) -> int:
        return self._get_abi().balance_of.call(address)

    def is_transfer_restricted(
        self,
    ) -> bool:
        # TODO: Implement - Relies on ROLES
        raise NotImplementedError

    def is_approved(self, address: str, operator: str) -> bool:
        return self._get_abi().is_approved_for_all.call(address, operator)

    """
    WRITE FUNCTIONS
    """

    def transfer(self, to: str, token_id: int) -> TxReceipt:
        fr = self._contract_wrapper.get_signer_address()
        return self._contract_wrapper.send_transaction(
            "safeTransferFrom(address,address,uint256)", [fr, to, token_id]
        )

    def burn(self, token_id: int) -> TxReceipt:
        return self._contract_wrapper.send_transaction("burn", [token_id])

    def set_approval_for_all(self, operator: str, approved: bool) -> TxReceipt:
        return self._contract_wrapper.send_transaction(
            "setApprovalForAll", [operator, approved]
        )

    """
    PRIVATE FUNCTIONS
    """

    def _get_abi(self) -> TokenERC721:
        return cast(TokenERC721, self._contract_wrapper._contract_abi)

    def _get_token_metadata(self, token_id: int) -> NFTMetadata:
        token_uri = self._get_abi().token_uri.call(token_id)

        if not token_uri:
            raise NotFoundException(str(token_id))

        return fetch_token_metadata(token_id, token_uri, self._storage)
