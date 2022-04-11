# thirdweb.types package

## Submodules

## thirdweb.types.contract module


### _class_ thirdweb.types.contract.ContractType(value)
Bases: `enum.Enum`

An enumeration.


#### EDITION(_ = 'edition_ )

#### MARKETPLACE(_ = 'marketplace_ )

#### NFT_COLLECTION(_ = 'nft-collection_ )

#### TOKEN(_ = 'token_ )
## thirdweb.types.currency module


### _class_ thirdweb.types.currency.Currency(name, symbol, decimals)
Bases: `object`


#### \__init__(name, symbol, decimals)

#### decimals(_: in_ )

#### name(_: st_ )

#### symbol(_: st_ )

### _class_ thirdweb.types.currency.CurrencyValue(name, symbol, decimals, value, display_value)
Bases: `thirdweb.types.currency.Currency`


#### \__init__(name, symbol, decimals, value, display_value)

#### display_value(_: floa_ )

#### value(_: in_ )

### _class_ thirdweb.types.currency.NativeToken(name, symbol, decimals, wrapped)
Bases: `object`


#### \__init__(name, symbol, decimals, wrapped)

#### decimals(_: in_ )

#### name(_: st_ )

#### symbol(_: st_ )

#### wrapped(_: thirdweb.types.currency.WrappedToke_ )

### _class_ thirdweb.types.currency.TokenAmount(to_address, amount)
Bases: `object`


#### \__init__(to_address, amount)

#### amount(_: floa_ )

#### to_address(_: st_ )

### _class_ thirdweb.types.currency.WrappedToken(address, name, symbol)
Bases: `object`


#### \__init__(address, name, symbol)

#### address(_: st_ )

#### name(_: st_ )

#### symbol(_: st_ )
## thirdweb.types.marketplace module


### _class_ thirdweb.types.marketplace.AuctionListing(id, asset_contract_address, token_id, asset, start_time_in_epoch_seconds, end_time_in_epoch_seconds, quantity, currency_contract_address, reserve_price, buyout_price, buyout_currency_value_per_token, reserve_price_currency_value_per_token, seller_address)
Bases: `object`


#### \__init__(id, asset_contract_address, token_id, asset, start_time_in_epoch_seconds, end_time_in_epoch_seconds, quantity, currency_contract_address, reserve_price, buyout_price, buyout_currency_value_per_token, reserve_price_currency_value_per_token, seller_address)

#### asset(_: thirdweb.types.nft.NFTMetadat_ )

#### asset_contract_address(_: st_ )

#### buyout_currency_value_per_token(_: thirdweb.types.currency.CurrencyValu_ )

#### buyout_price(_: in_ )

#### currency_contract_address(_: st_ )

#### end_time_in_epoch_seconds(_: in_ )

#### id(_: in_ )

#### quantity(_: in_ )

#### reserve_price(_: in_ )

#### reserve_price_currency_value_per_token(_: thirdweb.types.currency.CurrencyValu_ )

#### seller_address(_: st_ )

#### start_time_in_epoch_seconds(_: in_ )

#### token_id(_: in_ )

#### type(_ = _ )

### _class_ thirdweb.types.marketplace.ContractListing(listing_id, token_owner, asset_contract, token_id, start_time, end_time, quantity, currency, reserve_price_per_token, buyout_price_per_token, token_type, listing_type)
Bases: `object`


#### \__init__(listing_id, token_owner, asset_contract, token_id, start_time, end_time, quantity, currency, reserve_price_per_token, buyout_price_per_token, token_type, listing_type)

#### asset_contract(_: st_ )

#### buyout_price_per_token(_: in_ )

#### currency(_: st_ )

#### end_time(_: in_ )

#### listing_id(_: in_ )

#### listing_type(_: in_ )

#### quantity(_: in_ )

#### reserve_price_per_token(_: in_ )

#### start_time(_: in_ )

#### token_id(_: in_ )

