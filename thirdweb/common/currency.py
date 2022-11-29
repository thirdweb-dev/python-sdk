from thirdweb.constants.chains import ChainId
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.types.currency import Currency, CurrencyValue, Price, PriceWei
from thirdweb.abi import TokenERC20, IERC20
from thirdweb.constants.currency import (
    NATIVE_TOKEN_ADDRESS,
    ZERO_ADDRESS,
    get_native_token_by_chain_id,
)
from web3.constants import MAX_INT
from zero_ex.contract_wrappers.tx_params import TxParams

from web3 import Web3


def is_native_token(token_address: str) -> bool:
    return (
        token_address.lower() == ZERO_ADDRESS
        or token_address.lower() == NATIVE_TOKEN_ADDRESS.lower()
    )


def parse_units(token_value: Price, decimals: int) -> PriceWei:
    return int(token_value * (10**decimals))


def format_units(wei_value: PriceWei, decimals: int) -> Price:
    return wei_value / (10**decimals)


def fetch_currency_metadata(provider: Web3, asset: str) -> Currency:
    if is_native_token(asset):
        chain_id = provider.eth.chain_id
        native_token = get_native_token_by_chain_id(ChainId(chain_id))
        return Currency(native_token.name, native_token.symbol, native_token.decimals)

    abi = TokenERC20(provider, asset)
    return Currency(abi.name.call(), abi.symbol.call(), abi.decimals.call())


def fetch_currency_value(provider: Web3, asset: str, price: PriceWei) -> CurrencyValue:
    metadata = fetch_currency_metadata(provider, asset)
    return CurrencyValue(
        metadata.name,
        metadata.symbol,
        metadata.decimals,
        price,
        format_units(price, metadata.decimals),
    )

def convert_to_readable_quantity(value: int, decimals: int) -> str:
    if value == int(MAX_INT, 0):
        return "unlimited"
    return str(format_units(value, decimals))

def convert_quantity_to_number(quantity: str, decimals: int) -> int:
    if quantity == "unlimited":
        return int(MAX_INT, 0)
    return parse_units(float(quantity), decimals)



def normalize_price_value(
    provider: Web3, input_price: Price, currency_address: str
) -> PriceWei:
    metadata = fetch_currency_metadata(provider, currency_address)
    return parse_units(input_price, metadata.decimals)


def set_erc20_allowance(
    contract_to_approve: ContractWrapper,
    value: int,
    currency_address: str,
    overrides: TxParams,
):
    if is_native_token(currency_address):
        overrides.value = value
    else:
        signer = contract_to_approve.get_signer()
        provider = contract_to_approve.get_provider()

        abi = IERC20(provider, currency_address)
        erc20 = ContractWrapper[IERC20](abi, provider, signer)

        owner = contract_to_approve.get_signer_address()
        spender = contract_to_approve._contract_abi.contract_address
        allowance = erc20._contract_abi.allowance.call(owner, spender)

        if allowance < value:
            erc20.send_transaction("approve", [spender, value])

        return overrides


def approve_erc20_allowance(
    contract_to_approve: ContractWrapper,
    currency_address: str,
    price: PriceWei,
    quantity: int,
):
    signer = contract_to_approve.get_signer()
    provider = contract_to_approve.get_provider()

    abi = IERC20(provider, currency_address)
    erc20 = ContractWrapper[IERC20](abi, provider, signer)

    owner = contract_to_approve.get_signer_address()
    spender = contract_to_approve._contract_abi.contract_address
    allowance = erc20._contract_abi.allowance.call(owner, spender)
    total_price = price * quantity

    if allowance < total_price:
        erc20.send_transaction("approve", [spender, allowance + total_price])


def has_erc20_allowance(
    contract_to_approve: ContractWrapper,
    currency_address: str,
    value: int,
):
    provider = contract_to_approve.get_provider()
    erc20 = TokenERC20(provider, currency_address)
    owner = contract_to_approve.get_signer_address()
    spender = contract_to_approve._contract_abi.contract_address
    allowance = erc20.allowance.call(owner, spender)
    return allowance >= value
