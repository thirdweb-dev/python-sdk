from typing import Final, List, Optional, Union

from web3 import Web3
from web3.eth import TxReceipt
from eth_account.account import LocalAccount
from thirdweb.abi.multiwrap import ITokenBundleToken
from thirdweb.common.marketplace import is_token_approved_for_transfer
from thirdweb.common.nft import upload_or_extract_uri
from thirdweb.constants.role import Role
from thirdweb.core.classes.contract_events import ContractEvents
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_roles import ContractRoles
from thirdweb.core.classes.contract_royalty import ContractRoyalty
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.erc_721 import ERC721
from thirdweb.abi import Multiwrap as MultiwrapABI
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.contract import ContractType
from thirdweb.types.nft import NFTMetadataInput, NFTMetadataOwner
from thirdweb.types.sdk import SDKOptions
from thirdweb.types.multiwrap import (
    ERC1155Wrappable,
    ERC20Wrappable,
    ERC721Wrappable,
    TokensToWrap,
    WrappedTokens,
)
from thirdweb.types.settings.metadata import MultiwrapContractMetadata
from thirdweb.common.currency import (
    fetch_currency_metadata,
    format_units,
    has_erc20_allowance,
    normalize_price_value,
)
from thirdweb.types.tx import TxResultWithId


class Multiwrap(ERC721[MultiwrapABI]):
    """
    Multiwrap lets you wrap any number of ERC20, ERC721, or ERC1155 tokens into
    a single wrapped token bundle.

    ```python
    from thirdweb import ThirdwebSDK

    # You can customize this to a supported network or your own RPC URL
    network = "mumbai"

    # Now we can create a new instance of the SDK
    sdk = ThirdwebSDK(network)

    # If you want to send transactions, you can instantiate the SDK with a private key instead:
    #   sdk = ThirdwebSDK.from_private_key(PRIVATE_KEY, network)

    contract = sdk.get_multiwrap("{{contract_address}}")
    ```
    """

    _abi_type = MultiwrapABI

    contract_type: Final[ContractType] = ContractType.MULTIWRAP
    contract_roles: Final[List[Role]] = [
        Role.ADMIN,
        Role.MINTER,
        Role.TRANSFER,
        Role.UNWRAP,
    ]

    metadata: ContractMetadata[MultiwrapABI, MultiwrapContractMetadata]
    roles: ContractRoles
    royalty: ContractRoyalty[MultiwrapABI]
    events: ContractEvents[MultiwrapABI]

    def __init__(
        self,
        provider: Web3,
        address: str,
        storage: IpfsStorage,
        signer: Optional[LocalAccount] = None,
        options: SDKOptions = SDKOptions(),
    ):
        abi = MultiwrapABI(provider, address)
        contract_wrapper = ContractWrapper(abi, provider, signer, options)
        super().__init__(contract_wrapper, storage)

        self.metadata = ContractMetadata(
            contract_wrapper,
            storage,
            MultiwrapContractMetadata,
        )
        self.roles = ContractRoles(contract_wrapper, self.contract_roles)
        self.royalty = ContractRoyalty(contract_wrapper, self.metadata)
        self.events = ContractEvents(contract_wrapper)

    """
    READ FUNCTIONS
    """

    def get_wrapped_contents(self, wrapped_token_id: int) -> WrappedTokens:
        """
        Get the contents of a wrapped token bundle

        :param wrapped_token_id: The ID of the wrapped token to get the contents of
        :returns: The contents of the wrapped token bundle

        ```python
        token_id = 0
        contents = contract.get_wrapped_contents(token_id)
        print(contents.erc20_tokens)
        print(contents.erc721_tokens)
        print(contents.erc1155_tokens)
        ```
        """
        wrapped_tokens = self._contract_wrapper._contract_abi.get_wrapped_contents.call(
            wrapped_token_id
        )

        erc20_tokens = []
        erc721_tokens = []
        erc1155_tokens = []

        for token in wrapped_tokens:
            if token["tokenType"] == 0:
                token_metadata = fetch_currency_metadata(
                    self._contract_wrapper.get_provider(), token["assetContract"]
                )
                erc20_tokens.append(
                    ERC20Wrappable(
                        token["assetContract"],
                        format_units(token["totalAmount"], token_metadata.decimals),
                    )
                )
                continue
            if token["tokenType"] == 1:
                erc721_tokens.append(
                    ERC721Wrappable(token["assetContract"], token["tokenId"])
                )
                continue
            if token["tokenType"] == 2:
                erc1155_tokens.append(
                    ERC1155Wrappable(
                        token["assetContract"], token["tokenId"], token["totalAmount"]
                    )
                )

        return WrappedTokens(erc20_tokens, erc721_tokens, erc1155_tokens)

    """
    WRITE FUNCTIONS
    """

    def wrap(
        self,
        contents: TokensToWrap,
        wrapped_token_metadata: Union[str, NFTMetadataInput],
        recipient_address: Optional[str] = None,
    ) -> TxResultWithId[NFTMetadataOwner]:
        """
        Wrap any number of ERC20, ERC721, or ERC1155 tokens into a single wrapped token

        :param contents: The tokens to wrap into a single wrapped token
        :param wrapped_token_metadata: The metadata to use for the wrapped token
        :param recipient_address: The optional address to send the wrapped token to
        :returns: The transaction receipt of the token wrapping

        ```python
        from thirdweb.types import (
            TokensToWrap,
            ERC20Wrappable,
            ERC721Wrappable,
            ERC1155Wrappable,
            NFTMetadataInput,
        )

        # Contract setup goes here...

        tx = contract.wrap(
            TokensToWrap(
                erc20_tokens=[
                    ERC20Wrappable(contract_address="0x...", quantity=0.8),
                ],
                erc721_tokens=[
                    ERC721Wrappable(contract_address="0x...", token_id=0),
                ],
                erc1155_tokens=[
                    ERC1155Wrappable(contract_address="0x...", token_id=0, quantity=1),
                ]
            ),
            NFTMetadataInput(
                name="Wrapped NFT",
                description="This is a wrapped bundle of tokens and NFTs",
                image="ipfs://...",
            )
        )

        print(tx.receipt, tx.id)
        ```
        """
        uri = upload_or_extract_uri(wrapped_token_metadata, self._storage)

        if recipient_address is None:
            recipient_address = self._contract_wrapper.get_signer_address()

        tokens = self._to_token_struct_list(contents)

        receipt = self._contract_wrapper.send_transaction(
            "wrap", [tokens, uri, recipient_address]
        )
        events = self._contract_wrapper.get_events("TokensWrapped", receipt)
        if len(events) == 0:
            raise Exception("No TokensWrapped event found")

        id = events[0].get("args").get("tokenIdOfWrappedToken")  # type: ignore
        return TxResultWithId(receipt, id=id, data=lambda: self.get(id))

    def unwrap(
        self, wrapped_token_id: int, recipient_address: Optional[str] = None
    ) -> TxReceipt:
        """
        Unwrap a wrapped token bundle

        :param wrapped_token_id: The ID of the wrapped token to unwrap
        :param recipient_address: The optional address to send the unwrapped tokens to
        :returns: The transaction receipt of the token unwrapping

        ```python
        tx = contract.unwrap(wrapped_token_id, receipientAddress)
        ```
        """
        if recipient_address is None:
            recipient_address = self._contract_wrapper.get_signer_address()

        return self._contract_wrapper.send_transaction(
            "unwrap", [wrapped_token_id, recipient_address]
        )

    """
    INTERNAL FUNCTIONS
    """

    def _to_token_struct_list(self, contents: TokensToWrap) -> List[ITokenBundleToken]:
        tokens: List[ITokenBundleToken] = []

        provider = self._contract_wrapper.get_provider()
        owner = self._contract_wrapper.get_signer_address()

        if len(contents.erc20_tokens) > 0:
            for erc20 in contents.erc20_tokens:
                normalized_quantity = normalize_price_value(
                    provider,
                    erc20.quantity,
                    erc20.contract_address,
                )

                has_allowance = has_erc20_allowance(
                    self._contract_wrapper,
                    erc20.contract_address,
                    normalized_quantity,
                )
                if not has_allowance:
                    raise Exception(
                        (
                            f"ERC20 with contract address {erc20.contract_address} does not have enough allowance to transfer. "
                            "You can set allowance to the multiwrap contract to transfer these tokens by running:\n"
                            f'sdk.get_token("{erc20.contract_address}").set_allowance("{owner}", {erc20.quantity})'
                        )
                    )

                tokens.append(
                    {
                        "tokenType": 0,
                        "tokenId": 0,
                        "assetContract": erc20.contract_address,
                        "totalAmount": normalized_quantity,
                    }
                )

        if len(contents.erc721_tokens) > 0:
            for erc721 in contents.erc721_tokens:
                is_approved = is_token_approved_for_transfer(
                    self._contract_wrapper.get_provider(),
                    self.get_address(),
                    erc721.contract_address,
                    erc721.token_id,
                    owner,
                )

                if not is_approved:
                    raise Exception(
                        (
                            f"ERC721 token {erc721.token_id} with contract address {erc721.contract_address} is not approved for transfer. "
                            "You can approve this token for transfer by running:\n"
                            f'sdk.get_nft_collection("{erc721.contract_address}")'
                            f'.set_approval_for_token("{self._contract_wrapper._contract_abi.contract_address}", {erc721.token_id})'
                        )
                    )

                tokens.append(
                    {
                        "tokenType": 1,
                        "tokenId": erc721.token_id,
                        "assetContract": erc721.contract_address,
                        "totalAmount": 0,
                    }
                )

        if len(contents.erc1155_tokens) > 0:
            for erc1155 in contents.erc1155_tokens:
                is_approved = is_token_approved_for_transfer(
                    self._contract_wrapper.get_provider(),
                    self.get_address(),
                    erc1155.contract_address,
                    erc1155.token_id,
                    owner,
                )

                if not is_approved:
                    raise Exception(
                        (
                            f"ERC1155 token {erc1155.token_id} with contract address {erc1155.contract_address} is not approved for transfer. "
                            "You can approve this token for transfer by running:\n"
                            f'sdk.get_edition("{erc1155.contract_address}")'
                            f'.set_approval_for_all("{self._contract_wrapper._contract_abi.contract_address}", True)'
                        )
                    )

                tokens.append(
                    {
                        "tokenType": 2,
                        "tokenId": erc1155.token_id,
                        "assetContract": erc1155.contract_address,
                        "totalAmount": erc1155.quantity,
                    }
                )

        return tokens
