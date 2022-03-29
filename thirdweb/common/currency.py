from thirdweb.constants.chains import ChainId
from thirdweb.types.currency import Currency, CurrencyValue
from thirdweb.abi import TokenERC20
from thirdweb.constants.currency import (
    NATIVE_TOKEN_ADDRESS,
    ZERO_ADDRESS,
    get_native_token_by_chain_id,
)

from web3 import Web3


def is_native_token(token_address: str) -> bool:
    return (
        token_address.lower() == ZERO_ADDRESS
        or token_address.lower() == NATIVE_TOKEN_ADDRESS
    )


def parse_units(value: int, decimals: int) -> int:
    return value * (10**decimals)


def format_units(value: int, decimals: int) -> int:
    return value / (10**decimals)


def fetch_currency_metadata(provider: Web3, asset: str) -> Currency:
    if is_native_token(asset):
        chain_id = provider.eth.chain_id
        native_token = get_native_token_by_chain_id(ChainId(chain_id))
        return Currency(native_token.name, native_token.symbol, native_token.decimals)

    abi = TokenERC20(provider, asset)
    return Currency(abi.name.call(), abi.symbol.call(), abi.decimals.call())


def fetch_currency_value(provider: Web3, asset: str, price: int) -> CurrencyValue:
    metadata = fetch_currency_metadata(provider, asset)
    return CurrencyValue(
        metadata.name,
        metadata.symbol,
        metadata.decimals,
        price,
        format_units(price, metadata.decimals),
    )


def normalize_price_value(
    provider: Web3, input_price: int, currency_address: str
) -> int:
    metadata = fetch_currency_metadata(provider, currency_address)
    return parse_units(input_price, metadata.decimals)
