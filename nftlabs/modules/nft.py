import web3
import json

from . import BaseModule
from typing import Callable, Dict
from ..abi.nft import NFT
from ..storage.ipfs_storage import IpfsStorage

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

        self.address = address
        self.__abi_module = NFT(self.get_client(), address)

    def mint(self, name: str = "", description: str = "", image_uri: str = "", properties: Dict = None):
        storage = self.get_storage()

        meta = {
            'name': name,
            'description': description,
            'image': image_uri,
            properties: json.dumps(properties)
        }

        uri = storage.upload(json.dumps(meta), self.address, self.get_signer_address())

        tx = self.__abi_module.mint_nft.build_transaction(self.get_signer_address(), uri, self.get_transact_opts())
        receipt = self.execute_tx(tx)
        print(receipt)

    def total_supply(self) -> int:
        return self.__abi_module.total_supply.call()
