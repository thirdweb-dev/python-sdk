from thirdweb.core.sdk import ThirdwebSDK
from thirdweb.contracts import Multiwrap, NFTCollection, Edition, Token
from brownie import accounts
import pytest
from thirdweb.types.currency import TokenAmount
from thirdweb.types.multiwrap import (
    ERC1155Wrappable,
    ERC20Wrappable,
    ERC721Wrappable,
    TokensToWrap,
)

from thirdweb.types.nft import EditionMetadataInput, NFTMetadataInput
from thirdweb.types.settings.metadata import (
    EditionContractMetadata,
    MultiwrapContractMetadata,
    NFTCollectionContractMetadata,
    TokenContractMetadata,
)


@pytest.mark.usefixtures("sdk", "primary_account")
@pytest.fixture(scope="function")
def multiwrap(sdk: ThirdwebSDK, primary_account) -> Multiwrap:
    sdk.update_signer(primary_account)
    return sdk.get_multiwrap(
        sdk.deployer.deploy_multiwrap(
            MultiwrapContractMetadata(
                name="Test Multiwrap",
            )
        )
    )


@pytest.mark.usefixtures("sdk", "multiwrap")
@pytest.fixture(scope="function")
def nft_collection(sdk: ThirdwebSDK, multiwrap: Multiwrap) -> NFTCollection:
    nft_collection = sdk.get_nft_collection(
        sdk.deployer.deploy_nft_collection(
            NFTCollectionContractMetadata(
                name="Test NFT",
                seller_fee_basis_points=200,
                fee_recipient=sdk.get_signer().address,  # type: ignore
                primary_sale_recipient=sdk.get_signer().address,  # type: ignore
            )
        )
    )

    nft_collection.mint_batch(
        [
            NFTMetadataInput(name="Test 0"),
            NFTMetadataInput(name="Test 1"),
            NFTMetadataInput(name="Test 2"),
            NFTMetadataInput(name="Test 3"),
        ]
    )

    nft_collection.set_approval_for_all(multiwrap.get_address(), True)

    return nft_collection


@pytest.mark.usefixtures("sdk", "multiwrap")
@pytest.fixture()
def edition(sdk: ThirdwebSDK, multiwrap: Multiwrap) -> Edition:
    edition = sdk.get_edition(
        sdk.deployer.deploy_edition(
            EditionContractMetadata(
                name="Test Edition",
                seller_fee_basis_points=100,
                primary_sale_recipient=sdk.get_signer().address,  # type: ignore
            )
        )
    )

    edition.mint_batch(
        [
            EditionMetadataInput(metadata=NFTMetadataInput(name="Test 0"), supply=1),
            EditionMetadataInput(metadata=NFTMetadataInput(name="Test 1"), supply=1),
        ]
    )

    edition.set_approval_for_all(multiwrap.get_address(), True)

    return edition


@pytest.mark.usefixtures("sdk", "multiwrap")
@pytest.fixture(scope="function")
def token(sdk: ThirdwebSDK, multiwrap: Multiwrap) -> Token:
    token = sdk.get_token(
        sdk.deployer.deploy_token(
            TokenContractMetadata(
                name="Test Token",
                symbol="TEST",
                primary_sale_recipient=sdk.get_signer().address,  # type: ignore
            )
        )
    )

    token.mint_batch_to(
        [
            TokenAmount(to_address=sdk.get_signer().address, amount=10),  # type: ignore
        ]
    )

    token.set_allowance(multiwrap.get_address(), 10)

    return token


@pytest.mark.usefixtures("multiwrap", "nft_collection", "edition", "token")
def test_wrap_tokens(
    multiwrap: Multiwrap, nft_collection: NFTCollection, token: Token, edition: Edition
):
    assert token.balance() == 10
    assert nft_collection.balance() == 4
    assert edition.balance(0) == 1

    tx = multiwrap.wrap(
        TokensToWrap(
            erc20_tokens=[
                ERC20Wrappable(contract_address=token.get_address(), quantity=10),
            ],
            erc721_tokens=[
                ERC721Wrappable(
                    contract_address=nft_collection.get_address(), token_id=0
                ),
            ],
            erc1155_tokens=[
                ERC1155Wrappable(
                    contract_address=edition.get_address(), token_id=0, quantity=1
                ),
            ],
        ),
        NFTMetadataInput(
            name="Wrapped NFT",
            description="This is a wrapped bundle of tokens and NFTs",
        ),
    )

    token_metadata = tx.data()

    assert token_metadata.metadata.name == "Wrapped NFT"

    assert token.balance() == 0
    assert nft_collection.balance() == 3
    assert edition.balance(0) == 0


@pytest.mark.usefixtures("multiwrap", "nft_collection", "edition", "token")
def test_wrapped_contents(
    multiwrap: Multiwrap, nft_collection: NFTCollection, token: Token, edition: Edition
):
    tx = multiwrap.wrap(
        TokensToWrap(
            erc20_tokens=[
                ERC20Wrappable(contract_address=token.get_address(), quantity=10),
            ],
            erc721_tokens=[
                ERC721Wrappable(
                    contract_address=nft_collection.get_address(), token_id=0
                ),
            ],
            erc1155_tokens=[
                ERC1155Wrappable(
                    contract_address=edition.get_address(), token_id=0, quantity=1
                ),
            ],
        ),
        NFTMetadataInput(
            name="Wrapped NFT",
            description="This is a wrapped bundle of tokens and NFTs",
        ),
    )

    wrapped_tokens = multiwrap.get_wrapped_contents(tx.id)

    assert len(wrapped_tokens.erc20_tokens) == 1
    assert wrapped_tokens.erc20_tokens[0].contract_address == token.get_address()

    assert len(wrapped_tokens.erc721_tokens) == 1
    assert (
        wrapped_tokens.erc721_tokens[0].contract_address == nft_collection.get_address()
    )

    assert len(wrapped_tokens.erc1155_tokens) == 1
    assert wrapped_tokens.erc1155_tokens[0].contract_address == edition.get_address()


@pytest.mark.usefixtures("multiwrap", "nft_collection", "edition", "token")
def test_unwrap(
    multiwrap: Multiwrap, nft_collection: NFTCollection, token: Token, edition: Edition
):
    tx = multiwrap.wrap(
        TokensToWrap(
            erc20_tokens=[
                ERC20Wrappable(contract_address=token.get_address(), quantity=10),
            ],
            erc721_tokens=[
                ERC721Wrappable(
                    contract_address=nft_collection.get_address(), token_id=0
                ),
            ],
            erc1155_tokens=[
                ERC1155Wrappable(
                    contract_address=edition.get_address(), token_id=0, quantity=1
                ),
            ],
        ),
        NFTMetadataInput(
            name="Wrapped NFT",
            description="This is a wrapped bundle of tokens and NFTs",
        ),
    )

    assert token.balance() == 0
    assert nft_collection.balance() == 3
    assert edition.balance(0) == 0

    multiwrap.unwrap(tx.id)

    assert token.balance() == 10
    assert nft_collection.balance() == 4
    assert edition.balance(0) == 1
