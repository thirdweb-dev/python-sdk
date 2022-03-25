from thirdweb.contracts import Edition
from thirdweb.core.sdk import ThirdwebSDK
import pytest

OTHER_ADDRESS = "0x9e31E40Dda94976A405D7BDe6c698DB60E95C87d"
EDITION_ADDRESS = "0x522B1fE8BDF70fB0c3a4931aCB94fBa6C232c74f"


@pytest.mark.usefixtures("sdk")
@pytest.fixture()
def edition(sdk: ThirdwebSDK) -> Edition:
    edition = sdk.get_edition(EDITION_ADDRESS)
    return edition


def test_edition_provider(edition: Edition):
    assert edition._contract_wrapper.get_provider() is not None
    assert edition._contract_wrapper.get_signer() is not None
