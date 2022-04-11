# thirdweb.core.classes package

## Submodules

## thirdweb.core.classes.base_contract module


### _class_ thirdweb.core.classes.base_contract.BaseContract(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper[thirdweb.types.contract.TContractABI])
Bases: `Generic`[`thirdweb.types.contract.TContractABI`]

Base contract class to define usage of the contract wrapper and enable
easy provider and signer switching across all contracts


#### \__init__(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper[thirdweb.types.contract.TContractABI])

#### get_address()
Get the address of the contract


#### on_provider_updated(provider: web3.main.Web3)
Updates the contract provider when the SDK provider is updated


* **Parameters**

    **provider** – web3 provider instance to use



#### on_signer_updated(signer: Optional[eth_account.signers.local.LocalAccount] = None)
Updates the contract signer when the SDK signer is updated


* **Parameters**

    **signer** – optional account to use for signing transactions


## thirdweb.core.classes.contract_deployer module


### _class_ thirdweb.core.classes.contract_deployer.ContractDeployer(provider: web3.main.Web3, signer: typing.Optional[eth_account.signers.local.LocalAccount] = None, options: thirdweb.types.sdk.SDKOptions = SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)), storage: thirdweb.core.classes.ipfs_storage.IpfsStorage = <thirdweb.core.classes.ipfs_storage.IpfsStorage object>)
Bases: `thirdweb.core.classes.provider_handler.ProviderHandler`


#### \__init__(provider: web3.main.Web3, signer: typing.Optional[eth_account.signers.local.LocalAccount] = None, options: thirdweb.types.sdk.SDKOptions = SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)), storage: thirdweb.core.classes.ipfs_storage.IpfsStorage = <thirdweb.core.classes.ipfs_storage.IpfsStorage object>)
Initialize the provider handler.


* **Parameters**

    
    * **provider** – web3 provider instance to use


    * **signer** – optional account to use for signing transactions


    * **options** – optional SDKOptions instance to specify read-only RPC URL and gas settings



#### deploy_contract(contract_type: [thirdweb.types.contract.ContractType](thirdweb.types.md#thirdweb.types.contract.ContractType), contract_metadata: Dict[str, Any])

#### deploy_edition(metadata: thirdweb.types.settings.metadata.EditionContractMetadata)

#### deploy_marketplace(metadata: thirdweb.types.settings.metadata.MarketplaceContractMetadata)

#### deploy_nft_collection(metadata: thirdweb.types.settings.metadata.NFTCollectionContractMetadata)

#### deploy_token(metadata: thirdweb.types.settings.metadata.TokenContractMetadata)
## thirdweb.core.classes.contract_metadata module


### _class_ thirdweb.core.classes.contract_metadata.ContractMetadata(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper[thirdweb.types.contract.TMetadataABI], storage: thirdweb.core.classes.ipfs_storage.IpfsStorage, schema: thirdweb.types.contract.TContractSchema)
Bases: `Generic`[`thirdweb.types.contract.TMetadataABI`, `thirdweb.types.contract.TContractSchema`]


#### \__init__(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper[thirdweb.types.contract.TMetadataABI], storage: thirdweb.core.classes.ipfs_storage.IpfsStorage, schema: thirdweb.types.contract.TContractSchema)

#### get()
Get the metadata associated with this contract.


* **Returns**

    metadata associated with this contract



#### set(metadata: thirdweb.types.contract.TContractSchema)
Set the metadata associated with this contract.


* **Parameters**

    **metadata** – metadata to set



* **Returns**

    transaction receipt of setting the metadata


## thirdweb.core.classes.contract_platform_fee module


### _class_ thirdweb.core.classes.contract_platform_fee.ContractPlatformFee(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper[thirdweb.types.contract.TPlatformFeeABI])
Bases: `Generic`[`thirdweb.types.contract.TPlatformFeeABI`]


#### \__init__(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper[thirdweb.types.contract.TPlatformFeeABI])

