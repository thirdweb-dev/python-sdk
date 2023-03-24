from typing import Generic, List, Union

from web3 import Web3
from thirdweb.abi.drop_erc1155 import DropERC1155
from thirdweb.abi.drop_erc721 import IDropAllowlistProof
from thirdweb.abi.token_erc1155 import TokenERC1155
from thirdweb.common.claim_conditions import prepare_claim
from thirdweb.common.error import NotFoundException
from thirdweb.common.nft import fetch_token_metadata, upload_or_extract_uri, upload_or_extract_uris
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.constants.role import Role, get_role_hash
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.drop_erc1155_claim_conditions import DropERC1155ClaimConditions
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from web3.constants import MAX_INT
from thirdweb.types.contract import TERC1155
from zero_ex.contract_wrappers.tx_params import TxParams
from thirdweb.types.contracts.claim_conditions import ClaimVerification
from thirdweb.types.nft import (
    EditionMetadata,
    EditionMetadataInput,
    EditionMetadataOwner,
    NFTMetadata,
    NFTMetadataInput,
    QueryAllParams,
)
from web3.eth import TxReceipt
from thirdweb.types.settings.metadata import EditionDropContractMetadata

from thirdweb.types.tx import TxResultWithId


class ERC1155(Generic[TERC1155], BaseContract[TERC1155]):
    _storage: IpfsStorage
    _token: ContractWrapper[TokenERC1155]
    _drop: ContractWrapper[DropERC1155]
    _metadata: ContractMetadata

    claim_conditions: DropERC1155ClaimConditions

    def __init__(
        self,
        contract_wrapper: ContractWrapper[TERC1155],
        storage: IpfsStorage,
    ):
        super().__init__(contract_wrapper)
        self._storage = storage

        address = contract_wrapper._contract_abi.contract_address
        provider = contract_wrapper.get_provider()
        signer = contract_wrapper.get_signer()
        options = contract_wrapper.get_options()

        token_abi = TokenERC1155(provider, address)
        self._token = ContractWrapper(
            token_abi,
            provider,
            signer,
            options
        )

        drop_abi = DropERC1155(provider, address)
        self._drop = ContractWrapper(
            drop_abi,
            provider,
            signer,
            options
        )

        self._metadata: ContractMetadata = ContractMetadata(
            self._drop, storage, EditionDropContractMetadata
        )
        self.claim_conditions = DropERC1155ClaimConditions(
            self._drop, self._metadata, self._storage
        )

    """
    READ FUNCTIONS
    """

    def get(self, token_id: int) -> EditionMetadata:
        """
        Get an NFT

        ```python
        nft = contract.erc1155.get(0)
        print(nft)
        ```

        :extension: ERC1155
        :param token_id: token ID to check the metadata for
        :return: Metadata for the token
        """

        try:
            supply = self._contract_wrapper._contract_abi.total_supply.call(token_id)
        except:
            supply = 0

        metadata = self._get_token_metadata(token_id)
        return EditionMetadata(metadata, supply)

    def get_all(
        self, query_params: QueryAllParams = QueryAllParams()
    ) -> List[EditionMetadata]:
        """
        Get all NFTs

        ```python
        metadatas = contract.erc1155.get_all()
        print(metadatas)
        ```

        :extension: ERC1155Enumerable
        :param query_params: optional QueryAllParams to define which tokens to get metadata for
        :return: list of metadata for all tokens
        """

        max_id = min(query_params.start + query_params.count, self.get_total_count())
        return [self.get(token_id) for token_id in range(query_params.start, max_id)]

    def get_total_count(self) -> int:
        """
        Get the total number of NFTs

        ```python
        total_count = contract.erc1155.get_total_count()
        print(total_count)
        ```

        :extension: ERC1155Enumerable
        :return: total number of tokens on the contract
        """

        return self._contract_wrapper._contract_abi.next_token_id_to_mint.call()

    def get_owned(self, address: str = "") -> List[EditionMetadataOwner]:
        """
        Get NFTs owned by a specific wallet

        ```python
        address = "{{wallet_address}}"
        owned = contract.erc1155.get_owned(address)
        print(owned)
        ```

        :extension: ERC1155Enumerable
        :param address: address to get the owned tokens for
        :return: list of metadata for all tokens owned by the address
        """

        owner = address if address else self._contract_wrapper.get_signer_address()
        max_id = self._contract_wrapper._contract_abi.next_token_id_to_mint.call()
        balances = self._contract_wrapper._contract_abi.balance_of_batch.call(
            [owner for i in range(max_id)],
            [id for id in range(max_id)],
        )

        metadatas = []
        for index, balance in enumerate(balances):
            metadata = self.get(index)
            metadatas.append(
                EditionMetadataOwner(metadata.metadata, metadata.supply, owner, balance)
            )

        return metadatas

    def total_supply(self, token_id: int) -> int:
        """
        Get the total number of NFTs

        ```python
        token_id = 0

        total_supply = contract.erc1155.total_supply(token_id)
        print(total_supply)
        ```

        :extension: ERC1155
        :return: total number of tokens on the contract
        """

        return self._contract_wrapper._contract_abi.total_supply.call(token_id)

    def balance(self, token_id: int) -> int:
        """
        Get NFT balance

        ```python
        token_id = 0

        balance = contract.erc1155.balance(token_id)
        print(balance)
        ```

        :extension: ERC1155
        :param token_id: token ID to check the balance for
        :return: balance of the token
        """

        return self.balance_of(self._contract_wrapper.get_signer_address(), token_id)

    def balance_of(self, address: str, token_id: int) -> int:
        """
        Get NFT balance of a specific wallet

        ```python
        address = "{{wallet_address}}"
        token_id = 0

        balance = contract.erc1155.balance_of(address, token_id)
        ```

        :extension: ERC1155
        :param address: address to check the balance for
        :param token_id: token ID to check the balance for
        :return: balance of the token
        """

        return self._contract_wrapper._contract_abi.balance_of.call(address, token_id)

    def is_transfer_restricted(self) -> bool:
        """
        Check if the contract is restricted so transfers can only be made by admins

        ```python
        is_restricted = contract.erc1155.is_transfer_restricted()
        print(is_restricted)
        ```

        :return: True if the contract is restricted, False otherwise
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

        is_approved = contract.erc1155.is_approved(address, operator)
        print(is_approved)
        ```

        :extension: ERC1155
        :param address: address whose assets to check the approval of
        :param operator: operator address to check the approval for
        :return: True if the operator is approved, False otherwise
        """

        return self._contract_wrapper._contract_abi.is_approved_for_all.call(
            address, operator
        )

    """
    WRITE FUNCTIONS
    """

    def transfer(
        self, to: str, token_id: int, amount: int, data: Union[bytes, str] = b"0"
    ) -> TxReceipt:
        """
        Transfer NFTs

        ```python
        to = "{{wallet_address}}"
        token_id = 0
        amount = 1

        receipt = contract.erc1155.transfer(to, token_id, amount)
        ```

        :extension: ERC1155
        :param to: wallet address to transfer the tokens to
        :param token_id: the specific token ID to transfer
        :param amount: the amount of tokens to transfer
        :returns: transaction receipt of the transfer
        """

        fr = self._contract_wrapper.get_signer_address()
        return self._contract_wrapper.send_transaction(
            "safe_transfer_from",
            [fr, to, token_id, amount, data],
        )

    def burn(self, token_id: int, amount: int) -> TxReceipt:
        """
        Burn NFTs

        ```python
        token_id = 0
        amount = 1

        receipt = contract.erc1155.burn(token_id, amount)
        ```

        :extension: ERC1155Burnable
        :param amount: amount of tokens to burn
        :returns: transaction receipt of the burn
        """

        account = self._contract_wrapper.get_signer_address()
        return self._contract_wrapper.send_transaction(
            "burn", [account, token_id, amount]
        )

    def set_approval_for_all(self, operator: str, approved: bool) -> TxReceipt:
        """
        Set approval for all NFTs

        ```python
        operator = "{{wallet_address}}"
        approved = true

        receipt = contract.erc1155.set_approval_for_all(operator, approved)
        ```

        :extension: ERC1155
        :param operator: operator address to set the approval for
        :param approved: True if the operator is approved, False otherwise
        """

        return self._contract_wrapper.send_transaction(
            "set_approval_for_all", [operator, approved]
        )

    def mint(
        self, metadata_with_supply: EditionMetadataInput
    ) -> TxResultWithId[EditionMetadata]:
        """
        Mint a new NFT

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
        tx = contract.erc1155.mint(metadata_with_supply)
        receipt = tx.receipt
        token_id = tx.id
        nft = tx.data()
        ```

        :extension: ERC1155Mintable
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
        Mint a new NFT to a specific wallet

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
        tx = contract.erc1155.mint_to("{{wallet_address}}", metadata_with_supply)
        receipt = tx.receipt
        token_id = tx.id
        nft = tx.data()
        ```

        :extension: ERC1155Mintable
        :param to: wallet address to mint the NFT to
        :param metadata_with_supply: EditionMetadataInput for the NFT to mint
        :returns: receipt, id, and metadata of the mint
        """

        uri = upload_or_extract_uri(metadata_with_supply.metadata, self._storage)
        receipt = self._token.send_transaction(
            "mint_to", [to, int(MAX_INT, 16), uri, metadata_with_supply.supply]
        )
        events = self._token.get_events("TransferSingle", receipt)

        if len(events) == 0:
            raise Exception("No TransferSingle event found")

        id = events[0].get("args").get("id")  # type: ignore

        return TxResultWithId(receipt, id=id, data=lambda: self.get(id))

    def mint_additional_supply(
        self, token_id: int, additional_supply: int
    ) -> TxResultWithId[EditionMetadata]:
        """
        Mint additional supply of an NFT

        ```python
        token_id = 0
        additional_supply = 1

        tx = contract.erc1155.mint_additional_supply(token_id, additional_supply)
        receipt = tx.receipt
        token_id = tx.id
        nft = tx.data()
        ```

        :extension: ERC1155Mintable
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
        Mint additional supply of an NFT to a specific wallet

        ```python
        to = "{{wallet_address}}"
        token_id = 0
        additional_supply = 1

        tx = contract.erc1155.mint_additional_supply_to(to, token_id, additional_supply)
        receipt = tx.receipt
        token_id = tx.id
        nft = tx.data()
        ```

        :extension: ERC1155Mintable
        :param to: wallet address to mint additional supply to
        :param token_id: token ID to mint additional supply of
        :param additional_supply: additional supply to mint
        :returns: receipt, id, and metadata of the mint
        """

        metadata = self._get_token_metadata(token_id)
        receipt = self._token.send_transaction(
            "mint_to", [to, token_id, metadata.uri, additional_supply]
        )
        return TxResultWithId(receipt, id=token_id, data=lambda: self.get(token_id))

    def mint_batch(
        self, metadatas_with_supply: List[EditionMetadataInput]
    ) -> List[TxResultWithId[EditionMetadata]]:
        """
        Mint many NFTs

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
        txs = contract.erc1155.mint_batch(metadatas_with_supply)
        receipt = txs[0].receipt
        token_id = txs[0].id
        nft = txs[0].data()
        ```

        :extension: ERC1155BatchMintable
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
        Mint many NFTs to a specific wallet

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
        txs = contract.erc1155.mint_batch_to("{{wallet_address}}", metadatas_with_supply)
        receipt = txs[0].receipt
        token_id = txs[0].id
        nft = txs[0].data()
        ```

        :extension: ERC1155BatchMintable
        :param to: wallet address to mint the NFTs to
        :param metadatas_with_supply: list of EditionMetadataInput for the NFTs to mint
        :returns: receipts, ids, and metadatas of the mint
        """

        metadatas = [a.metadata for a in metadatas_with_supply]
        supplies = [a.supply for a in metadatas_with_supply]
        uris = upload_or_extract_uris(metadatas, self._storage)

        encoded = []
        interface = self._token.get_contract_interface()
        for index, uri in enumerate(uris):
            encoded.append(
                interface.encodeABI(
                    "mintTo", [to, int(MAX_INT, 16), uri, supplies[index]]
                )
            )

        receipt = self._token.multi_call(encoded)
        events = self._token.get_events("TokensMinted", receipt)

        if len(events) == 0 and len(events) < len(metadatas):
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

        txs = contract.erc1155.create_batch(metadata_with_supply)
        first_token_id = txs[0].id
        first_nft = txs[0].data()
        ```

        :extension: ERC1155LazyMintableV2
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
        token_id: int,
        quantity: int,
    ) -> TxReceipt:
        """
        Claim NFTs to a specific wallet

        ```python
        address = {{wallet_address}}
        token_id = 0
        quantity = 1

        tx = contract.erc1155.claim_to(address, token_id, quantity)
        receipt = tx.receipt
        claimed_token_id = tx.id
        claimed_nft = tx.data()
        ```

        :extension: ERC1155ClaimCustom | ERC1155ClaimPhasesV2 | ERC1155ClaimConditionsV2
        :param destination_address: Destination address to claim to.
        :param token_id: token ID of the token to claim.
        :param quantity: Number of NFTs to claim.
        :param proofs: List of merkle proofs.
        :return: tx receipt of the claim
        """

        claim_verification = self._prepare_claim(token_id, quantity)
        overrides: TxParams = TxParams(value=claim_verification.value)

        proof = IDropAllowlistProof(
            proof=claim_verification.proofs,
            quantityLimitPerWallet=claim_verification.max_claimable,
            pricePerToken=claim_verification.price_in_proof,
            currency=claim_verification.currency_address_in_proof
        )

        return self._drop.send_transaction(
            "claim",
            [
                destination_address,
                token_id,
                quantity,
                claim_verification.currency_address,
                claim_verification.price,
                proof,
                "",
            ],
            overrides
        )

    def claim(
        self,
        token_id: int,
        quantity: int,
    ) -> TxReceipt:
        """
        Claim NFTs

        ```python
        token_id = 0
        quantity = 1

        tx = contract.erc1155.claim(token_id, quantity)
        receipt = tx.receipt
        claimed_token_id = tx.id
        claimed_nft = tx.data()
        ```

        :extension: ERC1155ClaimCustom | ERC1155ClaimPhasesV2 | ERC1155ClaimConditionsV2
        :param quantity: Number of NFTs to claim.
        :param token_id: token ID of the token to claim.
        :param proofs: List of merkle proofs.
        :return: tx receipt of the claim
        """
        return self.claim_to(
            self._contract_wrapper.get_signer_address(),
            token_id,
            quantity,
        )

    """
    INTERNAL FUNCTIONS
    """

    def _get_token_metadata(self, token_id: int) -> NFTMetadata:
        token_uri = self._token._contract_abi.uri.call(token_id)

        if not token_uri:
            raise NotFoundException(str(token_id))

        return fetch_token_metadata(token_id, token_uri, self._storage)

    def _prepare_claim(
        self,
        token_id: int,
        quantity: int,
    ) -> ClaimVerification:
        address_to_claim = self._drop.get_signer_address()
        active = self.claim_conditions.get_active(token_id)
        merkle_metadata = self._metadata.get().merkle

        return prepare_claim(
            address_to_claim,
            quantity,
            active,
            merkle_metadata,
            self._drop,
            self._storage,
        )
