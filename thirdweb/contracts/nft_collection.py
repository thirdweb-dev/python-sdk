from thirdweb.common.nft import upload_or_extract_uri
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.erc_721 import ERC721
from thirdweb.abi import TokenERC721

from eth_account.account import LocalAccount
from web3.eth import TxReceipt
from web3 import Web3
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.nft import NFTMetadataInput

from thirdweb.types.sdk import SDKOptions
from typing import Optional, List, Union


class NFTCollection(ERC721):
    def __init__(
        self,
        provider: Web3,
        address: str,
        storage: IpfsStorage,
        signer: Optional[LocalAccount],
        options: SDKOptions = SDKOptions(),
    ):
        abi = TokenERC721(provider, address)
        contract_wrapper = ContractWrapper(abi, provider, signer, options)
        super().__init__(contract_wrapper, storage)

    """
    WRITE FUNCTIONS
    """

    def mint(self, metadata: Union[NFTMetadataInput, str]) -> TxReceipt:
        return self.mint_to(self._contract_wrapper.get_signer_address(), metadata)

    def mint_to(self, to: str, metadata: Union[NFTMetadataInput, str]) -> TxReceipt:
        uri = upload_or_extract_uri(metadata, self._storage)
        return self._contract_wrapper.send_transaction("mint_to", [to, uri])

    def mint_batch(self, metadatas: List[Union[NFTMetadataInput, str]]) -> TxReceipt:
        return self.mint_batch_to(
            self._contract_wrapper.get_signer_address(), metadatas
        )

    def mint_batch_to(
        self, to: str, metadatas: List[Union[NFTMetadataInput, str]]
    ) -> TxReceipt:
        # TODO: Implement - relies on MULTICALL
        raise NotImplementedError
