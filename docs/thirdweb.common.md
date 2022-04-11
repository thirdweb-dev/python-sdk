# thirdweb.common package

## Submodules

## thirdweb.common.currency module


### thirdweb.common.currency.approve_erc20_allowance(contract_to_approve, currency_address, price, quantity)

### thirdweb.common.currency.fetch_currency_metadata(provider, asset)

* **Return type**

    [`Currency`](thirdweb.types.md#thirdweb.types.currency.Currency)



### thirdweb.common.currency.fetch_currency_value(provider, asset, price)

* **Return type**

    [`CurrencyValue`](thirdweb.types.md#thirdweb.types.currency.CurrencyValue)



### thirdweb.common.currency.format_units(wei_value, decimals)

* **Return type**

    `float`



### thirdweb.common.currency.is_native_token(token_address)

* **Return type**

    `bool`



### thirdweb.common.currency.normalize_price_value(provider, input_price, currency_address)

* **Return type**

    `int`



### thirdweb.common.currency.parse_units(token_value, decimals)

* **Return type**

    `int`



### thirdweb.common.currency.set_erc20_allowance(contract_to_approve, value, currency_address, overrides)
## thirdweb.common.error module


### _exception_ thirdweb.common.error.AuctionAlreadyStartedException(listing_id)
Bases: `Exception`


#### \__init__(listing_id)

### _exception_ thirdweb.common.error.AuctionHasNotEndedException(listing_id)
Bases: `Exception`


#### \__init__(listing_id)

### _exception_ thirdweb.common.error.DuplicateFileNameException(filename)
Bases: `Exception`


#### \__init__(filename)

### _exception_ thirdweb.common.error.FetchException(message)
Bases: `Exception`


#### \__init__(message)

### _exception_ thirdweb.common.error.ListingNotFoundException(listing_id)
Bases: `Exception`


#### \__init__(listing_id)

### _exception_ thirdweb.common.error.NoSignerException()
Bases: `Exception`


#### \__init__()

### _exception_ thirdweb.common.error.NotEnoughTokensException(contract_address, quantity, available)
Bases: `Exception`


#### \__init__(contract_address, quantity, available)

### _exception_ thirdweb.common.error.NotFoundException(indentifier)
Bases: `Exception`


#### \__init__(indentifier)

### _exception_ thirdweb.common.error.RestrictedTransferException(asset_address)
Bases: `Exception`


#### \__init__(asset_address)

### _exception_ thirdweb.common.error.RoleException(message)
Bases: `Exception`


#### \__init__(message)

### _exception_ thirdweb.common.error.UploadException(message)
Bases: `Exception`


#### \__init__(message)

### _exception_ thirdweb.common.error.WrongListingTypeException(listing_id, listing_type, expected_type)
Bases: `Exception`


#### \__init__(listing_id, listing_type, expected_type)
## thirdweb.common.marketplace module


### thirdweb.common.marketplace.handle_token_approval(provider, signer, marketplace_address, asset_contract, token_id, fr)

### thirdweb.common.marketplace.is_token_approved_for_marketplace(provider, marketplace_address, asset_contract, token_id, fr)

* **Return type**

    `bool`



### thirdweb.common.marketplace.is_winning_bid(winning_price, new_bid_price, bid_buffer)

* **Return type**

    `bool`



### thirdweb.common.marketplace.map_offer(provider, listing_id, offer)

* **Return type**

    [`Offer`](thirdweb.types.md#thirdweb.types.marketplace.Offer)



### thirdweb.common.marketplace.validate_new_listing_param(param)
## thirdweb.common.nft module


### thirdweb.common.nft.fetch_token_metadata(token_id, token_uri, storage)

* **Return type**

    [`NFTMetadata`](thirdweb.types.md#thirdweb.types.nft.NFTMetadata)



### thirdweb.common.nft.fetch_token_metadata_for_contract(contract_address, provider, token_id, storage)

### thirdweb.common.nft.is_metadata_list(metadatas)

* **Return type**

    `bool`



### thirdweb.common.nft.is_uri_list(metadatas)

* **Return type**

    `bool`



### thirdweb.common.nft.upload_or_extract_uri(metadata, storage)

* **Return type**

    `str`



### thirdweb.common.nft.upload_or_extract_uris(metadatas, storage)

* **Return type**

    `List`[`str`]


## Module contents
