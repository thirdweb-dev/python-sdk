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


### _class_ thirdweb.types.currency.Currency(name: str, symbol: str, decimals: int)
Bases: `object`


#### \__init__(name: str, symbol: str, decimals: int)

#### decimals(_: in_ )

#### name(_: st_ )

#### symbol(_: st_ )

### _class_ thirdweb.types.currency.CurrencyValue(name: str, symbol: str, decimals: int, value: int, display_value: float)
Bases: `thirdweb.types.currency.Currency`


#### \__init__(name: str, symbol: str, decimals: int, value: int, display_value: float)

#### display_value(_: floa_ )

#### value(_: in_ )

### _class_ thirdweb.types.currency.NativeToken(name: str, symbol: str, decimals: int, wrapped: thirdweb.types.currency.WrappedToken)
Bases: `object`


#### \__init__(name: str, symbol: str, decimals: int, wrapped: thirdweb.types.currency.WrappedToken)

#### decimals(_: in_ )

#### name(_: st_ )

#### symbol(_: st_ )

#### wrapped(_: thirdweb.types.currency.WrappedToke_ )

### _class_ thirdweb.types.currency.TokenAmount(to_address: str, amount: float)
Bases: `object`


#### \__init__(to_address: str, amount: float)

#### amount(_: floa_ )

#### to_address(_: st_ )

### _class_ thirdweb.types.currency.WrappedToken(address: str, name: str, symbol: str)
Bases: `object`


#### \__init__(address: str, name: str, symbol: str)

#### address(_: st_ )

#### name(_: st_ )

#### symbol(_: st_ )
## thirdweb.types.marketplace module


### _class_ thirdweb.types.marketplace.AuctionListing(id: int, asset_contract_address: str, token_id: int, asset: thirdweb.types.nft.NFTMetadata, start_time_in_epoch_seconds: int, end_time_in_epoch_seconds: int, quantity: int, currency_contract_address: str, reserve_price: int, buyout_price: int, buyout_currency_value_per_token: thirdweb.types.currency.CurrencyValue, reserve_price_currency_value_per_token: thirdweb.types.currency.CurrencyValue, seller_address: str)
Bases: `object`


#### \__init__(id: int, asset_contract_address: str, token_id: int, asset: thirdweb.types.nft.NFTMetadata, start_time_in_epoch_seconds: int, end_time_in_epoch_seconds: int, quantity: int, currency_contract_address: str, reserve_price: int, buyout_price: int, buyout_currency_value_per_token: thirdweb.types.currency.CurrencyValue, reserve_price_currency_value_per_token: thirdweb.types.currency.CurrencyValue, seller_address: str)

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

### _class_ thirdweb.types.marketplace.ContractListing(listing_id: int, token_owner: str, asset_contract: str, token_id: int, start_time: int, end_time: int, quantity: int, currency: str, reserve_price_per_token: int, buyout_price_per_token: int, token_type: int, listing_type: int)
Bases: `object`


#### \__init__(listing_id: int, token_owner: str, asset_contract: str, token_id: int, start_time: int, end_time: int, quantity: int, currency: str, reserve_price_per_token: int, buyout_price_per_token: int, token_type: int, listing_type: int)

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

### _class_ thirdweb.types.marketplace.ContractOffer(listing_id: int, offeror: str, quantity_wanted: int, currency: str, price_per_token: int)
Bases: `object`


#### \__init__(listing_id: int, offeror: str, quantity_wanted: int, currency: str, price_per_token: int)

#### currency(_: st_ )

#### listing_id(_: in_ )

#### offeror(_: st_ )

#### price_per_token(_: in_ )

#### quantity_wanted(_: in_ )

### _class_ thirdweb.types.marketplace.DirectListing(id: int, asset_contract_address: str, token_id: int, asset: thirdweb.types.nft.NFTMetadata, start_time_in_seconds: int, seconds_until_end: int, quantity: int, currency_contract_address: str, buyout_currency_value_per_token: thirdweb.types.currency.CurrencyValue, buyout_price: int, seller_address: str)
Bases: `object`


