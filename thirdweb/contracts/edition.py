from thirdweb.common.nft import upload_or_extract_uri
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.erc_1155 import ERC1155
from thirdweb.abi import TokenERC1155

from eth_account.account import LocalAccount
from web3.constants import MAX_INT
from web3.eth import TxReceipt
from web3 import Web3
from thirdweb.core.classes.ipfs_storage import IpfsStorage

from thirdweb.types.nft import EditionMetadataInput
from thirdweb.types.sdk import SDKOptions
from typing import Optional, List


class Edition(ERC1155):
    def __init__(
        self,
        provider: Web3,
        address: str,
        storage: IpfsStorage,
        signer: Optional[LocalAccount],
        options: SDKOptions = SDKOptions(),
    ):
        abi = TokenERC1155(provider, address)
        contract_wrapper = ContractWrapper(abi, provider, signer, options)
        super().__init__(contract_wrapper, storage)

    def mint(self, metadata_with_supply: EditionMetadataInput) -> TxReceipt:
        return self.mint_to(
            self._contract_wrapper.get_signer_address(), metadata_with_supply
        )

    def mint_to(self, to: str, metadata_with_supply: EditionMetadataInput) -> TxReceipt:
        uri = upload_or_extract_uri(metadata_with_supply.metadata, self._storage)
        return self._contract_wrapper.send_transaction(
            "mint_to", [to, MAX_INT, uri, metadata_with_supply.supply]
        )

    def mint_additional_supply(
        self, token_id: int, additional_supply: int
    ) -> TxReceipt:
        return self.mint_additional_supply_to(
            self._contract_wrapper.get_signer_address(), token_id, additional_supply
        )

    def mint_additional_supply_to(
        self, to: str, token_id: int, additional_supply: int
    ) -> TxReceipt:
        metadata = self._get_token_metadata(token_id)
        return self._contract_wrapper.send_transaction(
            "mint_to", [to, token_id, metadata.uri, additional_supply]
        )

    def mint_batch(
        self, metadatas_with_supply: List[EditionMetadataInput]
    ) -> TxReceipt:
        return self.mint_batch_to(
            self._contract_wrapper.get_signer_address(), metadatas_with_supply
        )

    def mint_batch_to(
        self, to: str, metadatas_with_supply: List[EditionMetadataInput]
    ) -> TxReceipt:
        # TODO: Implement - relies on MULTICALL
        raise NotImplementedError
