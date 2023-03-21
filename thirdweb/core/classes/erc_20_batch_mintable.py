from typing import List
from thirdweb.abi.token_erc20 import TokenERC20
from thirdweb.common.currency import parse_units
from thirdweb.core.classes.base_contract import BaseContract
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.erc_20 import ERC20
from thirdweb.types.currency import TokenAmount


class ERC20BatchMintable(BaseContract[TokenERC20]):
    _erc20: ERC20

    def __init__(self, erc20: ERC20, contract_wrapper: ContractWrapper):
        super().__init__(contract_wrapper)
        self._erc20 = erc20

    def to(self, args: List[TokenAmount]):
        encoded = []
        interface = self._contract_wrapper.get_contract_interface()
        for arg in args:
            encoded.append(
                interface.encodeABI(
                    "mintTo",
                    [arg.to_address, parse_units(arg.amount, self._erc20.get().decimals)],
                )
            )
        return self._contract_wrapper.multi_call(encoded)