#### get()
Get the platform fee of this contract.


* **Returns**

    the platform fee.



#### set(platform_fee_info: thirdweb.types.settings.metadata.ContractPlatformFeeSchema)
Set the platform fee of this contract.


* **Parameters**

    **platform_fee_info** – the platform fee info to set.



* **Returns**

    the transaction receipt of setting the platform fee.


## thirdweb.core.classes.contract_roles module


### _class_ thirdweb.core.classes.contract_roles.ContractRoles(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper, roles: List[[thirdweb.constants.role.Role](thirdweb.constants.md#thirdweb.constants.role.Role)])
Bases: `object`


#### \__init__(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper, roles: List[[thirdweb.constants.role.Role](thirdweb.constants.md#thirdweb.constants.role.Role)])

#### get(role: [thirdweb.constants.role.Role](thirdweb.constants.md#thirdweb.constants.role.Role))
Get all members of a role on this contract.


* **Parameters**

    **role** – role to get members of



* **Returns**

    list of members of the role



#### get_all()
Get all role members on this contract.


* **Returns**

    a dictionary of role members for each role



#### get_revoke_role_function_name(address: str)

#### grant(role: [thirdweb.constants.role.Role](thirdweb.constants.md#thirdweb.constants.role.Role), address: str)
Grant a role to an address.


* **Parameters**

    
    * **role** – role to grant


    * **address** – address to grant the role to



* **Returns**

    transaction receipt of granting the role



#### revoke(role: [thirdweb.constants.role.Role](thirdweb.constants.md#thirdweb.constants.role.Role), address: str)
Revoke a role from an address.


* **Parameters**

    
    * **role** – role to revoke


    * **address** – address to revoke the role from



* **Returns**

    transaction receipt of revoking the role



#### verify(roles: List[[thirdweb.constants.role.Role](thirdweb.constants.md#thirdweb.constants.role.Role)], address: str)
## thirdweb.core.classes.contract_royalty module


### _class_ thirdweb.core.classes.contract_royalty.ContractRoyalty(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper[thirdweb.types.contract.TRoyaltyABI], metadata: thirdweb.core.classes.contract_metadata.ContractMetadata)
Bases: `Generic`[`thirdweb.types.contract.TRoyaltyABI`]


#### \__init__(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper[thirdweb.types.contract.TRoyaltyABI], metadata: thirdweb.core.classes.contract_metadata.ContractMetadata)

#### get_default_royalty_info()
Get the default royalty information for this contract.


* **Returns**

    the default royalty information.



#### get_token_royalty_info(token_id: int)
Get the royalty information for a specific token.


* **Parameters**

    **token_id** – the id of the token.



* **Returns**

    the royalty information for the token.



#### set_default_royalty_info(royalty_data: thirdweb.types.settings.metadata.ContractRoyaltySchema)
Set the default royalty information for this contract.


* **Parameters**

    **royalty_data** – the default royalty information.



* **Returns**

    the transaction receipt of setting the royalty.



#### set_token_royalty_info(token_id: int, royalty_data: thirdweb.types.settings.metadata.ContractRoyaltySchema)
Set the royalty information for a specific token.


* **Parameters**

    
    * **token_id** – the id of the token.


    * **royalty_data** – the royalty information for the token.



* **Returns**

    the transaction receipt of setting the royalty.


## thirdweb.core.classes.contract_sales module


### _class_ thirdweb.core.classes.contract_sales.ContractPrimarySale(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper[thirdweb.types.contract.TPrimarySaleABI])
Bases: `Generic`[`thirdweb.types.contract.TPrimarySaleABI`]


#### \__init__(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper[thirdweb.types.contract.TPrimarySaleABI])

#### get_recipient()
Get the primary sale recipient of this contract.


* **Returns**

    the address of the primary sale recipient.



#### set_recipient(recipient: str)
Set the primary sale recipient of this contract


* **Parameters**

    **recipient** – the address of the primary sale recipient.



