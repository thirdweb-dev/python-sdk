from abc import ABC
from io import IOBase
import re
import json
from requests import get, Response, post
from typing import Any, Dict, List, Sequence, TextIO, BinaryIO, Union, cast
from thirdweb.common.error import (
    DuplicateFileNameException,
    FetchException,
    UploadException,
)
from thirdweb.constants.urls import (
    DEFAULT_IPFS_GATEWAY,
    PINATA_IPFS_URL,
    TW_IPFS_SERVER_URL,
)
from thirdweb.core.helpers.storage import (
    replace_file_properties_with_hashes,
    replace_hash_with_gateway_url,
    resolve_gateway_url,
)
from thirdweb.types.storage import CidWithFileName, UriWithMetadata


class IpfsStorage(ABC):
    """
    Upload and download files from IPFS.

    ```python
    from thirdweb import ThirdwebSDK

    # You can customize this to a supported network or your own RPC URL
    network = "mumbai"

    sdk = ThirdwebSDK(network)

    # Now all the IPFS functions will be available on the sdk.storage name space
    sdk.storage.get("<IPFS_HASH>")
    ```
    """

    _gateway_url: str

    def __init__(self, gateway_url=DEFAULT_IPFS_GATEWAY):
        self._gateway_url = re.sub(r"\/$", "", gateway_url) + "/"

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

        :param contract_address: address of the contract to get the token for.
        :returns: upload token.
        """

        res = get(
            f"{TW_IPFS_SERVER_URL}/grant",
            headers={
                "X-App-Name": f"CONSOLE-PYTHON-SDK-{contract_address}",
            },
        )

        if not res.ok:
            raise FetchException("Failed to upload token")

        return res.text

    def upload(
        self,
        data: Union[TextIO, BinaryIO, str],
        contract_address: str = "",
        signer_address: str = "",
    ) -> str:
        """
        Uploads data to IPFS and returns the hash of the data.

        :param data: data to upload.
        :param contract_address: optional address of the contract to get the token for.
        :param signer_address: optional address of the signer to get the token for.
        :returns: hash of the data.
        """

        cid = self.upload_batch([data], 0, contract_address, signer_address)
        return f"{cid}0"

    def upload_batch(
        self,
        files: Sequence[Union[TextIO, BinaryIO, str, Dict[str, Any]]],
        file_start_number: int = 0,
        contract_address: str = "",
        signer_address: str = "",
    ) -> str:
        """
        Uploads a list of files to IPFS and returns the hash.

        :param files: list of files to upload.
        :param file_start_number: optional number to start the file names with.
        :param contract_address: optional address of the contract to get the token for.
        :param signer_address: optional address of the signer to get the token for.
        :returns: hash of the data.
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

        :param metadata: metadata to upload.
        :param contract_address: optional address of the contract to get the token for.
        :param signer_address: optional address of the signer to get the token for.
        :returns: hash of the metadata.
        """

        uri_with_metadata = self.upload_metadata_batch(
            [metadata], 0, contract_address, signer_address
        )

        return uri_with_metadata.metadata_uris[0]

    def upload_metadata_batch(
        self,
        metadatas: Sequence[Dict[str, Any]],
        file_start_number: int = 0,
        contract_address: str = "",
        signer_address: str = "",
    ) -> UriWithMetadata:
        """
        Uploads a list of metadata to IPFS and returns the hash.

        :param metadatas: list of metadata to upload.
        :param file_start_number: optional number to start the file names with.
        :param contract_address: optional address of the contract to get the token for.
        :param signer_address: optional address of the signer to get the token for.
        :returns: hash of the metadata.
        """

        metadata_to_upload = self._batch_upload_properties(metadatas)
        cid_with_filename = self._upload_batch_with_cid(
            metadata_to_upload, file_start_number, contract_address, signer_address
        )

        base_uri = f"ipfs://{cid_with_filename.cid}/"
        metadata_uris = [
            f"{base_uri}{filename}" for filename in cid_with_filename.filenames
        ]

        return UriWithMetadata(base_uri, metadata_uris)

    """
    PROTECTED FUNCTIONS
    """

    def _get(self, hash: str) -> Response:
        hash = resolve_gateway_url(hash, "ipfs://", self._gateway_url)
        res = get(hash)

        if not res.ok:
            raise FetchException(f"Could not get {hash}")

        return res

    def _batch_upload_properties(self, metadatas: Sequence[Dict[str, Any]]):
        file_lists = [
            self._build_file_properties_map(metadata, []) for metadata in metadatas
        ]
        files_to_upload = [file for file_list in file_lists for file in file_list]

        if len(files_to_upload) == 0:
            return metadatas

        cid_with_filename = self._upload_batch_with_cid(
            cast(List[Union[TextIO, BinaryIO, str, Dict[str, Any]]], files_to_upload)
        )

        cids = []
        for filename in cid_with_filename.filenames:
            cids.append(f"{cid_with_filename.cid}/{filename}")

        final_metadata = replace_file_properties_with_hashes(metadatas, cids)
        return final_metadata

    def _build_file_properties_map(
        self,
        object: Union[Dict[str, Any], List[Any]],
        files: List[IOBase],
    ) -> List[IOBase]:
        if isinstance(object, list):
            [self._build_file_properties_map(item, files) for item in object]
        else:
            for val in object.values():
                if isinstance(val, IOBase):
                    files.append(cast(IOBase, val))
                elif isinstance(val, dict) or isinstance(val, list):
                    self._build_file_properties_map(val, files)
        return files

    def _upload_batch_with_cid(
        self,
        files: Sequence[Union[TextIO, BinaryIO, str, Dict[str, Any]]],
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
            file_data = cast(Union[str, Dict[str, Any]], file)

            if not isinstance(file, str) and not isinstance(file, dict):
                if file.name:
                    extensions = file.name.split(".")
                    extension = extensions[-1]
                    file_name = f"{file_start_number + i}.{extension}"
            elif (
                isinstance(file, dict)
                and "name" in file
                and file["name"] is not None
                and "data" in file
                and file["data"] is not None
            ):
                file_name = file["name"]
                file_data = file["data"]
            else:
                file_data = json.dumps(file)

            if file_name in file_names:
                raise DuplicateFileNameException(file_name)

            file_names.append(file_name)
            form.append(("file", (f"files/{file_name}", file_data)))

        # form.append(("pinataMetadata", metadata))

        res = post(
            PINATA_IPFS_URL,
            files=form,
            headers={
                "Authorization": f"Bearer {token}",
            },
        )
        body = res.json()

        if not res.ok:
            raise UploadException(f"Failed to upload files to IPFS. {res.json()}")

        return CidWithFileName(body["IpfsHash"], file_names)
