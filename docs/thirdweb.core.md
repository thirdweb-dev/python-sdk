# thirdweb.core package

## Subpackages


* [thirdweb.core.classes package](thirdweb.core.classes.md)


    * [Submodules](thirdweb.core.classes.md#submodules)


    * [thirdweb.core.classes.base_contract module](thirdweb.core.classes.md#module-thirdweb.core.classes.base_contract)


    * [thirdweb.core.classes.contract_deployer module](thirdweb.core.classes.md#module-thirdweb.core.classes.contract_deployer)


    * [thirdweb.core.classes.contract_metadata module](thirdweb.core.classes.md#module-thirdweb.core.classes.contract_metadata)


    * [thirdweb.core.classes.contract_platform_fee module](thirdweb.core.classes.md#module-thirdweb.core.classes.contract_platform_fee)


    * [thirdweb.core.classes.contract_roles module](thirdweb.core.classes.md#module-thirdweb.core.classes.contract_roles)


    * [thirdweb.core.classes.contract_royalty module](thirdweb.core.classes.md#module-thirdweb.core.classes.contract_royalty)


    * [thirdweb.core.classes.contract_sales module](thirdweb.core.classes.md#module-thirdweb.core.classes.contract_sales)


    * [thirdweb.core.classes.contract_wrapper module](thirdweb.core.classes.md#module-thirdweb.core.classes.contract_wrapper)


    * [thirdweb.core.classes.erc_1155 module](thirdweb.core.classes.md#module-thirdweb.core.classes.erc_1155)


    * [thirdweb.core.classes.erc_20 module](thirdweb.core.classes.md#module-thirdweb.core.classes.erc_20)


    * [thirdweb.core.classes.erc_721 module](thirdweb.core.classes.md#module-thirdweb.core.classes.erc_721)


    * [thirdweb.core.classes.factory module](thirdweb.core.classes.md#module-thirdweb.core.classes.factory)


    * [thirdweb.core.classes.ipfs_storage module](thirdweb.core.classes.md#module-thirdweb.core.classes.ipfs_storage)


    * [thirdweb.core.classes.marketplace_auction module](thirdweb.core.classes.md#module-thirdweb.core.classes.marketplace_auction)


    * [thirdweb.core.classes.marketplace_direct module](thirdweb.core.classes.md#module-thirdweb.core.classes.marketplace_direct)


    * [thirdweb.core.classes.provider_handler module](thirdweb.core.classes.md#module-thirdweb.core.classes.provider_handler)


    * [thirdweb.core.classes.registry module](thirdweb.core.classes.md#module-thirdweb.core.classes.registry)


    * [Module contents](thirdweb.core.classes.md#module-thirdweb.core.classes)


## Submodules

## thirdweb.core.sdk module


### _class_ thirdweb.core.sdk.ThirdwebSDK(provider, signer=None, options=SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)), storage=<thirdweb.core.classes.ipfs_storage.IpfsStorage object>)
Bases: [`thirdweb.core.classes.provider_handler.ProviderHandler`](thirdweb.core.classes.md#thirdweb.core.classes.provider_handler.ProviderHandler)


#### \__init__(provider, signer=None, options=SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)), storage=<thirdweb.core.classes.ipfs_storage.IpfsStorage object>)
Initialize the thirdweb SDK.


* **Parameters**

    
    * **provider** (`Web3`) – web3 provider instance to use for getting on-chain data


    * **signer** (`Optional`[`LocalAccount`]) – signer to use for sending transactions


    * **options** ([`SDKOptions`](thirdweb.types.md#thirdweb.types.sdk.SDKOptions)) – optional SDK configuration options


    * **storage** ([`IpfsStorage`](thirdweb.core.classes.md#thirdweb.core.classes.ipfs_storage.IpfsStorage)) – optional IPFS storage instance to use for storing data



#### deployer(_: [thirdweb.core.classes.contract_deployer.ContractDeployer](thirdweb.core.classes.md#thirdweb.core.classes.contract_deployer.ContractDeployer_ )

#### get_edition(address)
Returns an Edition contract SDK instance


* **Parameters**

    **address** (`str`) – address of the Edition contract



* **Return type**

    [`Edition`](thirdweb.contracts.md#thirdweb.contracts.edition.Edition)



* **Returns**

    Edition contract SDK instance



#### get_marketplace(address)
Returns a Marketplace contract SDK instance


* **Parameters**

    **address** (`str`) – address of the Marketplace contract



* **Return type**

    [`Marketplace`](thirdweb.contracts.md#thirdweb.contracts.marketplace.Marketplace)



* **Returns**

    Marketplace contract SDK instance



#### get_nft_collection(address)
Returns an NFT Collection contract SDK instance


* **Parameters**

    **address** (`str`) – address of the NFT Collection contract



* **Return type**

    [`NFTCollection`](thirdweb.contracts.md#thirdweb.contracts.nft_collection.NFTCollection)



* **Returns**

    NFT Collection contract SDK instance



#### get_token(address)
Returns a Token contract SDK instance


* **Parameters**

    **address** (`str`) – address of the Token contract



* **Return type**

    [`Token`](thirdweb.contracts.md#thirdweb.contracts.token.Token)



* **Returns**

    Token contract SDK instance



#### update_provider(provider)
Update the provider instance used by the SDK.


* **Parameters**

    **provider** (`Web3`) – web3 provider instance to use for getting on-chain data



#### update_signer(signer=None)
Update the signer instance used by the SDK.


* **Parameters**

    **signer** (`Optional`[`LocalAccount`]) – signer to use for sending transactions


## Module contents
