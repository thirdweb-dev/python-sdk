"""Base Module."""

from abc import ABC, abstractmethod
from typing import Callable, Dict, List, Optional, Union, cast

from eth_account.account import LocalAccount
from thirdweb_web3 import Web3
from thirdweb_web3.types import TxReceipt
from zero_ex.contract_wrappers import TxParams
import json
from ..abi.coin import Coin
from ..abi.erc165 import ERC165
from ..abi.market import Market
from ..abi.nft import NFT
from ..abi.nft_collection import NFTCollection as NFTBundle
from ..abi.pack import Pack
from ..constants.erc_interfaces import InterfaceIdErc721, InterfaceIdErc1155
from ..errors import NoSignerException
import io
from ..options import SdkOptions
from ..storage import IpfsStorage
from ..types.role import Role

ModuleTypes = Union[NFT, Market, Pack, NFTBundle, Coin]


class BaseModule(ABC):
    """
    Base module for all modules.
    """
    get_client: Optional[Callable[[], Web3]]
    """ Returns the client object. """
    get_storage: Optional[Callable[[], IpfsStorage]]
    """ Returns the storage object. """
    get_signer_address: Optional[Callable[[], str]]
    """ Returns the signer address. """
    get_private_key: Optional[Callable[[], str]]
    """ Returns the private key. """
    get_transact_opts: Optional[Callable[[], TxParams]]
    """ Returns the transaction options. """
    get_account: Optional[Callable[[], LocalAccount]]
    """ Returns the account object. """
    get_options: Optional[Callable[[], SdkOptions]]
    """ Returns the options object. """

    def __init__(self):
        self.get_client = None
        self.get_storage = None
        self.get_signer_address = None
        self.get_private_key = None
        self.get_transact_opts = None
        self.get_account = None
        self.get_options = None

    def execute_tx(self, tx) -> TxReceipt:
        """
        Execute a transaction and return the receipt.
        """
        client = self.get_client()
        nonce = client.eth.get_transaction_count(self.get_signer_address())
        tx['nonce'] = nonce
        del tx['from']
        signed_tx = self.__sign_tx(tx)
        tx_hash = client.eth.send_raw_transaction(signed_tx.rawTransaction)
        return cast(
            TxReceipt,
            client.eth.wait_for_transaction_receipt(
                tx_hash, timeout=self.get_options().tx_timeout_in_seconds)
        )

    def __sign_tx(self, tx):
        """
        Sign a transaction.
        """
        signed_tx = self.get_account().sign_transaction(tx)
        return signed_tx

    def grant_role(self, role: Role, address: str):
        """
        Grants the given role to the given address
        """

        role_hash = role.get_hash()
        tx = self.__abi_module.grant_role.build_transaction(
            role_hash, address,
            self.get_transact_opts()
        )
        self.execute_tx(tx)

    @abstractmethod
    def get_abi_module(self) -> ModuleTypes:
        pass

    def grant_role(self, role: Role, address: str):
        """
        Grants the given role to the given address
        """

        role_hash = role.get_hash()
        tx = self.get_abi_module().grant_role.build_transaction(
            role_hash, address,
            self.get_transact_opts()
        )
        self.execute_tx(tx)

    def upload_metadata(self, data: Union[Dict, str]) -> str:
        """
        Uploads the metadata to IPFS and returns the uri.
        """
        storage = self.get_storage()
        if isinstance(data, str) and data.startswith("ipfs://"):
            return data

        if 'image_uri' in data and data["image"] == "":
            data["image"] = data["image_uri"]

        if 'image' in data:
            if isinstance(data["image"], bytes) or isinstance(data["image"], bytearray):
                data["image"] = storage.upload(
                    data["image"], self.address, self.get_signer_address())

        return storage.upload(json.dumps(data), self.address, self.get_signer_address())

    def revoke_role(self, role: Role, address: str):
        """
        Revokes the given role from the given address
        """
        role_hash = role.get_hash()
        try:
            signer_address = self.get_signer_address()
            if signer_address.lower() == address.lower():
                self.execute_tx(self.get_abi_module().renounce_role.build_transaction(
                    role_hash, address, self.get_transact_opts()
                ))
                return
        except NoSignerException:
            pass

        self.execute_tx(self.get_abi_module().revoke_role.build_transaction(
            role_hash, address, self.get_transact_opts()
        ))

    def get_role_member_count(self, role: Role):
        """
        Returns the number of members in the given role
        """
        return self.get_abi_module().get_role_member_count.call(role.get_hash())

    def get_role_members(self, role: Role) -> List[str]:
        """
        Returns the members of the given role
        """
        return [self.get_role_member(role, x) for x in range(self.get_role_member_count(role))]

    def get_role_member(self, role: Role, index: int) -> str:
        """
        Returns the member at the given index of the given role
        """
        return self.get_abi_module().get_role_member.call(role.get_hash(), index)

    def get_all_role_members(self) -> Dict[str, List[str]]:
        """
        Returns all the members of all the roles
        """
        return {
            Role.admin.name: self.get_role_members(Role.admin),
            Role.minter.name: self.get_role_members(Role.minter),
            Role.transfer.name: self.get_role_members(Role.transfer),
            Role.pauser.name: self.get_role_members(Role.pauser)
        }

    def is_erc721(self, address: str) -> bool:
        erc165 = ERC165(self.get_client(), address)
        return erc165.supports_interface.call(InterfaceIdErc721)

    def is_erc1155(self, address: str) -> bool:
        erc165 = ERC165(self.get_client(), address)
        return erc165.supports_interface.call(InterfaceIdErc1155)

    def __get_token_uri(self, token_id: int) -> ModuleTypes:
        module = self.get_abi_module()
        uri = ""
        try:
            uri = module.token_uri(token_id)
        except:
            pass
        if uri != "":
            return uri
        try:
            uri = module.uri(token_id)
        except:
            pass
        return uri
