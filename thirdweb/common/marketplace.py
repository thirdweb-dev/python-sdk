from typing import Optional, Union, cast
from thirdweb.abi import IERC165, IERC721, IERC1155
from thirdweb.common.currency import fetch_currency_value
from thirdweb.constants.contract import INTERFACE_ID_IERC1155, INTERFACE_ID_IERC721
from eth_account.account import LocalAccount
from web3 import Web3
from thirdweb.core.classes.contract_wrapper import ContractWrapper
from thirdweb.types.currency import Price, PriceWei

from thirdweb.types.marketplace import (
    ContractOffer,
    NewAuctionListing,
    NewDirectListing,
    Offer,
)

MAX_BPS = 10000


def is_token_approved_for_transfer(
    provider: Web3,
    transferrer_contract_address: str,
    asset_contract: str,
    token_id: int,
    fr: str,
) -> bool:
    try:
        erc165 = IERC165(provider, asset_contract)
        is_erc721 = erc165.supports_interface.call(INTERFACE_ID_IERC721)
        is_erc1155 = erc165.supports_interface.call(INTERFACE_ID_IERC1155)

        if is_erc721:
            ierc721 = IERC721(provider, asset_contract)
            approved = ierc721.is_approved_for_all.call(
                fr, transferrer_contract_address
            )

            if approved:
                return True

            return (
                ierc721.get_approved.call(token_id).lower()
                == transferrer_contract_address.lower()
            )
        elif is_erc1155:
            ierc1155 = IERC1155(provider, asset_contract)
            return ierc1155.is_approved_for_all.call(fr, transferrer_contract_address)
        else:
            print("Contract does not implement ERC1155 or ERC721")
            return False
    except:
        print("Failed to check if token is approved")
        return False


def handle_token_approval(
    provider: Web3,
    signer: Optional[LocalAccount],
    marketplace_address: str,
    asset_contract: str,
    token_id: int,
    fr: str,
):
    erc165 = IERC165(provider, asset_contract)
    is_erc721 = erc165.supports_interface.call(INTERFACE_ID_IERC721)
    is_erc1155 = erc165.supports_interface.call(INTERFACE_ID_IERC1155)

    if is_erc721:
        ierc721_abi = IERC721(provider, asset_contract)
        ierc721 = ContractWrapper[IERC721](ierc721_abi, provider, signer)
        approved = ierc721._contract_abi.is_approved_for_all.call(
            fr, marketplace_address
        )

        if not approved:
            is_token_approved = (
                ierc721._contract_abi.get_approved.call(token_id).lower()
                == marketplace_address.lower()
            )

            if not is_token_approved:
                ierc721.send_transaction(
                    "set_approval_for_all", [marketplace_address, True]
                )
    elif is_erc1155:
        ierc1155_abi = IERC1155(provider, asset_contract)
        ierc1155 = ContractWrapper[IERC1155](ierc1155_abi, provider, signer)
        approved = ierc1155._contract_abi.is_approved_for_all.call(
            fr, marketplace_address
        )

        if not approved:
            ierc1155.send_transaction(
                "set_approval_for_all", [marketplace_address, True]
            )
    else:
        raise Exception("Contract does not implement ERC1155 or ERC721")


def validate_new_listing_param(param: Union[NewDirectListing, NewAuctionListing]):
    if param.asset_contract_address == None:
        raise Exception("Asset contract address is required")
    if param.buyout_price_per_token == None:
        raise Exception("Buyout price per token is required")
    if param.listing_duration_in_seconds == None:
        raise Exception("Listing duration is required")
    if param.start_time_in_seconds == None:
        raise Exception("Start time is required")
    if param.token_id == None:
        raise Exception("Token id is required")
    if param.quantity == None:
        raise Exception("Quantity is required")

    if param.type == "NewAuctionListing":
        if cast(NewAuctionListing, param).reserve_price_per_token == None:
            raise Exception("Reserve price per token is required")


def map_offer(provider: Web3, listing_id: int, offer: ContractOffer) -> Offer:
    return Offer(
        quantity_desired=offer.quantity_wanted,
        price_per_token=offer.price_per_token,
        buyer_address=offer.offeror,
        currency_contract_address=offer.currency,
        currency_value=fetch_currency_value(
            provider, offer.currency, offer.quantity_wanted * offer.price_per_token
        ),
        listing_id=listing_id,
    )


def is_winning_bid(
    winning_price: PriceWei, new_bid_price: PriceWei, bid_buffer: int
) -> bool:
    buffer = ((new_bid_price - winning_price) * MAX_BPS) / winning_price
    return buffer >= bid_buffer