#### token_owner(_: st_ )

#### token_type(_: in_ )

### _class_ thirdweb.types.marketplace.ContractOffer(listing_id, offeror, quantity_wanted, currency, price_per_token)
Bases: `object`


#### \__init__(listing_id, offeror, quantity_wanted, currency, price_per_token)

#### currency(_: st_ )

#### listing_id(_: in_ )

#### offeror(_: st_ )

#### price_per_token(_: in_ )

#### quantity_wanted(_: in_ )

### _class_ thirdweb.types.marketplace.DirectListing(id, asset_contract_address, token_id, asset, start_time_in_seconds, seconds_until_end, quantity, currency_contract_address, buyout_currency_value_per_token, buyout_price, seller_address)
Bases: `object`


#### \__init__(id, asset_contract_address, token_id, asset, start_time_in_seconds, seconds_until_end, quantity, currency_contract_address, buyout_currency_value_per_token, buyout_price, seller_address)

#### asset(_: thirdweb.types.nft.NFTMetadat_ )

#### asset_contract_address(_: st_ )

#### buyout_currency_value_per_token(_: thirdweb.types.currency.CurrencyValu_ )

#### buyout_price(_: in_ )

#### currency_contract_address(_: st_ )

#### id(_: in_ )

#### quantity(_: in_ )

#### seconds_until_end(_: in_ )

#### seller_address(_: st_ )

#### start_time_in_seconds(_: in_ )

#### token_id(_: in_ )

#### type(_ = _ )

### _class_ thirdweb.types.marketplace.ListingType(value)
Bases: `enum.Enum`

An enumeration.


#### AUCTION(_ = _ )

#### DIRECT(_ = _ )

### _class_ thirdweb.types.marketplace.MarketplaceFilter(start=0, count=100, seller=None, token_contract=None, token_id=None)
Bases: `object`


#### \__init__(start=0, count=100, seller=None, token_contract=None, token_id=None)

#### count(_: in_ _ = 10_ )

#### seller(_: Optional[str_ _ = Non_ )

#### start(_: in_ _ = _ )

#### token_contract(_: Optional[str_ _ = Non_ )

#### token_id(_: Optional[int_ _ = Non_ )

### _class_ thirdweb.types.marketplace.NewAuctionListing(asset_contract_address, token_id, start_time_in_seconds, listing_duration_in_seconds, quantity, currency_contract_address, reserve_price_per_token, buyout_price_per_token)
Bases: `object`


#### \__init__(asset_contract_address, token_id, start_time_in_seconds, listing_duration_in_seconds, quantity, currency_contract_address, reserve_price_per_token, buyout_price_per_token)

#### asset_contract_address(_: st_ )

#### buyout_price_per_token(_: in_ )

#### currency_contract_address(_: st_ )

#### listing_duration_in_seconds(_: in_ )

#### quantity(_: in_ )

#### reserve_price_per_token(_: in_ )

#### start_time_in_seconds(_: in_ )

#### token_id(_: in_ )

#### type(_ = 'NewAuctionListing_ )

### _class_ thirdweb.types.marketplace.NewDirectListing(asset_contract_address, token_id, start_time_in_seconds, listing_duration_in_seconds, quantity, currency_contract_address, buyout_price_per_token)
Bases: `object`


#### \__init__(asset_contract_address, token_id, start_time_in_seconds, listing_duration_in_seconds, quantity, currency_contract_address, buyout_price_per_token)

#### asset_contract_address(_: st_ )

#### buyout_price_per_token(_: in_ )

#### currency_contract_address(_: st_ )

#### listing_duration_in_seconds(_: in_ )

#### quantity(_: in_ )

#### start_time_in_seconds(_: in_ )

#### token_id(_: in_ )

#### type(_ = 'NewDirectListing_ )

### _class_ thirdweb.types.marketplace.Offer(listing_id, buyer_address, quantity_desired, price_per_token, currency_value, currency_contract_address)
Bases: `object`


