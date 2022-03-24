from brownie import accounts, Forwarder
import pytest

# Setup necessary deployments for other contracts


@pytest.fixture(scope="session")
def deploy_contracts():
    forwarder = accounts[0].deploy(Forwarder)
    return forwarder


def test_deploy_contracts(deploy_contracts):
    assert deploy_contracts.address is not None
