# thirdweb.contracts package

## Submodules

## thirdweb.contracts.edition module

Interface for interacting with an edition contract


### _class_ thirdweb.contracts.edition.Edition(provider: web3.main.Web3, address: str, storage: thirdweb.core.classes.ipfs_storage.IpfsStorage, signer: typing.Optional[eth_account.signers.local.LocalAccount] = None, options: thirdweb.types.sdk.SDKOptions = SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))
Bases: [`thirdweb.core.classes.erc_1155.ERC1155`](thirdweb.core.classes.md#thirdweb.core.classes.erc_1155.ERC1155)


#### \__init__(provider: web3.main.Web3, address: str, storage: thirdweb.core.classes.ipfs_storage.IpfsStorage, signer: typing.Optional[eth_account.signers.local.LocalAccount] = None, options: thirdweb.types.sdk.SDKOptions = SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))

#### contract_roles(_: Final[List[[thirdweb.constants.role.Role](thirdweb.constants.md#thirdweb.constants.role.Role)]_ _ = [<Role.ADMIN: 'admin'>, <Role.MINTER: 'minter'>, <Role.TRANSFER: 'transfer'>_ )

#### contract_type(_: Final[[thirdweb.types.contract.ContractType](thirdweb.types.md#thirdweb.types.contract.ContractType)_ _ = 'edition_ )

#### metadata(_: [thirdweb.core.classes.contract_metadata.ContractMetadata](thirdweb.core.classes.md#thirdweb.core.classes.contract_metadata.ContractMetadata)[[thirdweb.abi.token_erc1155.TokenERC1155](thirdweb.abi.token_erc1155.md#thirdweb.abi.token_erc1155.TokenERC1155), thirdweb.types.settings.metadata.EditionContractMetadata_ )

#### mint(metadata_with_supply: [thirdweb.types.nft.EditionMetadataInput](thirdweb.types.md#thirdweb.types.nft.EditionMetadataInput))
Mint a new NFT to the connected wallet


* **Parameters**

    **metadata_with_supply** – EditionMetadataInput for the NFT to mint



* **Returns**

    receipt, id, and metadata of the mint



#### mint_additional_supply(token_id: int, additional_supply: int)
Mint additional supply of a token to the connected wallet


* **Parameters**

    
    * **token_id** – token ID to mint additional supply of


    * **additional_supply** – additional supply to mint



* **Returns**

    receipt, id, and metadata of the mint



#### mint_additional_supply_to(to: str, token_id: int, additional_supply: int)
Mint additional supply of a token to the specified wallet


* **Parameters**

    
    * **to** – wallet address to mint additional supply to


    * **token_id** – token ID to mint additional supply of


    * **additional_supply** – additional supply to mint



* **Returns**

    receipt, id, and metadata of the mint



#### mint_batch(metadatas_with_supply: List[[thirdweb.types.nft.EditionMetadataInput](thirdweb.types.md#thirdweb.types.nft.EditionMetadataInput)])
Mint a batch of NFTs to the connected wallet


* **Parameters**

    **metadatas_with_supply** – list of EditionMetadataInput for the NFTs to mint



* **Returns**

    receipts, ids, and metadatas of the mint



#### mint_batch_to(to: str, metadatas_with_supply: List[[thirdweb.types.nft.EditionMetadataInput](thirdweb.types.md#thirdweb.types.nft.EditionMetadataInput)])
Mint a batch of NFTs to the specified wallet


* **Parameters**

    
    * **to** – wallet address to mint the NFTs to


    * **metadatas_with_supply** – list of EditionMetadataInput for the NFTs to mint



* **Returns**

    receipts, ids, and metadatas of the mint



#### mint_to(to: str, metadata_with_supply: [thirdweb.types.nft.EditionMetadataInput](thirdweb.types.md#thirdweb.types.nft.EditionMetadataInput))
Mint a new NFT to the specified wallet


* **Parameters**

    
    * **to** – wallet address to mint the NFT to


    * **metadata_with_supply** – EditionMetadataInput for the NFT to mint



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


### _class_ thirdweb.contracts.marketplace.Marketplace(provider: web3.main.Web3, address: str, storage: thirdweb.core.classes.ipfs_storage.IpfsStorage, signer: typing.Optional[eth_account.signers.local.LocalAccount] = None, options: thirdweb.types.sdk.SDKOptions = SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))
Bases: [`thirdweb.core.classes.base_contract.BaseContract`](thirdweb.core.classes.md#thirdweb.core.classes.base_contract.BaseContract)[[`thirdweb.abi.marketplace.Marketplace`](thirdweb.abi.marketplace.md#thirdweb.abi.marketplace.Marketplace)]


#### \__init__(provider: web3.main.Web3, address: str, storage: thirdweb.core.classes.ipfs_storage.IpfsStorage, signer: typing.Optional[eth_account.signers.local.LocalAccount] = None, options: thirdweb.types.sdk.SDKOptions = SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))

#### allow_listing_from_any_asset()

#### allow_listing_from_specific_asset_only(contract_address: str)

#### auction(_: [thirdweb.core.classes.marketplace_auction.MarketplaceAuction](thirdweb.core.classes.md#thirdweb.core.classes.marketplace_auction.MarketplaceAuction_ )

#### buyout_listing(listing_id: int, quantity_desired: Optional[int] = None, receiver: Optional[str] = None)

#### contract_roles(_: Final[List[[thirdweb.constants.role.Role](thirdweb.constants.md#thirdweb.constants.role.Role)]_ _ = [<Role.ADMIN: 'admin'>, <Role.LISTER: 'lister'>, <Role.ASSET: 'asset'>_ )

#### contract_type(_: Final[[thirdweb.types.contract.ContractType](thirdweb.types.md#thirdweb.types.contract.ContractType)_ _ = 'marketplace_ )

#### direct(_: [thirdweb.core.classes.marketplace_direct.MarketplaceDirect](thirdweb.core.classes.md#thirdweb.core.classes.marketplace_direct.MarketplaceDirect_ )

#### get_active_listings()

#### get_all(filter: Optional[[thirdweb.types.marketplace.MarketplaceFilter](thirdweb.types.md#thirdweb.types.marketplace.MarketplaceFilter)] = None)

#### get_all_listings(filter: Optional[[thirdweb.types.marketplace.MarketplaceFilter](thirdweb.types.md#thirdweb.types.marketplace.MarketplaceFilter)] = None)

#### get_bid_buffer_bps()

#### get_listing(listing_id: int)

#### get_time_buffer_in_seconds()

#### get_total_count()

#### is_restricted_to_lister_role_only()

#### metadata(_: [thirdweb.core.classes.contract_metadata.ContractMetadata](thirdweb.core.classes.md#thirdweb.core.classes.contract_metadata.ContractMetadata)[[thirdweb.abi.marketplace.Marketplace](thirdweb.abi.marketplace.md#thirdweb.abi.marketplace.Marketplace), thirdweb.types.settings.metadata.MarketplaceContractMetadata_ )

#### platform_fee(_: [thirdweb.core.classes.contract_platform_fee.ContractPlatformFee](thirdweb.core.classes.md#thirdweb.core.classes.contract_platform_fee.ContractPlatformFee)[[thirdweb.abi.marketplace.Marketplace](thirdweb.abi.marketplace.md#thirdweb.abi.marketplace.Marketplace)_ )

#### roles(_: [thirdweb.core.classes.contract_roles.ContractRoles](thirdweb.core.classes.md#thirdweb.core.classes.contract_roles.ContractRoles_ )

#### schema()
alias of `thirdweb.types.settings.metadata.MarketplaceContractMetadata`


#### set_bid_buffer_bps(buffer_bps: int)

#### set_time_buffer_in_seconds(buffer_in_seconds: int)
## thirdweb.contracts.nft_collection module

Interface for interacting with an nft collection contract


### _class_ thirdweb.contracts.nft_collection.NFTCollection(provider: web3.main.Web3, address: str, storage: thirdweb.core.classes.ipfs_storage.IpfsStorage, signer: typing.Optional[eth_account.signers.local.LocalAccount] = None, options: thirdweb.types.sdk.SDKOptions = SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))
Bases: [`thirdweb.core.classes.erc_721.ERC721`](thirdweb.core.classes.md#thirdweb.core.classes.erc_721.ERC721)


#### \__init__(provider: web3.main.Web3, address: str, storage: thirdweb.core.classes.ipfs_storage.IpfsStorage, signer: typing.Optional[eth_account.signers.local.LocalAccount] = None, options: thirdweb.types.sdk.SDKOptions = SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))

#### contract_roles(_: Final[List[[thirdweb.constants.role.Role](thirdweb.constants.md#thirdweb.constants.role.Role)]_ _ = [<Role.ADMIN: 'admin'>, <Role.MINTER: 'minter'>, <Role.TRANSFER: 'transfer'>_ )

#### contract_type(_: Final[[thirdweb.types.contract.ContractType](thirdweb.types.md#thirdweb.types.contract.ContractType)_ _ = 'nft-collection_ )

#### metadata(_: [thirdweb.core.classes.contract_metadata.ContractMetadata](thirdweb.core.classes.md#thirdweb.core.classes.contract_metadata.ContractMetadata)[[thirdweb.abi.token_erc721.TokenERC721](thirdweb.abi.token_erc721.md#thirdweb.abi.token_erc721.TokenERC721), thirdweb.types.settings.metadata.NFTCollectionContractMetadata_ )

#### mint(metadata: Union[[thirdweb.types.nft.NFTMetadataInput](thirdweb.types.md#thirdweb.types.nft.NFTMetadataInput), str])
Mint a new NFT to the connected wallet


* **Parameters**

    **metadata** – metadata of the NFT to mint



* **Returns**

    receipt, id, and metadata for the mint



#### mint_batch(metadatas: List[Union[[thirdweb.types.nft.NFTMetadataInput](thirdweb.types.md#thirdweb.types.nft.NFTMetadataInput), str]])
Mint a batch of new NFTs to the connected wallet


* **Parameters**

    **metadatas** – list of metadata of the NFTs to mint



* **Returns**

    receipts, ids, and metadatas for each mint



#### mint_batch_to(to: str, metadatas: List[Union[[thirdweb.types.nft.NFTMetadataInput](thirdweb.types.md#thirdweb.types.nft.NFTMetadataInput), str]])
Mint a batch of new NFTs to the specified wallet


* **Parameters**

    
    * **to** – wallet address to mint the NFTs to


    * **metadatas** – list of metadata of the NFTs to mint



* **Returns**

    receipts, ids, and metadatas for each mint



#### mint_to(to: str, metadata: Union[[thirdweb.types.nft.NFTMetadataInput](thirdweb.types.md#thirdweb.types.nft.NFTMetadataInput), str])
Mint a new NFT to the specified wallet


* **Parameters**

    
    * **to** – wallet address to mint the NFT to


    * **metadata** – metadata of the NFT to mint



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


### _class_ thirdweb.contracts.token.Token(provider: web3.main.Web3, address: str, storage: thirdweb.core.classes.ipfs_storage.IpfsStorage, signer: typing.Optional[eth_account.signers.local.LocalAccount] = None, options: thirdweb.types.sdk.SDKOptions = SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))
Bases: [`thirdweb.core.classes.erc_20.ERC20`](thirdweb.core.classes.md#thirdweb.core.classes.erc_20.ERC20)


#### \__init__(provider: web3.main.Web3, address: str, storage: thirdweb.core.classes.ipfs_storage.IpfsStorage, signer: typing.Optional[eth_account.signers.local.LocalAccount] = None, options: thirdweb.types.sdk.SDKOptions = SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))

#### contract_roles(_: Final[List[[thirdweb.constants.role.Role](thirdweb.constants.md#thirdweb.constants.role.Role)]_ _ = [<Role.ADMIN: 'admin'>, <Role.MINTER: 'minter'>, <Role.TRANSFER: 'transfer'>_ )

#### contract_type(_: Final[[thirdweb.types.contract.ContractType](thirdweb.types.md#thirdweb.types.contract.ContractType)_ _ = 'token_ )

#### delegate_to(delegatee_address: str)
Delegate the connected wallets tokens to a specified wallet.


* **Parameters**

    **delegatee_address** – wallet address to delegate tokens to



* **Returns**

    transaction receipt of the delegation



#### get_delegation()
Get the connected wallets delegatee address for this token.


* **Returns**

    delegation address of the connected wallet



#### get_delegation_of(account: str)
Get a specified wallets delegatee for this token.


* **Parameters**

    **account** – wallet address to check the delegation of



* **Returns**

    delegation address of the specified wallet



#### get_vote_balance()
Get the connected wallets voting power in this token.


* **Returns**

    vote balance of the connected wallet



#### get_vote_balance_of(account: str)
Get the voting power of the specified wallet in this token.


* **Parameters**

    **account** – wallet address to check the balance of



* **Returns**

    vote balance of the specified wallet



#### metadata(_: [thirdweb.core.classes.contract_metadata.ContractMetadata](thirdweb.core.classes.md#thirdweb.core.classes.contract_metadata.ContractMetadata)[[thirdweb.abi.token_erc20.TokenERC20](thirdweb.abi.token_erc20.md#thirdweb.abi.token_erc20.TokenERC20), thirdweb.types.settings.metadata.TokenContractMetadata_ )

#### mint(amount: float)
Mint tokens to the connected wallet.


* **Parameters**

    **amount** – amount of tokens to mint



* **Returns**

    transaction receipt of the mint



#### mint_batch_to(args: List[[thirdweb.types.currency.TokenAmount](thirdweb.types.md#thirdweb.types.currency.TokenAmount)])
Mint tokens to a list of wallets.


* **Parameters**

    **args** – list of wallet addresses and amounts to mint



* **Returns**

    transaction receipt of the mint



#### mint_to(to: str, amount: float)
Mint tokens to a specified wallet.


* **Parameters**

    
    * **to** – wallet address to mint tokens to


    * **amount** – amount of tokens to mint



* **Returns**

    transaction receipt of the mint



#### platform_fee(_: [thirdweb.core.classes.contract_platform_fee.ContractPlatformFee](thirdweb.core.classes.md#thirdweb.core.classes.contract_platform_fee.ContractPlatformFee_ )

#### roles(_: [thirdweb.core.classes.contract_roles.ContractRoles](thirdweb.core.classes.md#thirdweb.core.classes.contract_roles.ContractRoles_ )

#### schema()
alias of `thirdweb.types.settings.metadata.TokenContractMetadata`

## Module contents
