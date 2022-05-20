from typing import Final, List, Optional
from thirdweb.abi import DropERC721
from thirdweb.common.claim_conditions import prepare_claim
from thirdweb.constants.addresses import DEFAULT_MERKLE_ROOT
from thirdweb.constants.role import Role
from thirdweb.core.classes.contract_events import ContractEvents
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_platform_fee import ContractPlatformFee
from thirdweb.core.classes.contract_roles import ContractRoles
from thirdweb.core.classes.contract_royalty import ContractRoyalty
from thirdweb.core.classes.contract_sales import ContractPrimarySale
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.drop_claim_conditions import DropClaimConditions
from thirdweb.core.classes.erc_721 import ERC721
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import ContractType
from thirdweb.types.contracts.claim_conditions import ClaimVerification
from thirdweb.types.nft import (
    NFTMetadata,
    NFTMetadataInput,
    NFTMetadataOwner,
    QueryAllParams,
)
from thirdweb.types.sdk import SDKOptions
from thirdweb.types.settings.metadata import NFTDropContractMetadata
from eth_account.account import LocalAccount
from web3 import Web3

from thirdweb.types.tx import TxResultWithId


class NFTDrop(ERC721[DropERC721]):
    """
    Setup a collection of one-of-one NFTs that are minted as users claim them.

    ```python
    from thirdweb import ThirdwebSDK
    from eth_account import Account

    # You can customize this to a supported network or your own RPC URL
    network = "mumbai"

    # This will create a random account to use for signing transactions
    signer = Account.create()

    sdk = ThirdwebSDK(network, signer)
    contract = sdk.get_nft_drop("{{contract_address}}")
    ```
    """

    _abi_type = DropERC721

    contract_type: Final[ContractType] = ContractType.NFT_DROP
    contract_roles: Final[List[Role]] = [Role.ADMIN, Role.MINTER, Role.TRANSFER]

    metadata: ContractMetadata[DropERC721, NFTDropContractMetadata]
    roles: ContractRoles
    primary_sale: ContractPrimarySale[DropERC721]
    platform_fee: ContractPlatformFee[DropERC721]
    royalty: ContractRoyalty[DropERC721]
    claim_conditions: DropClaimConditions
    events: ContractEvents[DropERC721]

    def __init__(
        self,
        provider: Web3,
        address: str,
        storage: IpfsStorage,
        signer: Optional[LocalAccount] = None,
        options: SDKOptions = SDKOptions(),
    ):
        abi = DropERC721(provider, address)
        contract_wrapper = ContractWrapper(abi, provider, signer, options)
        super().__init__(contract_wrapper, storage)

        self.metadata = ContractMetadata(
            contract_wrapper, storage, NFTDropContractMetadata
        )
        self.roles = ContractRoles(contract_wrapper, self.contract_roles)
        self.primary_sale = ContractPrimarySale(contract_wrapper)
        self.platform_fee = ContractPlatformFee(contract_wrapper)
        self.royalty = ContractRoyalty(contract_wrapper, self.metadata)
        self.claim_conditions = DropClaimConditions(
            self._contract_wrapper, self.metadata, self._storage
        )
        self.events = ContractEvents(contract_wrapper)

    def get_all_claimed(
        self, query_params: QueryAllParams = QueryAllParams()
    ) -> List[NFTMetadataOwner]:
        """
        Get all claimed NFTs.

        ```python
        claimed_nfts = contract.get_all_claimed()
        first_owner = claimed_nfts[0].owner
        ```

        :param query_params: Query parameters.
        :return: List of nft metadatas and owners for claimed nfts.
        """

        max_id = min(
            self._contract_wrapper._contract_abi.next_token_id_to_claim.call(),
            query_params.start + query_params.count,
        )

        return [self.get(token_id) for token_id in range(query_params.start, max_id)]

    def get_all_unclaimed(
        self, query_params: QueryAllParams = QueryAllParams()
    ) -> List[NFTMetadata]:
        """
        Get all unclaimed NFTs.

        ```python
        unclaimed_nfts = contract.get_all_unclaimed()
        first_nft_name = unclaimed_nfts[0].name
        ```

        :param query_params: Query parameters.
        :return: List of nft metadatas.
        """

        max_id = min(
            self._contract_wrapper._contract_abi.next_token_id_to_mint.call(),
            query_params.start + query_params.count,
        )
        unminted_id = self._contract_wrapper._contract_abi.next_token_id_to_claim.call()

        return [
            self._get_token_metadata(unminted_id + i)
            for i in range(max_id - unminted_id)
        ]

    def total_claimed_supply(self) -> int:
        """
        Get the total number of NFTs claimed from this contract

        ```python
        total_claimed = contract.total_claimed_supply()
        ```

        :return: Total number of NFTs claimed from this contract
        """
        return self._contract_wrapper._contract_abi.next_token_id_to_claim.call()

    def total_unclaimed_supply(self) -> int:
        """
        Get the total number of unclaimed NFTs in this contract

        ```python
        total_unclaimed = contract.total_unclaimed_supply()
        ```

        :return: Total number of unclaimed NFTs in this contract
        """
        return (
            self._contract_wrapper._contract_abi.next_token_id_to_mint.call()
            - self.total_claimed_supply()
        )

    def create_batch(
        self, metadatas: List[NFTMetadataInput]
    ) -> List[TxResultWithId[NFTMetadata]]:
        """
        Create a batch of NFTs.

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

        txs = contract.create_batch(metadatas)
        first_token_id = txs[0].id
        first_nft = txs[0].data()
        ```


        :param metadatas: List of NFT metadata inputs.
        :return: List of tx results with ids for created NFTs.
        """

        start_file_number = (
            self._contract_wrapper._contract_abi.next_token_id_to_mint.call()
        )
        batch = self._storage.upload_metadata_batch(
            [metadata.to_json() for metadata in metadatas],
            start_file_number,
            self._contract_wrapper._contract_abi.contract_address,
            self._contract_wrapper.get_signer_address(),
        )
        base_uri = batch.base_uri

        receipt = self._contract_wrapper.send_transaction(
            "lazy_mint",
            [
                len(batch.metadata_uris),
                base_uri if base_uri.endswith("/") else base_uri + "/",
                Web3.toBytes(text=""),
            ],
        )

        events = self._contract_wrapper.get_events("TokensLazyMinted", receipt)
        start_index = events[0].get("args").get("startTokenId")  # type: ignore
        ending_index = events[0].get("args").get("endTokenId")  # type: ignore
        results = []

        for id in range(start_index, ending_index + 1):
            results.append(
                TxResultWithId(
                    receipt,
                    id=id,
                    data=lambda: self._get_token_metadata(id),
                )
            )

        return results

    def claim_to(
        self,
        destination_address: str,
        quantity: int,
        proofs: List[str] = [DEFAULT_MERKLE_ROOT],
    ) -> List[TxResultWithId[NFTMetadata]]:
        """
        Claim NFTs to a destination address.

        ```python
        address = {{wallet_address}}
        quantity = 1

        tx = contract.claim_to(address, quantity)
        receipt = tx.receipt
        claimed_token_id = tx.id
        claimed_nft = tx.data()
        ```

        :param destination_address: Destination address to claim to.
        :param quantity: Number of NFTs to claim.
        :param proofs: List of merkle proofs.
        :return: List of tx results with ids for claimed NFTs.
        """

        # TODO: OVERRIDES
        claim_verification = self._prepare_claim(quantity, proofs)
        receipt = self._contract_wrapper.send_transaction(
            "claim",
            [
                destination_address,
                quantity,
                claim_verification.currency_address,
                claim_verification.price,
                claim_verification.proofs,
                claim_verification.max_quantity_per_transaction,
            ],
        )

        events = self._contract_wrapper.get_events("TokensClaimed", receipt)
        start_index = events[0].get("args").get("startTokenId")  # type: ignore
        ending_index = start_index + quantity

        results = []
        for id in range(start_index, ending_index + 1):
            results.append(
                TxResultWithId(
                    receipt,
                    id=id,
                    data=lambda: self._get_token_metadata(id),
                )
            )

        return results

    def claim(
        self,
        quantity: int,
        proofs: List[str] = [DEFAULT_MERKLE_ROOT],
    ) -> List[TxResultWithId[NFTMetadata]]:
        """
        Claim NFTs.

        :param quantity: Number of NFTs to claim.
        :param proofs: List of merkle proofs.
        :return: List of tx results with ids for claimed NFTs.
        """
        return self.claim_to(
            self._contract_wrapper.get_signer_address(),
            quantity,
            proofs,
        )

    """
    INTERNAL FUNCTIONS
    """

    def _prepare_claim(
        self,
        quantity: int,
        proofs: List[str] = [DEFAULT_MERKLE_ROOT],
    ) -> ClaimVerification:
        return prepare_claim(
            quantity,
            self.claim_conditions.get_active(),
            self.metadata.get().merkle,
            self._contract_wrapper,
            self._storage,
            proofs,
        )
