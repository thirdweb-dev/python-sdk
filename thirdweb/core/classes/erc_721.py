from typing import List, Generic
from thirdweb.common.error import NotFoundException
from thirdweb.common.nft import fetch_token_metadata
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.constants.role import Role, get_role_hash
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import TERC721
from thirdweb.types.nft import NFTMetadata, NFTMetadataOwner, QueryAllParams
from web3.eth import TxReceipt


class ERC721(Generic[TERC721], BaseContract[TERC721]):
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
        """
        Get metadata for a token

        ```python
        nft = contract.get(0)
        print(nft)
        ```

        :param token_id: token ID of the token to get the metadata for
        :return: the metadata for the token and its owner
        """

        try:
            owner = self.owner_of(token_id)
        except:
            owner = ZERO_ADDRESS

        metadata = self._get_token_metadata(token_id)
        return NFTMetadataOwner(metadata, owner)

    def get_all(
        self, query_params: QueryAllParams = QueryAllParams()
    ) -> List[NFTMetadataOwner]:
        """
        Get the metadata of all tokens in the contract

        ```python
        nfts = contract.get_all()
        print(nfts)
        ```

        :param query_params: optionally define a QueryAllParams instance to narrow the metadata query to specific tokens
        :return: the metadata of all tokens in the contract
        """

        max_id = min(query_params.start + query_params.count, self.get_total_count())

        nfts = []
        for token_id in range(query_params.start, max_id):
            try:
                nft = self.get(token_id)
                nfts.append(nft)
            except:
                pass

        return nfts

    def get_total_count(self) -> int:
        """
        Get the total number of NFTs minted by this contract

        :return: the total number of NFTs minted by this contract
        """

        return self._contract_wrapper._contract_abi.next_token_id_to_mint.call()

    def owner_of(self, token_id: int) -> str:
        """
        Get the owner of a token

        :param token_id: the token ID of the token to get the owner of
        :return: the owner of the token
        """
        return self._contract_wrapper._contract_abi.owner_of.call(token_id)

    def total_supply(
        self,
    ) -> int:
        """
        Get the total number of tokens in the contract

        :return: the total number of tokens in the contract
        """
        return self._contract_wrapper._contract_abi.next_token_id_to_mint.call()

    def balance(
        self,
    ) -> int:
        """
        Get the token balance of the connected wallet

        :return: the token balance of the connected wallet
        """

        return self.balance_of(self._contract_wrapper.get_signer_address())

    def balance_of(self, address: str) -> int:
        """
        Get the token balance of a specific address

        ```python
        balance = contract.balance_of("{{wallet_address}}")
        print(balance)
        ```

        :param address: the address to get the token balance of
        """

        return self._contract_wrapper._contract_abi.balance_of.call(address)

    def is_transfer_restricted(
        self,
    ) -> bool:
        """
        Check if the contract is restricted to transfers only by admins

        :return: True if the contract is restricted to transfers only by admins, False otherwise
        """

        anyone_can_transfer = self._contract_wrapper._contract_abi.has_role.call(
            get_role_hash(Role.TRANSFER), ZERO_ADDRESS
        )

        return not anyone_can_transfer

    def is_approved(self, address: str, operator: str) -> bool:
        """
        Check whether an operator address is approved for all operations of a specific addresses assets

        :param address: the address whose assets are to be checked
        :param operator: the address of the operator to check
        :return: True if the operator is approved for all operations of the assets, False otherwise
        """

        return self._contract_wrapper._contract_abi.is_approved_for_all.call(
            address, operator
        )

    """
    WRITE FUNCTIONS
    """

    def transfer(self, to: str, token_id: int) -> TxReceipt:
        """
        Transfer a specified token from the connected wallet to a specified address.

        ```python
        to = "{{wallet_address}}"
        token_id = 0

        receipt = contract.transfer(to, token_id)
        ```

        :param to: wallet address to transfer the tokens to
        :param token_id: the specific token ID to transfer
        :returns: transaction receipt of the transfer
        """

        fr = self._contract_wrapper.get_signer_address()
        return self._contract_wrapper.send_transaction(
            "safe_transfer_from1", [fr, to, token_id]
        )

    def burn(self, token_id: int) -> TxReceipt:
        """
        Burn a specified token from the connected wallet.

        :param token_id: token ID of the token to burn
        :returns: transaction receipt of the burn
        """

        return self._contract_wrapper.send_transaction("burn", [token_id])

    def set_approval_for_all(self, operator: str, approved: bool) -> TxReceipt:
        """
        Set the approval of an operator for all operations of a specific address's assets

        :param operator: the address of the operator to set the approval for
        :param approved: the address whos assets the operator is approved to manage
        :returns: transaction receipt of the approval
        """

        return self._contract_wrapper.send_transaction(
            "set_approval_for_all", [operator, approved]
        )

    def set_approval_for_token(self, operator: str, token_id: int) -> TxReceipt:
        """
        Approve an operator for the NFT owner, which allows the operator to call transferFrom
        or safeTransferFrom for the specified token.

        :param operator: the address of the operator to set the approval for
        :param token_id: the specific token ID to set the approval for
        :returns: transaction receipt of the approval
        """
        return self._contract_wrapper.send_transaction("approve", [operator, token_id])

    """
    INTERNAL FUNCTIONS
    """

    def _get_token_metadata(self, token_id: int) -> NFTMetadata:
        token_uri = self._contract_wrapper._contract_abi.token_uri.call(token_id)

        if not token_uri:
            raise NotFoundException(str(token_id))

        return fetch_token_metadata(token_id, token_uri, self._storage)