#### \__init__(id: int, asset_contract_address: str, token_id: int, asset: thirdweb.types.nft.NFTMetadata, start_time_in_seconds: int, seconds_until_end: int, quantity: int, currency_contract_address: str, buyout_currency_value_per_token: thirdweb.types.currency.CurrencyValue, buyout_price: int, seller_address: str)

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

### _class_ thirdweb.types.marketplace.MarketplaceFilter(start: int = 0, count: int = 100, seller: Union[str, NoneType] = None, token_contract: Union[str, NoneType] = None, token_id: Union[int, NoneType] = None)
Bases: `object`


#### \__init__(start: int = 0, count: int = 100, seller: Optional[str] = None, token_contract: Optional[str] = None, token_id: Optional[int] = None)

#### count(_: in_ _ = 10_ )

#### seller(_: Optional[str_ _ = Non_ )

#### start(_: in_ _ = _ )

#### token_contract(_: Optional[str_ _ = Non_ )

#### token_id(_: Optional[int_ _ = Non_ )

### _class_ thirdweb.types.marketplace.NewAuctionListing(asset_contract_address: str, token_id: int, start_time_in_seconds: int, listing_duration_in_seconds: int, quantity: int, currency_contract_address: str, reserve_price_per_token: int, buyout_price_per_token: int)
Bases: `object`


#### \__init__(asset_contract_address: str, token_id: int, start_time_in_seconds: int, listing_duration_in_seconds: int, quantity: int, currency_contract_address: str, reserve_price_per_token: int, buyout_price_per_token: int)

#### asset_contract_address(_: st_ )

#### buyout_price_per_token(_: in_ )

#### currency_contract_address(_: st_ )

#### listing_duration_in_seconds(_: in_ )

#### quantity(_: in_ )

#### reserve_price_per_token(_: in_ )

#### start_time_in_seconds(_: in_ )

#### token_id(_: in_ )

#### type(_ = 'NewAuctionListing_ )

### _class_ thirdweb.types.marketplace.NewDirectListing(asset_contract_address: str, token_id: int, start_time_in_seconds: int, listing_duration_in_seconds: int, quantity: int, currency_contract_address: str, buyout_price_per_token: int)
Bases: `object`


#### \__init__(asset_contract_address: str, token_id: int, start_time_in_seconds: int, listing_duration_in_seconds: int, quantity: int, currency_contract_address: str, buyout_price_per_token: int)

#### asset_contract_address(_: st_ )

#### buyout_price_per_token(_: in_ )

#### currency_contract_address(_: st_ )

#### listing_duration_in_seconds(_: in_ )

#### quantity(_: in_ )

#### start_time_in_seconds(_: in_ )

#### token_id(_: in_ )

#### type(_ = 'NewDirectListing_ )

### _class_ thirdweb.types.marketplace.Offer(listing_id: int, buyer_address: str, quantity_desired: int, price_per_token: int, currency_value: thirdweb.types.currency.CurrencyValue, currency_contract_address: str)
Bases: `object`


#### \__init__(listing_id: int, buyer_address: str, quantity_desired: int, price_per_token: int, currency_value: thirdweb.types.currency.CurrencyValue, currency_contract_address: str)

#### buyer_address(_: st_ )

#### currency_contract_address(_: st_ )

#### currency_value(_: thirdweb.types.currency.CurrencyValu_ )

#### listing_id(_: in_ )

#### price_per_token(_: in_ )

#### quantity_desired(_: in_ )
## thirdweb.types.nft module


### _class_ thirdweb.types.nft.EditionMetadata(metadata: thirdweb.types.nft.NFTMetadata, supply: int)
Bases: `object`


#### \__init__(metadata: thirdweb.types.nft.NFTMetadata, supply: int)

#### metadata(_: thirdweb.types.nft.NFTMetadat_ )

#### supply(_: in_ )

### _class_ thirdweb.types.nft.EditionMetadataInput(metadata: Union[thirdweb.types.nft.NFTMetadataInput, str], supply: int)
Bases: `object`

The metadata of an edition NFT to mint


* **Parameters**

    
    * **metadata** – The metadata of the edition NFT


    * **supply** – The supply of the edition NFT



