
from .util import replace_ipfs_prefix_with_gateway
from requests import get, post
import json
import io
from ..errors import UploadError

import base64


class IpfsStorage:
    __nftlabsApiUrl = "https://upload.nftlabs.co"

    gateway_uri: str

    def __init__(self, gateway_uri: str):
        self.gateway_uri = gateway_uri

    def get(self, uri: str) -> str:
        ipfs_uri = replace_ipfs_prefix_with_gateway(uri, self.gateway_uri)

        response = get(ipfs_uri, timeout=10)

        if response.status_code != 200:
            raise Exception("Failed to download metadata")

        return response.text

    """
    Upload data to IPFS, data parameter
    """

    def upload(self, data, contract_address: str, signer_address: str) -> str:
        if isinstance(data, str) and data.startswith("ipfs://"):
            return data
        form = {
            'file': data
        }
        result = post(f'{self.__nftlabsApiUrl}/upload', files=form, headers={
            'X-App-Name': f'CONSOLE-PYTHON-SDK-{contract_address}',
            'X-Public-Address': signer_address,
        })
        if result.status_code != 200:
            raise UploadError(result.text)
        response = result.json()
        return response['IpfsUri']

    def upload_metadata(self, metadata: str, contract_address: str, signer_address: str) -> str:
        if type(metadata) == str:
            return self.upload(metadata, contract_address, signer_address)

    def get_upload_token(self, address: str):
        headers = {
            'X-App-Name': f'CONSOLE-PYTHON-SDK-{address}',
        }
        result = post(f'{self.__nftlabsApiUrl}/grant', headers=headers)
        if result.status_code != 200:
            raise UploadError(result.text)
        return result.text

    def upload_batch(self, files: list, contract_address: str, signer_address: str) -> list:
        token = self.get_upload_token(contract_address)
        metadata = {
            'name': f'CONSOLE-PYTHON-SDK-{contract_address}',
        }
        file_list = [('file', (f'images/{i}', files[i]))
                     for i in range(0, len(files))]
        form = {
            'metadata': json.dumps(metadata),
        }
        result = post("https://api.pinata.cloud/pinning/pinFileToIPFS", files=file_list, data=form, headers={
            "Authorization": f'Bearer {token}'
        })
        if result.status_code != 200:
            raise UploadError(result.text)
        response = result.json()
        print(response)
        return response['IpfsUris']
