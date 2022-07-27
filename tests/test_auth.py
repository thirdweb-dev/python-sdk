import pytest
from thirdweb import ThirdwebSDK
from thirdweb.types.auth import AuthenticationOptions, LoginOptions, VerifyOptions
from datetime import datetime, timedelta

domain = "thirdweb.com"


@pytest.mark.usefixtures("sdk", "primary_account", "secondary_account")
def test_verify(sdk: ThirdwebSDK, primary_account, secondary_account):
    sdk.update_signer(primary_account)
    payload = sdk.auth.login(domain)

    sdk.update_signer(secondary_account)
    address = sdk.auth.verify(domain, payload)

    assert address == primary_account.address


@pytest.mark.usefixtures("sdk", "primary_account", "secondary_account")
def test_verify_with_params(sdk: ThirdwebSDK, primary_account, secondary_account):
    sdk.update_signer(primary_account)
    payload = sdk.auth.login(
        domain,
        LoginOptions(
            expiration_time=datetime.utcnow() + timedelta(hours=5), chain_id=137
        ),
    )

    sdk.update_signer(secondary_account)
    address = sdk.auth.verify(
        domain,
        payload,
        VerifyOptions(
            chain_id=137,
        ),
    )

    assert address == primary_account.address


@pytest.mark.usefixtures("sdk", "primary_account", "secondary_account")
def test_reject_incorrect_domain(sdk: ThirdwebSDK, primary_account, secondary_account):
    sdk.update_signer(primary_account)
    payload = sdk.auth.login(domain)

    sdk.update_signer(secondary_account)
    try:
        sdk.auth.verify("test.thirdweb.com", payload)
        assert False
    except Exception as e:
        assert "Expected domain 'test.thirdweb.com" in str(e)


@pytest.mark.usefixtures("sdk", "primary_account", "secondary_account")
def test_reject_expired_payload(sdk: ThirdwebSDK, primary_account, secondary_account):
    sdk.update_signer(primary_account)
    payload = sdk.auth.login(
        domain, LoginOptions(expiration_time=datetime.utcnow() - timedelta(hours=5))
    )

    sdk.update_signer(secondary_account)
    try:
        sdk.auth.verify(domain, payload)
        assert False
    except Exception as e:
        assert "Login request has expired" in str(e)


@pytest.mark.usefixtures("sdk", "primary_account", "secondary_account")
def test_reject_incorrect_chain_id(
    sdk: ThirdwebSDK, primary_account, secondary_account
):
    sdk.update_signer(primary_account)
    payload = sdk.auth.login(domain, LoginOptions(chain_id=1))

    sdk.update_signer(secondary_account)
    try:
        sdk.auth.verify(domain, payload, VerifyOptions(chain_id=137))
        assert False
    except Exception as e:
        assert "Chain ID '137' does not match payload chain ID '1'" in str(e)


@pytest.mark.usefixtures("sdk", "primary_account", "secondary_account")
def test_reject_incorrect_signer(sdk: ThirdwebSDK, primary_account, secondary_account):
    sdk.update_signer(primary_account)
    payload = sdk.auth.login(domain)
    payload.payload.address = secondary_account.address

    sdk.update_signer(secondary_account)
    try:
        sdk.auth.verify(domain, payload)
        assert False
    except Exception as e:
        assert (
            str(e)
            == f"The intended payload address '{secondary_account.address.lower()}' is not the payload signer"
        )


@pytest.mark.usefixtures("sdk", "primary_account", "secondary_account")
def test_generate_token(sdk: ThirdwebSDK, primary_account, secondary_account):
    sdk.update_signer(primary_account)
    payload = sdk.auth.login(domain)

    sdk.update_signer(secondary_account)
    token = sdk.auth.generate_auth_token(domain, payload)
    address = sdk.auth.authenticate(domain, token)

    assert address == primary_account.address


@pytest.mark.usefixtures("sdk", "primary_account", "secondary_account")
def test_reject_token_incorrect_domain(
    sdk: ThirdwebSDK, primary_account, secondary_account
):
    sdk.update_signer(primary_account)
    payload = sdk.auth.login(domain)

    sdk.update_signer(secondary_account)
    token = sdk.auth.generate_auth_token(domain, payload)
    try:
        sdk.auth.authenticate("test.thirdweb.com", token)
        assert False
    except Exception as e:
        assert "Expected token to be for the domain 'test.thirdweb.com'" in str(e)


@pytest.mark.usefixtures("sdk", "primary_account", "secondary_account")
def test_reject_token_before_invalid(
    sdk: ThirdwebSDK, primary_account, secondary_account
):
    sdk.update_signer(primary_account)
    payload = sdk.auth.login(domain)

    sdk.update_signer(secondary_account)
    token = sdk.auth.generate_auth_token(
        domain,
        payload,
        AuthenticationOptions(invalid_before=datetime.utcnow() + timedelta(hours=5)),
    )
    try:
        sdk.auth.authenticate(domain, token)
        assert False
    except Exception as e:
        assert "This token is invalid before" in str(e)


@pytest.mark.usefixtures("sdk", "primary_account", "secondary_account")
def test_reject_expired_token(sdk: ThirdwebSDK, primary_account, secondary_account):
    sdk.update_signer(primary_account)
    payload = sdk.auth.login(domain)

    sdk.update_signer(secondary_account)
    token = sdk.auth.generate_auth_token(
        domain,
        payload,
        AuthenticationOptions(expiration_time=datetime.utcnow() - timedelta(hours=5)),
    )
    try:
        sdk.auth.authenticate(domain, token)
        assert False
    except Exception as e:
        assert "This token expired" in str(e)


@pytest.mark.usefixtures("sdk", "primary_account", "secondary_account")
def test_reject_admin_not_connected(
    sdk: ThirdwebSDK, primary_account, secondary_account
):
    sdk.update_signer(primary_account)
    payload = sdk.auth.login(domain)

    sdk.update_signer(secondary_account)
    token = sdk.auth.generate_auth_token(domain, payload)

    sdk.update_signer(primary_account)
    try:
        sdk.auth.authenticate(domain, token)
        assert False
    except Exception as e:
        assert "Expected the connected wallet address" in str(e)
