from typing import Any, Final, List, Optional
from thirdweb.abi import DropERC721
from thirdweb.abi.drop_erc721 import IDropAllowlistProof
from thirdweb.constants.role import Role
from thirdweb.core.classes.contract_events import ContractEvents
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_platform_fee import ContractPlatformFee
from thirdweb.core.classes.contract_roles import ContractRoles
from thirdweb.core.classes.contract_royalty import ContractRoyalty
from thirdweb.core.classes.contract_sales import ContractPrimarySale
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.drop_claim_conditions import DropClaimConditions
from thirdweb.core.classes.erc_721_standard import ERC721Standard
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import ContractType
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


class NFTDrop(ERC721Standard[DropERC721]):
    """
    Setup a collection of one-of-one NFTs that are minted as users claim them.

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

        total_count = self._contract_wrapper._contract_abi.next_token_id_to_mint.call()
        token_ids = []
        for i in range(total_count):
            if self._contract_wrapper._contract_abi.owner_of.call(i).lower() == owner.lower():
                token_ids.append(i)

        return token_ids

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

        return self._erc721.get_all_claimed(query_params)

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

        return self._erc721.get_all_unclaimed(query_params)

    def total_claimed_supply(self) -> int:
        """
        Get the total number of NFTs claimed from this contract

        ```python
        total_claimed = contract.total_claimed_supply()
        ```

        :return: Total number of NFTs claimed from this contract
        """
        return self._erc721.total_claimed_supply()

    def total_unclaimed_supply(self) -> int:
        """
        Get the total number of unclaimed NFTs in this contract

        ```python
        total_unclaimed = contract.total_unclaimed_supply()
        ```

        :return: Total number of unclaimed NFTs in this contract
        """
        return self._erc721.total_unclaimed_supply()

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

        return self._erc721.create_batch(metadatas)

    def claim_to(
        self,
        destination_address: str,
        quantity: int,
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

        return self._erc721.claim_to(destination_address, quantity)

    def claim(
        self,
        quantity: int,
    ) -> List[TxResultWithId[NFTMetadata]]:
        """
        Claim NFTs.

        :param quantity: Number of NFTs to claim.
        :param proofs: List of merkle proofs.
        :return: List of tx results with ids for claimed NFTs.
        """
        return self._erc721.claim(quantity)

    def call(self, fn: str, *args) -> Any:
        return self._contract_wrapper.call(fn, *args)