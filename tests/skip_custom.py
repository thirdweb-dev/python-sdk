import pytest
from thirdweb.abi import TokenERC721
from thirdweb.abi.token_erc20 import TokenERC20
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.constants.urls import DEFAULT_API_KEY
from thirdweb.contracts.nft_collection import NFTCollection
from thirdweb.contracts.token import Token
from thirdweb.core.sdk import ThirdwebSDK
from zero_ex.contract_wrappers.tx_params import TxParams
from web3 import Web3

from thirdweb.types.settings.metadata import (
    NFTCollectionContractMetadata,
    TokenContractMetadata,
)


@pytest.mark.usefixtures("sdk", "primary_account")
@pytest.fixture(scope="function")
def nft_collection(sdk: ThirdwebSDK, primary_account) -> NFTCollection:
    sdk.update_signer(primary_account)
    return sdk.get_nft_collection(
        sdk.deployer.deploy_nft_collection(
            NFTCollectionContractMetadata(
                name="SDK NFT Collection",
            )
        )
    )


@pytest.mark.usefixtures("sdk", "primary_account")
@pytest.fixture(scope="function")
def token(sdk: ThirdwebSDK, primary_account) -> Token:
    sdk.update_signer(primary_account)
    return sdk.get_token(
        sdk.deployer.deploy_token(
            TokenContractMetadata(
                name="SDK Token",
                symbol="SDK",
                primary_sale_recipient=ZERO_ADDRESS,
            )
        )
    )


@pytest.mark.usefixtures("sdk")
def test_custom_functions(sdk: ThirdwebSDK, nft_collection: NFTCollection):
    custom = sdk.get_contract_from_abi(nft_collection.get_address(), TokenERC721.abi())

    contract_uri = custom.functions.contractURI().call()
    metadata = sdk.storage.get(contract_uri)  # type: ignore
    assert metadata["name"] == "SDK NFT Collection"


@pytest.mark.usefixtures("sdk")
def test_feature_detection(
    sdk: ThirdwebSDK, nft_collection: NFTCollection, token: Token
):
    custom = sdk.get_contract_from_abi(nft_collection.get_address(), TokenERC721.abi())

    assert custom.nft.balance() == 0

    try:
        custom.token.balance()
        assert False
    except:
        assert True

    custom = sdk.get_contract_from_abi(token.get_address(), TokenERC20.abi())

    assert custom.token.balance().display_value == 0

    try:
        custom.nft.balance()
        assert False
    except:
        assert True


@pytest.mark.usefixtures("sdk")
def test_write(sdk: ThirdwebSDK, nft_collection: NFTCollection):
    custom = sdk.get_contract_from_abi(nft_collection.get_address(), TokenERC721.abi())

    assert custom.functions.totalSupply().call() == 0
    custom.send_transaction("mintTo", [sdk.get_signer().address, "https://example.com"])  # type: ignore
    assert custom.functions.totalSupply().call() == 1
