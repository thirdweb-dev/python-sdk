import base64
from datetime import datetime, timedelta
import json
from typing import Any, Optional, cast
from uuid import uuid4
from web3 import Web3
from thirdweb.core.classes.provider_handler import ProviderHandler
from eth_account.account import LocalAccount
from thirdweb.types.auth import (
    AuthenticationOptions,
    AuthenticationPayloadData,
    LoginOptions,
    LoginPayload,
    LoginPayloadData,
    VerifyOptions,
)
from thirdweb.types.sdk import SDKOptions
from eth_account.messages import encode_defunct
from eth_account.datastructures import SignedMessage


class WalletAuthenticator(ProviderHandler):
    """
    The wallet authenticator enables server-side applications to securely identify the
    connected wallet address of users on the client-side, and also enables users to authenticate
    to any backend using just their wallet. It implements the JSON Web Token (JWT) authentication
    standard.

    ```python
    # We specify the domain of the application to authenticate to
    domain = "thirdweb.com"

    # We can then generate a payload for the connected wallet to login
    # This can also be done on the client side with the thirdweb TypeScript SDK
    payload = sdk.auth.login(domain)

    # Then, on the server, we can securely verify the connected address that signed the payload
    address = sdk.auth.verify(domain, payload)

    # And we can also generate an authentication token to send back to the original payload sender
    token = sdk.auth.generate(domain, payload)

    # Finally, the token can be use dby the original payload sender to authenticate to the backend
    # And the server can use the following function to authenticate the token and verify the address
    address = sdk.auth.authenticate(domain, token)
    ```
    """

    def __init__(
        self,
        provider: Web3,
        signer: Optional[LocalAccount] = None,
        options: SDKOptions = SDKOptions(),
    ):
        super().__init__(provider, signer, options)

    def login(
        self, domain: str, options: LoginOptions = LoginOptions()
    ) -> LoginPayload:
        """
        Client-side function that allows the connected wallet to login to a server-side application.
        Generates a login payload that can be sent to the server-side for verification or authentication.

        ```python
        #  Add the domain of the application that you want to log in to
        domain = "thirdweb.com"

        # Generate a signed login payload for the connected wallet to authenticate with
        payload = sdk.auth.login(domain)
        ```

        :param domain: The domain of the application that you want to log in to
        :param options: Optionional configuration options for the login payload
        :return: A login payload that can be sent to the server-side for verification or authentication
        """

        signer_address = self._require_signer().address
        payload_data = LoginPayloadData(
            domain=domain,
            expirationTime=options.expirationTime
            if options.expirationTime is not None
            else datetime.utcnow(),
            address=signer_address,
            nonce=options.nonce if options.nonce is not None else str(uuid4()),
            chainId=options.chainId,
        )

        message = self._generate_message(payload_data)
        signature = self._sign_message(message)

        return LoginPayload(
            payload=payload_data,
            signature=signature,
        )

    def verify(
        self,
        domain: str,
        payload: LoginPayload,
        options: VerifyOptions = VerifyOptions(),
    ) -> str:
        """
        Server-side function to securely verify the address of the logged in client-side wallet
        by validating the provided client-side login request.

        ```python
        domain = "thirdweb.com"
        payload = sdk.auth.login(domain)

        # Verify the login request
        address = sdk.auth.verify(domain, payload)
        ```

        :param domain: The domain of the application to verify the login request for
        :param payload: The login payload to verify
        :return: The address of the logged in wallet that signed the payload
        """

        # Check that the intended domain matches the domain of the payload
        if payload.payload.domain != domain:
            raise Exception(
                f"Expected domain {domain} did not match domain on payload {payload.payload.domain}"
            )

        # Check that the payload hasn't expired
        current_time = datetime.utcnow()
        if current_time > payload.payload.expirationTime:
            raise Exception(f"Login request has expired")

        # If chain ID is specified, check that it matches the chain ID of the signature
        if options.chainId is not None and options.chainId != payload.payload.chainId:
            raise Exception(
                f"Chain ID {options.chainId} did not match payload chain ID {payload.payload.chainId}"
            )

        # Check that the signing address is the claimed wallet address
        message = self._generate_message(payload.payload)
        user_address = self._recover_address(message, payload.signature)
        if user_address.lower() != payload.payload.address.lower():
            raise Exception(
                f"Signer address {user_address.lower()} does not match payload address {payload.payload.address.lower()}"
            )

        return user_address

    def generate(
        self,
        domain: str,
        payload: LoginPayload,
        options: AuthenticationOptions = AuthenticationOptions(),
    ) -> str:
        """
        Server-side function that generates a JWT token from the provided login request that the
        client-side wallet can use to authenticate to the server-side application.

        ```python
        domain = "thirdweb.com"
        payload = sdk.auth.login(domain)

        # Generate an authentication token for the logged in wallet
        token = sdk.auth.generate(domain, payload)
        ```

        :param domain: The domain of the application to authenticate to
        :param payload: The login payload to authenticate with
        :param options: Optional configuration options for the authentication token
        :return: An authentication token that can be used to make authenticated requests to the server
        """

        user_address = self.verify(domain, payload)
        admin_address = self._require_signer().address
        payload_data = AuthenticationPayloadData(
            iss=admin_address,
            sub=user_address,
            aud=domain,
            nbf=int(options.invalidBefore.timestamp())
            if options.invalidBefore is not None
            else int(datetime.utcnow().timestamp()),
            exp=int(options.expirationTime.timestamp())
            if options.expirationTime is not None
            else int((datetime.utcnow() + timedelta(hours=5)).timestamp()),
            iat=int(datetime.utcnow().timestamp()),
            jti=str(uuid4()),
        )

        # Configure json.dumps to work exactly as JSON.stringify works for compatibility
        message = self._stringify(payload_data)
        signature = self._sign_message(message)

        # Header used for JWT token specifying hash algorithm
        header = {
            # Specify ECDSA with SHA-256 for hashing algorithm
            "alg": "ES256",
            "typ": "JWT",
        }

        encoded_header = self._base64encode(self._stringify(header))
        encoded_data = self._base64encode(self._stringify(payload_data))
        encoded_signature = self._base64encode(signature)

        # Generate a JWT token with base64 encoded header, payload, and signature
        token = f"{encoded_header}.{encoded_data}.{encoded_signature}"

        return token

    def authenticate(
        self,
        domain: str,
        token: str,
    ) -> str:
        """
        Server-side function that authenticates the provided JWT token. This function verifies that
        the provided authentication token is valid and returns the address of the authenticated wallet.

        ```python
        domain = "thirdweb.com"
        payload = sdk.auth.login(domain)
        token = sdk.auth.generate(domain, payload)

        # Authenticate the token and get the address of the authenticating wallet
        address = sdk.auth.authenticate(domain, token)
        ```

        :param domain: The domain of the application to authenticate the token to
        :param token: The authentication token to authenticate with
        :return: The address of the authenticated wallet
        """

        encoded_payload = token.split(".")[1]
        encoded_signature = token.split(".")[2]
        payload_dict = json.loads(self._base64decode(encoded_payload))
        payload = AuthenticationPayloadData(**payload_dict)
        signature = self._base64decode(encoded_signature)

        # Check that the intended audience matches the domain
        if payload.aud != domain:
            raise Exception(
                f"Expected token to be for the domain {domain}, but found token with domain {payload.aud}"
            )

        # Check that the token is past the invalid before time
        current_time = datetime.utcnow()
        if current_time < datetime.fromtimestamp(payload.nbf):
            raise Exception(
                f"The token is invalid before epoch time {payload.nbf}, current epoch time is {current_time.timestamp()}"
            )

        # Check that the token hasn't expired
        if current_time > datetime.fromtimestamp(payload.exp):
            raise Exception(
                f"The token expired at epoch time {payload.exp}, current epoch time is {current_time.timestamp()}"
            )

        # Check that the connected wallet matches the token issuer
        if self._require_signer().address.lower() != payload.iss.lower():
            raise Exception(
                f"Expected the connected wallet address {self._require_signer().address} to match the token issuer address {payload.iss}"
            )

        # Check that the connected wallet signed the token
        admin_address = self._recover_address(self._stringify(payload), signature)
        if admin_address.lower() != self._require_signer().address.lower():
            raise Exception(
                f"The connected wallet address {self._require_signer().address} did not sign the token"
            )

        return payload.sub

    """
    INTERNAL FUNCTIONS
    """

    def _generate_message(self, payload: LoginPayloadData) -> str:
        """
        Generates an EIP-4361 compliant message to sign based on the login payload
        """

        message = ""

        # Add the domain and login address for transparency
        message += f"{payload.domain} wants you to sign in with your account:\n{payload.address}\n\n"

        # Prompt user to make sure domain is correct to prevent phishing attacks
        message += "Make sure that the requesting domain above matches the URL of the current website.\n\n"

        # Add data fields in compliance with the EIP-4361 standard
        if payload.chainId is not None:
            message += f"Chain ID: {payload.chainId}\n"

        message += f"Nonce: {payload.nonce}\n"
        message += f"Expiration Time: {payload.expirationTime.isoformat()}\n"

        return message

    def _recover_address(self, message: str, signature: str) -> str:
        """
        Recover the signing address from a signed message
        """

        message_hash = encode_defunct(text=message)
        provider = self.get_provider()
        address = provider.eth.account.recover_message(
            message_hash, signature=signature
        )

        return address

    def _require_signer(self) -> LocalAccount:
        """
        Raises an error if the signer is not set
        """

        signer = self.get_signer()
        if signer is None:
            raise Exception(
                "This action requires a connected wallet. Please pass a valid signer to the SDK."
            )

        return signer

    def _sign_message(self, message: str) -> str:
        """
        Sign a message with the connected wallet
        """

        self._require_signer()

        provider = self.get_provider()
        message_hash = encode_defunct(text=message)
        signature = provider.eth.account.sign_message(message_hash)

        return cast(SignedMessage, signature).signature.hex()

    def _stringify(self, value: Any) -> str:
        """
        Configure json.dumps to work exactly as JSON.stringify works for compatibility
        """

        return json.dumps(value, separators=(",", ":"))

    def _base64encode(self, message: str) -> str:
        """
        Encode a message in base64
        """

        return base64.b64encode(message.encode("utf-8")).decode("utf-8")

    def _base64decode(self, message: str) -> str:
        """
        Decode a message from base64
        """

        return base64.b64decode(message).decode("utf-8")