#### \__init__(listing_id, buyer_address, quantity_desired, price_per_token, currency_value, currency_contract_address)

#### buyer_address(_: st_ )

#### currency_contract_address(_: st_ )

#### currency_value(_: thirdweb.types.currency.CurrencyValu_ )

#### listing_id(_: in_ )

#### price_per_token(_: in_ )

#### quantity_desired(_: in_ )
## thirdweb.types.nft module


### _class_ thirdweb.types.nft.EditionMetadata(metadata, supply)
Bases: `object`


#### \__init__(metadata, supply)

#### metadata(_: thirdweb.types.nft.NFTMetadat_ )

#### supply(_: in_ )

### _class_ thirdweb.types.nft.EditionMetadataInput(metadata, supply)
Bases: `object`

The metadata of an edition NFT to mint


* **Parameters**

    
    * **metadata** (`Union`[`NFTMetadataInput`, `str`]) – The metadata of the edition NFT


    * **supply** (`int`) – The supply of the edition NFT



#### \__init__(metadata, supply)

#### metadata(_: Union[thirdweb.types.nft.NFTMetadataInput, str_ )

#### supply(_: in_ )

### _class_ thirdweb.types.nft.EditionMetadataOwner(metadata, supply, owner, quantity_owned)
Bases: `thirdweb.types.nft.EditionMetadata`


#### \__init__(metadata, supply, owner, quantity_owned)

#### owner(_: st_ )

#### quantity_owned(_: in_ )

### _class_ thirdweb.types.nft.NFTMetadata(id, uri, name, description=None, image=None, external_url=None, animation_url=None, background_color=None, properties=None)
Bases: `object`


#### \__init__(id, uri, name, description=None, image=None, external_url=None, animation_url=None, background_color=None, properties=None)

#### animation_url(_: Optional[str_ _ = Non_ )

#### background_color(_: Optional[str_ _ = Non_ )

#### description(_: Optional[str_ _ = Non_ )

#### external_url(_: Optional[str_ _ = Non_ )

#### _static_ from_json(json)

* **Return type**

    `NFTMetadata`



#### id(_: in_ )

#### image(_: Optional[str_ _ = Non_ )

#### name(_: st_ )

#### properties(_: Optional[Dict[Any, Any]_ _ = Non_ )

#### uri(_: st_ )

### _class_ thirdweb.types.nft.NFTMetadataInput(name, description=None, image=None, external_url=None, animation_url=None, background_color=None, properties=None)
Bases: `object`

The metadata of an NFT to mint

You can use the NFTMetadataInput.from_json(json) method to create
an instance of this class from a dictionary.


* **Parameters**

    
    * **name** (`str`) – The name of the NFT


    * **description** (`Optional`[`str`]) – The optional description of the NFT


    * **image** (`Optional`[`str`]) – The optional image of the NFT


    * **external_url** (`Optional`[`str`]) – The optional external URL of the NFT


    * **animation_url** (`Optional`[`str`]) – The optional animation URL of the NFT


    * **background_color** (`Optional`[`str`]) – The optional background color of the NFT


    * **properties** (`Optional`[`Dict`[`str`, `Any`]]) – The optional properties of the NFT



#### \__init__(name, description=None, image=None, external_url=None, animation_url=None, background_color=None, properties=None)

#### animation_url(_: Optional[str_ _ = Non_ )

#### background_color(_: Optional[str_ _ = Non_ )

#### description(_: Optional[str_ _ = Non_ )

#### external_url(_: Optional[str_ _ = Non_ )

#### _static_ from_json(json)

* **Return type**

    `NFTMetadataInput`



#### image(_: Optional[str_ _ = Non_ )

#### name(_: st_ )

#### properties(_: Optional[Dict[str, Any]_ _ = Non_ )

#### to_json()

* **Return type**

    `Dict`[`str`, `Any`]



