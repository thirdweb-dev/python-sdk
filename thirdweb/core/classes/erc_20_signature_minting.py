from typing import Any, Dict, List
from thirdweb.abi.token_erc20 import ITokenERC20MintRequest
from thirdweb.common.currency import (
    normalize_price_value,
    parse_units,
    set_erc20_allowance,
)
from web3.eth import TxReceipt
from thirdweb.common.nft import upload_or_extract_uris
from thirdweb.common.sign import EIP712StandardDomain
from thirdweb.constants.currency import ZERO_ADDRESS
from thirdweb.constants.role import Role
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.contract_roles import ContractRoles
from thirdweb.abi import TokenERC20
from thirdweb.types.tx import TxResultWithId
from thirdweb.types.contracts.signature import (
    EIP712DomainType,
    MintRequest1155,
    MintRequest20,
    PayloadToSign20,
    PayloadWithUri20,
    Signature20PayloadOutput,
    SignedPayload20,
)


class ERC20SignatureMinting:
    _contract_wrapper: ContractWrapper[TokenERC20]
    _storage: IpfsStorage

    roles: ContractRoles

    def __init__(
        self,
        contract_wrapper: ContractWrapper[TokenERC20],
        roles: ContractRoles,
        storage: IpfsStorage,
    ):
        self._contract_wrapper = contract_wrapper
        self._storage = storage
        self.roles = roles

    def mint(self, signed_payload: SignedPayload20) -> TxReceipt:
        """
        Mint a token with the given payload

        :param signed_payload: Signed payload
        :return: transaction result with the token ID of the minted token
        """
        mint_request = signed_payload.payload
        signature = signed_payload.signature
        message = self._map_payload_to_contract_struct(mint_request)

        # TODO: OVERRIDES
        overrides: Dict[str, Any] = {}
        set_erc20_allowance(
            self._contract_wrapper,
            message["price"],
            mint_request.currency_address,
            overrides,
        )

        return self._contract_wrapper.send_transaction(
            "mint_with_signature", [message, signature]
        )

    def mint_batch(self, signed_payloads: List[SignedPayload20]) -> TxReceipt:
        """
        Mint a batch of tokens with the given payloads

        :param signed_payloads: Signed payloads
        :return: transaction results with the token IDs of the minted tokens
        """
        contract_payloads = []
        for payload in signed_payloads:
            message = self._map_payload_to_contract_struct(payload.payload)
            signature = payload.signature
            price = payload.payload.price

            if price > 0:
                raise Exception(
                    "Can only batch free mints. For mints with price, use regulare mint()"
                )

            contract_payloads.append((message, signature))

        encoded = []
        interface = self._contract_wrapper.get_contract_interface()
        for message, signature in contract_payloads:
            encoded.append(
                interface.encodeABI("mintWithSignature", [message, signature])
            )

        return self._contract_wrapper.multi_call(encoded)

    def verify(self, signed_payload: SignedPayload20) -> bool:
        """
        Verify the signature of the given payload

        :param signed_payload: Signed payload
        :return: True if the signature is valid, False otherwise
        """
        mint_request = signed_payload.payload
        signature = signed_payload.signature
        message = self._map_payload_to_contract_struct(mint_request)
        verification = self._contract_wrapper._contract_abi.verify.call(
            message, signature
        )
        return verification[0]

    def generate(self, mint_request: PayloadToSign20) -> SignedPayload20:
        """
        Generate a signed payload from the given payload

        :param mint_request: Payload to sign
        :return: Signed payload
        """
        return self.generate_batch([mint_request])[0]

    def generate_batch(
        self, payloads_to_sign: List[PayloadToSign20]
    ) -> List[SignedPayload20]:
        """
        Generate a batch of signed payloads from the given payloads

        :param payloads_to_sign: Payloads to sign
        :return: Signed payloads
        """
        self.roles.verify([Role.MINTER], self._contract_wrapper.get_signer_address())

        parsed_requests = payloads_to_sign
        chain_id = self._contract_wrapper.get_chain_id()
        signer = self._contract_wrapper.get_signer()

        if signer is None:
            raise Exception("No signer found")

        name = self._contract_wrapper._contract_abi.name.call()

        signed_payloads = []
        for request in parsed_requests:
            final_payload = Signature20PayloadOutput(
                to=request.to,
                currency_address=request.currency_address,
                price=request.price,
                mint_end_time=request.mint_end_time,
                mint_start_time=request.mint_start_time,
                uid=request.uid,
                primary_sale_recipient=request.primary_sale_recipient,
                quantity=request.quantity,
            ).set_uid(request.uid)
            signature = self._contract_wrapper.sign_typed_data(
                signer,
                EIP712StandardDomain(
                    name="TokenERC20",
                    version="1",
                    chainId=chain_id,
                    verifyingContract=self._contract_wrapper._contract_abi.contract_address,
                ),
                {"MintRequest": MintRequest20},
                self._map_payload_to_contract_struct(final_payload),
            )
            signed_payloads.append(
                SignedPayload20(payload=final_payload, signature=signature)
            )

        return signed_payloads

    """
    INTERNAL FUNCTIONS
    """

    def _map_payload_to_contract_struct(
        self,
        mint_request: PayloadWithUri20,
    ) -> ITokenERC20MintRequest:
        normalized_price_per_token = normalize_price_value(
            self._contract_wrapper.get_provider(),
            mint_request.price,
            mint_request.currency_address,
        )

        amount_with_decimals = parse_units(
            mint_request.quantity, self._contract_wrapper._contract_abi.decimals.call()
        )

        return ITokenERC20MintRequest(
            to=mint_request.to,
            price=normalized_price_per_token,
            currency=mint_request.currency_address,
            validityEndTimestamp=mint_request.mint_end_time,
            validityStartTimestamp=mint_request.mint_start_time,
            uid=mint_request.uid,
            quantity=amount_with_decimals,
            primarySaleRecipient=mint_request.primary_sale_recipient,
        )
