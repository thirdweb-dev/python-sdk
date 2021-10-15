import copy
from collections import namedtuple

import web3
import json

from web3.types import TxReceipt

from . import BaseModule
from typing import Callable, Dict, NamedTuple, List
from ..abi.nft import NFT
from ..storage.ipfs_storage import IpfsStorage

from ..types import NFT as NftType
from .nft_types import MintArg

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

    def mint(self, arg: MintArg):
        return self.mint_to(self.get_signer_address(), arg)

    def mint_to(
            self,
            to_address: str,
            arg: MintArg,
    ):
        final_properties: Dict
        if arg.properties is None:
            final_properties = {}
        else:
            final_properties = copy.copy(arg.properties)
        storage = self.get_storage()

        meta = {
            'name': arg.name,
            'description': arg.description,
            'image': arg.image_uri,
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

    def mint_batch(self):
        pass

    def burn(self, token_id: int):
        tx = self.__abi_module.burn.build_transaction(
            token_id,
            self.get_transact_opts()
        )
        self.execute_tx(tx)


    def transfer_from(self, from_address: str, to_address: str, token_id: int):
        tx = self.__abi_module.transfer_from.build_transaction(
            from_address,
            to_address,
            token_id,
            self.get_transact_opts()
        )
        self.execute_tx(tx)

    """
    Transfers NFT from the current signers wallet to another wallet
    """
    def transfer(self, to_address: str, token_id: int):
        tx = self.__abi_module.safe_transfer_from1.build_transaction(
            self.get_signer_address(),
            to_address,
            token_id,
            self.get_transact_opts()
        )
        self.execute_tx(tx)

    def set_royalty_bps(self, amount: int):
        tx = self.__abi_module.set_royalty_bps.build_transaction(amount, self.get_transact_opts())
        self.execute_tx(tx)

    def get_all(self) -> List[NftType]:
        max_id = self.__abi_module.next_token_id.call()
        return [self.get(i) for i in range(max_id)]

    """
    Defaults to fetching the NFTs owned by the current signer (as indicated by the private key)
    if the address parameter is not supplied
    """
    def get_owned(self, address: str = "") -> List[NftType]:
        if address == "":
            address = self.get_signer_address()

        balance = self.__abi_module.balance_of.call(address)
        owned_tokens = [self.__token_of_owner_by_index(address, i) for i in range(balance)]
        return [self.get(i) for i in owned_tokens]

    def __token_of_owner_by_index(self, address: str, token_id: int) -> int:
        return self.__abi_module.token_of_owner_by_index.call(address, token_id)