### _class_ thirdweb.types.nft.NFTMetadataOwner(metadata, owner)
Bases: `object`


#### \__init__(metadata, owner)

#### metadata(_: thirdweb.types.nft.NFTMetadat_ )

#### owner(_: st_ )

### _class_ thirdweb.types.nft.QueryAllParams(start=0, count=100)
Bases: `object`


#### \__init__(start=0, count=100)

#### count(_: in_ _ = 10_ )

#### start(_: in_ _ = _ )
## thirdweb.types.sdk module


### _class_ thirdweb.types.sdk.GasSettings(max_price_in_gwei=300, speed=GasSpeed.FASTEST)
Bases: `object`

The gas settings for the SDK.


* **Parameters**

    
    * **max_price_in_gwei** (`int`) – maximum gas price in gwei, defaults to 300


    * **speed** (`GasSpeed`) – gas speed to use, defaults to “fastest”



#### \__init__(max_price_in_gwei=300, speed=GasSpeed.FASTEST)

#### max_price_in_gwei(_: in_ _ = 30_ )

#### speed(_: thirdweb.types.sdk.GasSpee_ _ = 'fastest_ )

### _class_ thirdweb.types.sdk.GasSpeed(value)
Bases: `enum.Enum`

An enumeration.


#### FAST(_ = 'fast_ )

#### FASTEST(_ = 'fastest_ )

#### STANDARD(_ = 'standard_ )

### _class_ thirdweb.types.sdk.ReadOnlySettings(rpc_url='', chain_id=None)
Bases: `object`

The read-only RPC settings for the SDK.


* **Parameters**

    
    * **rpc_url** (`str`) – URL of the RPC


    * **chain_id** (`Optional`[[`ChainId`](thirdweb.constants.md#thirdweb.constants.chains.ChainId)]) – optional chain ID to use for the RPC



#### \__init__(rpc_url='', chain_id=None)

#### chain_id(_: Optional[[thirdweb.constants.chains.ChainId](thirdweb.constants.md#thirdweb.constants.chains.ChainId)_ _ = Non_ )

#### rpc_url(_: st_ _ = '_ )

### _class_ thirdweb.types.sdk.SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>))
Bases: `object`

Optional settings to configure the SDK


* **Parameters**

    
    * **read_only_settings** (`Optional`[`ReadOnlySettings`]) – optional read-only RPC settings


    * **gas_settings** (`GasSettings`) – gas settings



#### \__init__(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>))

#### gas_settings(_: thirdweb.types.sdk.GasSetting_ _ = GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>_ )

#### read_only_settings(_: Optional[thirdweb.types.sdk.ReadOnlySettings_ _ = Non_ )
## thirdweb.types.storage module


### _class_ thirdweb.types.storage.CidWithFileName(cid, filenames)
Bases: `object`


#### \__init__(cid, filenames)

#### cid(_: st_ )

#### filenames(_: List[str_ )

### _class_ thirdweb.types.storage.UriWithMetadata(base_uri, metadata_uris)
Bases: `object`


#### \__init__(base_uri, metadata_uris)

#### base_uri(_: st_ )

#### metadata_uris(_: List[str_ )
## thirdweb.types.tx module


### _class_ thirdweb.types.tx.TxResult(receipt)
Bases: `object`


#### \__init__(receipt)

#### receipt(_: web3.types.TxReceip_ )

### _class_ thirdweb.types.tx.TxResultWithData(receipt, data)
Bases: `thirdweb.types.tx.TxResult`, `Generic`[`thirdweb.types.tx.T`]


#### \__init__(receipt, data)

#### data(_: Callable[[], thirdweb.types.tx.T_ )

### _class_ thirdweb.types.tx.TxResultWithId(receipt, data, id)
Bases: `thirdweb.types.tx.TxResultWithData`[`thirdweb.types.tx.T`]


#### \__init__(receipt, data, id)

#### id(_: in_ )
## Module contents
