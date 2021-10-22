from typing import List, Dict

from zero_ex.contract_wrappers import TxParams

from .base import BaseModule
from ..types.nft import NftMetadata
from ..errors import NoSignerException
from ..types.role import Role
from ..abi.nft_collection import NFTCollection
from web3 import Web3

from ..types.collection import CollectionMetadata


class CollectionModule(BaseModule):
    address: str
    __abi_module: NFTCollection

    def __init__(self, address: str, client: Web3):
        super().__init__()
        self.address = address
        self.__abi_module = NFTCollection(client, address)

    def get(self, token_id: int) -> CollectionMetadata:
        uri = self.__abi_module.uri.call(token_id, TxParams(from_=self.address))
        meta_str = self.get_storage().get(uri)
        meta: NftMetadata = NftMetadata.from_json(meta_str)
        meta.id = token_id
        return CollectionMetadata(
            metadata=meta,
            supply=self.__abi_module.total_supply.call(token_id, TxParams(from_=self.address)),
            creator=self.__abi_module.creator.call(token_id, TxParams(from_=self.address)),
            id=token_id
        )

    def get_all(self) -> List[CollectionMetadata]:
        return [self.get(i) for i in range(self.__abi_module.next_token_id.call(TxParams(from_=self.address)))]

    '''
    Returns the balance for a given token at owned by a specific address
    '''
    def balance_of(self, address: str, token_id: int) -> int:
        return self.__abi_module.balance_of.call(address, token_id, TxParams(from_=self.address))

    '''
    Returns the balance for a given token id for the current signers address
    '''
    def balance(self, token_id: int) -> int:
        return self.__abi_module.balance_of.call(
            self.__get_signer_address(),
            token_id,
            TxParams(from_=self.address)
        )

    def is_approved(self, address: str, operator: str) -> bool:
        return self.__abi_module.is_approved_for_all.call(
            address,
            operator,
            TxParams(from_=self.address)
        )

    def set_approval(self, operator: str, approved: bool = True):
        self.execute_tx(self.__abi_module.set_approval_for_all.build_transaction(
            operator, approved, self.__get_transact_opts()
        ))

    def transfer(self, to_address: str, token_id: int, amount: int):
        self.execute_tx(self.__abi_module.safe_transfer_from.build_transaction(
            self.__get_signer_address(), to_address, token_id, amount, "", self.__get_transact_opts()
        ))

    def create(self, metadata) -> CollectionMetadata:
        pass

    def create_batch(self, metas) -> List[CollectionMetadata]:
        pass

    def create_and_mint(self, meta_with_supply) -> List[CollectionMetadata]:
        pass

    def create_with_erc20(self, token_contract: str, token_amount: int, metadata):
        pass

    def create_with_erc721(self, token_contract: str, token_id: int, metadata):
        pass

    def mint(self, args):
        pass

    def mint_to(self, to_address: str, args):
        pass

    def mint_batch(self, args):
        pass

    def mint_batch_to(self, to_address, args):
        pass

    def burn(self, args):
        pass

    def burn_batch(self, args):
        pass

    def burn_from(self, account: str, args):
        pass

    def burn_batch_from(self, account: str, args):
        pass

    def transfer_from(self, from_address: str, to_address: str, args):
        pass

    def transfer_batch_from(self, from_address: str, to_address: str, args):
        pass

    def set_royalty_bps(self, amount: int):
        self.execute_tx(self.__abi_module.set_royalty_bps.build_transaction(
            amount, self.__get_transact_opts()
        ))

    def grant_role(self, role: Role, address: str):
        role_hash = role.get_hash()
        self.execute_tx(self.__abi_module.grant_role.build_transaction(
            role_hash, address, self.__get_transact_opts()
        ))

    def revoke_role(self, role: Role, address: str):
        role_hash = role.get_hash()

        try:
            signer_address = self.__get_signer_address()
            if signer_address.lower() != address.lower():
                pass
            self.execute_tx(self.__abi_module.renounce_role.build_transaction(
                role_hash, address, self.__get_transact_opts()
            ))
            return
        except NoSignerException:
            pass

        self.execute_tx(self.__abi_module.revoke_role.build_transaction(
            role_hash, address, self.__get_transact_opts()
        ))

    def get_role_members(self, role: Role) -> List[str]:
        role_hash = role.get_hash()
        count = self.__abi_module.get_role_member_count.call(role_hash)
        return [self.__abi_module.get_role_member.call(role_hash, i) for i in range(count)]

    def get_all_role_members(self) -> Dict[Role, List[str]]:
        return {
            Role.admin.name: self.get_role_members(Role.admin),
            Role.minter.name: self.get_role_members(Role.minter),
            Role.transfer.name: self.get_role_members(Role.transfer),
            Role.pauser.name: self.get_role_members(Role.pauser)
        }
