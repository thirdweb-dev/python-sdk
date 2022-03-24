import pytest


@pytest.mark.usefixtures("contracts")
def test_deploy_contracts(contracts):
    (thirdweb_registry, thirdweb_factory, thirdweb_fee) = contracts
    assert thirdweb_registry.address is not None
    assert thirdweb_factory.address is not None
    assert thirdweb_fee.address is not None
