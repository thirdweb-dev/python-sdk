import os
from dotenv import load_dotenv
from eth_account import Account
from eth_account.account import LocalAccount
import pytest

load_dotenv()


@pytest.fixture(scope="session")
def primary_account() -> LocalAccount:
    return Account.from_key(os.environ.get("PRIVATE_KEY"))


@pytest.fixture(scope="session")
def secondary_account() -> LocalAccount:
    return Account.from_key(os.environ.get("PRIVATE_KEY_2"))
