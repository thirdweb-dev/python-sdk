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
from thirdweb.core.classes.erc_1155 import ERC1155
from thirdweb.core.classes.erc_1155_signature_minting import ERC1155SignatureMinting
from thirdweb.abi import TokenERC1155

from eth_account.account import LocalAccount
from web3.constants import MAX_INT
from web3 import Web3
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import ContractType

from thirdweb.types.nft import EditionMetadata, EditionMetadataInput
from thirdweb.types.sdk import SDKOptions
from typing import Final, Optional, List

from thirdweb.types.settings.metadata import EditionContractMetadata
from thirdweb.types.tx import TxResultWithId


class Edition(ERC1155[TokenERC1155]):
    """
    Create a collection of NFTs that lets you mint multiple copies of each NFT.

    ```python
    from thirdweb import ThirdwebSDK
    from eth_account import Account

    # You can customize this to a supported network or your own RPC URL
    network = "mumbai"

    # This will create a random account to use for signing transactions
    signer = Account.create()

    sdk = ThirdwebSDK(network, signer)
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

        return self.mint_to(
            self._contract_wrapper.get_signer_address(), metadata_with_supply
        )

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

        uri = upload_or_extract_uri(metadata_with_supply.metadata, self._storage)
        receipt = self._contract_wrapper.send_transaction(
            "mint_to", [to, int(MAX_INT, 16), uri, metadata_with_supply.supply]
        )
        events = self._contract_wrapper.get_events("TokensMinted", receipt)

        if len(events) == 0:
            raise Exception("No TokensMinted event found")

        id = events[0].get("args").get("tokenIdMinted")  # type: ignore

        return TxResultWithId(receipt, id=id, data=lambda: self.get(id))

    def mint_additional_supply(
        self, token_id: int, additional_supply: int
    ) -> TxResultWithId[EditionMetadata]:
        """
        Mint additional supply of a token to the connected wallet

        :param token_id: token ID to mint additional supply of
        :param additional_supply: additional supply to mint
        :returns: receipt, id, and metadata of the mint
        """

        return self.mint_additional_supply_to(
            self._contract_wrapper.get_signer_address(), token_id, additional_supply
        )

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

        metadata = self._get_token_metadata(token_id)
        receipt = self._contract_wrapper.send_transaction(
            "mint_to", [to, token_id, metadata.uri, additional_supply]
        )
        return TxResultWithId(receipt, id=token_id, data=lambda: self.get(token_id))

    def mint_batch(
        self, metadatas_with_supply: List[EditionMetadataInput]
    ) -> List[TxResultWithId[EditionMetadata]]:
        """
        Mint a batch of NFTs to the connected wallet

        :param metadatas_with_supply: list of EditionMetadataInput for the NFTs to mint
        :returns: receipts, ids, and metadatas of the mint
        """

        return self.mint_batch_to(
            self._contract_wrapper.get_signer_address(), metadatas_with_supply
        )

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
        txs = contract.mint_to("{{wallet_address}}", metadata_with_supply)
        receipt = txs[0].receipt
        token_id = txs[0].id
        nft = txs[0].data()
        ```

        :param to: wallet address to mint the NFTs to
        :param metadatas_with_supply: list of EditionMetadataInput for the NFTs to mint
        :returns: receipts, ids, and metadatas of the mint
        """

        metadatas = [a.metadata for a in metadatas_with_supply]
        supplies = [a.supply for a in metadatas_with_supply]
        uris = upload_or_extract_uris(metadatas, self._storage)

        encoded = []
        interface = self._contract_wrapper.get_contract_interface()
        for index, uri in enumerate(uris):
            encoded.append(
                interface.encodeABI(
                    "mintTo", [to, int(MAX_INT, 16), uri, supplies[index]]
                )
            )

        receipt = self._contract_wrapper.multi_call(encoded)
        events = self._contract_wrapper.get_events("TokensMinted", receipt)

        if len(events) == 0 and len(events) < len(metadatas):
            raise Exception("No TokensMinted event found, minting failed")

        results = []
        for event in events:
            id = event.get("args").get("tokenIdMinted")  # type: ignore
            results.append(TxResultWithId(receipt, id=id, data=lambda: self.get(id)))

        return results
