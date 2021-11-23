""" Interact with the NFT module of the app"""
import copy
import json
from typing import Dict, List
import io

from thirdweb_web3 import Web3

from ..abi.nft import NFT
from ..types.nft import MintArg
from ..types.nft import NftMetadata as NftType
from .base import BaseModule


class NftModule(BaseModule):
    """
    NFT Methods
    """

    address: str
    __abi_module: NFT

    def __init__(self, address: str, client: Web3):
        """
        Initializing the class attributes
        """
        super().__init__()
        self.address = address
        """
        NFT module contract address [https://thirdweb.com/: Dashboard: Project ➝ NFT Module]
        """

        self.__abi_module = NFT(client, address)
        """
        The ABI makes calls the EVM. Client is default 'Web3' and Address is nft module contract address.
        """

    def mint(self, arg: MintArg) -> NftType:
        """
        Mints a new token to the signer. 
        - Arguments passed: Note, a class is used -> MintArg(name, description, image_uri, properties)
        - Returns the `NftMetadata(name,description,image,properties,id,uri)`  *Preferrably, using a link
        """
        return self.mint_to(self.get_signer_address(), arg)

    def mint_to(
        self,
        to_address: str,
        arg: MintArg,
    ) -> NftType:
        """
        Mints a new token to an address
        - Arguments passed: `to_address` and a class -> `MintArg(name, description, image_uri, properties)`
        - Returns the `NftMetadata(name,description,image,properties,id,uri)`  *Preferrably, using a link
        """
        final_properties: Dict
        if arg.properties is None:
            final_properties = {}
        else:
            final_properties = copy.copy(arg.properties)

        if arg.image == "":
            arg.image = arg.image_uri

        meta = {
            'name': arg.name,
            'description': arg.description,
            'image': arg.image,
            'properties': final_properties
        }

        uri = self.upload_metadata(meta)
        tx = self.__abi_module.mint_nft.build_transaction(
            to_address, uri, self.get_transact_opts()
        )
        receipt = self.execute_tx(tx)
        result = self.__abi_module.get_minted_event(
            tx_hash=receipt.transactionHash.hex()
        )
        token_id = result[0]["args"]["tokenId"]
        return self.get(token_id)

    def total_supply(self) -> int:
        """
        Returns the total supply
        """
        return self.__abi_module.total_supply.call()

    def get(self, token_id: int) -> NftType:
        """
        Returns the Metadata of a token
        """
        uri = self.__get_metadata_uri(token_id)
        meta = self.get_storage().get(uri)
        meta_obj: NftType = NftType.from_json(meta)
        meta_obj.id = token_id
        meta_obj.uri = uri
        return meta_obj

    def __get_metadata_uri(self, token_id: int):
        """
        Returns the uri of the metadata of a token
        """
        uri = self.__abi_module.token_uri.call(token_id)
        if uri == "":
            raise Exception(
                "Could not find NFT metadata, are you sure it exists?")
        return uri

    def mint_batch(self, args: List[MintArg]):
        """
        Mints a batch of tokens to the signer address
        """
        return self.mint_batch_to(self.get_signer_address(), args)

    def mint_batch_to(self, to_address: str, args: List[MintArg]):
        """
        Mints a batch of tokens to the given address
        """
        uris = [self.upload_metadata({
            'name': arg.name,
            'description': arg.description,
            'image': arg.image,
            'properties': arg.properties if arg.properties is not None else {}
        }) for arg in args]

        tx = self.__abi_module.mint_nft_batch.build_transaction(
            to_address, uris, self.get_transact_opts()
        )

        receipt = self.execute_tx(tx)
        result = self.__abi_module.get_minted_batch_event(
            tx_hash=receipt.transactionHash.hex()
        )
        token_ids = result[0]["args"]["tokenIds"]
        return [self.get(i) for i in token_ids]

    def burn(self, token_id: int):
        """
        Burns a given token
        """
        tx = self.__abi_module.burn.build_transaction(
            token_id, self.get_transact_opts()
        )
        self.execute_tx(tx)

    def transfer_from(self, from_address: str, to_address: str, token_id: int):
        """
        Transfers a token from one address to another
        """
        tx = self.__abi_module.transfer_from.build_transaction(
            from_address, to_address, token_id, self.get_transact_opts()
        )
        self.execute_tx(tx)

    def transfer(self, to_address: str, token_id: int):
        """
        Transfers NFT from the current signers wallet to another wallet
        """
        tx = self.__abi_module.safe_transfer_from1.build_transaction(
            self.get_signer_address(), to_address, token_id, self.get_transact_opts()
        )
        self.execute_tx(tx)

    def set_royalty_bps(self, amount: int):
        """
        Sets the royalty percentage for the NFT
        """
        tx = self.__abi_module.set_royalty_bps.build_transaction(
            amount, self.get_transact_opts()
        )

        self.execute_tx(tx)

    def get_all(self) -> List[NftType]:
        """
        Returns all the NFTs in the system
        """
        max_id = self.__abi_module.next_token_id.call()
        return [self.get(i) for i in range(max_id)]

    def get_owned(self, address: str = "") -> List[NftType]:
        """
        Defaults to fetching the NFTs owned by the current signer (as indicated by the private key)
        if the address parameter is not supplied
        """
        if address == "":
            address = self.get_signer_address()

        balance = self.__abi_module.balance_of.call(address)
        owned_tokens = [
            self.__token_of_owner_by_index(address, i) for i in range(balance)
        ]
        return [self.get(i) for i in owned_tokens]

    def __token_of_owner_by_index(self, address: str, token_id: int) -> int:
        return self.__abi_module.token_of_owner_by_index.call(address, token_id)

    def balance(self) -> int:
        """
        Returns balance of the current signers wallet
        - Arguments: none. Method refers to nft module class.
        - Use-case: Use this method if you want to use the currently connected wallet
        - Dashboard: Project ➝ NFT Module ➝ Total amount of NFT's

        """

        return self.__abi_module.balance_of.call(self.get_signer_address())

    def balance_of(self, address: str) -> int:
        """
        Returns balance of the given addressss
        - Arguments: Pass the address of which to check the balance
        - Use-case: Use this method if you don't want to use the connected wallet, but want to check another wallet.
        - Dashboard: Project ➝ NFT Module ➝ Total amount of NFT's 
        """
        return self.__abi_module.balance_of.call(address)

    def owner_of(self, token_id: int) -> str:
        """
        Returns the owner of the given token
        """
        return self.__abi_module.owner_of.call(token_id)

    def get_metadata(self, token_id: int) -> NftType:
        """
        Returns the metadata of the given token
        """
        uri = self.__get_metadata_uri(token_id)
        meta = self.get_storage().get(uri)
        meta_obj: NftType = NftType.from_json(meta)
        meta_obj.id = token_id
        meta_obj.uri = uri
        return meta_obj

    def is_approved(self, address: str, operator: str) -> bool:
        """
        Returns whether the given address is approved
        """
        return self.__abi_module.is_approved_for_all.call(address, operator)

    def set_approval(self, operator: str, approved: bool = True):
        """
        Sets approval for specified operator, defaults to grant approval
        """
        tx = self.__abi_module.set_approval_for_all.build_transaction(
            operator, approved, self.get_transact_opts()
        )
        self.execute_tx(tx)

    def set_restricted_transfer(self, restricted: bool = True):
        self.execute_tx(
            self.__abi_module.set_restricted_transfer.build_transaction(
                restricted, self.get_transact_opts()
            )
        )

    def get_with_owner(self, token_id: int, owner: str):
        """
        Returns the NFT with the given token id and owner
        """
        owner = self.owner_of(token_id)
        meta = self.get_metadata(token_id)
        return {owner: owner, meta: meta}

    def set_module_metadata(self, metadata: str):
        """
        Sets the metadata for the module
        """
        uri = self.get_storage().upload_metadata(
            metadata, self.address, self.get_signer_address()
        )
        tx = self.__abi_module.set_contract_uri.build_transaction(
            uri, self.get_transact_opts()
        )
        self.execute_tx(tx)

    def set_restricted_transfer(self, restricted: bool = False):
        """
        Sets the restricted transfer flag
        """

        tx = self.__abi_module.set_restricted_transfer.build_transaction(
            restricted, self.get_transact_opts()
        )
        self.execute_tx(tx)

    def get_abi_module(self) -> NFT:
        return self.__abi_module
