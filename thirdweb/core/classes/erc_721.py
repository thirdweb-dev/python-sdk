from typing import Generic, List, Union

from web3 import Web3
from thirdweb.abi.drop_erc721 import DropERC721, IDropAllowlistProof
from thirdweb.abi.token_erc721 import TokenERC721
from thirdweb.common.claim_conditions import prepare_claim
from thirdweb.common.error import NotFoundException
from thirdweb.common.nft import fetch_token_metadata, upload_or_extract_uri, upload_or_extract_uris
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.constants.role import Role, get_role_hash
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.drop_claim_conditions import DropClaimConditions
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import TERC721
from zero_ex.contract_wrappers.tx_params import TxParams
from thirdweb.types.contracts.claim_conditions import ClaimVerification
from thirdweb.types.nft import NFTMetadata, NFTMetadataInput, NFTMetadataOwner, QueryAllParams
from web3.eth import TxReceipt
from thirdweb.types.settings.metadata import NFTDropContractMetadata

from thirdweb.types.tx import TxResultWithId


class ERC721(Generic[TERC721], BaseContract[TERC721]):
    _storage: IpfsStorage
    _token: ContractWrapper[TokenERC721]
    _drop: ContractWrapper[DropERC721]
    _metadata: ContractMetadata

    claim_conditions: DropClaimConditions

    def __init__(self, contract_wrapper: ContractWrapper[TERC721], storage: IpfsStorage):
        super().__init__(contract_wrapper)
        self._storage = storage

        address = contract_wrapper._contract_abi.contract_address
        provider = contract_wrapper.get_provider()
        signer = contract_wrapper.get_signer()
        options = contract_wrapper.get_options()

        token_abi = TokenERC721(provider, address)
        self._token = ContractWrapper(
            token_abi,
            provider,
            signer,
            options
        )

        drop_abi = DropERC721(provider, address)
        self._drop = ContractWrapper(
            drop_abi,
            provider,
            signer,
            options
        )

        self._metadata: ContractMetadata = ContractMetadata(
            self._drop, storage, NFTDropContractMetadata
        )
        self.claim_conditions = DropClaimConditions(
            self._drop, self._metadata, self._storage
        )

    """
    READ FUNCTIONS
    """

    def get(self, token_id: int) -> NFTMetadataOwner:
        """
        Get a single NFT

        ```python
        nft = contract.erc721.get(0)
        print(nft)
        ```

        :extension: ERC721
        :param token_id: token ID of the token to get the metadata for
        :return: the metadata for the token and its owner
        """

        try:
            owner = self.owner_of(token_id)
        except:
            owner = ZERO_ADDRESS

        metadata = self._get_token_metadata(token_id)
        return NFTMetadataOwner(metadata, owner)

    def get_all(
        self, query_params: QueryAllParams = QueryAllParams()
    ) -> List[NFTMetadataOwner]:
        """
        Get all NFTs

        ```python
        nfts = contract.erc721.get_all()
        print(nfts)
        ```

        :extension: ERC721Supply | ERC721Enumerable
        :param query_params: optionally define a QueryAllParams instance to narrow the metadata query to specific tokens
        :return: the metadata of all tokens in the contract
        """

        max_id = min(query_params.start + query_params.count, self.get_total_count())

        nfts = []
        for token_id in range(query_params.start, max_id):
            try:
                nft = self.get(token_id)
                nfts.append(nft)
            except:
                pass

        return nfts
    
    def get_all_claimed(
        self, query_params: QueryAllParams = QueryAllParams()
    ) -> List[NFTMetadataOwner]:
        """
        Get all claimed NFTs

        ```python
        claimed_nfts = contract.erc721.get_all_claimed()
        first_owner = claimed_nfts[0].owner
        ```

        :param query_params: Query parameters.
        :return: List of nft metadatas and owners for claimed nfts.
        """

        max_id = min(
            self._drop._contract_abi.next_token_id_to_claim.call(),
            query_params.start + query_params.count,
        )

        return [self.get(token_id) for token_id in range(query_params.start, max_id)]

    def get_all_unclaimed(
        self, query_params: QueryAllParams = QueryAllParams()
    ) -> List[NFTMetadata]:
        """
        Get all unclaimed NFTs

        ```python
        unclaimed_nfts = contract.erc721.get_all_unclaimed()
        first_nft_name = unclaimed_nfts[0].name
        ```

        :param query_params: Query parameters.
        :return: List of nft metadatas.
        """

        max_id = min(
            self._drop._contract_abi.next_token_id_to_mint.call(),
            query_params.start + query_params.count,
        )
        unminted_id = self._drop._contract_abi.next_token_id_to_claim.call()

        return [
            self._get_token_metadata(unminted_id + i)
            for i in range(max_id - unminted_id)
        ]

    def total_claimed_supply(self) -> int:
        """
        Get the number of claimed NFTs

        ```python
        total_claimed = contract.erc721.total_claimed_supply()
        print(total_claimed)
        ```

        :extension: ERC721ClaimCustom | ERC721ClaimPhasesV2 | ERC721ClaimConditionsV2
        :return: Total number of NFTs claimed from this contract
        """
        return self._drop._contract_abi.next_token_id_to_claim.call()

    def total_unclaimed_supply(self) -> int:
        """
        Get the number of unclaimed NFTs

        ```python
        total_unclaimed = contract.erc721.total_unclaimed_supply()
        print(total_unclaimed)
        ```

        :extension: ERC721ClaimCustom | ERC721ClaimPhasesV2 | ERC721ClaimConditionsV2
        :return: Total number of unclaimed NFTs in this contract
        """
        return (
            self._drop._contract_abi.next_token_id_to_mint.call()
            - self.total_claimed_supply()
        )

    def get_total_count(self) -> int:
        """
        Get the total number of NFTs

        ```python
        total_count = contract.erc721.get_total_count()
        print(total_count)
        ```

        :extension: ERC721ClaimCustom | ERC721ClaimPhasesV2 | ERC721ClaimConditionsV2
        :return: the total number of NFTs minted by this contract
        """

        return self._contract_wrapper._contract_abi.next_token_id_to_mint.call()

    def owner_of(self, token_id: int) -> str:
        """
        Get the owner of an NFT

        ```python
        token_id = 0

        owner = contract.erc721.owner_of(token_id)
        print(owner)
        ```

        :extension: ERC721
        :param token_id: the token ID of the token to get the owner of
        :return: the owner of the token
        """
        return self._contract_wrapper._contract_abi.owner_of.call(token_id)

    def total_supply(
        self,
    ) -> int:
        """
        Get the total number of NFTs

        ```python
        total_supply = contract.erc721.total_supply()
        print(total_supply)
        ```

        :extension: ERC721ClaimCustom | ERC721ClaimPhasesV2 | ERC721ClaimConditionsV2
        :return: the total number of tokens in the contract
        """
        return self._contract_wrapper._contract_abi.next_token_id_to_mint.call()

    def balance(
        self,
    ) -> int:
        """
        Get NFT balance

        ```python
        balance = contract.erc721.balance()
        print(balance)
        ```

        :extension: ERC721
        :return: the token balance of the connected wallet
        """

        return self.balance_of(self._contract_wrapper.get_signer_address())

    def balance_of(self, address: str) -> int:
        """
        Get NFT balance of a specific wallet

        ```python
        balance = contract.erc721.balance_of("{{wallet_address}}")
        print(balance)
        ```

        :extension: ERC721
        :param address: the address to get the token balance of
        """

        return self._contract_wrapper._contract_abi.balance_of.call(address)

    def is_transfer_restricted(
        self,
    ) -> bool:
        """
        Check if the contract is restricted to transfers only by admins

        ```python
        is_restricted = contract.erc721.is_transfer_restricted()
        print(is_restricted)
        ```

        :return: True if the contract is restricted to transfers only by admins, False otherwise
        """

        anyone_can_transfer = self._contract_wrapper._contract_abi.has_role.call(
            get_role_hash(Role.TRANSFER), ZERO_ADDRESS
        )

        return not anyone_can_transfer

    def is_approved(self, address: str, operator: str) -> bool:
        """
        Check approval of a specific wallet

        ```python
        address = "{{wallet_address}}"
        operator = "0x..."

        is_approved = contract.erc721.is_approved(address, operator)
        print(is_approved)
        ```

        :extension: ERC721
        :param address: the address whose assets are to be checked
        :param operator: the address of the operator to check
        :return: True if the operator is approved for all operations of the assets, False otherwise
        """

        return self._contract_wrapper._contract_abi.is_approved_for_all.call(
            address, operator
        )

    """
    WRITE FUNCTIONS
    """

    def transfer(self, to: str, token_id: int) -> TxReceipt:
        """
        Transfer an NFT

        ```python
        to = "{{wallet_address}}"
        token_id = 0

        receipt = contract.erc721.transfer(to, token_id)
        ```

        :extension: ERC721
        :param to: wallet address to transfer the tokens to
        :param token_id: the specific token ID to transfer
        :returns: transaction receipt of the transfer
        """

        fr = self._contract_wrapper.get_signer_address()
        return self._contract_wrapper.send_transaction(
            "safe_transfer_from1", [fr, to, token_id]
        )

    def burn(self, token_id: int) -> TxReceipt:
        """
        Burn an NFT

        ```python
        token_id = 0 

        receipt = contract.erc721.burn(token_id)
        ```

        :extension: ERC721Burnable
        :param token_id: token ID of the token to burn
        :returns: transaction receipt of the burn
        """

        return self._contract_wrapper.send_transaction("burn", [token_id])

    def set_approval_for_all(self, operator: str, approved: bool) -> TxReceipt:
        """
        Set approval for all NFTs

        ```python
        operator = "{{wallet_address}}"
        approved = true

        receipt = contract.erc721.set_approval_for_all(operator, approved)
        ```

        :extension: ERC721
        :param operator: the address of the operator to set the approval for
        :param approved: the address whos assets the operator is approved to manage
        :returns: transaction receipt of the approval
        """

        return self._contract_wrapper.send_transaction(
            "set_approval_for_all", [operator, approved]
        )

    def set_approval_for_token(self, operator: str, token_id: int) -> TxReceipt:
        """
        Set approval for a specific NFT

        ```python
        operator = "{{wallet_address}}"
        token_id = 0

        receipt = contract.erc721.set_approval_for_token(operator, token_id)
        ```

        :param operator: the address of the operator to set the approval for
        :param token_id: the specific token ID to set the approval for
        :returns: transaction receipt of the approval
        """
        return self._contract_wrapper.send_transaction("approve", [operator, token_id])

    def mint(
        self, metadata: Union[NFTMetadataInput, str]
    ) -> TxResultWithId[NFTMetadataOwner]:
        """
        Mint an NFT

        ```python
        from thirdweb.types.nft import NFTMetadataInput

        # You can customize the metadata to your needs
        metadata = NFTMetadataInput.from_json({
            "name": "Cool NFT",
            "description": "This is a cool NFT",
            "image": open("path/to/file.jpg", "rb")
        })

        tx = contract.erc721.mint(metadata)
        receipt = tx.receipt
        token_id = tx.id
        nft = tx.data()
        ```

        :extension: ERC721Mintable
        :param metadata: metadata of the NFT to mint
        :returns: receipt, id, and metadata for the mint
        """

        return self.mint_to(self._contract_wrapper.get_signer_address(), metadata)

    def mint_to(
        self, to: str, metadata: Union[NFTMetadataInput, str]
    ) -> TxResultWithId[NFTMetadataOwner]:
        """
        Mint an NFT to a specific wallet

        ```python
        from thirdweb.types.nft import NFTMetadataInput

        # Note that you can customize this metadata however you like
        metadata = NFTMetadataInput.from_json({
            "name": "Cool NFT",
            "description": "This is a cool NFT",
            "image": open("path/to/file.jpg", "rb"),
        })

        # You can pass in any address here to mint the NFT to
        tx = contract.erc721.mint_to("{{wallet_address}}", metadata)
        receipt = tx.receipt
        token_id = tx.id
        nft = tx.data()
        ```

        :extension: ERC721Mintable
        :param to: wallet address to mint the NFT to
        :param metadata: metadata of the NFT to mint
        :returns: receipt, id, and metadata for the mint
        """

        uri = upload_or_extract_uri(metadata, self._storage)
        receipt = self._token.send_transaction("mint_to", [to, uri])
        events = self._token.get_events("Transfer", receipt)

        if len(events) == 0:
            raise Exception("No Transfer event found")

        id = events[0].get("args").get("tokenId")  # type: ignore

        return TxResultWithId(receipt, id=id, data=lambda: self.get(id))

    def mint_batch(
        self, metadatas: List[Union[NFTMetadataInput, str]]
    ) -> List[TxResultWithId[NFTMetadataOwner]]:
        """
        Mint many NFTs

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
        txs = contract.erc721.mint_batch(metadatas)
        receipt = txs[0].receipt
        first_token_id = txs[0].id
        first_nft = txs[0].data()
        ```

        :extension: ERC721BatchMintable
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
        Mint many NFTs to a specific wallet

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
        txs = contract.erc721.mint_batch_to("{{wallet_address}}", metadatas)
        receipt = txs[0].receipt
        first_token_id = txs[0].id
        first_nft = txs[0].data()
        ```

        :extension: ERC721BatchMintable
        :param to: wallet address to mint the NFTs to
        :param metadatas: list of metadata of the NFTs to mint
        :returns: receipts, ids, and metadatas for each mint
        """

        uris = upload_or_extract_uris(metadatas, self._storage)

        encoded = []
        interface = self._token.get_contract_interface()
        for uri in uris:
            encoded.append(interface.encodeABI("mintTo", [to, uri]))

        receipt = self._token.multi_call(encoded)
        events = self._token.get_events("TokensMinted", receipt)

        if len(events) == 0 or len(events) < len(metadatas):
            raise Exception("No TokensMinted event found, minting failed")

        results = []
        for event in events:
            id = event.get("args").get("tokenIdMinted")  # type: ignore
            results.append(TxResultWithId(receipt, id=id, data=lambda: self.get(id)))

        return results

    def create_batch(
        self, metadatas: List[NFTMetadataInput]
    ) -> List[TxResultWithId[NFTMetadata]]:
        """
        Lazy mint NFTs

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

        txs = contract.erc721.create_batch(metadatas)
        first_token_id = txs[0].id
        first_nft = txs[0].data()
        ```

        :extension: ERC721LazyMintable
        :param metadatas: List of NFT metadata inputs.
        :return: List of tx results with ids for created NFTs.
        """

        start_file_number = (
            self._drop._contract_abi.next_token_id_to_mint.call()
        )
        batch = self._storage.upload_metadata_batch(
            [metadata.to_json() for metadata in metadatas],
            start_file_number,
            self._drop._contract_abi.contract_address,
            self._drop.get_signer_address(),
        )
        base_uri = batch.base_uri

        receipt = self._drop.send_transaction(
            "lazy_mint",
            [
                len(batch.metadata_uris),
                base_uri if base_uri.endswith("/") else base_uri + "/",
                Web3.toBytes(text=""),
            ],
        )

        events = self._drop.get_events("TokensLazyMinted", receipt)
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
    ) -> List[TxResultWithId[NFTMetadata]]:
        """
        Claim NFTs to a specific wallet

        ```python
        address = {{wallet_address}}
        quantity = 1

        tx = contract.erc721.claim_to(address, quantity)
        receipt = tx.receipt
        claimed_token_id = tx.id
        claimed_nft = tx.data()
        ```

        :extension: ERC721ClaimCustom | ERC721ClaimPhasesV2 | ERC721ClaimConditionsV2
        :param destination_address: Destination address to claim to.
        :param quantity: Number of NFTs to claim.
        :param proofs: List of merkle proofs.
        :return: List of tx results with ids for claimed NFTs.
        """

        # TODO: OVERRIDES
        claim_verification = self._prepare_claim(quantity)
        overrides: TxParams = TxParams(value=claim_verification.value)

        proof = IDropAllowlistProof(
            proof=claim_verification.proofs,
            quantityLimitPerWallet=claim_verification.max_claimable,
            pricePerToken=claim_verification.price_in_proof,
            currency=claim_verification.currency_address_in_proof
        )

        receipt = self._drop.send_transaction(
            "claim",
            [
                destination_address,
                quantity,
                claim_verification.currency_address,
                claim_verification.price,
                proof,
                "",
            ],
            overrides
        )

        events = self._drop.get_events("TokensClaimed", receipt)
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
    ) -> List[TxResultWithId[NFTMetadata]]:
        """
        Claim NFTs

        ```python
        quantity = 1

        tx = contract.erc721.claim(quantity)
        receipt = tx.receipt
        claimed_token_id = tx.id
        claimed_nft = tx.data()
        ```

        :extension: ERC721ClaimCustom | ERC721ClaimPhasesV2 | ERC721ClaimConditionsV2
        :param quantity: Number of NFTs to claim.
        :param proofs: List of merkle proofs.
        :return: List of tx results with ids for claimed NFTs.
        """
        return self.claim_to(
            self._contract_wrapper.get_signer_address(),
            quantity,
        )

    """
    INTERNAL FUNCTIONS
    """

    def _get_token_metadata(self, token_id: int) -> NFTMetadata:
        token_uri = self._contract_wrapper._contract_abi.token_uri.call(token_id)

        if not token_uri:
            raise NotFoundException(str(token_id))

        return fetch_token_metadata(token_id, token_uri, self._storage)
    
    def _prepare_claim(
        self,
        quantity: int,
    ) -> ClaimVerification:
        address_to_claim = self._drop.get_signer_address()
        active = self.claim_conditions.get_active()
        merkle_metadata = self._metadata.get().merkle

        return prepare_claim(
            address_to_claim,
            quantity,
            active,
            merkle_metadata,
            self._drop,
            self._storage,
        )
