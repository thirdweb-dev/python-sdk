from dotenv import load_dotenv
from eth_account import Account
from brownie import accounts
from brownie.network.account import LocalAccount
import pytest

load_dotenv()


@pytest.fixture(scope="session")
def primary_account() -> LocalAccount:
    account, mnemonic = Account.create_with_mnemonic()
    brownie_account = LocalAccount(account.address, account, account.key)
    accounts._accounts.append(brownie_account)
    address = brownie_account.address

    account = accounts.at(address, force=True)
    accounts[0].transfer(account, accounts[0].balance().__truediv__(3))
    return Account.from_mnemonic(mnemonic)


@pytest.fixture(scope="session")
def secondary_account() -> LocalAccount:
    account, mnemonic = Account.create_with_mnemonic()
    brownie_account = LocalAccount(account.address, account, account.key)
    accounts._accounts.append(brownie_account)
    address = brownie_account.address

    account = accounts.at(address, force=True)
    accounts[0].transfer(account, accounts[0].balance().__truediv__(2))
    return Account.from_mnemonic(mnemonic)
