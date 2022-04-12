from dataclasses import dataclass
from typing import Any, Dict, List, Union
from eth_account.account import LocalAccount
from thirdweb_eth_account.messages import encode_structured_data
from web3 import Web3

from thirdweb.types.contracts.signature import SignedPayload721


@dataclass
class EIP712StandardDomain:
    name: str
    version: str
    chainId: int
    verifyingContract: str

    def to_json(self) -> Dict[str, Any]:
        return self.__dict__


@dataclass
class EIP712PolygonDomain:
    name: str
    version: str
    verifyingContract: str
    salt: str

    def to_json(self) -> Dict[str, Any]:
        return self.__dict__


EIP712Domain = Union[EIP712StandardDomain, EIP712PolygonDomain]


def sign_typed_data_internal(
    provider: Web3,
    signer: LocalAccount,
    domain: EIP712Domain,
    types: Dict[str, List[Any]],
    message: Dict[str, Any],
) -> bytes:
    encoded_message = encode_structured_data(
        {
            "domain": domain.to_json(),
            "types": types,
            "primaryType": "MintRequest",
            "message": message,
        }
    )

    signature = provider.eth.account.sign_message(
        encoded_message, signer._private_key
    ).signature.hex()
    return signature
