import re
from requests import get, Response, post
from typing import Any, Dict, List, Text, TextIO, BinaryIO, Union, cast
from thirdweb.common.error import FetchException, UploadException
from thirdweb.constants.urls import (
    DEFAULT_IPFS_GATEWAY,
    PINATA_IPFS_URL,
    TW_IPFS_SERVER_URL,
)
from thirdweb.core.helpers.storage import (
    replace_hash_with_gateway_url,
    resolve_gateway_url,
)
from thirdweb.types.storage import CidWithFileName, UriWithMetadata


class IpfsStorage:
    _gateway_url: str

    def __init__(self, gateway_url=DEFAULT_IPFS_GATEWAY):
        self._gateway_url = re.sub(r"\/$", "", gateway_url)

    def get(self, hash: str) -> Dict[str, Any]:
        """
        Gets IPFS data at a given hash and returns it as a dictionary.

        :param hash: hash of the data to get.
        :returns: dictionary of the data.
        """

        res = self._get(hash)
        data = res.json()
        return replace_hash_with_gateway_url(data, "ipfs://", self._gateway_url)

    def get_upload_token(self, contract_address: str) -> str:
        """
        Gets an upload token for a given contract address.
        """

        res = get(
            f"{TW_IPFS_SERVER_URL}/grant",
            headers={"X-App-Name": f"CONSOLE-PYTHON-SDK-{contract_address}"},
        )

        if not res.ok:
            raise FetchException("Failed to upload token")

        return res.json()

    def upload(
        self,
        data: Union[TextIO, BinaryIO, str],
        contract_address: str = "",
        signer_address: str = "",
    ) -> str:
        """
        Uploads data to IPFS and returns the hash of the data.
        """

        cid = self.upload_batch([data], 0, contract_address, signer_address)
        return f"{cid}0"

    def upload_batch(
        self,
        files: List[Union[TextIO, BinaryIO, str]],
        file_start_number: int = 0,
        contract_address: str = "",
        signer_address: str = "",
    ) -> str:
        """
        Uploads a list of files to IPFS and returns the hash.
        """

        cid_with_filename = self._upload_batch_with_cid(
            files,
            file_start_number,
            contract_address,
            signer_address,
        )

        return f"ipfs://{cid_with_filename.cid}"

    def upload_metadata(
        self,
        metadata: Dict[str, Any],
        contract_address: str = "",
        signer_address: str = "",
    ) -> str:
        """
        Uploads metadata to IPFS and returns the hash of the metadata.
        """

        uri_with_metadata = self.upload_metadata_batch(
            [metadata], 0, contract_address, signer_address
        )

        return uri_with_metadata.metadata_uris[0]

    def upload_metadata_batch(
        self,
        metadatas: List[Dict[str, Any]],
        file_start_number: int = 0,
        contract_address: str = "",
        signer_address: str = "",
    ) -> UriWithMetadata:
        """
        Uploads a list of metadata to IPFS and returns the hash.
        """

        raise NotImplementedError

    """
    PROTECTED FUNCTIONS
    """

    def _get(self, hash: str) -> Response:
        hash = resolve_gateway_url(hash, "ipfs://", self._gateway_url)
        res = get(hash)

        if not res.ok:
            raise FetchException(f"Could not get {hash}")

        return res

    def _batch_upload_properties(self, metadatas: List[Dict[str, Any]]):
        raise NotImplementedError

    def _build_file_properties_map(
        self, object: Dict[str, Any], files: List[Union[TextIO, BinaryIO]]
    ) -> Union[TextIO, BinaryIO]:
        raise NotImplementedError

    def _upload_batch_with_cid(
        self,
        files: List[Union[TextIO, BinaryIO, str]],
        file_start_number: int = 0,
        contract_address: str = "",
        signer_address: str = "",
    ) -> CidWithFileName:
        token = self.get_upload_token(contract_address)
        metadata = {
            "name": f"CONSOLE-PYTHON-SDK-{contract_address}",
            "keyvalues": {
                "sdk": "python",
                "contractAddress": contract_address,
                "signerAddress": signer_address,
            },
        }

        form: List[Any] = []
        file_names: List[str] = []

        for i, file in enumerate(files):
            file_name = f"{file_start_number + i}"
            file_data: Union[bytes, str] = cast(str, file)

            if not isinstance(file, str):
                file_name = file.name
                file_data = file.read()

            file_names.append(file_name)
            form.append(file_data)

        data = {"form": form, "pinataMetadata": metadata}
        res = post(
            PINATA_IPFS_URL,
            json=data,
            headers={
                "Authorization": f"Bearer {token}",
            },
        )
        body = res.json()

        if not res.ok:
            raise UploadException("Failed to upload files to IPFS")

        return CidWithFileName(body["IpfsHash"], file_names)
