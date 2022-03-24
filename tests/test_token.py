from brownie import accounts, Forwarder


def test_deploy_token():
    accounts[0].deploy(Forwarder)

    assert True