#### \__init__(metadata: Union[thirdweb.types.nft.NFTMetadataInput, str], supply: int)

#### metadata(_: Union[thirdweb.types.nft.NFTMetadataInput, str_ )

#### supply(_: in_ )

### _class_ thirdweb.types.nft.EditionMetadataOwner(metadata: thirdweb.types.nft.NFTMetadata, supply: int, owner: str, quantity_owned: int)
Bases: `thirdweb.types.nft.EditionMetadata`


#### \__init__(metadata: thirdweb.types.nft.NFTMetadata, supply: int, owner: str, quantity_owned: int)

#### owner(_: st_ )

#### quantity_owned(_: in_ )

### _class_ thirdweb.types.nft.NFTMetadata(id: int, uri: str, name: str, description: Union[str, NoneType] = None, image: Union[str, NoneType] = None, external_url: Union[str, NoneType] = None, animation_url: Union[str, NoneType] = None, background_color: Union[str, NoneType] = None, properties: Union[Dict[Any, Any], NoneType] = None)
Bases: `object`


#### \__init__(id: int, uri: str, name: str, description: Optional[str] = None, image: Optional[str] = None, external_url: Optional[str] = None, animation_url: Optional[str] = None, background_color: Optional[str] = None, properties: Optional[Dict[Any, Any]] = None)

#### animation_url(_: Optional[str_ _ = Non_ )

#### background_color(_: Optional[str_ _ = Non_ )

#### description(_: Optional[str_ _ = Non_ )

#### external_url(_: Optional[str_ _ = Non_ )

#### _static_ from_json(json: Dict[str, Any])

#### id(_: in_ )

#### image(_: Optional[str_ _ = Non_ )

#### name(_: st_ )

#### properties(_: Optional[Dict[Any, Any]_ _ = Non_ )

#### uri(_: st_ )

### _class_ thirdweb.types.nft.NFTMetadataInput(name: str, description: Optional[str] = None, image: Optional[str] = None, external_url: Optional[str] = None, animation_url: Optional[str] = None, background_color: Optional[str] = None, properties: Optional[Dict[str, Any]] = None)
Bases: `object`

The metadata of an NFT to mint

You can use the NFTMetadataInput.from_json(json) method to create
an instance of this class from a dictionary.


* **Parameters**

    
    * **name** – The name of the NFT


    * **description** – The optional description of the NFT


    * **image** – The optional image of the NFT


    * **external_url** – The optional external URL of the NFT


    * **animation_url** – The optional animation URL of the NFT


    * **background_color** – The optional background color of the NFT


    * **properties** – The optional properties of the NFT



#### \__init__(name: str, description: Optional[str] = None, image: Optional[str] = None, external_url: Optional[str] = None, animation_url: Optional[str] = None, background_color: Optional[str] = None, properties: Optional[Dict[str, Any]] = None)

#### animation_url(_: Optional[str_ _ = Non_ )

#### background_color(_: Optional[str_ _ = Non_ )

#### description(_: Optional[str_ _ = Non_ )

#### external_url(_: Optional[str_ _ = Non_ )

#### _static_ from_json(json: Dict[str, Any])

#### image(_: Optional[str_ _ = Non_ )

#### name(_: st_ )

#### properties(_: Optional[Dict[str, Any]_ _ = Non_ )

#### to_json()

### _class_ thirdweb.types.nft.NFTMetadataOwner(metadata: thirdweb.types.nft.NFTMetadata, owner: str)
Bases: `object`


#### \__init__(metadata: thirdweb.types.nft.NFTMetadata, owner: str)

#### metadata(_: thirdweb.types.nft.NFTMetadat_ )

#### owner(_: st_ )

### _class_ thirdweb.types.nft.QueryAllParams(start: int = 0, count: int = 100)
Bases: `object`


#### \__init__(start: int = 0, count: int = 100)

#### count(_: in_ _ = 10_ )

#### start(_: in_ _ = _ )
## thirdweb.types.sdk module


