from typing import Any, Optional


class NoSignerException(Exception):
    def __init__(self):
        super().__init__("No signer (private key) supplied to SDK")


class AssetNotFoundException(Exception):
    def __init__(self, identifier: Optional[Any] = None):
        super().__init__(
            f"Asset with ID '{identifier}' not found" if identifier is not None else "Asset not found")


class UnsupportedAssetException(Exception):
    def __init__(self, identifier: Optional[Any] = None):
        super().__init__(
            f"Asset with address {identifier} is not compatible with this method")
