from brownie import accounts
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.constants.role import Role
from thirdweb.contracts import Edition
from thirdweb.core.sdk import ThirdwebSDK
import pytest

from thirdweb.types.nft import EditionMetadataInput, NFTMetadataInput
from thirdweb.types.settings.metadata import EditionContractMetadata


@pytest.mark.usefixtures("sdk", "primary_account")
@pytest.fixture()
def edition(sdk: ThirdwebSDK, primary_account) -> Edition:
    sdk.update_signer(primary_account)
    return sdk.get_edition(
        sdk.deployer.deploy_edition(
            EditionContractMetadata(
                name="SDK Edition",
                symbol="SDK",
                primary_sale_recipient=ZERO_ADDRESS,
                fee_recipient=ZERO_ADDRESS,
                platform_fee_basis_points=10,
                platform_fee_recipient=ZERO_ADDRESS,
            )
        )
    )


def test_mint(edition: Edition):
    result = edition.mint(
        EditionMetadataInput(
            NFTMetadataInput.from_json(
                {"name": "Python SDK NFT", "description": "Minted with the python SDK!"}
            ),
            100,
        )
    )

    assert result.id == 0
    assert result.data().metadata.name == "Python SDK NFT"

    metadata = edition.get(0).metadata

    assert metadata.name == "Python SDK NFT"
    assert metadata.description == "Minted with the python SDK!"
    assert edition.balance(0) == 100


def test_transfer(edition: Edition):
    edition.mint(
        EditionMetadataInput(
            NFTMetadataInput.from_json(
                {"name": "Python SDK NFT", "description": "Minted with the python SDK!"}
            ),
            100,
        )
    )

    my_balance = edition.balance(0)
    other_balance = edition.balance_of(accounts[0].address, 0)

    edition.transfer(accounts[0].address, 0, 50)

    assert edition.balance_of(accounts[0].address, 0) == other_balance + 50
    assert edition.balance(0) == my_balance - 50


def test_roles(edition: Edition):
    address = edition._contract_wrapper.get_signer_address()

    assert address in edition.roles.get_all()[Role.ADMIN]
    assert address in edition.roles.get_all()[Role.MINTER]

    edition.roles.grant(Role.ADMIN, accounts[0].address)
    edition.roles.grant(Role.MINTER, accounts[0].address)

    assert accounts[0].address in edition.roles.get_all()[Role.ADMIN]
    assert accounts[0].address in edition.roles.get_all()[Role.MINTER]

    edition.roles.revoke(Role.ADMIN, accounts[0].address)
    edition.roles.revoke(Role.MINTER, address)

    assert accounts[0].address not in edition.roles.get_all()[Role.ADMIN]
    assert address not in edition.roles.get_all()[Role.MINTER]
