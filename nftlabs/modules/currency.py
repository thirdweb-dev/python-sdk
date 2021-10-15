from ..errors import NoSignerException
from ..types import Role
from ..abi.coin import Coin
from .base import BaseModule
from .currency_types import Currency, CurrencyValue
from ..abi.erc20 import ERC20
from web3 import Web3
from typing import List, Dict


class CurrencyModule(BaseModule):
    address: str
    __abi_module: Coin

    def __init__(self, address: str, client: Web3):
        super().__init__()
        self.address = address
        self.__abi_module = Coin(client, address)

    def total_supply(self) -> int:
        return self.__abi_module.total_supply.call()

    """
    Gets the currency name, symbol, and decimals
    """

    def get(self) -> Currency:
        return self.__get_currency_metadata(self.address)

    def balance_of(self, address: str) -> int:
        return self.__abi_module.balance_of.call(address)

    def balance(self):
        return self.__abi_module.balance_of.call(self.get_signer_address())

    def allowance(self, spender: str) -> int:
        return self.__abi_module.allowance.call(self.get_signer_address(), spender)

    def allowance_of(self, owner: str, spender: str) -> int:
        return self.__abi_module.allowance.call(owner, spender)

    def set_allowance(self, spender: str, amount: int):
        return self.execute_tx(self.__abi_module.approve.build_transaction(
            spender, amount, self.get_transact_opts()
        ))

    def mint_to(self, to: str, amount: int):
        return self.execute_tx(self.__abi_module.mint.build_transaction(
            to, amount, self.get_transact_opts()
        ))

    def mint(self, amount: int):
        return self.execute_tx(self.__abi_module.mint.build_transaction(
            self.get_signer_address(), amount, self.get_transact_opts()
        ))

    def burn(self, amount: int):
        return self.execute_tx(self.__abi_module.burn.build_transaction(
            amount, self.get_transact_opts()
        ))

    def burn_from(self, from_address: str, amount: int):
        return self.execute_tx(self.__abi_module.burn_from.build_transaction(
            from_address, amount, self.get_transact_opts()
        ))

    def transfer_from(self, from_address: str, to_address: str, amount: int):
        return self.execute_tx(self.__abi_module.transfer_from.build_transaction(
            from_address, to_address, amount, self.get_transact_opts()
        ))

    def grant_role(self, role: Role, address: str):
        role_hash = role.get_hash()
        self.execute_tx(self.__abi_module.grant_role.build_transaction(
            role_hash, address, self.get_transact_opts()
        ))

    def revoke_role(self, role: Role, address: str):
        role_hash = role.get_hash()

        try:
            signer_address = self.get_signer_address()
            if signer_address.lower() != address.lower():
                pass
            self.execute_tx(self.__abi_module.renounce_role.build_transaction(
                role_hash, address, self.get_transact_opts()
            ))
            return
        except NoSignerException:
            pass

        self.execute_tx(self.__abi_module.revoke_role.build_transaction(
            role_hash, address, self.get_transact_opts()
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

    def get_value(self, value: int) -> Currency:
        return self.__get_currency_value(self.address, value)

    def __get_currency_value(self, asset_address: str, price: int) -> CurrencyValue:
        metadata = self.__get_currency_metadata(asset_address)
        return CurrencyValue(
            name=metadata.name,
            decimals=metadata.decimals,
            symbol=metadata.symbol,
            value=str(price),
            display_value=self.format_units(price, metadata.decimals)
        )

    @staticmethod
    def format_units(value: int, decimals: int) -> str:
        decimal_transformer = float(10**decimals)
        val = float(value) / decimal_transformer
        return f'{val:.{decimals}f}'

    def __get_currency_metadata(self, asset_address: str) -> Currency:
        if asset_address.lower().startswith("0x0000000000000000000000000000000000000000"):
            return Currency(name="", symbol="", decimals=0)

        erc20_module = ERC20(self.get_client(), asset_address)
        return Currency(
            name=erc20_module.name.call(),
            symbol=erc20_module.symbol.call(),
            decimals=erc20_module.decimals.call()
        )
