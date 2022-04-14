from typing import Any


class NotFoundException(Exception):
    def __init__(self, indentifier: str):
        super().__init__(f"NOT FOUND: Object with ID {indentifier} not found")


class NoSignerException(Exception):
    def __init__(self):
        super().__init__(
            (
                "You need to pass a valid signer to the SDK to use this function. "
                "Please use the `update_signer` method of the SDK to set a valid signer. "
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


class DuplicateFileNameException(Exception):
    def __init__(self, filename: str):
        super().__init__(f"File with name {filename} already exists")


class RoleException(Exception):
    def __init__(self, message: str):
        super().__init__(f"ROLE ERROR: {message}")


class WrongListingTypeException(Exception):
    def __init__(self, listing_id: int, listing_type: str, expected_type: str):
        super().__init__(
            f"The listing type of {str(listing_id)} is not valid : {listing_type}, expected {expected_type}."
        )


class AuctionAlreadyStartedException(Exception):
    def __init__(self, listing_id: int):
        super().__init__(
            f"The auction of listing {str(listing_id)} has already started."
        )


class AuctionHasNotEndedException(Exception):
    def __init__(self, listing_id: int):
        super().__init__(f"The auction of listing {str(listing_id)} has not ended yet.")


class ListingNotFoundException(Exception):
    def __init__(self, listing_id: int):
        super().__init__(f"Error getting the listing with ID {str(listing_id)}.")


class DuplicateLeafsException(Exception):
    def __init__(self, message: str = ""):
        super().__init__(f"Duplicate leafs: {message}")


def includes_error_message(err: Any, message: str) -> bool:
    return message in str(err)
