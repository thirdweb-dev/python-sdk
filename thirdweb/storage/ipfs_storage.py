
#from .util import replace_ipfs_prefix_with_gateway
from requests import get, post
import json
from io import TextIOBase, BytesIO


class IpfsStorage:
    __nftlabsApiUrl = "https://upload.nftlabs.co"

    gateway_uri: str

    def __init__(self, gateway_uri: str):
        self.gateway_uri = gateway_uri

    def get(self, uri: str) -> str:
        ipfs_uri = replace_ipfs_prefix_with_gateway(uri, self.gateway_uri)

        response = get(ipfs_uri)

        if response.status_code != 200:
            raise Exception("Failed to download metadata")

        return response.text

    """
    Upload data to IPFS, data parameter
    """

    def upload(self, data, contract_address: str, signer_address: str) -> str:
        if isinstance(data, str) and data.startswith("ipfs://"):
            return data

        if isinstance(data, TextIOBase):
            form = {
                'file': data
            }
            result = post(f'{self.__nftlabsApiUrl}/upload', data=form, headers={
                'X-App-Name': f'CONSOLE-PYTHON-SDK-{contract_address}',
                'X-Public-Address': signer_address,
            })
            if result.status_code != 200:
                raise Exception("Failed to upload image")
            response = result.json()
            return response['IpfsUri']

        form = {
            'file': data
        }
        result = post(f'{self.__nftlabsApiUrl}/upload', files=form, headers={
            'X-App-Name': f'CONSOLE-PYTHON-SDK-{contract_address}',
            'X-Public-Address': signer_address,
        })
        if result.status_code != 200:
            raise Exception(
                "Failed to upload image. Please provide a valid URL.")
        response = result.json()
        return response['IpfsUri']

    def upload_metadata(self, metadata, contract_address: str, signer_address: str) -> str:
        if type(metadata) == str:
            return self.upload(metadata, contract_address, signer_address)
