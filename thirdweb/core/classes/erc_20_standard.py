from typing import List
from thirdweb.abi.token_erc20 import TokenERC20
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.erc_20 import ERC20
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.currency import (
    Currency,
    CurrencyValue,
    Price,
    TokenAmount,
)
from web3.eth import TxReceipt

class ERC20Standard(BaseContract[TokenERC20]):
    _storage: IpfsStorage
    _erc20: ERC20

    def __init__(self, contract_wrapper: ContractWrapper, storage: IpfsStorage):
        super().__init__(contract_wrapper)
        self._storage = storage
        self._erc20 = ERC20(contract_wrapper, storage)

    def get(self) -> Currency:
        """
        Get the token metadata including name, symbol, decimals, etc.

        ```python
        token = contract.get()
        print(token)
        ```

        :returns: token metadata
        """

        return self._erc20.get()

    def balance(self) -> CurrencyValue:
        """
        Get the token balance of the connected wallet.

        ```python
        balance = contract.balance()
        print(balance)
        ```

        :returns: balance of the connected wallet
        """

        return self._erc20.balance()

    def balance_of(self, address: str) -> CurrencyValue:
        """
        Get the balance of the specified wallet

        ```python
        address = "{{wallet_address}}"
        balance = contract.balance_of(address)
        print(balance)
        ```

        :param address: wallet address to check the balance of
        :returns: balance of the specified wallet
        """

        return self._erc20.balance_of(address)

    def total_supply(self) -> CurrencyValue:
        """
        Get the total minted supply of the token.

        :returns: total minted supply of the token
        """

        return self._erc20.total_supply()

    def allowance(self, spender: str) -> CurrencyValue:
        """
        Get a specific spenders allowance of this token for the connected wallet.

        ```python
        spender = "{{wallet_address}}"
        allowance = contract.allowance(spender)
        ```

        :param spender: wallet address to check the allowance of
        :returns: allowance of the connected wallet
        """

        return self._erc20.allowance(spender)

    def allowance_of(self, owner: str, spender: str) -> CurrencyValue:
        """
        Get the allowance of the specified spender for a specified owner.

        ```python
        # Address of the wallet who owns the funds
        address = "{{wallet_address}}"

        # Address of the wallet to check the token allowance
        spender = "0x..."

        allowance = contract.allowance_of(address, spender)
        print(allowance)
        ```

        :param owner: wallet address whose assets will be spent
        :param spender: wallet address to check the allowance of
        :returns: allowance of the specified spender for the specified owner
        """

        return self._erc20.allowance_of(owner, spender)

    def is_transfer_restricted(self) -> bool:
        """
        Check whether transfer is restricted for tokens in this module.

        :returns: True if transfer is restricted, False otherwise
        """

        return self._erc20.is_transfer_restricted()

    """
    WRITE FUNCTIONS
    """

    def transfer(self, to: str, amount: Price) -> TxReceipt:
        """
        Transfer a specified amount of tokens from the connected wallet to a specified address.

        ```python
        # Address to send tokens to
        to = "0x...

        # Amount of tokens to transfer
        amount = 0.1

        contract.transfer(to, amount)
        ```

        :param to: wallet address to transfer the tokens to
        :param amount: amount of tokens to transfer
        :returns: transaction receipt of the transfer
        """

        return self._erc20.transfer(to, amount)

    def transfer_from(self, fr: str, to: str, amount: Price) -> TxReceipt:
        """
        Transfer a specified amount of tokens from one specified address to another.

        ```python
        # Address to send tokens from
        fr = "{{wallet_address}}"

        # Address to send tokens to
        to = "0x..."

        # Amount of tokens to transfer
        amount = 0.1

        contract.transfer_from(fr, to, amount)
        ```

        :param fr: wallet address to transfer the tokens from
        :param to: wallet address to transfer the tokens to
        :param amount: amount of tokens to transfer
        :returns: transaction receipt of the transfer
        """

        return self._erc20.transfer_from(fr, to, amount)

    def set_allowance(self, spender: str, amount: Price) -> TxReceipt:
        """
        Sets the allowance of the specified wallet over the connected wallets funds to
        a specified amount.

        ```python
        spender = "0x..."
        amount = 100
        contract.set_allowance(spender, amount)
        ```

        :param spender: wallet address to set the allowance of
        :param amount: amount to set the allowance to
        :returns: transaction receipt of the allowance set
        """

        return self._erc20.set_allowance(spender, amount)

    def transfer_batch(self, args: List[TokenAmount]):
        """
        Transfer tokens from the connected wallet to many wallets.

        ```python
        from thirdweb.types.currency import TokenAmount

        data = [
            TokenAmount("{{wallet_address}}", 0.1),
            TokenAmount("0x...", 0.2),
        ]

        contract.transfer_batch(data)
        ```

        :param args: list of token amounts and addressed to transfer to
        :returns: transaction receipt of the transfers
        """

        return self._erc20.transfer_batch(args)

    def burn(self, amount: Price) -> TxReceipt:
        """
        Burn a specified amount of tokens from the connected wallet.

        ```python
        amount = 0.1
        contract.burn(amount)
        ```

        :param amount: amount of tokens to burn
        :returns: transaction receipt of the burn
        """

        return self._erc20.burn(amount)

    def burn_from(self, holder: str, amount: Price) -> TxReceipt:
        """
        Burn a specified amount of tokens from a specified wallet.

        ```python
        holder = "{{wallet_address}}"
        amount = 0.1
        contract.burn_from(holder, amount)
        ```

        :param holder: wallet address to burn the tokens from
        :param amount: amount of tokens to burn
        :returns: transaction receipt of the burn
        """

        return self._erc20.burn_from(holder, amount)