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


### _class_ thirdweb.core.sdk.ThirdwebSDK(provider: web3.main.Web3, signer: typing.Optional[eth_account.signers.local.LocalAccount] = None, options: thirdweb.types.sdk.SDKOptions = SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)), storage: thirdweb.core.classes.ipfs_storage.IpfsStorage = <thirdweb.core.classes.ipfs_storage.IpfsStorage object>)
Bases: [`thirdweb.core.classes.provider_handler.ProviderHandler`](thirdweb.core.classes.md#thirdweb.core.classes.provider_handler.ProviderHandler)


#### \__init__(provider: web3.main.Web3, signer: typing.Optional[eth_account.signers.local.LocalAccount] = None, options: thirdweb.types.sdk.SDKOptions = SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)), storage: thirdweb.core.classes.ipfs_storage.IpfsStorage = <thirdweb.core.classes.ipfs_storage.IpfsStorage object>)
Initialize the thirdweb SDK.


* **Parameters**

    
    * **provider** – web3 provider instance to use for getting on-chain data


    * **signer** – signer to use for sending transactions


    * **options** – optional SDK configuration options


    * **storage** – optional IPFS storage instance to use for storing data



#### deployer(_: [thirdweb.core.classes.contract_deployer.ContractDeployer](thirdweb.core.classes.md#thirdweb.core.classes.contract_deployer.ContractDeployer_ )

#### get_edition(address: str)
Returns an Edition contract SDK instance


* **Parameters**

    **address** – address of the Edition contract



* **Returns**

    Edition contract SDK instance



#### get_marketplace(address: str)
Returns a Marketplace contract SDK instance


* **Parameters**

    **address** – address of the Marketplace contract



* **Returns**

    Marketplace contract SDK instance



#### get_nft_collection(address: str)
Returns an NFT Collection contract SDK instance


* **Parameters**

    **address** – address of the NFT Collection contract



* **Returns**

    NFT Collection contract SDK instance



#### get_token(address: str)
Returns a Token contract SDK instance


* **Parameters**

    **address** – address of the Token contract



* **Returns**

    Token contract SDK instance



#### update_provider(provider: web3.main.Web3)
Update the provider instance used by the SDK.


* **Parameters**

    **provider** – web3 provider instance to use for getting on-chain data



#### update_signer(signer: Optional[eth_account.signers.local.LocalAccount] = None)
Update the signer instance used by the SDK.


* **Parameters**

    **signer** – signer to use for sending transactions


## Module contents
