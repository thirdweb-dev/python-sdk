from typing import Any, Generic, List, Optional, Union, cast
from thirdweb.abi import TokenERC1155
from thirdweb.common.error import NotFoundException
from thirdweb.common.nft import fetch_token_metadata
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.constants.role import Role, get_role_hash
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import TERC1155
from thirdweb.types.nft import (
    EditionMetadata,
    EditionMetadataOwner,
    NFTMetadata,
    QueryAllParams,
)
from web3.eth import TxReceipt


class ERC1155(Generic[TERC1155], BaseContract[TERC1155]):
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

    def get(self, token_id: int) -> EditionMetadata:
        """
        Get metadata for a token

        ```python
        nft = contract.get(0)
        print(nft)
        ```

        :param token_id: token ID to check the metadata for
        :return: Metadata for the token
        """

        try:
            supply = self._contract_wrapper._contract_abi.total_supply.call(token_id)
        except:
            supply = 0

        metadata = self._get_token_metadata(token_id)
        return EditionMetadata(metadata, supply)

    def get_all(
        self, query_params: QueryAllParams = QueryAllParams()
    ) -> List[EditionMetadata]:
        """
        Get the metadata for all tokens on the contract

        ```python
        metadatas = contract.get_all()
        print(metadatas)
        ```

        :param query_params: optional QueryAllParams to define which tokens to get metadata for
        :return: list of metadata for all tokens
        """

        max_id = min(query_params.start + query_params.count, self.get_total_count())
        return [self.get(token_id) for token_id in range(query_params.start, max_id)]

    def get_total_count(self) -> int:
        """
        Get the total number of NFTs on the contract

        :return: total number of tokens on the contract
        """

        return self._contract_wrapper._contract_abi.next_token_id_to_mint.call()

    def get_owned(self, address: str = "") -> List[EditionMetadataOwner]:
        """
        Get the metadata for all the tokens owned by an address

        ```python
        address = "{{wallet_address}}"
        owned = contract.get_owned(address)
        print(owned)
        ```

        :param address: address to get the owned tokens for
        :return: list of metadata for all tokens owned by the address
        """

        owner = address if address else self._contract_wrapper.get_signer_address()
        max_id = self._contract_wrapper._contract_abi.next_token_id_to_mint.call()
        balances = self._contract_wrapper._contract_abi.balance_of_batch.call(
            [owner for i in range(max_id)],
            [id for id in range(max_id)],
        )

        metadatas = []
        for index, balance in enumerate(balances):
            metadata = self.get(index)
            metadatas.append(
                EditionMetadataOwner(metadata.metadata, metadata.supply, owner, balance)
            )

        return metadatas

    def total_supply(self, token_id: int) -> int:
        """
        Get the total number of tokens on the contract

        :return: total number of tokens on the contract
        """

        return self._contract_wrapper._contract_abi.total_supply.call(token_id)

    def balance(self, token_id: int) -> int:
        """
        Get the connected wallets balance of a specific token

        :param token_id: token ID to check the balance for
        :return: balance of the token
        """

        return self.balance_of(self._contract_wrapper.get_signer_address(), token_id)

    def balance_of(self, address: str, token_id: int) -> int:
        """
        Get a specific wallets balance of a specific token

        ```python
        address = "{{wallet_address}}"
        token_id = 0

        balance = contract.balance_of(address, token_id)
        ```

        :param address: address to check the balance for
        :param token_id: token ID to check the balance for
        :return: balance of the token
        """

        return self._contract_wrapper._contract_abi.balance_of.call(address, token_id)

    def is_transfer_restricted(self) -> bool:
        """
        Check if the contract is restricted so transfers can only be made by admins

        :return: True if the contract is restricted, False otherwise
        """

        anyone_can_transfer = self._contract_wrapper._contract_abi.has_role.call(
            get_role_hash(Role.TRANSFER), ZERO_ADDRESS
        )

        return not anyone_can_transfer

    def is_approved(self, address: str, operator: str) -> bool:
        """
        Check if an operator address is approved to manage a target addresses assets

        :param address: address whose assets to check the approval of
        :param operator: operator address to check the approval for
        :return: True if the operator is approved, False otherwise
        """

        return self._contract_wrapper._contract_abi.is_approved_for_all.call(
            address, operator
        )

    """
    WRITE FUNCTIONS
    """

    def transfer(
        self, to: str, token_id: int, amount: int, data: Union[bytes, str] = b"0"
    ) -> TxReceipt:
        """
        Transfer a specified token from the connected wallet to a specified address.

        ```python
        to = "{{wallet_address}}"
        token_id = 0
        amount = 1

        receipt = contract.transfer(to, token_id, amount)
        ```

        :param to: wallet address to transfer the tokens to
        :param token_id: the specific token ID to transfer
        :param amount: the amount of tokens to transfer
        :returns: transaction receipt of the transfer
        """

        fr = self._contract_wrapper.get_signer_address()
        return self._contract_wrapper.send_transaction(
            "safe_transfer_from",
            [fr, to, token_id, amount, data],
        )

    def burn(self, token_id: int, amount: int) -> TxReceipt:
        """
        Burn a specified amount of tokens from the connected wallet.

        :param amount: amount of tokens to burn
        :returns: transaction receipt of the burn
        """

        account = self._contract_wrapper.get_signer_address()
        return self._contract_wrapper.send_transaction(
            "burn", [account, token_id, amount]
        )

    def set_approval_for_all(self, operator: str, approved: bool) -> TxReceipt:
        """
        Set the approval for an operator address to manage the connected wallets assets

        :param operator: operator address to set the approval for
        :param approved: True if the operator is approved, False otherwise
        """

        return self._contract_wrapper.send_transaction(
            "set_approval_for_all", [operator, approved]
        )

    """
    INTERNAL FUNCTIONS
    """

    def _get_token_metadata(self, token_id: int) -> NFTMetadata:
        token_uri = self._contract_wrapper._contract_abi.uri.call(token_id)

        if not token_uri:
            raise NotFoundException(str(token_id))

        return fetch_token_metadata(token_id, token_uri, self._storage)