* **Returns**

    the transaction receipt.


## thirdweb.core.classes.contract_wrapper module


### _class_ thirdweb.core.classes.contract_wrapper.ContractWrapper(contract_abi: thirdweb.types.contract.TContractABI, provider: web3.main.Web3, signer: typing.Optional[eth_account.signers.local.LocalAccount] = None, options: thirdweb.types.sdk.SDKOptions = SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))
Bases: `Generic`[`thirdweb.types.contract.TContractABI`], `thirdweb.core.classes.provider_handler.ProviderHandler`

The contract wrapper wraps an instance of a specific thirdweb contract ABI
and exposed functions for interacting with the contract.


#### \__init__(contract_abi: thirdweb.types.contract.TContractABI, provider: web3.main.Web3, signer: typing.Optional[eth_account.signers.local.LocalAccount] = None, options: thirdweb.types.sdk.SDKOptions = SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))
Initializes the contract wrapper.


* **Parameters**

    
    * **contract_abi** – ABI of the thirdweb contract to use


    * **provider** – web3 provider instance to use


    * **signer** – optional account to use for signing transactions



#### get_chain_id()
Get the chain ID of the active provider


* **Returns**

    chain ID of the active provider



#### get_contract_interface()
Get the contract interface of the contract wrapper.


* **Returns**

    contract interface of the contract wrapper



#### get_events(event: str, receipt: web3.types.TxReceipt)
Get the events from a transaction receipt.


* **Parameters**

    
    * **event** – name of the event to get


    * **receipt** – transaction receipt to get the events from



#### get_signer_address()
Get the address of the active signer


* **Returns**

    address of the active signer



#### multi_call(encoded: List[str])
Execute a multicall and return the result.


* **Parameters**

    **encoded** – list of encoded function calls to execute



#### send_transaction(fn: str, args: List[Any])
Send and execute a transaction and return the receipt.


* **Parameters**

    
    * **fn** – name of the function you want to call on the contract


    * **args** – list of arguments to pass to the function


## thirdweb.core.classes.erc_1155 module


