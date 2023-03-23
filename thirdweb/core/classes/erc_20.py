from typing import List
from thirdweb.abi.token_erc20 import TokenERC20
from thirdweb.common.currency import (
    fetch_currency_metadata,
    fetch_currency_value,
    parse_units,
)
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.constants.role import Role, get_role_hash
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.currency import (
    Currency,
    CurrencyValue,
    Price,
    PriceWei,
    TokenAmount,
)
from web3.eth import TxReceipt


class ERC20(BaseContract[TokenERC20]):
    _storage: IpfsStorage

    def __init__(
        self,
        contract_wrapper: ContractWrapper,
        storage: IpfsStorage,
    ):
        super().__init__(contract_wrapper)
        self._storage = storage

    """
    READ FUNCTIONS
    """

    def get(self) -> Currency:
        """
        Get token metadata

        ```python
        token = contract.erc20.get()
        print(token)
        ```

        :extension: ERC20
        :returns: token metadata
        """

        return fetch_currency_metadata(
            self._contract_wrapper.get_provider(), self.get_address()
        )

    def balance(self) -> CurrencyValue:
        """
        Get token balance

        ```python
        balance = contract.erc20.balance()
        print(balance)
        ```

        :extension: ERC20
        :returns: balance of the connected wallet
        """

        return self.balance_of(self._contract_wrapper.get_signer_address())

    def balance_of(self, address: str) -> CurrencyValue:
        """
        Get token balance of a specific wallet

        ```python
        address = "{{wallet_address}}"
        balance = contract.erc20.balance_of(address)
        print(balance)
        ```

        :extension: ERC20
        :param address: wallet address to check the balance of
        :returns: balance of the specified wallet
        """

        return self._get_value(
            self._contract_wrapper._contract_abi.balance_of.call(address)
        )

    def total_supply(self) -> CurrencyValue:
        """
        Get the total minted supply

        ```python
        supply = contract.erc20.total_supply()
        print(supply)
        ```

        :extension: ERC20
        :returns: total minted supply of the token
        """

        return self._get_value(self._contract_wrapper._contract_abi.total_supply.call())

    def allowance(self, spender: str) -> CurrencyValue:
        """
        Get the allowance of a specific spender

        ```python
        spender = "{{wallet_address}}"
        allowance = contract.erc20.allowance(spender)
        print(allowance)
        ```

        :extension: ERC20
        :param spender: wallet address to check the allowance of
        :returns: allowance of the connected wallet
        """

        return self.allowance_of(self._contract_wrapper.get_signer_address(), spender)

    def allowance_of(self, owner: str, spender: str) -> CurrencyValue:
        """
        Get the allowance of a spender for a specific owner

        ```python
        # Address of the wallet who owns the funds
        address = "{{wallet_address}}"

        # Address of the wallet to check the token allowance
        spender = "0x..."

        allowance = contract.erc20.allowance_of(address, spender)
        print(allowance)
        ```

        :extension: ERC20
        :param owner: wallet address whose assets will be spent
        :param spender: wallet address to check the allowance of
        :returns: allowance of the specified spender for the specified owner
        """

        return self._get_value(
            self._contract_wrapper._contract_abi.allowance.call(owner, spender)
        )

    def is_transfer_restricted(self) -> bool:
        """
        Check whether transfer is restricted for tokens in this module

        ```python
        is_restricted = contract.erc20.is_transfer_restricted()
        print(is_restricted)
        ```

        :returns: True if transfer is restricted, False otherwise
        """

        anyone_can_transfer = self._contract_wrapper._contract_abi.has_role.call(
            get_role_hash(Role.TRANSFER), ZERO_ADDRESS
        )

        return not anyone_can_transfer

    """
    WRITE FUNCTIONS
    """

    def mint(self, amount: Price) -> TxReceipt:
        """
        Mint tokens

        ```python
        address = "{{wallet_address}}"
        amount = 100

        receipt = contract.erc20.mint(amount)
        ```

        :extension: ERC20Mintable
        :param amount: amount of tokens to mint
        :returns: transaction receipt of the mint
        """

        return self.mint_to(self._contract_wrapper.get_signer_address(), amount)

    def mint_to(self, to: str, amount: Price) -> TxReceipt:
        """
        Mint tokens to a specific wallet

        ```python
        address = "{{wallet_address}}"
        amount = 100

        receipt = contract.erc20.mint_to(address, amount)
        ```

        :extension: ERC20Mintable
        :param to: wallet address to mint tokens to
        :param amount: amount of tokens to mint
        :returns: transaction receipt of the mint
        """

        amount_with_decimals = parse_units(amount, self.get().decimals)
        return self._contract_wrapper.send_transaction(
            "mint_to", [to, amount_with_decimals]
        )

    def mint_batch_to(self, args: List[TokenAmount]) -> TxReceipt:
        """
        Mint tokens to many wallets

        ```python
        from thirdweb.types.currency import TokenAmount

        args = [
            TokenAmount("{{wallet_address}}", 1),
            TokenAmount("{{wallet_address}}", 2),
        ]

        :extension: ERC20BatchMintable
        contract.erc20.mint_batch_to(args)
        ```

        :param args: list of wallet addresses and amounts to mint
        :returns: transaction receipt of the mint
        """

        encoded = []
        interface = self._contract_wrapper.get_contract_interface()
        for arg in args:
            encoded.append(
                interface.encodeABI(
                    "mintTo",
                    [arg.to_address, parse_units(arg.amount, self.get().decimals)],
                )
            )
        return self._contract_wrapper.multi_call(encoded)

    def transfer(self, to: str, amount: Price) -> TxReceipt:
        """
        Transfer tokens

        ```python
        # Address to send tokens to
        to = "0x...

        # Amount of tokens to transfer
        amount = 0.1

        contract.erc20.transfer(to, amount)
        ```

        :extension: ERC20
        :param to: wallet address to transfer the tokens to
        :param amount: amount of tokens to transfer
        :returns: transaction receipt of the transfer
        """

        amount_with_decimals = parse_units(amount, self.get().decimals)
        return self._contract_wrapper.send_transaction(
            "transfer", [to, amount_with_decimals]
        )

    def transfer_from(self, fr: str, to: str, amount: Price) -> TxReceipt:
        """
        Transfer tokens from a specific wallet

        ```python
        # Address to send tokens from
        fr = "{{wallet_address}}"

        # Address to send tokens to
        to = "0x..."

        # Amount of tokens to transfer
        amount = 0.1

        contract.erc20.transfer_from(fr, to, amount)
        ```

        :extension: ERC20
        :param fr: wallet address to transfer the tokens from
        :param to: wallet address to transfer the tokens to
        :param amount: amount of tokens to transfer
        :returns: transaction receipt of the transfer
        """

        amount_with_decimals = parse_units(amount, self.get().decimals)
        return self._contract_wrapper.send_transaction(
            "transfer_from", [fr, to, amount_with_decimals]
        )

    def set_allowance(self, spender: str, amount: Price) -> TxReceipt:
        """
        Approve a specific wallet to spend tokens

        ```python
        spender = "0x..."
        amount = 100
        contract.erc20.set_allowance(spender, amount)
        ```

        :extension: ERC20
        :param spender: wallet address to set the allowance of
        :param amount: amount to set the allowance to
        :returns: transaction receipt of the allowance set
        """

        amount_with_decimals = parse_units(amount, self.get().decimals)
        return self._contract_wrapper.send_transaction(
            "approve", [spender, amount_with_decimals]
        )

    def transfer_batch(self, args: List[TokenAmount]):
        """
        Transfer tokens to many wallets

        ```python
        from thirdweb.types.currency import TokenAmount

        data = [
            TokenAmount("{{wallet_address}}", 0.1),
            TokenAmount("0x...", 0.2),
        ]

        contract.erc20.transfer_batch(data)
        ```

        :param args: list of token amounts and addressed to transfer to
        :returns: transaction receipt of the transfers
        """

        encoded = []
        interface = self._contract_wrapper.get_contract_interface()

        for arg in args:
            amount_with_decimals = self.normalize_amount(arg.amount)
            encoded.append(
                interface.encodeABI("transfer", [arg.to_address, amount_with_decimals])
            )

        return self._contract_wrapper.multi_call(encoded)

    def burn(self, amount: Price) -> TxReceipt:
        """
        Burn tokens

        ```python
        amount = 0.1
        contract.erc20.burn(amount)
        ```

        :extension: ERC20Burnable
        :param amount: amount of tokens to burn
        :returns: transaction receipt of the burn
        """

        amount_with_decimals = parse_units(amount, self.get().decimals)
        return self._contract_wrapper.send_transaction("burn", [amount_with_decimals])

    def burn_from(self, holder: str, amount: Price) -> TxReceipt:
        """
        Burn tokens from a specific wallet

        ```python
        holder = "{{wallet_address}}"
        amount = 0.1
        contract.erc20.burn_from(holder, amount)
        ```

        :extension: ERC20Burnable
        :param holder: wallet address to burn the tokens from
        :param amount: amount of tokens to burn
        :returns: transaction receipt of the burn
        """

        amount_with_decimals = parse_units(amount, self.get().decimals)
        return self._contract_wrapper.send_transaction(
            "burn_from", [holder, amount_with_decimals]
        )

    """
    INTERNAL FUNCTIONS
    """

    def _get_value(self, value: PriceWei) -> CurrencyValue:
        return fetch_currency_value(
            self._contract_wrapper.get_provider(),
            self.get_address(),
            value,
        )

    def normalize_amount(self, amount: Price) -> PriceWei:
        decimals = self.get().decimals
        return parse_units(amount, decimals)
