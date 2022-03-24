from brownie import accounts, Split


def deploy_token():
    accounts[0].deploy(Split, "Test Token", "TST", 18, "1000000000000000000000000")
