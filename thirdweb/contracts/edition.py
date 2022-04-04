from thirdweb.common.nft import upload_or_extract_uri, upload_or_extract_uris
from thirdweb.constants.role import Role
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_platform_fee import ContractPlatformFee
from thirdweb.core.classes.contract_roles import ContractRoles
from thirdweb.core.classes.contract_royalty import ContractRoyalty
from thirdweb.core.classes.contract_sales import ContractPrimarySale
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.erc_1155 import ERC1155
from thirdweb.abi import TokenERC1155

from eth_account.account import LocalAccount
from web3.constants import MAX_INT
from web3.eth import TxReceipt
from web3 import Web3
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import ContractType

from thirdweb.types.nft import EditionMetadataInput
from thirdweb.types.sdk import SDKOptions
from typing import Final, Optional, List

from thirdweb.types.settings.metadata import EditionContractMetadata


class Edition(ERC1155):
    _abi_type = TokenERC1155

    contract_type: Final[ContractType] = ContractType.EDITION
    contract_roles: Final[List[Role]] = [Role.ADMIN, Role.MINTER, Role.TRANSFER]

    schema = EditionContractMetadata
    metadata: ContractMetadata[TokenERC1155, EditionContractMetadata]
    roles: ContractRoles
    primary_sale: ContractPrimarySale[TokenERC1155]
    platform_fee: ContractPlatformFee[TokenERC1155]
    royalty: ContractRoyalty[TokenERC1155]

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

        self.metadata = ContractMetadata(contract_wrapper, storage, self.schema)
        self.roles = ContractRoles(contract_wrapper, self.contract_roles)
        self.primary_sale = ContractPrimarySale(contract_wrapper)
        self.platform_fee = ContractPlatformFee(contract_wrapper)
        self.royalty = ContractRoyalty(contract_wrapper, self.metadata)

    def mint(self, metadata_with_supply: EditionMetadataInput) -> TxReceipt:
        """
        Mint a new NFT to the connected wallet

        :param metadata_with_supply: EditionMetadataInput for the NFT to mint
        :returns: transaction receipt of the mint
        """

        return self.mint_to(
            self._contract_wrapper.get_signer_address(), metadata_with_supply
        )

    def mint_to(self, to: str, metadata_with_supply: EditionMetadataInput) -> TxReceipt:
        """
        Mint a new NFT to the specified wallet

        :param to: wallet address to mint the NFT to
        :param metadata_with_supply: EditionMetadataInput for the NFT to mint
        :returns: transaction receipt of the mint
        """

        uri = upload_or_extract_uri(metadata_with_supply.metadata, self._storage)
        return self._contract_wrapper.send_transaction(
            "mint_to", [to, int(MAX_INT, 16), uri, metadata_with_supply.supply]
        )

    def mint_additional_supply(
        self, token_id: int, additional_supply: int
    ) -> TxReceipt:
        """
        Mint additional supply of a token to the connected wallet

        :param token_id: token ID to mint additional supply of
        :param additional_supply: additional supply to mint
        :returns: transaction receipt of the mint
        """

        return self.mint_additional_supply_to(
            self._contract_wrapper.get_signer_address(), token_id, additional_supply
        )

    def mint_additional_supply_to(
        self, to: str, token_id: int, additional_supply: int
    ) -> TxReceipt:
        """
        Mint additional supply of a token to the specified wallet

        :param to: wallet address to mint additional supply to
        :param token_id: token ID to mint additional supply of
        :param additional_supply: additional supply to mint
        :returns: transaction receipt of the mint
        """

        metadata = self._get_token_metadata(token_id)
        return self._contract_wrapper.send_transaction(
            "mint_to", [to, token_id, metadata.uri, additional_supply]
        )

    def mint_batch(
        self, metadatas_with_supply: List[EditionMetadataInput]
    ) -> TxReceipt:
        """
        Mint a batch of NFTs to the connected wallet

        :param metadatas_with_supply: list of EditionMetadataInput for the NFTs to mint
        :returns: transaction receipt of the mint
        """

        return self.mint_batch_to(
            self._contract_wrapper.get_signer_address(), metadatas_with_supply
        )

    def mint_batch_to(
        self, to: str, metadatas_with_supply: List[EditionMetadataInput]
    ) -> TxReceipt:
        """
        Mint a batch of NFTs to the specified wallet

        :param to: wallet address to mint the NFTs to
        :param metadatas_with_supply: list of EditionMetadataInput for the NFTs to mint
        :returns: transaction receipt of the mint
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

        return self._contract_wrapper.multi_call(encoded)