### _class_ thirdweb.types.sdk.GasSettings(max_price_in_gwei: int = 300, speed: thirdweb.types.sdk.GasSpeed = GasSpeed.FASTEST)
Bases: `object`

The gas settings for the SDK.


* **Parameters**

    
    * **max_price_in_gwei** – maximum gas price in gwei, defaults to 300


    * **speed** – gas speed to use, defaults to “fastest”



#### \__init__(max_price_in_gwei: int = 300, speed: thirdweb.types.sdk.GasSpeed = GasSpeed.FASTEST)

#### max_price_in_gwei(_: in_ _ = 30_ )

#### speed(_: thirdweb.types.sdk.GasSpee_ _ = 'fastest_ )

### _class_ thirdweb.types.sdk.GasSpeed(value)
Bases: `enum.Enum`

An enumeration.


#### FAST(_ = 'fast_ )

#### FASTEST(_ = 'fastest_ )

#### STANDARD(_ = 'standard_ )

### _class_ thirdweb.types.sdk.ReadOnlySettings(rpc_url: str = '', chain_id: Optional[[thirdweb.constants.chains.ChainId](thirdweb.constants.md#thirdweb.constants.chains.ChainId)] = None)
Bases: `object`

The read-only RPC settings for the SDK.


* **Parameters**

    
    * **rpc_url** – URL of the RPC


    * **chain_id** – optional chain ID to use for the RPC



#### \__init__(rpc_url: str = '', chain_id: Optional[[thirdweb.constants.chains.ChainId](thirdweb.constants.md#thirdweb.constants.chains.ChainId)] = None)

#### chain_id(_: Optional[[thirdweb.constants.chains.ChainId](thirdweb.constants.md#thirdweb.constants.chains.ChainId)_ _ = Non_ )

#### rpc_url(_: st_ _ = '_ )

### _class_ thirdweb.types.sdk.SDKOptions(read_only_settings: typing.Optional[thirdweb.types.sdk.ReadOnlySettings] = None, gas_settings: thirdweb.types.sdk.GasSettings = GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>))
Bases: `object`

Optional settings to configure the SDK


* **Parameters**

    
    * **read_only_settings** – optional read-only RPC settings


    * **gas_settings** – gas settings



#### \__init__(read_only_settings: typing.Optional[thirdweb.types.sdk.ReadOnlySettings] = None, gas_settings: thirdweb.types.sdk.GasSettings = GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>))

#### gas_settings(_: thirdweb.types.sdk.GasSetting_ _ = GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>_ )

#### read_only_settings(_: Optional[thirdweb.types.sdk.ReadOnlySettings_ _ = Non_ )
## thirdweb.types.storage module


### _class_ thirdweb.types.storage.CidWithFileName(cid: str, filenames: List[str])
Bases: `object`


#### \__init__(cid: str, filenames: List[str])

#### cid(_: st_ )

#### filenames(_: List[str_ )

### _class_ thirdweb.types.storage.UriWithMetadata(base_uri: str, metadata_uris: List[str])
Bases: `object`


#### \__init__(base_uri: str, metadata_uris: List[str])

#### base_uri(_: st_ )

#### metadata_uris(_: List[str_ )
## thirdweb.types.tx module


### _class_ thirdweb.types.tx.TxResult(receipt: web3.types.TxReceipt)
Bases: `object`


#### \__init__(receipt: web3.types.TxReceipt)

#### receipt(_: web3.types.TxReceip_ )

### _class_ thirdweb.types.tx.TxResultWithData(\*args, \*\*kwds)
Bases: `thirdweb.types.tx.TxResult`, `Generic`[`thirdweb.types.tx.T`]


#### \__init__(receipt: web3.types.TxReceipt, data: Callable[[], thirdweb.types.tx.T])

#### data(_: Callable[[], thirdweb.types.tx.T_ )

### _class_ thirdweb.types.tx.TxResultWithId(\*args, \*\*kwds)
Bases: `thirdweb.types.tx.TxResultWithData`[`thirdweb.types.tx.T`]


#### \__init__(receipt: web3.types.TxReceipt, data: Callable[[], thirdweb.types.tx.T], id: int)

#### id(_: in_ )
## Module contents