### _class_ thirdweb.core.classes.erc_1155.ERC1155(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper, storage: thirdweb.core.classes.ipfs_storage.IpfsStorage)
Bases: `thirdweb.core.classes.base_contract.BaseContract`[[`thirdweb.abi.token_erc1155.TokenERC1155`](thirdweb.abi.token_erc1155.md#thirdweb.abi.token_erc1155.TokenERC1155)]


#### \__init__(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper, storage: thirdweb.core.classes.ipfs_storage.IpfsStorage)

#### balance(token_id: int)
Get the connected wallets balance of a specific token


* **Parameters**

    **token_id** – token ID to check the balance for



* **Returns**

    balance of the token



#### balance_of(address: str, token_id: int)
Get a specific wallets balance of a specific token


* **Parameters**

    
    * **address** – address to check the balance for


    * **token_id** – token ID to check the balance for



* **Returns**

    balance of the token



#### burn(token_id: int, amount: int)
Burn a specified amount of tokens from the connected wallet.


* **Parameters**

    **amount** – amount of tokens to burn



* **Returns**

    transaction receipt of the burn



#### get(token_id: int)
Get metadata for a token


* **Parameters**

    **token_id** – token ID to check the metadata for



* **Returns**

    Metadata for the token



#### get_all(query_params: [thirdweb.types.nft.QueryAllParams](thirdweb.types.md#thirdweb.types.nft.QueryAllParams))
Get the metadata for all tokens on the contract


* **Parameters**

    **query_params** – optional QueryAllParams to define which tokens to get metadata for



* **Returns**

    list of metadata for all tokens



#### get_owned(address: str = '')
Get the metadata for all the tokens owned by an address


* **Parameters**

    **address** – address to get the owned tokens for



* **Returns**

    list of metadata for all tokens owned by the address



#### get_total_count()
Get the total number of NFTs on the contract


* **Returns**

    total number of tokens on the contract



#### is_approved(address: str, operator: str)
Check if an operator address is approved to manage a target addresses assets


* **Parameters**

    
    * **address** – address whose assets to check the approval of


    * **operator** – operator address to check the approval for



* **Returns**

    True if the operator is approved, False otherwise



#### is_transfer_restricted()
Check if the contract is restricted so transfers can only be made by admins


* **Returns**

    True if the contract is restricted, False otherwise



#### set_approval_for_all(operator: str, approved: bool)
Set the approval for an operator address to manage the connected wallets assets


* **Parameters**

    
    * **operator** – operator address to set the approval for


    * **approved** – True if the operator is approved, False otherwise



#### total_supply(token_id: int)
Get the total number of tokens on the contract


* **Returns**

    total number of tokens on the contract



#### transfer(to: str, token_id: int, amount: int, data: Union[bytes, str] = b'0')
Transfer a specified token from the connected wallet to a specified address.


* **Parameters**

    
    * **to** – wallet address to transfer the tokens to


    * **token_id** – the specific token ID to transfer


    * **amount** – the amount of tokens to transfer



* **Returns**

    transaction receipt of the transfer


## thirdweb.core.classes.erc_20 module


### _class_ thirdweb.core.classes.erc_20.ERC20(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper, storage: thirdweb.core.classes.ipfs_storage.IpfsStorage)
Bases: `thirdweb.core.classes.base_contract.BaseContract`[[`thirdweb.abi.token_erc20.TokenERC20`](thirdweb.abi.token_erc20.md#thirdweb.abi.token_erc20.TokenERC20)]


#### \__init__(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper, storage: thirdweb.core.classes.ipfs_storage.IpfsStorage)

#### allowance(spender: str)
Get a specific spenders allowance of this token for the connected wallet.


* **Parameters**

    **spender** – wallet address to check the allowance of



* **Returns**

    allowance of the connected wallet



#### allowance_of(owner: str, spender: str)
Get the allowance of the specified spender for a specified owner.


* **Parameters**

    
    * **owner** – wallet address whose assets will be spent


    * **spender** – wallet address to check the allowance of



* **Returns**

    allowance of the specified spender for the specified owner



#### balance()
Get the token balance of the connected wallet.


* **Returns**

    balance of the connected wallet



#### balance_of(address: str)
Get the balance of the specified wallet


* **Parameters**

    **address** – wallet address to check the balance of



* **Returns**

    balance of the specified wallet



#### burn(amount: float)
Burn a specified amount of tokens from the connected wallet.


* **Parameters**

    **amount** – amount of tokens to burn



* **Returns**

    transaction receipt of the burn



#### burn_from(holder: str, amount: float)
Burn a specified amount of tokens from a specified wallet.


* **Parameters**

    
    * **holder** – wallet address to burn the tokens from


    * **amount** – amount of tokens to burn



* **Returns**

    transaction receipt of the burn



#### get()
Get the token metadata including name, symbol, decimals, etc.


* **Returns**

    token metadata



#### is_transfer_restricted()
Check whether transfer is restricted for tokens in this module.


* **Returns**

    True if transfer is restricted, False otherwise



#### normalize_amount(amount: float)

#### set_allowance(spender: str, amount: float)
Sets the allowance of the specified wallet over the connected wallets funds to
a specified amount.


* **Parameters**

    
    * **spender** – wallet address to set the allowance of


    * **amount** – amount to set the allowance to



* **Returns**

    transaction receipt of the allowance set



#### total_supply()
Get the total minted supply of the token.


* **Returns**

    total minted supply of the token



#### transfer(to: str, amount: float)
Transfer a specified amount of tokens from the connected wallet to a specified address.


* **Parameters**

    
    * **to** – wallet address to transfer the tokens to


    * **amount** – amount of tokens to transfer



* **Returns**

    transaction receipt of the transfer



#### transfer_batch(args: List[[thirdweb.types.currency.TokenAmount](thirdweb.types.md#thirdweb.types.currency.TokenAmount)])
Transfer tokens from the connected wallet to many wallets.


* **Parameters**

    **args** – list of token amounts and addressed to transfer to



* **Returns**

    transaction receipt of the transfers



#### transfer_from(fr: str, to: str, amount: float)
Transfer a specified amount of tokens from one specified address to another.


* **Parameters**

    
    * **fr** – wallet address to transfer the tokens from


    * **to** – wallet address to transfer the tokens to


    * **amount** – amount of tokens to transfer



* **Returns**

    transaction receipt of the transfer


## thirdweb.core.classes.erc_721 module


### _class_ thirdweb.core.classes.erc_721.ERC721(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper, storage: thirdweb.core.classes.ipfs_storage.IpfsStorage)
Bases: `thirdweb.core.classes.base_contract.BaseContract`[[`thirdweb.abi.token_erc721.TokenERC721`](thirdweb.abi.token_erc721.md#thirdweb.abi.token_erc721.TokenERC721)]


#### \__init__(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper, storage: thirdweb.core.classes.ipfs_storage.IpfsStorage)

#### balance()
Get the token balance of the connected wallet


* **Returns**

    the token balance of the connected wallet



#### balance_of(address: str)
Get the token balance of a specific address


* **Parameters**

    **address** – the address to get the token balance of



#### burn(token_id: int)
Burn a specified token from the connected wallet.


* **Parameters**

    **token_id** – token ID of the token to burn



* **Returns**

    transaction receipt of the burn



#### get(token_id: int)
Get metadata for a token


* **Parameters**

    **token_id** – token ID of the token to get the metadata for



* **Returns**

    the metadata for the token and its owner



#### get_all(query_params: [thirdweb.types.nft.QueryAllParams](thirdweb.types.md#thirdweb.types.nft.QueryAllParams) = QueryAllParams(start=0, count=100))
Get the metadata of all tokens in the contract


* **Parameters**

    **query_params** – optionally define a QueryAllParams instance to narrow the metadata query to specific tokens



* **Returns**

    the metadata of all tokens in the contract



#### get_owned(address: str = '')
Get the metadata of all tokens owned by a specific address


* **Parameters**

    **address** – the address to get the metadata for



* **Returns**

    the metadata of all tokens owned by the address



#### get_total_count()
Get the total number of NFTs minted by this contract


* **Returns**

    the total number of NFTs minted by this contract



#### is_approved(address: str, operator: str)
Check whether an operator address is approved for all operations of a specific addresses assets


* **Parameters**

    
    * **address** – the address whose assets are to be checked


    * **operator** – the address of the operator to check



* **Returns**

    True if the operator is approved for all operations of the assets, False otherwise



#### is_transfer_restricted()
Check if the contract is restricted to transfers only by admins


* **Returns**

    True if the contract is restricted to transfers only by admins, False otherwise



#### owner_of(token_id: int)
Get the owner of a token


* **Parameters**

    **token_id** – the token ID of the token to get the owner of



* **Returns**

    the owner of the token



#### set_approval_for_all(operator: str, approved: bool)
Set the approval of an operator for all operations of a specific address’s assets


* **Parameters**

    
    * **operator** – the address of the operator to set the approval for


    * **approved** – the address whos assets the operator is approved to manage



* **Returns**

    transaction receipt of the approval setting



#### total_supply()
Get the total number of tokens in the contract


* **Returns**

    the total number of tokens in the contract



#### transfer(to: str, token_id: int)
Transfer a specified token from the connected wallet to a specified address.


* **Parameters**

    
    * **to** – wallet address to transfer the tokens to


    * **token_id** – the specific token ID to transfer



* **Returns**

    transaction receipt of the transfer


## thirdweb.core.classes.factory module


### _class_ thirdweb.core.classes.factory.ContractFactory(factory_address: str, provider: web3.main.Web3, signer: typing.Optional[eth_account.signers.local.LocalAccount] = None, options: thirdweb.types.sdk.SDKOptions = SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)), storage: thirdweb.core.classes.ipfs_storage.IpfsStorage = <thirdweb.core.classes.ipfs_storage.IpfsStorage object>)
Bases: `thirdweb.core.classes.contract_wrapper.ContractWrapper`[[`thirdweb.abi.t_w_factory.TWFactory`](thirdweb.abi.t_w_factory.md#thirdweb.abi.t_w_factory.TWFactory)]


#### \__init__(factory_address: str, provider: web3.main.Web3, signer: typing.Optional[eth_account.signers.local.LocalAccount] = None, options: thirdweb.types.sdk.SDKOptions = SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)), storage: thirdweb.core.classes.ipfs_storage.IpfsStorage = <thirdweb.core.classes.ipfs_storage.IpfsStorage object>)
Initializes the contract wrapper.


* **Parameters**

    
    * **contract_abi** – ABI of the thirdweb contract to use


    * **provider** – web3 provider instance to use


    * **signer** – optional account to use for signing transactions



#### deploy(contract_type: [thirdweb.types.contract.ContractType](thirdweb.types.md#thirdweb.types.contract.ContractType), contract_metadata: Dict[str, Any])

#### get_deploy_arguments(contract_type: [thirdweb.types.contract.ContractType](thirdweb.types.md#thirdweb.types.contract.ContractType), contract_metadata: Dict[str, Any], contract_uri: str)
## thirdweb.core.classes.ipfs_storage module


### _class_ thirdweb.core.classes.ipfs_storage.IpfsStorage(gateway_url='https://gateway.ipfscdn.io/ipfs/')
Bases: `abc.ABC`


#### \__init__(gateway_url='https://gateway.ipfscdn.io/ipfs/')

#### get(hash: str)
Gets IPFS data at a given hash and returns it as a dictionary.


* **Parameters**

    **hash** – hash of the data to get.



* **Returns**

    dictionary of the data.



#### get_upload_token(contract_address: str)
Gets an upload token for a given contract address.


#### upload(data: Union[TextIO, BinaryIO, str], contract_address: str = '', signer_address: str = '')
Uploads data to IPFS and returns the hash of the data.


#### upload_batch(files: Sequence[Union[TextIO, BinaryIO, str, Dict[str, Any]]], file_start_number: int = 0, contract_address: str = '', signer_address: str = '')
Uploads a list of files to IPFS and returns the hash.


#### upload_metadata(metadata: Dict[str, Any], contract_address: str = '', signer_address: str = '')
Uploads metadata to IPFS and returns the hash of the metadata.


#### upload_metadata_batch(metadatas: Sequence[Dict[str, Any]], file_start_number: int = 0, contract_address: str = '', signer_address: str = '')
Uploads a list of metadata to IPFS and returns the hash.

## thirdweb.core.classes.marketplace_auction module


### _class_ thirdweb.core.classes.marketplace_auction.MarketplaceAuction(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper, storage: thirdweb.core.classes.ipfs_storage.IpfsStorage)
Bases: `thirdweb.core.classes.base_contract.BaseContract`[[`thirdweb.abi.marketplace.Marketplace`](thirdweb.abi.marketplace.md#thirdweb.abi.marketplace.Marketplace)]


#### \__init__(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper, storage: thirdweb.core.classes.ipfs_storage.IpfsStorage)

#### buyout_listing(listing_id: int)

#### cancel_listing(listing_id: int)

#### close_listing(listing_id: int, close_for: Optional[str] = None)

#### create_listing(listing: [thirdweb.types.marketplace.NewAuctionListing](thirdweb.types.md#thirdweb.types.marketplace.NewAuctionListing))

#### get_listing(listing_id: int)

#### get_winner(listing_id)

#### get_winning_bid(listing_id: int)

#### make_bid(listing_id: int, price_per_token: float)

#### update_listing(listing: [thirdweb.types.marketplace.AuctionListing](thirdweb.types.md#thirdweb.types.marketplace.AuctionListing))
## thirdweb.core.classes.marketplace_direct module


### _class_ thirdweb.core.classes.marketplace_direct.MarketplaceDirect(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper, storage: thirdweb.core.classes.ipfs_storage.IpfsStorage)
Bases: `thirdweb.core.classes.base_contract.BaseContract`[[`thirdweb.abi.marketplace.Marketplace`](thirdweb.abi.marketplace.md#thirdweb.abi.marketplace.Marketplace)]


#### \__init__(contract_wrapper: thirdweb.core.classes.contract_wrapper.ContractWrapper, storage: thirdweb.core.classes.ipfs_storage.IpfsStorage)

#### accept_offer(listing_id: int, address_or_offerror: str)

#### buyout_listing(listing_id: int, quantity_desired: int, receiver: Optional[str] = None)

#### cancel_listing(listing_id: int)

#### create_listing(listing: [thirdweb.types.marketplace.NewDirectListing](thirdweb.types.md#thirdweb.types.marketplace.NewDirectListing))

#### get_active_offer(listing_id: int, address: str)

#### get_listing(listing_id: int)

#### make_offer(listing_id: int, quantity_desired: int, currency_contract_address: str, price_per_token: float)

#### update_listing(listing: [thirdweb.types.marketplace.DirectListing](thirdweb.types.md#thirdweb.types.marketplace.DirectListing))
## thirdweb.core.classes.provider_handler module


### _class_ thirdweb.core.classes.provider_handler.ProviderHandler(provider: web3.main.Web3, signer: typing.Optional[eth_account.signers.local.LocalAccount] = None, options: thirdweb.types.sdk.SDKOptions = SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))
Bases: `object`

The provider handler is responsible for managing the connected provider and signer
for any class including the read-only provider.


#### \__init__(provider: web3.main.Web3, signer: typing.Optional[eth_account.signers.local.LocalAccount] = None, options: thirdweb.types.sdk.SDKOptions = SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))
Initialize the provider handler.


* **Parameters**

    
    * **provider** – web3 provider instance to use


    * **signer** – optional account to use for signing transactions


    * **options** – optional SDKOptions instance to specify read-only RPC URL and gas settings



#### get_options()

#### get_provider()
Get the active provider.


* **Returns**

    the Web3 instance of the active provider



#### get_signer()
Get the active signer.


* **Returns**

    the Account instance of the active signer, otherwise None



#### is_read_only()
Check if there is no active signer.


#### update_provider(provider: web3.main.Web3)
Update the active provider.


* **Parameters**

    **provider** – web3 provider instance to use



#### update_signer(signer: Optional[eth_account.signers.local.LocalAccount] = None)
Update the active signer.


* **Parameters**

    **signer** – optional account to use for signing transactions


## thirdweb.core.classes.registry module


### _class_ thirdweb.core.classes.registry.ContractRegistry(registry_address: str, provider: web3.main.Web3, signer: typing.Optional[eth_account.signers.local.LocalAccount], options: thirdweb.types.sdk.SDKOptions = SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))
Bases: `thirdweb.core.classes.contract_wrapper.ContractWrapper`


#### \__init__(registry_address: str, provider: web3.main.Web3, signer: typing.Optional[eth_account.signers.local.LocalAccount], options: thirdweb.types.sdk.SDKOptions = SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))
Initializes the contract wrapper.


* **Parameters**

    
    * **contract_abi** – ABI of the thirdweb contract to use


    * **provider** – web3 provider instance to use


    * **signer** – optional account to use for signing transactions



#### get_contract_addresses(address: str)
Get all the contract addresses registered for a given address.


* **Parameters**

    **address** – address to get the contract addresses for



* **Returns**

    list of contract addresses


## Module contents
