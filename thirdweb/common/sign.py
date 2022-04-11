from dataclasses import dataclass
from typing import Any, Dict, List, Union
from eth_account.account import LocalAccount
from sphinx_autodoc_typehints import NewType
from web3 import Web3

from thirdweb.types.contracts.signature import SignedPayload721


@dataclass
class EIP712StandardDomain:
    name: str
    version: str
    chain_id: int
    verifying_contract: str


@dataclass
class EIP712PolygonDomain:
    name: str
    version: str
    verifying_contract: str
    salt: str


EIP712Domain = Union[EIP712StandardDomain, EIP712PolygonDomain]


def sign_typed_data_internal(
    provider: Web3,
    signer: LocalAccount,
    domain: EIP712Domain,
    types: Dict[str, List[Any]],
    message: Dict[str, Any],
) -> SignedPayload721:
    # TODO: implement
    pass
