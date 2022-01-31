"""
Interact with the Currency module of the app.
"""
from thirdweb.errors import RestrictedTransferError
from thirdweb_web3 import Web3

from ..abi.coin import Coin
from ..abi.erc20 import ERC20
from ..types.currency import Currency, CurrencyValue
from .base import BaseModule


class CurrencyModule(BaseModule):
    """
    Interact with the Currency module of the app.
    """

    address: str
    """
    Address of the module
    """
    __abi_module: Coin

    def __init__(self, address: str, client: Web3):
        """
        :param address: The address of the module
        :param client: Web3 client

        Initializes the module
        """
        super().__init__()
        self.address = address
        """ The address of the Currency contract """
        self.__abi_module = Coin(client, address)

    def total_supply(self) -> int:
        """
        :return: The total supply of the currency

        Gets the total supply of the currency

        """
        return self.__abi_module.total_supply.call()

    def get(self) -> Currency:
        """
        :return: The currency name, symbol, and decimals

        Gets the currency name, symbol, and decimals

        """
        return self.__get_currency_metadata(self.address)

    def balance_of(self, address: str) -> int:
        """
        :param address: The address to get the balance of
        :return: The balance of the given address

        Gets the balance of the given address

        """
        return self.__abi_module.balance_of.call(address)

    def balance(self) -> int:
        """ 
        :return: The balance of the current address

        Gets the balance of the current address
        """
        return self.__abi_module.balance_of.call(self.get_signer_address())

    def allowance(self, spender: str) -> int:
        """ 
        :param spender: The address to get the allowance of
        :return: The allowance of the current address

        Gets the allowance of the current address

        """
        return self.__abi_module.allowance.call(self.get_signer_address(), spender)

    def allowance_of(self, owner: str, spender: str) -> int:
        """ 
        :param owner: The address to get the allowance of
        :param spender: The address to get the allowance of
        :return: The allowance of the current address

        Gets the allowance of the current address

        """
        return self.__abi_module.allowance.call(owner, spender)

    def set_allowance(self, spender: str, amount: int):
        """ 
        :param spender: The address to set the allowance of
        :param amount: The amount to set the allowance to
        :return: The transaction receipt

        Sets the allowance of the current address
        """
        return self.execute_tx(self.__abi_module.approve.build_transaction(
            spender, amount, self.get_transact_opts()
        ))

    def mint_to(self, to: str, amount: int):
        """ 
        :param to: The address to mint to
        :param amount: The amount to mint

        Mints the given amount to the given address

        """
        return self.execute_tx(self.__abi_module.mint.build_transaction(
            to, amount, self.get_transact_opts()
        ))

    def mint(self, amount: int):
        """ 
        :param amount: The amount to mint
        :return: The transaction hash

        Mints the given amount to the current address

        """
        return self.execute_tx(self.__abi_module.mint.build_transaction(
            self.get_signer_address(), amount, self.get_transact_opts()
        ))

    def burn(self, amount: int):
        """ 
        :param amount: The amount to burn
        :return: The transaction hash

        Burns the given amount from the current address

        """
        return self.execute_tx(self.__abi_module.burn.build_transaction(
            amount, self.get_transact_opts()
        ))

    def burn_from(self, from_address: str, amount: int):
        """ 
        :param from_address: The address to burn from
        :param amount: The amount to burn
        :return: The transaction hash

        Burns the given amount from the current address

        """
        return self.execute_tx(self.__abi_module.burn_from.build_transaction(
            from_address, amount, self.get_transact_opts()
        ))

    def transfer(self, to_address: str, amount: int):
        """ 
        :param to_address: The address to transfer to
        :param amount: The amount to transfer

        Transfers the given amount from the current address
        """
        if(self.__abi_module.is_restricted_transfer.call()):
            raise RestrictedTransferError(self.address)
        return self.execute_tx(self.__abi_module.transfer.build_transaction(
            self.get_signer_address(), to_address, amount, self.get_transact_opts()
        ))

    def transfer_from(self, from_address: str, to_address: str, amount: int):
        """ 
        :param from_address: The address to transfer from
        :param to_address: The address to transfer to
        :param amount: The amount to transfer

        Transfers the given amount from the current address
        """
        return self.execute_tx(self.__abi_module.transfer_from.build_transaction(
            from_address, to_address, amount, self.get_transact_opts()
        ))

    def set_module_metadata(self, metadata: str):
        """
        :param metadata: The metadata to set
        :return: The transaction hash

        Sets the metadata for the module
        """
        uri = self.get_storage().upload_metadata(
            metadata, self.address, self.get_signer_address())
        self.execute_tx(self.__abi_module.set_contract_uri.build_transaction(
            uri, self.get_transact_opts()
        ))

    def get_value(self, value: int) -> Currency:
        """ 
        :param value: The value to get
        :return: The value of the given amount

        Gets the value of the given amount

        """
        return self.__get_currency_value(self.address, value)

    def __get_currency_value(self, asset_address: str, price: int) -> CurrencyValue:
        """ 
        :param asset_address: The address of the asset
        :param price: The price of the asset

        Gets the value of the given amount

        """
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
        """ 
        :param value: The value to format
        :param decimals: The number of decimals
        :return: The formatted amount

        Formats the given amount

        """
        decimal_transformer = float(10**decimals)
        val = float(value) / decimal_transformer
        return f'{val:.{decimals}f}'

    def __get_currency_metadata(self, asset_address: str) -> Currency:
        """ 
        Gets the metadata of the given asset
        """
        if asset_address.lower().startswith("0x0000000000000000000000000000000000000000"):
            return Currency(name="", symbol="", decimals=0)

        erc20_module = ERC20(self.get_client(), asset_address)
        return Currency(
            name=erc20_module.name.call(),
            symbol=erc20_module.symbol.call(),
            decimals=erc20_module.decimals.call()
        )

    def set_restricted_transfer(self, restricted: bool = True):
        """
        :param restricted: Whether to grant restricted transfer or revoke it

        Sets restricted transfer for the NFT, defaults to restricted.

        """
        self.execute_tx(
            self.__abi_module.set_restricted_transfer.build_transaction(
                restricted, self.get_transact_opts()
            )
        )

    def get_abi_module(self) -> Coin:
        """
        :return: The ABI for the Coin contract

        Gets the ABI module
        """
        return self.__abi_module
