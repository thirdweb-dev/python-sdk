# thirdweb.contracts package

## Submodules

## thirdweb.contracts.edition module

Interface for interacting with an edition contract


### _class_ thirdweb.contracts.edition.Edition(provider, address, storage, signer=None, options=SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))
Bases: [`thirdweb.core.classes.erc_1155.ERC1155`](thirdweb.core.classes.md#thirdweb.core.classes.erc_1155.ERC1155)


#### \__init__(provider, address, storage, signer=None, options=SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))

#### contract_roles(_: Final[List[[thirdweb.constants.role.Role](thirdweb.constants.md#thirdweb.constants.role.Role)]_ _ = [<Role.ADMIN: 'admin'>, <Role.MINTER: 'minter'>, <Role.TRANSFER: 'transfer'>_ )

#### contract_type(_: Final[[thirdweb.types.contract.ContractType](thirdweb.types.md#thirdweb.types.contract.ContractType)_ _ = 'edition_ )

#### metadata(_: [thirdweb.core.classes.contract_metadata.ContractMetadata](thirdweb.core.classes.md#thirdweb.core.classes.contract_metadata.ContractMetadata)[[thirdweb.abi.token_erc1155.TokenERC1155](thirdweb.abi.token_erc1155.md#thirdweb.abi.token_erc1155.TokenERC1155), thirdweb.types.settings.metadata.EditionContractMetadata_ )

#### mint(metadata_with_supply)
Mint a new NFT to the connected wallet


* **Parameters**

    **metadata_with_supply** ([`EditionMetadataInput`](thirdweb.types.md#thirdweb.types.nft.EditionMetadataInput)) – EditionMetadataInput for the NFT to mint



* **Return type**

    [`TxResultWithId`](thirdweb.types.md#thirdweb.types.tx.TxResultWithId)[[`EditionMetadata`](thirdweb.types.md#thirdweb.types.nft.EditionMetadata)]



* **Returns**

    receipt, id, and metadata of the mint



#### mint_additional_supply(token_id, additional_supply)
Mint additional supply of a token to the connected wallet


* **Parameters**

    
    * **token_id** (`int`) – token ID to mint additional supply of


    * **additional_supply** (`int`) – additional supply to mint



* **Return type**

    [`TxResultWithId`](thirdweb.types.md#thirdweb.types.tx.TxResultWithId)[[`EditionMetadata`](thirdweb.types.md#thirdweb.types.nft.EditionMetadata)]



* **Returns**

    receipt, id, and metadata of the mint



#### mint_additional_supply_to(to, token_id, additional_supply)
Mint additional supply of a token to the specified wallet


* **Parameters**

    
    * **to** (`str`) – wallet address to mint additional supply to


    * **token_id** (`int`) – token ID to mint additional supply of


    * **additional_supply** (`int`) – additional supply to mint



* **Return type**

    [`TxResultWithId`](thirdweb.types.md#thirdweb.types.tx.TxResultWithId)[[`EditionMetadata`](thirdweb.types.md#thirdweb.types.nft.EditionMetadata)]



* **Returns**

    receipt, id, and metadata of the mint



#### mint_batch(metadatas_with_supply)
Mint a batch of NFTs to the connected wallet


* **Parameters**

    **metadatas_with_supply** (`List`[[`EditionMetadataInput`](thirdweb.types.md#thirdweb.types.nft.EditionMetadataInput)]) – list of EditionMetadataInput for the NFTs to mint



* **Return type**

    `List`[[`TxResultWithId`](thirdweb.types.md#thirdweb.types.tx.TxResultWithId)[[`EditionMetadata`](thirdweb.types.md#thirdweb.types.nft.EditionMetadata)]]



* **Returns**

    receipts, ids, and metadatas of the mint



#### mint_batch_to(to, metadatas_with_supply)
Mint a batch of NFTs to the specified wallet


* **Parameters**

    
    * **to** (`str`) – wallet address to mint the NFTs to


    * **metadatas_with_supply** (`List`[[`EditionMetadataInput`](thirdweb.types.md#thirdweb.types.nft.EditionMetadataInput)]) – list of EditionMetadataInput for the NFTs to mint



* **Return type**

    `List`[[`TxResultWithId`](thirdweb.types.md#thirdweb.types.tx.TxResultWithId)[[`EditionMetadata`](thirdweb.types.md#thirdweb.types.nft.EditionMetadata)]]



* **Returns**

    receipts, ids, and metadatas of the mint



#### mint_to(to, metadata_with_supply)
Mint a new NFT to the specified wallet


* **Parameters**

    
    * **to** (`str`) – wallet address to mint the NFT to


    * **metadata_with_supply** ([`EditionMetadataInput`](thirdweb.types.md#thirdweb.types.nft.EditionMetadataInput)) – EditionMetadataInput for the NFT to mint



* **Return type**

    [`TxResultWithId`](thirdweb.types.md#thirdweb.types.tx.TxResultWithId)[[`EditionMetadata`](thirdweb.types.md#thirdweb.types.nft.EditionMetadata)]



* **Returns**

    receipt, id, and metadata of the mint



#### platform_fee(_: [thirdweb.core.classes.contract_platform_fee.ContractPlatformFee](thirdweb.core.classes.md#thirdweb.core.classes.contract_platform_fee.ContractPlatformFee)[[thirdweb.abi.token_erc1155.TokenERC1155](thirdweb.abi.token_erc1155.md#thirdweb.abi.token_erc1155.TokenERC1155)_ )

#### primary_sale(_: [thirdweb.core.classes.contract_sales.ContractPrimarySale](thirdweb.core.classes.md#thirdweb.core.classes.contract_sales.ContractPrimarySale)[[thirdweb.abi.token_erc1155.TokenERC1155](thirdweb.abi.token_erc1155.md#thirdweb.abi.token_erc1155.TokenERC1155)_ )

#### roles(_: [thirdweb.core.classes.contract_roles.ContractRoles](thirdweb.core.classes.md#thirdweb.core.classes.contract_roles.ContractRoles_ )

#### royalty(_: [thirdweb.core.classes.contract_royalty.ContractRoyalty](thirdweb.core.classes.md#thirdweb.core.classes.contract_royalty.ContractRoyalty)[[thirdweb.abi.token_erc1155.TokenERC1155](thirdweb.abi.token_erc1155.md#thirdweb.abi.token_erc1155.TokenERC1155)_ )

#### schema()
alias of `thirdweb.types.settings.metadata.EditionContractMetadata`

## thirdweb.contracts.maps module

## thirdweb.contracts.marketplace module

Interface for interacting with a marketplace contract


### _class_ thirdweb.contracts.marketplace.Marketplace(provider, address, storage, signer=None, options=SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))
Bases: [`thirdweb.core.classes.base_contract.BaseContract`](thirdweb.core.classes.md#thirdweb.core.classes.base_contract.BaseContract)[[`thirdweb.abi.marketplace.Marketplace`](thirdweb.abi.marketplace.md#thirdweb.abi.marketplace.Marketplace)]


#### \__init__(provider, address, storage, signer=None, options=SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))

#### allow_listing_from_any_asset()

* **Return type**

    `TxReceipt`



#### allow_listing_from_specific_asset_only(contract_address)

* **Return type**

    `TxReceipt`



#### auction(_: [thirdweb.core.classes.marketplace_auction.MarketplaceAuction](thirdweb.core.classes.md#thirdweb.core.classes.marketplace_auction.MarketplaceAuction_ )

#### buyout_listing(listing_id, quantity_desired=None, receiver=None)

* **Return type**

    `TxReceipt`



#### contract_roles(_: Final[List[[thirdweb.constants.role.Role](thirdweb.constants.md#thirdweb.constants.role.Role)]_ _ = [<Role.ADMIN: 'admin'>, <Role.LISTER: 'lister'>, <Role.ASSET: 'asset'>_ )

#### contract_type(_: Final[[thirdweb.types.contract.ContractType](thirdweb.types.md#thirdweb.types.contract.ContractType)_ _ = 'marketplace_ )

#### direct(_: [thirdweb.core.classes.marketplace_direct.MarketplaceDirect](thirdweb.core.classes.md#thirdweb.core.classes.marketplace_direct.MarketplaceDirect_ )

#### get_active_listings()

* **Return type**

    `List`[`Union`[[`DirectListing`](thirdweb.types.md#thirdweb.types.marketplace.DirectListing), [`AuctionListing`](thirdweb.types.md#thirdweb.types.marketplace.AuctionListing)]]



#### get_all(filter=None)

* **Return type**

    `List`[`Union`[[`DirectListing`](thirdweb.types.md#thirdweb.types.marketplace.DirectListing), [`AuctionListing`](thirdweb.types.md#thirdweb.types.marketplace.AuctionListing)]]



#### get_all_listings(filter=None)

* **Return type**

    `List`[`Union`[[`DirectListing`](thirdweb.types.md#thirdweb.types.marketplace.DirectListing), [`AuctionListing`](thirdweb.types.md#thirdweb.types.marketplace.AuctionListing)]]



#### get_bid_buffer_bps()

* **Return type**

    `int`



#### get_listing(listing_id)

* **Return type**

    `Union`[[`DirectListing`](thirdweb.types.md#thirdweb.types.marketplace.DirectListing), [`AuctionListing`](thirdweb.types.md#thirdweb.types.marketplace.AuctionListing)]



#### get_time_buffer_in_seconds()

* **Return type**

    `int`



#### get_total_count()

* **Return type**

    `int`



#### is_restricted_to_lister_role_only()

* **Return type**

    `bool`



#### metadata(_: [thirdweb.core.classes.contract_metadata.ContractMetadata](thirdweb.core.classes.md#thirdweb.core.classes.contract_metadata.ContractMetadata)[[thirdweb.abi.marketplace.Marketplace](thirdweb.abi.marketplace.md#thirdweb.abi.marketplace.Marketplace), thirdweb.types.settings.metadata.MarketplaceContractMetadata_ )

#### platform_fee(_: [thirdweb.core.classes.contract_platform_fee.ContractPlatformFee](thirdweb.core.classes.md#thirdweb.core.classes.contract_platform_fee.ContractPlatformFee)[[thirdweb.abi.marketplace.Marketplace](thirdweb.abi.marketplace.md#thirdweb.abi.marketplace.Marketplace)_ )

#### roles(_: [thirdweb.core.classes.contract_roles.ContractRoles](thirdweb.core.classes.md#thirdweb.core.classes.contract_roles.ContractRoles_ )

#### schema()
alias of `thirdweb.types.settings.metadata.MarketplaceContractMetadata`


#### set_bid_buffer_bps(buffer_bps)

* **Return type**

    `TxReceipt`



#### set_time_buffer_in_seconds(buffer_in_seconds)

* **Return type**

    `TxReceipt`


## thirdweb.contracts.nft_collection module

Interface for interacting with an nft collection contract


### _class_ thirdweb.contracts.nft_collection.NFTCollection(provider, address, storage, signer=None, options=SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))
Bases: [`thirdweb.core.classes.erc_721.ERC721`](thirdweb.core.classes.md#thirdweb.core.classes.erc_721.ERC721)


#### \__init__(provider, address, storage, signer=None, options=SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))

#### contract_roles(_: Final[List[[thirdweb.constants.role.Role](thirdweb.constants.md#thirdweb.constants.role.Role)]_ _ = [<Role.ADMIN: 'admin'>, <Role.MINTER: 'minter'>, <Role.TRANSFER: 'transfer'>_ )

#### contract_type(_: Final[[thirdweb.types.contract.ContractType](thirdweb.types.md#thirdweb.types.contract.ContractType)_ _ = 'nft-collection_ )

#### metadata(_: [thirdweb.core.classes.contract_metadata.ContractMetadata](thirdweb.core.classes.md#thirdweb.core.classes.contract_metadata.ContractMetadata)[[thirdweb.abi.token_erc721.TokenERC721](thirdweb.abi.token_erc721.md#thirdweb.abi.token_erc721.TokenERC721), thirdweb.types.settings.metadata.NFTCollectionContractMetadata_ )

#### mint(metadata)
Mint a new NFT to the connected wallet


* **Parameters**

    **metadata** (`Union`[[`NFTMetadataInput`](thirdweb.types.md#thirdweb.types.nft.NFTMetadataInput), `str`]) – metadata of the NFT to mint



* **Return type**

    [`TxResultWithId`](thirdweb.types.md#thirdweb.types.tx.TxResultWithId)[[`NFTMetadataOwner`](thirdweb.types.md#thirdweb.types.nft.NFTMetadataOwner)]



* **Returns**

    receipt, id, and metadata for the mint



#### mint_batch(metadatas)
Mint a batch of new NFTs to the connected wallet


* **Parameters**

    **metadatas** (`List`[`Union`[[`NFTMetadataInput`](thirdweb.types.md#thirdweb.types.nft.NFTMetadataInput), `str`]]) – list of metadata of the NFTs to mint



* **Return type**

    `List`[[`TxResultWithId`](thirdweb.types.md#thirdweb.types.tx.TxResultWithId)[[`NFTMetadataOwner`](thirdweb.types.md#thirdweb.types.nft.NFTMetadataOwner)]]



* **Returns**

    receipts, ids, and metadatas for each mint



#### mint_batch_to(to, metadatas)
Mint a batch of new NFTs to the specified wallet


* **Parameters**

    
    * **to** (`str`) – wallet address to mint the NFTs to


    * **metadatas** (`List`[`Union`[[`NFTMetadataInput`](thirdweb.types.md#thirdweb.types.nft.NFTMetadataInput), `str`]]) – list of metadata of the NFTs to mint



* **Return type**

    `List`[[`TxResultWithId`](thirdweb.types.md#thirdweb.types.tx.TxResultWithId)[[`NFTMetadataOwner`](thirdweb.types.md#thirdweb.types.nft.NFTMetadataOwner)]]



* **Returns**

    receipts, ids, and metadatas for each mint



#### mint_to(to, metadata)
Mint a new NFT to the specified wallet


* **Parameters**

    
    * **to** (`str`) – wallet address to mint the NFT to


    * **metadata** (`Union`[[`NFTMetadataInput`](thirdweb.types.md#thirdweb.types.nft.NFTMetadataInput), `str`]) – metadata of the NFT to mint



* **Return type**

    [`TxResultWithId`](thirdweb.types.md#thirdweb.types.tx.TxResultWithId)[[`NFTMetadataOwner`](thirdweb.types.md#thirdweb.types.nft.NFTMetadataOwner)]



* **Returns**

    receipt, id, and metadata for the mint



#### platform_fee(_: [thirdweb.core.classes.contract_platform_fee.ContractPlatformFee](thirdweb.core.classes.md#thirdweb.core.classes.contract_platform_fee.ContractPlatformFee)[[thirdweb.abi.token_erc721.TokenERC721](thirdweb.abi.token_erc721.md#thirdweb.abi.token_erc721.TokenERC721)_ )

#### primary_sale(_: [thirdweb.core.classes.contract_sales.ContractPrimarySale](thirdweb.core.classes.md#thirdweb.core.classes.contract_sales.ContractPrimarySale)[[thirdweb.abi.token_erc721.TokenERC721](thirdweb.abi.token_erc721.md#thirdweb.abi.token_erc721.TokenERC721)_ )

#### roles(_: [thirdweb.core.classes.contract_roles.ContractRoles](thirdweb.core.classes.md#thirdweb.core.classes.contract_roles.ContractRoles_ )

#### royalty(_: [thirdweb.core.classes.contract_royalty.ContractRoyalty](thirdweb.core.classes.md#thirdweb.core.classes.contract_royalty.ContractRoyalty)[[thirdweb.abi.token_erc721.TokenERC721](thirdweb.abi.token_erc721.md#thirdweb.abi.token_erc721.TokenERC721)_ )

#### schema()
alias of `thirdweb.types.settings.metadata.NFTCollectionContractMetadata`

## thirdweb.contracts.token module

Interface for interacting with a token contract


### _class_ thirdweb.contracts.token.Token(provider, address, storage, signer=None, options=SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))
Bases: [`thirdweb.core.classes.erc_20.ERC20`](thirdweb.core.classes.md#thirdweb.core.classes.erc_20.ERC20)


#### \__init__(provider, address, storage, signer=None, options=SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))

#### contract_roles(_: Final[List[[thirdweb.constants.role.Role](thirdweb.constants.md#thirdweb.constants.role.Role)]_ _ = [<Role.ADMIN: 'admin'>, <Role.MINTER: 'minter'>, <Role.TRANSFER: 'transfer'>_ )

#### contract_type(_: Final[[thirdweb.types.contract.ContractType](thirdweb.types.md#thirdweb.types.contract.ContractType)_ _ = 'token_ )

#### delegate_to(delegatee_address)
Delegate the connected wallets tokens to a specified wallet.


* **Parameters**

    **delegatee_address** (`str`) – wallet address to delegate tokens to



* **Return type**

    `TxReceipt`



* **Returns**

    transaction receipt of the delegation



#### get_delegation()
Get the connected wallets delegatee address for this token.


* **Return type**

    `str`



* **Returns**

    delegation address of the connected wallet



#### get_delegation_of(account)
Get a specified wallets delegatee for this token.


* **Parameters**

    **account** (`str`) – wallet address to check the delegation of



* **Return type**

    `str`



* **Returns**

    delegation address of the specified wallet



#### get_vote_balance()
Get the connected wallets voting power in this token.


* **Return type**

    [`CurrencyValue`](thirdweb.types.md#thirdweb.types.currency.CurrencyValue)



* **Returns**

    vote balance of the connected wallet



#### get_vote_balance_of(account)
Get the voting power of the specified wallet in this token.


* **Parameters**

    **account** (`str`) – wallet address to check the balance of



* **Return type**

    [`CurrencyValue`](thirdweb.types.md#thirdweb.types.currency.CurrencyValue)



* **Returns**

    vote balance of the specified wallet



#### metadata(_: [thirdweb.core.classes.contract_metadata.ContractMetadata](thirdweb.core.classes.md#thirdweb.core.classes.contract_metadata.ContractMetadata)[[thirdweb.abi.token_erc20.TokenERC20](thirdweb.abi.token_erc20.md#thirdweb.abi.token_erc20.TokenERC20), thirdweb.types.settings.metadata.TokenContractMetadata_ )

#### mint(amount)
Mint tokens to the connected wallet.


* **Parameters**

    **amount** (`float`) – amount of tokens to mint



* **Return type**

    `TxReceipt`



* **Returns**

    transaction receipt of the mint



#### mint_batch_to(args)
Mint tokens to a list of wallets.


* **Parameters**

    **args** (`List`[[`TokenAmount`](thirdweb.types.md#thirdweb.types.currency.TokenAmount)]) – list of wallet addresses and amounts to mint



* **Return type**

    `TxReceipt`



* **Returns**

    transaction receipt of the mint



#### mint_to(to, amount)
Mint tokens to a specified wallet.


* **Parameters**

    
    * **to** (`str`) – wallet address to mint tokens to


    * **amount** (`float`) – amount of tokens to mint



* **Return type**

    `TxReceipt`



* **Returns**

    transaction receipt of the mint



#### platform_fee(_: [thirdweb.core.classes.contract_platform_fee.ContractPlatformFee](thirdweb.core.classes.md#thirdweb.core.classes.contract_platform_fee.ContractPlatformFee_ )

#### roles(_: [thirdweb.core.classes.contract_roles.ContractRoles](thirdweb.core.classes.md#thirdweb.core.classes.contract_roles.ContractRoles_ )

#### schema()
alias of `thirdweb.types.settings.metadata.TokenContractMetadata`

## Module contents
