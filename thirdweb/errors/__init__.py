from typing import Any, Optional
import json


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


class UploadError(Exception):
    def __init__(self, message: str):
        super().__init__(
            f"There was an error while uploading the image : {message}")


class WrongListingTypeException(Exception):
    def __init__(self, listing_id: int, listing_type: str, expected_type: str):
        super().__init__(
            f"The listing type of {str(listing_id)} is not valid : {listing_type}, expected {expected_type}.")


class AuctionAlreadyStartedException(Exception):
    def __init__(self, listing_id: int):
        super().__init__(
            f"The auction of listing {str(listing_id)} has already started.")


class AuctionHasNotEndedException(Exception):
    def __init__(self, listing_id: int):
        super().__init__(
            f"The auction of listing {str(listing_id)} has not ended yet.")


class ListingNotFoundException(Exception):
    def __init__(self, listing_id: int):
        super().__init__(
            f"The listing {str(listing_id)} has not been found.")


class RestrictedTransferError(Exception):
    def __init__(self, address: str = None):
        super().__init__(
            f"Failed to transfer asset, transfer is restricted.${f'Address : {address}' if address is not None else ''}")
