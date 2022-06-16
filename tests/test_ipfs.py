import pytest
from requests import get
from thirdweb.common.error import DuplicateFileNameException
from thirdweb.constants.urls import DEFAULT_IPFS_GATEWAY

from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.core.sdk import ThirdwebSDK


@pytest.mark.usefixtures("sdk")
@pytest.fixture()
def storage(sdk: ThirdwebSDK):
    storage = sdk.storage  # type: ignore
    return storage


def get_file(upload: str, gateway_url: str):
    url = upload.replace("ipfs://", "")

    try:
        res = get(f"{gateway_url}{url}")
        return res
    except:
        assert False


def test_batch(storage: IpfsStorage):
    mp4 = open("tests/files/test.mp4", "rb")
    jpg = open("tests/files/0.jpg", "rb")

    sample_objects = [
        {
            "name": "test2.mp4",
            "data": mp4,
        },
        {
            "name": "test3.mp4",
            "data": mp4,
        },
        {
            "name": "test.jpeg",
            "data": jpg,
        },
    ]

    cid = storage.upload_batch(sample_objects)

    assert get_file(f"{cid}test.jpeg", storage._gateway_url) is not None


def test_properties(storage: IpfsStorage):
    sample_objects = [
        {"name": "test 0", "image": open("tests/files/0.jpg", "rb")},
        {
            "name": "test 1",
            "image": open("tests/files/1.jpg", "rb"),
            "properties": {
                "image": open("tests/files/3.jpg", "rb"),
            },
        },
        {
            "name": "test 2",
            "image": open("tests/files/2.jpg", "rb"),
            "properties": {
                "image": open("tests/files/4.jpg", "rb"),
                "test": {"image": open("tests/files/5.jpg", "rb")},
            },
        },
    ]

    uri_with_metadata = storage.upload_metadata_batch(sample_objects)

    assert uri_with_metadata.base_uri.startswith(
        "ipfs://"
    ) and uri_with_metadata.base_uri.endswith("/")
    assert len(uri_with_metadata.metadata_uris) == len(sample_objects)


def test_bulk_upload(storage: IpfsStorage):
    sample_objects = [
        {
            "name": "test",
            "data": open("tests/files/test.mp4", "rb"),
        },
        {
            "name": "test",
            "data": open("tests/files/0.jpg", "rb"),
        },
    ]

    try:
        storage.upload_batch(sample_objects)
        assert False
    except DuplicateFileNameException:
        assert True


def test_upload_and_resolve(storage: IpfsStorage):
    upload = storage.upload_metadata(
        {
            "name": "test name",
            "description": "made with python sdk",
            "animation_url": open("tests/files/test.mp4", "rb"),
        }
    )

    meta = storage.get(upload)

    assert meta["description"].startswith("made with python sdk")
    assert "ipfs" in meta["animation_url"]


def test_replace_gateway_urls(storage: IpfsStorage):
    upload = storage.upload_metadata(
        {
            "svg": f"{DEFAULT_IPFS_GATEWAY}QmZsU8nTTexTxPzCKZKqo3Ntf5cUiWMRahoLmtpimeaCiT/backgrounds/SVG/Asset%20501.svg",
        }
    )

    other_storage = IpfsStorage(gateway_url="https://ipfs.thirdweb.com/ipfs/")
    downloaded = other_storage.get(upload)

    assert downloaded["svg"].startswith("https://ipfs.thirdweb.com/ipfs/")
