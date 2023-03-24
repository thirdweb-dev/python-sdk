from typing import Generic
from thirdweb.core.classes.contract_metadata import ContractMetadata
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.types.contract import TRoyaltyABI
from thirdweb.types.settings.metadata import ContractRoyaltySchema
from web3.eth import TxReceipt


class ContractRoyalty(Generic[TRoyaltyABI]):
    _contract_wrapper: ContractWrapper[TRoyaltyABI]
    _metadata: ContractMetadata

    def __init__(
        self, contract_wrapper: ContractWrapper[TRoyaltyABI], metadata: ContractMetadata
    ):
        self._contract_wrapper = contract_wrapper
        self._metadata = metadata

    def get_default_royalty_info(self) -> ContractRoyaltySchema:
        """
        Get the royalty recipient and fee

        ```python
        royalty_info = contract.royalties.get_default_royalty_info()
        print(royalty_info)
        ```

        :extension: Royalty
        :returns: the default royalty information.
        """

        (
            royalty_recipient,
            royalty_bps,
        ) = self._contract_wrapper._contract_abi.get_default_royalty_info.call()
        return ContractRoyaltySchema(royalty_bps, royalty_recipient)

    def get_token_royalty_info(self, token_id: int) -> ContractRoyaltySchema:
        """
        Get the royalty recipient and fee for a specific token

        ```python
        token_id = 0

        royalty_info = contract.royalties.get_token_royalty_info(token_id)
        print(royalty_info)
        ```

        :extensions: Royalty
        :param token_id: the id of the token.
        :returns: the royalty information for the token.
        """

        (
            royalty_recipient,
            royalty_bps,
        ) = self._contract_wrapper._contract_abi.get_royalty_info_for_token.call(
            token_id
        )
        return ContractRoyaltySchema(royalty_bps, royalty_recipient)

    def set_default_royalty_info(
        self, royalty_data: ContractRoyaltySchema
    ) -> TxReceipt:
        """
        Set the royalty recipient and fee

        ```python
        from thirdweb.types import ContractRoyaltySchema

        royalty_data = ContractRoyaltySchema(
            seller_fee_basis_points=100,
            fee_recipient="{{wallet_address}}"
        )

        receipt = contract.royalties.set_default_royalty_info()
        ```

        :extension: Royalty
        :param royalty_data: the default royalty information.
        :returns: the transaction receipt of setting the royalty.
        """

        metadata = self._metadata.get()
        metadata.fee_recipient = royalty_data.fee_recipient
        metadata.seller_fee_basis_points = royalty_data.seller_fee_basis_points

        contract_uri = self._metadata._parse_and_upload_metadata(metadata)

        encoded = [
            self._contract_wrapper.get_contract_interface().encodeABI(
                "set_default_royalty_info",
                [metadata.fee_recipient, metadata.seller_fee_basis_points],
            ),
            self._contract_wrapper.get_contract_interface().encodeABI(
                "set_contract_uri", [contract_uri]
            ),
        ]

        return self._contract_wrapper.multi_call(encoded)

    def set_token_royalty_info(
        self, token_id: int, royalty_data: ContractRoyaltySchema
    ) -> TxReceipt:
        """
        Set the royalty recipient and fee for a specific token

        ```python
        from thirdweb.types import ContractRoyaltySchema

        token_id = 0
        royalty_data = ContractRoyaltySchema(
            seller_fee_basis_points=100,
            fee_recipient="{{wallet_address}}"
        )

        receipt = contract.royalties.set_token_royalty_info(token_id, royalty_data)
        ```

        :extension: Royalty
        :param token_id: the id of the token.
        :param royalty_data: the royalty information for the token.
        :returns: the transaction receipt of setting the royalty.
        """

        return self._contract_wrapper.send_transaction(
            "set_royalty_info_for_token",
            [
                token_id,
                royalty_data.fee_recipient,
                royalty_data.seller_fee_basis_points,
            ],
        )
