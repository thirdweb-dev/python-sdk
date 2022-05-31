"""Interface for interacting with an nft collection contract"""

from thirdweb.constants.role import Role
from thirdweb.core.classes.contract_events import ContractEvents
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_platform_fee import ContractPlatformFee
from thirdweb.core.classes.contract_roles import ContractRoles
from thirdweb.core.classes.contract_royalty import ContractRoyalty
from thirdweb.core.classes.contract_sales import ContractPrimarySale
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.common.nft import upload_or_extract_uri, upload_or_extract_uris
from thirdweb.core.classes.erc_721 import ERC721
from thirdweb.core.classes.erc_721_signature_minting import ERC721SignatureMinting
from thirdweb.abi import TokenERC721

from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import ContractType
from thirdweb.types.nft import NFTMetadataInput, NFTMetadataOwner
from eth_account.account import LocalAccount
from web3 import Web3

from thirdweb.types.sdk import SDKOptions
from typing import Final, Optional, List, Union

from thirdweb.types.settings.metadata import NFTCollectionContractMetadata
from thirdweb.types.tx import TxResultWithId


class NFTCollection(ERC721[TokenERC721]):
    """
    Create a collection of one-of-one NFTs.

    ```python
    from thirdweb import ThirdwebSDK

    # You can customize this to a supported network or your own RPC URL
    network = "mumbai"

    # Now we can create a new instance of the SDK
    sdk = ThirdwebSDK(network)

    # If you want to send transactions, you can instantiate the SDK with a private key instead:
    #   sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, network)

    contract = sdk.get_nft_collection("{{contract_address}}")
    ```
    """

    _abi_type = TokenERC721

    contract_type: Final[ContractType] = ContractType.NFT_COLLECTION
    contract_roles: Final[List[Role]] = [Role.ADMIN, Role.MINTER, Role.TRANSFER]

    metadata: ContractMetadata[TokenERC721, NFTCollectionContractMetadata]
    roles: ContractRoles
    primary_sale: ContractPrimarySale[TokenERC721]
    platform_fee: ContractPlatformFee[TokenERC721]
    royalty: ContractRoyalty[TokenERC721]
    signature: ERC721SignatureMinting
    events: ContractEvents[TokenERC721]

    def __init__(
        self,
        provider: Web3,
        address: str,
        storage: IpfsStorage,
        signer: Optional[LocalAccount] = None,
        options: SDKOptions = SDKOptions(),
    ):
        abi = TokenERC721(provider, address)
        contract_wrapper = ContractWrapper(abi, provider, signer, options)
        super().__init__(contract_wrapper, storage)

        self.metadata = ContractMetadata(
            contract_wrapper, storage, NFTCollectionContractMetadata
        )
        self.roles = ContractRoles(contract_wrapper, self.contract_roles)
        self.primary_sale = ContractPrimarySale(contract_wrapper)
        self.platform_fee = ContractPlatformFee(contract_wrapper)
        self.royalty = ContractRoyalty(contract_wrapper, self.metadata)
        self.signature = ERC721SignatureMinting(
            contract_wrapper, self.roles, self._storage
        )
        self.events = ContractEvents(contract_wrapper)

    """
    READ FUNCTIONS
    """

    def get_owned(self, address: str = "") -> List[NFTMetadataOwner]:
        """
        Get the metadata of all tokens owned by a specific address

        ```python
        nfts = contract.get_owned("{{wallet_address}}")
        print(nfts)
        ```

        :param address: the address to get the metadata for
        :return: the metadata of all tokens owned by the address
        """

        token_ids = self.get_owned_token_ids(address)
        return [self.get(token_id) for token_id in token_ids]

    def get_owned_token_ids(self, address: str = "") -> List[int]:
        """
        Get the token IDs owned by a specific address

        :param address: the address to get the token IDs for
        :return: the token IDs owned by the address
        """

        owner = address if address else self._contract_wrapper.get_signer_address()
        balance = self._contract_wrapper._contract_abi.balance_of.call(owner)
        return [
            self._contract_wrapper._contract_abi.token_of_owner_by_index.call(owner, i)
            for i in range(balance)
        ]

    """
    WRITE FUNCTIONS
    """

    def mint(
        self, metadata: Union[NFTMetadataInput, str]
    ) -> TxResultWithId[NFTMetadataOwner]:
        """
        Mint a new NFT to the connected wallet

        :param metadata: metadata of the NFT to mint
        :returns: receipt, id, and metadata for the mint
        """

        return self.mint_to(self._contract_wrapper.get_signer_address(), metadata)

    def mint_to(
        self, to: str, metadata: Union[NFTMetadataInput, str]
    ) -> TxResultWithId[NFTMetadataOwner]:
        """
        Mint a new NFT to the specified wallet

        ```python
        from thirdweb.types.nft import NFTMetadataInput

        # Note that you can customize this metadata however you like
        metadata = NFTMetadataInput.from_json({
            "name": "Cool NFT",
            "description": "This is a cool NFT",
            "image": open("path/to/file.jpg", "rb"),
        })

        # You can pass in any address here to mint the NFT to
        tx = contract.mint_to("{{wallet_address}}", metadata)
        receipt = tx.receipt
        token_id = tx.id
        nft = tx.data()
        ```

        :param to: wallet address to mint the NFT to
        :param metadata: metadata of the NFT to mint
        :returns: receipt, id, and metadata for the mint
        """

        uri = upload_or_extract_uri(metadata, self._storage)
        receipt = self._contract_wrapper.send_transaction("mint_to", [to, uri])
        events = self._contract_wrapper.get_events("TokensMinted", receipt)

        if len(events) == 0:
            raise Exception("No TokensMinted event found")

        id = events[0].get("args").get("tokenIdMinted")  # type: ignore

        return TxResultWithId(receipt, id=id, data=lambda: self.get(id))

    def mint_batch(
        self, metadatas: List[Union[NFTMetadataInput, str]]
    ) -> List[TxResultWithId[NFTMetadataOwner]]:
        """
        Mint a batch of new NFTs to the connected wallet

        :param metadatas: list of metadata of the NFTs to mint
        :returns: receipts, ids, and metadatas for each mint
        """

        return self.mint_batch_to(
            self._contract_wrapper.get_signer_address(), metadatas
        )

    def mint_batch_to(
        self, to: str, metadatas: List[Union[NFTMetadataInput, str]]
    ) -> List[TxResultWithId[NFTMetadataOwner]]:
        """
        Mint a batch of new NFTs to the specified wallet

        ```python
        from thirdweb.types.nft import NFTMetadataInput

        # You can customize this metadata however you like
        metadatas = [
            NFTMetadataInput.from_json({
                "name": "Cool NFT",
                "description": "This is a cool NFT",
                "image": open("path/to/file.jpg", "rb"),
            }),
            NFTMetadataInput.from_json({
                "name": "Cooler NFT",
                "description": "This is a cooler NFT",
                "image": open("path/to/file.jpg", "rb"),
            }),
        ]

        # You can pass in any address here to mint the NFT to
        txs = contract.mint_batch_to("{{wallet_address}}", metadatas)
        receipt = txs[0].receipt
        first_token_id = txs[0].id
        first_nft = txs[0].data()
        ```

        :param to: wallet address to mint the NFTs to
        :param metadatas: list of metadata of the NFTs to mint
        :returns: receipts, ids, and metadatas for each mint
        """

        uris = upload_or_extract_uris(metadatas, self._storage)

        encoded = []
        interface = self._contract_wrapper.get_contract_interface()
        for uri in uris:
            encoded.append(interface.encodeABI("mintTo", [to, uri]))

        receipt = self._contract_wrapper.multi_call(encoded)
        events = self._contract_wrapper.get_events("TokensMinted", receipt)

        if len(events) == 0 or len(events) < len(metadatas):
            raise Exception("No TokensMinted event found, minting failed")

        results = []
        for event in events:
            id = event.get("args").get("tokenIdMinted")  # type: ignore
            results.append(TxResultWithId(receipt, id=id, data=lambda: self.get(id)))

        return results
