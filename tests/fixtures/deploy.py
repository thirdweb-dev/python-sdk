from brownie import Forwarder, TWFactory, TWFee, accounts
import pytest


@pytest.fixture
def deploy():
    accounts[0].deploy(Forwarder)
