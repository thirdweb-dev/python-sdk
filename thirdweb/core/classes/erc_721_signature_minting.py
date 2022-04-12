from typing import Any, Dict, List
from thirdweb.abi.token_erc721 import ITokenERC721MintRequest
from thirdweb.common.sign import EIP712StandardDomain
from thirdweb.constants.role import Role
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.core.classes.contract_roles import ContractRoles
from thirdweb.abi import TokenERC721
from thirdweb.common.currency import normalize_price_value, set_erc20_allowance
from thirdweb.common.nft import upload_or_extract_uris
from thirdweb.types.contracts.signature import (
    EIP712DomainType,
    MintRequest721,
    PayloadToSign721,
    PayloadWithUri721,
    Signature721PayloadOutput,
    SignedPayload721,
)
from thirdweb.types.tx import TxResultWithId


class ERC721SignatureMinting:
    _contract_wrapper: ContractWrapper[TokenERC721]
    _storage: IpfsStorage

    roles: ContractRoles

    def __init__(
        self,
        contract_wrapper: ContractWrapper[TokenERC721],
        roles: ContractRoles,
        storage: IpfsStorage,
    ):
        self._contract_wrapper = contract_wrapper
        self._storage = storage
        self.roles = roles

    def mint(self, signed_payload: SignedPayload721) -> TxResultWithId:
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
        receipt = self._contract_wrapper.send_transaction(
            "mint_with_signature", [message, signature]
        )
        events = self._contract_wrapper.get_events("TokensMintedWithSignature", receipt)

        if len(events) == 0:
            raise Exception("No MintWithSignature event found")

        token_id_minted = events[0].get("args").get("tokenIdMinted")  # type: ignore
        return TxResultWithId(receipt, data=lambda: None, id=token_id_minted)

    def mint_batch(
        self, signed_payloads: List[SignedPayload721]
    ) -> List[TxResultWithId]:
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

        receipt = self._contract_wrapper.multi_call(encoded)
        events = self._contract_wrapper.get_events("TokensMintedWithSignature", receipt)

        if len(events) == 0:
            raise Exception("No MintWithSignature event found")

        return [
            TxResultWithId(
                receipt, data=lambda: None, id=event.get("args").get("tokenIdMinted")  # type: ignore
            )
            for event in events
        ]

    def verify(self, signed_payload: SignedPayload721) -> bool:
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

    def generate(self, mint_request: PayloadToSign721) -> SignedPayload721:
        """
        Generate a signed payload from the given payload

        :param mint_request: Payload to sign
        :return: Signed payload
        """
        return self.generate_batch([mint_request])[0]

    def generate_batch(
        self, payloads_to_sign: List[PayloadToSign721]
    ) -> List[SignedPayload721]:
        """
        Generate a batch of signed payloads from the given payloads

        :param payloads_to_sign: Payloads to sign
        :return: Signed payloads
        """
        self.roles.verify([Role.MINTER], self._contract_wrapper.get_signer_address())

        parsed_requests = payloads_to_sign

        metadatas = [request.metadata for request in parsed_requests]
        uris = upload_or_extract_uris(metadatas, self._storage)

        chain_id = self._contract_wrapper.get_chain_id()
        signer = self._contract_wrapper.get_signer()

        if signer is None:
            raise Exception("No signer found")

        signed_payloads = []
        for i, request in enumerate(parsed_requests):
            uri = uris[i]
            final_payload = Signature721PayloadOutput(
                to=request.to,
                currency_address=request.currency_address,
                price=request.price,
                metadata=request.metadata,
                mint_end_time=request.mint_end_time,
                mint_start_time=request.mint_start_time,
                uid=request.uid,
                primary_sale_recipient=request.primary_sale_recipient,
                royalty_recipient=request.royalty_recipient,
                royalty_bps=request.royalty_bps,
                uri=uri,
            ).set_uid(request.uid)
            signature = self._contract_wrapper.sign_typed_data(
                signer,
                EIP712StandardDomain(
                    name="TokenERC721",
                    version="1",
                    chainId=chain_id,
                    verifyingContract=self._contract_wrapper._contract_abi.contract_address,
                ),
                {"MintRequest": MintRequest721, "EIP712Domain": EIP712DomainType},
                self._map_payload_to_contract_struct(final_payload),
            )
            signed_payloads.append(
                SignedPayload721(payload=final_payload, signature=signature)
            )

        return signed_payloads

    """
    INTERNAL FUNCTIONS
    """

    def _map_payload_to_contract_struct(
        self,
        mint_request: PayloadWithUri721,
    ) -> ITokenERC721MintRequest:
        normalized_price_per_token = normalize_price_value(
            self._contract_wrapper.get_provider(),
            mint_request.price,
            mint_request.currency_address,
        )

        return ITokenERC721MintRequest(
            to=mint_request.to,
            price=normalized_price_per_token,
            uri=mint_request.uri,
            currency=mint_request.currency_address,
            validityEndTimestamp=mint_request.mint_end_time,
            validityStartTimestamp=mint_request.mint_start_time,
            uid=mint_request.uid,
            royaltyRecipient=mint_request.royalty_recipient,
            royaltyBps=mint_request.royalty_bps,
            primarySaleRecipient=mint_request.primary_sale_recipient,
        )
