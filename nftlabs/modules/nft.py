import copy

import web3
import json

from web3.types import TxReceipt

from . import BaseModule
from typing import Callable, Dict
from ..abi.nft import NFT
from ..storage.ipfs_storage import IpfsStorage

from ..types import NFT as NftType

from zero_ex.contract_wrappers import TxParams

class NftModule(BaseModule):
    address: str
    __abi_module: NFT

    def __init__(
            self,
            address: str,
            get_client: Callable[[], web3.Web3],
            get_storage: Callable[[], IpfsStorage],
            get_signer_address: Callable[[], str],
            get_private_key: Callable[[], str],
            get_transact_opts: Callable[[], TxParams]
    ):
        super().__init__(get_client, get_storage, get_signer_address, get_private_key, get_transact_opts)
        # contract = self.get_client().eth.contract(
        #     address=address
        # )
        # print(contract.)

        self.address = address 
        self.__abi_module = NFT(self.get_client(), address)

    def mint(self, name: str = "", description: str = "", image_uri: str = "", properties: Dict = None):
        return self.mint_to(self.get_signer_address(), name, description, image_uri, properties)

    def mint_to(
            self,
            to_address: str,
            name: str = "",
            description: str = "",
            image_uri: str = "",
            properties: Dict = None
    ):
        final_properties: Dict
        if properties is None:
            final_properties = {}
        else:
            final_properties = copy.copy(properties)
        storage = self.get_storage()

        meta = {
            'name': name,
            'description': description,
            'image': image_uri,
            'properties': final_properties
        }

        uri = storage.upload(json.dumps(meta), self.address, self.get_signer_address())
        tx = self.__abi_module.mint_nft.build_transaction(to_address, uri, self.get_transact_opts())
        receipt = self.execute_tx(tx)
        result = self.__abi_module.get_minted_event(tx_hash=receipt.transactionHash.hex())
        token_id = result[0]['args']['tokenId']
        return self.get(token_id)

    def total_supply(self) -> int:
        return self.__abi_module.total_supply.call()

    def get(self, nft_id: int) -> NftType:
        return self.__get_metadata(nft_id)

    def __get_metadata(self, nft_id: int) -> NftType:
        uri = self.__get_metadata_uri(nft_id)
        meta = self.get_storage().get(uri)
        meta_obj: NftType = NftType.from_json(meta)
        meta_obj.id = nft_id
        meta_obj.uri = uri
        return meta_obj

    def __get_metadata_uri(self, nft_id: int):
        uri = self.__abi_module.token_uri.call(nft_id)
        if uri == "":
            raise Exception("Could not find NFT metadata, are you sure it exists?")
        return uri
