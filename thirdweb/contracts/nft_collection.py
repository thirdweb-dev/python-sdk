from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.erc_721 import ERC721
from thirdweb.abi import TokenERC721

from eth_account.account import LocalAccount
from web3.eth import TxReceipt
from web3 import Web3
from thirdweb.types.nft import NFTMetadata

from thirdweb.types.sdk import SDKOptions
from typing import Optional, List, Union


class NFTCollection(ERC721):
    def __init__(
        self,
        provider: Web3,
        address: str,
        signer: Optional[LocalAccount],
        options: SDKOptions = SDKOptions(),
    ):
        abi = TokenERC721(provider, address)
        contract_wrapper = ContractWrapper(abi, provider, signer, options)
        super().__init__(contract_wrapper)

    """
    WRITE FUNCTIONS
    """

    def mint(self, metadata: Union[NFTMetadata, str]) -> TxReceipt:
        pass

    def mint_to(self, to: str, metadata: Union[NFTMetadata, str]) -> TxReceipt:
        pass

    def mint_batch(self, metadatas: List[Union[NFTMetadata, str]]) -> TxReceipt:
        pass

    def mint_batch_to(
        self, to: str, metadatas: List[Union[NFTMetadata, str]]
    ) -> TxReceipt:
        pass
