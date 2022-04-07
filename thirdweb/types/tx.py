from typing import Generic, TypeVar
from web3.eth import TxReceipt
from dataclasses import dataclass

T = TypeVar("T")


@dataclass
class TxResult:
    receipt: TxReceipt


@dataclass
class TxResultWithData(TxResult, Generic[T]):
    data: T


@dataclass
class TxResultWithId(TxResultWithData[T]):
    id: int
