from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.erc_1155 import ERC1155
from thirdweb.abi import TokenERC1155

from eth_account.account import LocalAccount
from web3.eth import TxReceipt
from web3 import Web3

from thirdweb.types.nft import EditionMetadata
from thirdweb.types.sdk import SDKOptions
from typing import Optional, Union, List


class Edition(ERC1155):
    def __init__(
        self,
        provider: Web3,
        address: str,
        signer: Optional[LocalAccount],
        options: SDKOptions = SDKOptions(),
    ):
        abi = TokenERC1155(provider, address)
        contract_wrapper = ContractWrapper(abi, provider, signer, options)
        super().__init__(contract_wrapper)

    def mint(self, metadata_with_supply: Union[EditionMetadata, str]) -> TxReceipt:
        pass

    def mint_to(
        self, to: str, metadata_with_supply: Union[EditionMetadata, str]
    ) -> TxReceipt:
        pass

    def mint_additional_supply(
        self, token_id: int, additional_supply: int
    ) -> TxReceipt:
        pass

    def mint_additional_supply_to(
        self, to: str, token_id: int, additional_supply: int
    ) -> TxReceipt:
        pass

    def mint_batch(
        self, metadatas_with_supply: List[Union[EditionMetadata, str]]
    ) -> TxReceipt:
        pass

    def mint_batch_to(
        self, to: str, metadatas_with_supply: List[Union[EditionMetadata, str]]
    ) -> TxReceipt:
        pass
