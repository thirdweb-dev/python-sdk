from typing import Any, Final, List, Optional

from web3 import Web3
from thirdweb.abi import DropERC1155
from thirdweb.constants.role import Role
from thirdweb.core.classes.contract_events import ContractEvents
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_platform_fee import ContractPlatformFee
from thirdweb.core.classes.contract_roles import ContractRoles
from thirdweb.core.classes.contract_royalty import ContractRoyalty
from thirdweb.core.classes.contract_sales import ContractPrimarySale
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.erc_1155_standard import ERC1155Standard
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import ContractType
from thirdweb.types.nft import NFTMetadata, NFTMetadataInput
from thirdweb.types.sdk import SDKOptions
from thirdweb.types.settings.metadata import EditionDropContractMetadata
from eth_account.account import LocalAccount
from thirdweb.core.classes.drop_erc1155_claim_conditions import (
    DropERC1155ClaimConditions,
)
from thirdweb.types.tx import TxResultWithId
from web3.eth import TxReceipt


class EditionDrop(ERC1155Standard[DropERC1155]):
    """
    Setup a collection of NFTs with a customizable number of each NFT that are minted as users claim them.

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

    contract = sdk.get_edition_drop("{{contract_address}}")
    ```
    """

    _abi_type = DropERC1155

    contract_type: Final[ContractType] = ContractType.EDITION_DROP
    contract_roles: Final[List[Role]] = [Role.ADMIN, Role.MINTER, Role.TRANSFER]

    metadata: ContractMetadata[DropERC1155, EditionDropContractMetadata]
    roles: ContractRoles
    primary_sale: ContractPrimarySale[DropERC1155]
    platform_fee: ContractPlatformFee[DropERC1155]
    royalty: ContractRoyalty[DropERC1155]
    claim_conditions: DropERC1155ClaimConditions
    events: ContractEvents[DropERC1155]

    def __init__(
        self,
        provider: Web3,
        address: str,
        storage: IpfsStorage,
        signer: Optional[LocalAccount] = None,
        options: SDKOptions = SDKOptions(),
    ):
        abi = DropERC1155(provider, address)
        contract_wrapper = ContractWrapper(abi, provider, signer, options)
        super().__init__(contract_wrapper, storage)

        self.metadata = ContractMetadata(
            contract_wrapper, storage, EditionDropContractMetadata
        )
        self.roles = ContractRoles(contract_wrapper, self.contract_roles)
        self.primary_sale = ContractPrimarySale(contract_wrapper)
        self.platform_fee = ContractPlatformFee(contract_wrapper)
        self.royalty = ContractRoyalty(contract_wrapper, self.metadata)
        self.claim_conditions = DropERC1155ClaimConditions(
            self._contract_wrapper, self.metadata, self._storage
        )
        self.events = ContractEvents(contract_wrapper)

    def create_batch(
        self, metadatas: List[NFTMetadataInput]
    ) -> List[TxResultWithId[NFTMetadata]]:
        """
        Create a batch of NFTs.

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

        txs = contract.create_batch(metadata_with_supply)
        first_token_id = txs[0].id
        first_nft = txs[0].data()
        ```

        :param metadatas: List of NFT metadata inputs.
        :return: List of tx results with ids for created NFTs.
        """

        return self._erc1155.create_batch(metadatas)

    def claim_to(
        self,
        destination_address: str,
        token_id: int,
        quantity: int,
    ) -> TxReceipt:
        """
        Claim NFTs to a destination address.

        ```python
        address = {{wallet_address}}
        token_id = 0
        quantity = 1

        tx = contract.claim_to(address, token_id, quantity)
        receipt = tx.receipt
        claimed_token_id = tx.id
        claimed_nft = tx.data()
        ```

        :param destination_address: Destination address to claim to.
        :param token_id: token ID of the token to claim.
        :param quantity: Number of NFTs to claim.
        :param proofs: List of merkle proofs.
        :return: tx receipt of the claim
        """

        return self._erc1155.claim_to(destination_address, token_id, quantity)

    def claim(
        self,
        token_id: int,
        quantity: int,
    ) -> TxReceipt:
        """
        Claim NFTs.

        :param quantity: Number of NFTs to claim.
        :param token_id: token ID of the token to claim.
        :param proofs: List of merkle proofs.
        :return: tx receipt of the claim
        """
        return self._erc1155.claim(token_id, quantity)

    def call(self, fn: str, *args) -> Any:
        return self._contract_wrapper.call(fn, *args)
