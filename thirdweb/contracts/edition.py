"""Interface for interacting with an edition contract"""

from thirdweb.common.nft import upload_or_extract_uri, upload_or_extract_uris
from thirdweb.constants.role import Role
from thirdweb.core.classes.contract_events import ContractEvents
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_platform_fee import ContractPlatformFee
from thirdweb.core.classes.contract_roles import ContractRoles
from thirdweb.core.classes.contract_royalty import ContractRoyalty
from thirdweb.core.classes.contract_sales import ContractPrimarySale
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.erc_1155_standard import ERC1155Standard
from thirdweb.core.classes.erc_1155_signature_minting import ERC1155SignatureMinting
from thirdweb.abi import TokenERC1155

from eth_account.account import LocalAccount
from web3.constants import MAX_INT
from web3 import Web3
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import ContractType

from thirdweb.types.nft import EditionMetadata, EditionMetadataInput
from thirdweb.types.sdk import SDKOptions
from typing import Any, Final, Optional, List

from thirdweb.types.settings.metadata import EditionContractMetadata
from thirdweb.types.tx import TxResultWithId


class Edition(ERC1155Standard[TokenERC1155]):
    """
    Create a collection of NFTs that lets you mint multiple copies of each NFT.

    ```python
    from thirdweb import ThirdwebSDK
    from thirdweb.types import SDKOptions

    # Get your secret key from the thirdweb api keys dashboard
    secret_key = "..."

    # You can customize this to a supported network or your own RPC URL
    network = "mumbai"

    # Now we can create a new instance of the SDK
    sdk = ThirdwebSDK(network, options=SDKOptions(secret_key=secret_key))

    # If you want to send transactions, you can instantiate the SDK with a private key instead:
    #   sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, network, options=SDKOptions(secret_key=secret_key))

    contract = sdk.get_edition("{{contract_address}}")
    ```
    """

    _abi_type = TokenERC1155

    contract_type: Final[ContractType] = ContractType.EDITION
    contract_roles: Final[List[Role]] = [Role.ADMIN, Role.MINTER, Role.TRANSFER]

    metadata: ContractMetadata[TokenERC1155, EditionContractMetadata]
    roles: ContractRoles
    primary_sale: ContractPrimarySale[TokenERC1155]
    platform_fee: ContractPlatformFee[TokenERC1155]
    royalty: ContractRoyalty[TokenERC1155]
    signature: ERC1155SignatureMinting
    events: ContractEvents[TokenERC1155]

    def __init__(
        self,
        provider: Web3,
        address: str,
        storage: IpfsStorage,
        signer: Optional[LocalAccount] = None,
        options: SDKOptions = SDKOptions(),
    ):
        abi = TokenERC1155(provider, address)
        contract_wrapper = ContractWrapper(abi, provider, signer, options)
        super().__init__(contract_wrapper, storage)

        self.metadata = ContractMetadata(
            contract_wrapper, storage, EditionContractMetadata
        )
        self.roles = ContractRoles(contract_wrapper, self.contract_roles)
        self.primary_sale = ContractPrimarySale(contract_wrapper)
        self.platform_fee = ContractPlatformFee(contract_wrapper)
        self.royalty = ContractRoyalty(contract_wrapper, self.metadata)
        self.signature = ERC1155SignatureMinting(
            contract_wrapper, self.roles, self._storage
        )
        self.events = ContractEvents(contract_wrapper)

    def mint(
        self, metadata_with_supply: EditionMetadataInput
    ) -> TxResultWithId[EditionMetadata]:
        """
        Mint a new NFT to the connected wallet

        :param metadata_with_supply: EditionMetadataInput for the NFT to mint
        :returns: receipt, id, and metadata of the mint
        """

        return self._erc1155.mint(metadata_with_supply)

    def mint_to(
        self, to: str, metadata_with_supply: EditionMetadataInput
    ) -> TxResultWithId[EditionMetadata]:
        """
        Mint a new NFT to the specified wallet

        ```python
        from thirdweb.types.nft import NFTMetadataInput, EditionMetadataInput

        # Note that you can customize this metadata however you like
        metadata_with_supply = EditionMetadataInput(
            NFTMetadataInput.from_json({
                "name": "Cool NFT",
                "description": "This is a cool NFT",
                "image": open("path/to/file.jpg", "rb"),
            }),
            100
        )

        # You can pass in any address here to mint the NFT to
        tx = contract.mint_to("{{wallet_address}}", metadata_with_supply)
        receipt = tx.receipt
        token_id = tx.id
        nft = tx.data()
        ```

        :param to: wallet address to mint the NFT to
        :param metadata_with_supply: EditionMetadataInput for the NFT to mint
        :returns: receipt, id, and metadata of the mint
        """

        return self._erc1155.mint_to(to, metadata_with_supply)

    def mint_additional_supply(
        self, token_id: int, additional_supply: int
    ) -> TxResultWithId[EditionMetadata]:
        """
        Mint additional supply of a token to the connected wallet

        :param token_id: token ID to mint additional supply of
        :param additional_supply: additional supply to mint
        :returns: receipt, id, and metadata of the mint
        """

        return self._erc1155.mint_additional_supply(token_id, additional_supply)

    def mint_additional_supply_to(
        self, to: str, token_id: int, additional_supply: int
    ) -> TxResultWithId[EditionMetadata]:
        """
        Mint additional supply of a token to the specified wallet

        :param to: wallet address to mint additional supply to
        :param token_id: token ID to mint additional supply of
        :param additional_supply: additional supply to mint
        :returns: receipt, id, and metadata of the mint
        """

        return self._erc1155.mint_additional_supply_to(to, token_id, additional_supply)

    def mint_batch(
        self, metadatas_with_supply: List[EditionMetadataInput]
    ) -> List[TxResultWithId[EditionMetadata]]:
        """
        Mint a batch of NFTs to the connected wallet

        :param metadatas_with_supply: list of EditionMetadataInput for the NFTs to mint
        :returns: receipts, ids, and metadatas of the mint
        """

        return self._erc1155.mint_batch(metadatas_with_supply)

    def mint_batch_to(
        self, to: str, metadatas_with_supply: List[EditionMetadataInput]
    ) -> List[TxResultWithId[EditionMetadata]]:
        """
        Mint a batch of NFTs to the specified wallet

        ```python
        from thirdweb.types.nft import NFTMetadataInput, EditionMetadataInput

        # Note that you can customize this metadata however you like
        metadatas_with_supply = [
            EditionMetadataInput(
                NFTMetadataInput.from_json({
                    "name": "Cool NFT",
                    "description": "This is a cool NFT",
                    "image": open("path/to/file.jpg", "rb"),
                }),
                100
            ),
            EditionMetadataInput(
                NFTMetadataInput.from_json({
                    "name": "Cooler NFT",
                    "description": "This is a cooler NFT",
                    "image": open("path/to/file.jpg", "rb"),
                }),
                100
            )
        ]

        # You can pass in any address here to mint the NFT to
        txs = contract.mint_batch_to("{{wallet_address}}", metadatas_with_supply)
        receipt = txs[0].receipt
        token_id = txs[0].id
        nft = txs[0].data()
        ```

        :param to: wallet address to mint the NFTs to
        :param metadatas_with_supply: list of EditionMetadataInput for the NFTs to mint
        :returns: receipts, ids, and metadatas of the mint
        """

        return self._erc1155.mint_batch_to(to, metadatas_with_supply)

    def call(self, fn: str, *args) -> Any:
        return self._contract_wrapper.call(fn, *args)