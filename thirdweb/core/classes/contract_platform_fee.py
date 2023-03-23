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
        Get the contract platform fees

        ```python
        platform_fees = contract.platform_fee.get()
        print(platform_fees.platform_fee_basis_points)
        print(platform_fees.platform_fee_recipient)
        ```

        :extension: PlatformFee
        :returns: the platform fee.
        """

        (
            platform_fee_recipient,
            platform_fee_bps,
        ) = self._contract_wrapper._contract_abi.get_platform_fee_info.call()
        return ContractPlatformFeeSchema(platform_fee_bps, platform_fee_recipient)

    def set(self, platform_fee_info: ContractPlatformFeeSchema) -> TxReceipt:
        """
        Set the contract platform fees

        ```python
        from thirdweb.types import ContractPlatformFeeSchema

        platform_fee_info = ContractPlatformFeeSchema(
            platform_fee_basis_points=100 # 1%
            platform_fee_receipient="{{wallet_address}}"
        )

        receipt = contract.platform_fee.set(platform_fee_info)
        ```

        :extension: PlatformFee
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
