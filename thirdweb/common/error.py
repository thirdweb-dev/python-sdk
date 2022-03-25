class NotFoundException(Exception):
    def __init__(self, indentifier: str):
        super().__init__(f"NOT FOUND: Object with ID {indentifier} not found")


class NoSignerException(Exception):
    def __init__(self):
        super().__init__(
            (
                "You need to pass a valid signer to the SDK to use this function."
                "Please use the `update_signer` method of the SDK to set a valid signer."
                "You can create a signer using the `Account.from_key(<private_key>)` method."
            )
        )


class UploadException(Exception):
    def __init__(self, message: str):
        super().__init__(f"UPLOAD FAILED: {message}")


class NotEnoughTokensException(Exception):
    def __init__(self, contract_address: str, quantity: str, available: int):
        super().__init__(
            f"BALANCE ERROR: you do not have enough balance on contract ${contract_address} to use ${quantity} tokens. You have ${available} tokens available."
        )


class FetchException(Exception):
    def __init__(self, message: str):
        super().__init__(f"FETCH FAILED: {message}")


class RestrictedTransferException(Exception):
    def __init__(self, asset_address: str):
        super().__init__(
            f"Failed to transfer asset, transfer is restricted for asset {asset_address}"
        )