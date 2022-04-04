from typing import Generic
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.types.contract import TPlatformFeeABI
from thirdweb.types.settings.metadata import ContractPlatformFeeSchema
from web3.eth import TxReceipt


class ContractPlatformFee(Generic[TPlatformFeeABI]):
    _contract_wrapper: ContractWrapper[TPlatformFeeABI]

    def __init__(self, contract_wrapper: ContractWrapper[TPlatformFeeABI]):
        self._contract_wrapper = contract_wrapper

    def get(self) -> ContractPlatformFeeSchema:
        """
        Get the platform fee of this contract.

        :returns: the platform fee.
        """

        (
            platform_fee_recipient,
            platform_fee_bps,
        ) = self._contract_wrapper._contract_abi.get_platform_fee_info.call()
        return ContractPlatformFeeSchema(platform_fee_recipient, platform_fee_bps)

    def set(self, platform_fee_info: ContractPlatformFeeSchema) -> TxReceipt:
        """
        Set the platform fee of this contract.

        :param platform_fee_info: the platform fee info to set.
        :returns: the transaction receipt of setting the platform fee.
        """

        return self._contract_wrapper.send_transaction(
            "set_platform_fee_info",
            [
                platform_fee_info.platform_fee_recipient,
                platform_fee_info.platform_fee_basis_points,
            ],
        )
