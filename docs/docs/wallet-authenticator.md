<a id="core.auth.wallet_authenticator"></a>

# core.auth.wallet\_authenticator

<a id="core.auth.wallet_authenticator.WalletAuthenticator"></a>

## WalletAuthenticator Objects

```python
class WalletAuthenticator(ProviderHandler)
```

> This API is provided as a preview for developers and may change based on feedback that we receive. Do not use this API in a production environment.
>

The wallet authenticator enables server-side applications to securely identify the
connected wallet address of users on the client-side, and also enables users to authenticate
to any backend using just their wallet. It implements the JSON Web Token (JWT) authentication
standard.

```python
# We specify the domain of the application to authenticate to
domain = "example.com"

# We can then generate a payload for the connected wallet to login
# This can also be done on the client side with the thirdweb TypeScript SDK
payload = sdk.auth.login(domain)

# Then, on the server, we can securely verify the connected address that signed the payload
address = sdk.auth.verify(domain, payload)

# And we can also generate an authentication token to send back to the original payload sender
token = sdk.auth.generate_auth_token(domain, payload)

# Finally, the token can be use dby the original payload sender to authenticate to the backend
# And the server can use the following function to authenticate the token and verify the address
address = sdk.auth.authenticate(domain, token)
```

<a id="core.auth.wallet_authenticator.WalletAuthenticator.login"></a>

#### login

```python
def login(domain: str, options: LoginOptions = LoginOptions()) -> LoginPayload
```

Client-side function that allows the connected wallet to login to a server-side application.

Generates a login payload that can be sent to the server-side for verification or authentication.

```python
# Add the domain of the application that you want to log in to
domain = "example.com"

# Generate a signed login payload for the connected wallet to authenticate with
payload = sdk.auth.login(domain)
```

**Arguments**:

- `domain`: The domain of the application that you want to log in to
- `options`: Optional configuration options for the login payload

**Returns**:

A login payload that can be sent to the server-side for verification or authentication

<a id="core.auth.wallet_authenticator.WalletAuthenticator.verify"></a>

#### verify

```python
def verify(
    domain: str,
    payload: LoginPayload,
    options: VerifyOptions = VerifyOptions()) -> str
```

Server-side function to securely verify the address of the logged in client-side wallet

by validating the provided client-side login request.

```python
domain = "example.com"
payload = sdk.auth.login(domain)

# Verify the login request
address = sdk.auth.verify(domain, payload)
```

**Arguments**:

- `domain`: The domain of the application to verify the login request for
- `payload`: The login payload to verify

**Returns**:

The address of the logged in wallet that signed the payload

<a id="core.auth.wallet_authenticator.WalletAuthenticator.generate_auth_token"></a>

#### generate\_auth\_token

```python
def generate_auth_token(
    domain: str,
    payload: LoginPayload,
    options: AuthenticationOptions = AuthenticationOptions()
) -> str
```

Server-side function that generates a JWT token from the provided login request that the

client-side wallet can use to authenticate to the server-side application.

```python
domain = "example.com"
payload = sdk.auth.login(domain)

# Generate an authentication token for the logged in wallet
token = sdk.auth.generate_auth_token(domain, payload)
```

**Arguments**:

- `domain`: The domain of the application to authenticate to
- `payload`: The login payload to authenticate with
- `options`: Optional configuration options for the authentication token

**Returns**:

An authentication token that can be used to make authenticated requests to the server

<a id="core.auth.wallet_authenticator.WalletAuthenticator.authenticate"></a>

#### authenticate

```python
def authenticate(domain: str, token: str) -> str
```

Server-side function that authenticates the provided JWT token. This function verifies that

the provided authentication token is valid and returns the address of the authenticated wallet.

```python
domain = "example.com"
payload = sdk.auth.login(domain)
token = sdk.auth.generate_auth_token(domain, payload)

# Authenticate the token and get the address of the authenticating wallet
address = sdk.auth.authenticate(domain, token)
```

**Arguments**:

- `domain`: The domain of the application to authenticate the token to
- `token`: The authentication token to authenticate with

**Returns**:

The address of the authenticated wallet

