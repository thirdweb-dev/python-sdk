# thirdweb.core.classes package

## Submodules

## thirdweb.core.classes.base_contract module


### _class_ thirdweb.core.classes.base_contract.BaseContract(contract_wrapper)
Bases: `Generic`[`thirdweb.types.contract.TContractABI`]

Base contract class to define usage of the contract wrapper and enable
easy provider and signer switching across all contracts


#### \__init__(contract_wrapper)

#### get_address()
Get the address of the contract


* **Return type**

    `str`



#### on_provider_updated(provider)
Updates the contract provider when the SDK provider is updated


* **Parameters**

    **provider** (`Web3`) – web3 provider instance to use



#### on_signer_updated(signer=None)
Updates the contract signer when the SDK signer is updated


* **Parameters**

    **signer** (`Optional`[`LocalAccount`]) – optional account to use for signing transactions


## thirdweb.core.classes.contract_deployer module


### _class_ thirdweb.core.classes.contract_deployer.ContractDeployer(provider, signer=None, options=SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)), storage=<thirdweb.core.classes.ipfs_storage.IpfsStorage object>)
Bases: `thirdweb.core.classes.provider_handler.ProviderHandler`


#### \__init__(provider, signer=None, options=SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)), storage=<thirdweb.core.classes.ipfs_storage.IpfsStorage object>)
Initialize the provider handler.


* **Parameters**

    
    * **provider** (`Web3`) – web3 provider instance to use


    * **signer** (`Optional`[`LocalAccount`]) – optional account to use for signing transactions


    * **options** ([`SDKOptions`](thirdweb.types.md#thirdweb.types.sdk.SDKOptions)) – optional SDKOptions instance to specify read-only RPC URL and gas settings



#### deploy_contract(contract_type, contract_metadata)

* **Return type**

    `str`



#### deploy_edition(metadata)

* **Return type**

    `str`



#### deploy_marketplace(metadata)

* **Return type**

    `str`



#### deploy_nft_collection(metadata)

* **Return type**

    `str`



#### deploy_token(metadata)

* **Return type**

    `str`


## thirdweb.core.classes.contract_metadata module


### _class_ thirdweb.core.classes.contract_metadata.ContractMetadata(contract_wrapper, storage, schema)
Bases: `Generic`[`thirdweb.types.contract.TMetadataABI`, `thirdweb.types.contract.TContractSchema`]


#### \__init__(contract_wrapper, storage, schema)

#### get()
Get the metadata associated with this contract.


* **Return type**

    `TypeVar`(`TContractSchema`, bound= `ContractMetadataSchema`)



* **Returns**

    metadata associated with this contract



#### set(metadata)
Set the metadata associated with this contract.


* **Parameters**

    **metadata** (`TypeVar`(`TContractSchema`, bound= `ContractMetadataSchema`)) – metadata to set



* **Return type**

    `TxReceipt`



* **Returns**

    transaction receipt of setting the metadata


## thirdweb.core.classes.contract_platform_fee module


### _class_ thirdweb.core.classes.contract_platform_fee.ContractPlatformFee(contract_wrapper)
Bases: `Generic`[`thirdweb.types.contract.TPlatformFeeABI`]


#### \__init__(contract_wrapper)

#### get()
Get the platform fee of this contract.


* **Return type**

    `ContractPlatformFeeSchema`



* **Returns**

    the platform fee.



#### set(platform_fee_info)
Set the platform fee of this contract.


* **Parameters**

    **platform_fee_info** (`ContractPlatformFeeSchema`) – the platform fee info to set.



* **Return type**

    `TxReceipt`



* **Returns**

    the transaction receipt of setting the platform fee.


## thirdweb.core.classes.contract_roles module


### _class_ thirdweb.core.classes.contract_roles.ContractRoles(contract_wrapper, roles)
Bases: `object`


#### \__init__(contract_wrapper, roles)

#### get(role)
Get all members of a role on this contract.


* **Parameters**

    **role** ([`Role`](thirdweb.constants.md#thirdweb.constants.role.Role)) – role to get members of



* **Return type**

    `List`[`str`]



* **Returns**

    list of members of the role



#### get_all()
Get all role members on this contract.


* **Return type**

    `Dict`[[`Role`](thirdweb.constants.md#thirdweb.constants.role.Role), `List`[`str`]]



* **Returns**

    a dictionary of role members for each role



#### get_revoke_role_function_name(address)

* **Return type**

    `str`



#### grant(role, address)
Grant a role to an address.


* **Parameters**

    
    * **role** ([`Role`](thirdweb.constants.md#thirdweb.constants.role.Role)) – role to grant


    * **address** (`str`) – address to grant the role to



* **Return type**

    `TxReceipt`



* **Returns**

    transaction receipt of granting the role



#### revoke(role, address)
Revoke a role from an address.


* **Parameters**

    
    * **role** ([`Role`](thirdweb.constants.md#thirdweb.constants.role.Role)) – role to revoke


    * **address** (`str`) – address to revoke the role from



* **Return type**

    `TxReceipt`



* **Returns**

    transaction receipt of revoking the role



#### verify(roles, address)
## thirdweb.core.classes.contract_royalty module


### _class_ thirdweb.core.classes.contract_royalty.ContractRoyalty(contract_wrapper, metadata)
Bases: `Generic`[`thirdweb.types.contract.TRoyaltyABI`]


#### \__init__(contract_wrapper, metadata)

#### get_default_royalty_info()
Get the default royalty information for this contract.


* **Return type**

    `ContractRoyaltySchema`



* **Returns**

    the default royalty information.



#### get_token_royalty_info(token_id)
Get the royalty information for a specific token.


* **Parameters**

    **token_id** (`int`) – the id of the token.



* **Return type**

    `ContractRoyaltySchema`



* **Returns**

    the royalty information for the token.



#### set_default_royalty_info(royalty_data)
Set the default royalty information for this contract.


* **Parameters**

    **royalty_data** (`ContractRoyaltySchema`) – the default royalty information.



* **Return type**

    `TxReceipt`



* **Returns**

    the transaction receipt of setting the royalty.



#### set_token_royalty_info(token_id, royalty_data)
Set the royalty information for a specific token.


* **Parameters**

    
    * **token_id** (`int`) – the id of the token.


    * **royalty_data** (`ContractRoyaltySchema`) – the royalty information for the token.



* **Return type**

    `TxReceipt`



* **Returns**

    the transaction receipt of setting the royalty.


## thirdweb.core.classes.contract_sales module


### _class_ thirdweb.core.classes.contract_sales.ContractPrimarySale(contract_wrapper)
Bases: `Generic`[`thirdweb.types.contract.TPrimarySaleABI`]


#### \__init__(contract_wrapper)

#### get_recipient()
Get the primary sale recipient of this contract.


* **Return type**

    `str`



* **Returns**

    the address of the primary sale recipient.



#### set_recipient(recipient)
Set the primary sale recipient of this contract


* **Parameters**

    **recipient** (`str`) – the address of the primary sale recipient.



* **Return type**

    `TxReceipt`



* **Returns**

    the transaction receipt.


## thirdweb.core.classes.contract_wrapper module


### _class_ thirdweb.core.classes.contract_wrapper.ContractWrapper(contract_abi, provider, signer=None, options=SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))
Bases: `Generic`[`thirdweb.types.contract.TContractABI`], `thirdweb.core.classes.provider_handler.ProviderHandler`

The contract wrapper wraps an instance of a specific thirdweb contract ABI
and exposed functions for interacting with the contract.


#### \__init__(contract_abi, provider, signer=None, options=SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))
Initializes the contract wrapper.


* **Parameters**

    
    * **contract_abi** (`TypeVar`(`TContractABI`, bound= `Union`[[`TokenERC721`](thirdweb.abi.md#thirdweb.abi.token_erc721.TokenERC721), [`TokenERC1155`](thirdweb.abi.md#thirdweb.abi.token_erc1155.TokenERC1155), [`TokenERC20`](thirdweb.abi.md#thirdweb.abi.token_erc20.TokenERC20), [`Marketplace`](thirdweb.abi.md#thirdweb.abi.marketplace.Marketplace), [`IERC20`](thirdweb.abi.md#thirdweb.abi.ierc20.IERC20), [`IERC721`](thirdweb.abi.md#thirdweb.abi.ierc721.IERC721), [`IERC1155`](thirdweb.abi.md#thirdweb.abi.ierc1155.IERC1155), [`TWRegistry`](thirdweb.abi.md#thirdweb.abi.t_w_registry.TWRegistry), [`TWFactory`](thirdweb.abi.md#thirdweb.abi.t_w_factory.TWFactory)])) – ABI of the thirdweb contract to use


    * **provider** (`Web3`) – web3 provider instance to use


    * **signer** (`Optional`[`LocalAccount`]) – optional account to use for signing transactions



#### get_chain_id()
Get the chain ID of the active provider


* **Return type**

    `int`



* **Returns**

    chain ID of the active provider



#### get_contract_interface()
Get the contract interface of the contract wrapper.


* **Return type**

    `Contract`



* **Returns**

    contract interface of the contract wrapper



#### get_events(event, receipt)
Get the events from a transaction receipt.


* **Parameters**

    
    * **event** (`str`) – name of the event to get


    * **receipt** (`TxReceipt`) – transaction receipt to get the events from



* **Return type**

    `Tuple`[`AttributeDict`]



#### get_signer_address()
Get the address of the active signer


* **Return type**

    `str`



* **Returns**

    address of the active signer



#### multi_call(encoded)
Execute a multicall and return the result.


* **Parameters**

    **encoded** (`List`[`str`]) – list of encoded function calls to execute



* **Return type**

    `TxReceipt`



#### send_transaction(fn, args)
Send and execute a transaction and return the receipt.


* **Parameters**

    
    * **fn** (`str`) – name of the function you want to call on the contract


    * **args** (`List`[`Any`]) – list of arguments to pass to the function



* **Return type**

    `TxReceipt`


## thirdweb.core.classes.erc_1155 module


### _class_ thirdweb.core.classes.erc_1155.ERC1155(contract_wrapper, storage)
Bases: `thirdweb.core.classes.base_contract.BaseContract`[[`thirdweb.abi.token_erc1155.TokenERC1155`](thirdweb.abi.md#thirdweb.abi.token_erc1155.TokenERC1155)]


#### \__init__(contract_wrapper, storage)

#### balance(token_id)
Get the connected wallets balance of a specific token


* **Parameters**

    **token_id** (`int`) – token ID to check the balance for



* **Return type**

    `int`



* **Returns**

    balance of the token



#### balance_of(address, token_id)
Get a specific wallets balance of a specific token


* **Parameters**

    
    * **address** (`str`) – address to check the balance for


    * **token_id** (`int`) – token ID to check the balance for



* **Return type**

    `int`



* **Returns**

    balance of the token



#### burn(token_id, amount)
Burn a specified amount of tokens from the connected wallet.


* **Parameters**

    **amount** (`int`) – amount of tokens to burn



* **Return type**

    `TxReceipt`



* **Returns**

    transaction receipt of the burn



#### get(token_id)
Get metadata for a token


* **Parameters**

    **token_id** (`int`) – token ID to check the metadata for



* **Return type**

    [`EditionMetadata`](thirdweb.types.md#thirdweb.types.nft.EditionMetadata)



* **Returns**

    Metadata for the token



#### get_all(query_params)
Get the metadata for all tokens on the contract


* **Parameters**

    **query_params** ([`QueryAllParams`](thirdweb.types.md#thirdweb.types.nft.QueryAllParams)) – optional QueryAllParams to define which tokens to get metadata for



* **Return type**

    `List`[[`EditionMetadata`](thirdweb.types.md#thirdweb.types.nft.EditionMetadata)]



* **Returns**

    list of metadata for all tokens



#### get_owned(address='')
Get the metadata for all the tokens owned by an address


* **Parameters**

    **address** (`str`) – address to get the owned tokens for



* **Return type**

    `List`[[`EditionMetadataOwner`](thirdweb.types.md#thirdweb.types.nft.EditionMetadataOwner)]



* **Returns**

    list of metadata for all tokens owned by the address



#### get_total_count()
Get the total number of NFTs on the contract


* **Return type**

    `int`



* **Returns**

    total number of tokens on the contract



#### is_approved(address, operator)
Check if an operator address is approved to manage a target addresses assets


* **Parameters**

    
    * **address** (`str`) – address whose assets to check the approval of


    * **operator** (`str`) – operator address to check the approval for



* **Return type**

    `bool`



* **Returns**

    True if the operator is approved, False otherwise



#### is_transfer_restricted()
Check if the contract is restricted so transfers can only be made by admins


* **Return type**

    `bool`



* **Returns**

    True if the contract is restricted, False otherwise



#### set_approval_for_all(operator, approved)
Set the approval for an operator address to manage the connected wallets assets


* **Parameters**

    
    * **operator** (`str`) – operator address to set the approval for


    * **approved** (`bool`) – True if the operator is approved, False otherwise



* **Return type**

    `TxReceipt`



#### total_supply(token_id)
Get the total number of tokens on the contract


* **Return type**

    `int`



* **Returns**

    total number of tokens on the contract



#### transfer(to, token_id, amount, data=b'0')
Transfer a specified token from the connected wallet to a specified address.


* **Parameters**

    
    * **to** (`str`) – wallet address to transfer the tokens to


    * **token_id** (`int`) – the specific token ID to transfer


    * **amount** (`int`) – the amount of tokens to transfer



* **Return type**

    `TxReceipt`



* **Returns**

    transaction receipt of the transfer


## thirdweb.core.classes.erc_20 module


### _class_ thirdweb.core.classes.erc_20.ERC20(contract_wrapper, storage)
Bases: `thirdweb.core.classes.base_contract.BaseContract`[[`thirdweb.abi.token_erc20.TokenERC20`](thirdweb.abi.md#thirdweb.abi.token_erc20.TokenERC20)]


#### \__init__(contract_wrapper, storage)

#### allowance(spender)
Get a specific spenders allowance of this token for the connected wallet.


* **Parameters**

    **spender** (`str`) – wallet address to check the allowance of



* **Return type**

    [`CurrencyValue`](thirdweb.types.md#thirdweb.types.currency.CurrencyValue)



* **Returns**

    allowance of the connected wallet



#### allowance_of(owner, spender)
Get the allowance of the specified spender for a specified owner.


* **Parameters**

    
    * **owner** (`str`) – wallet address whose assets will be spent


    * **spender** (`str`) – wallet address to check the allowance of



* **Return type**

    [`CurrencyValue`](thirdweb.types.md#thirdweb.types.currency.CurrencyValue)



* **Returns**

    allowance of the specified spender for the specified owner



#### balance()
Get the token balance of the connected wallet.


* **Return type**

    [`CurrencyValue`](thirdweb.types.md#thirdweb.types.currency.CurrencyValue)



* **Returns**

    balance of the connected wallet



#### balance_of(address)
Get the balance of the specified wallet


* **Parameters**

    **address** (`str`) – wallet address to check the balance of



* **Return type**

    [`CurrencyValue`](thirdweb.types.md#thirdweb.types.currency.CurrencyValue)



* **Returns**

    balance of the specified wallet



#### burn(amount)
Burn a specified amount of tokens from the connected wallet.


* **Parameters**

    **amount** (`float`) – amount of tokens to burn



* **Return type**

    `TxReceipt`



* **Returns**

    transaction receipt of the burn



#### burn_from(holder, amount)
Burn a specified amount of tokens from a specified wallet.


* **Parameters**

    
    * **holder** (`str`) – wallet address to burn the tokens from


    * **amount** (`float`) – amount of tokens to burn



* **Return type**

    `TxReceipt`



* **Returns**

    transaction receipt of the burn



#### get()
Get the token metadata including name, symbol, decimals, etc.


* **Return type**

    [`Currency`](thirdweb.types.md#thirdweb.types.currency.Currency)



* **Returns**

    token metadata



#### is_transfer_restricted()
Check whether transfer is restricted for tokens in this module.


* **Return type**

    `bool`



* **Returns**

    True if transfer is restricted, False otherwise



#### normalize_amount(amount)

* **Return type**

    `int`



#### set_allowance(spender, amount)
Sets the allowance of the specified wallet over the connected wallets funds to
a specified amount.


* **Parameters**

    
    * **spender** (`str`) – wallet address to set the allowance of


    * **amount** (`float`) – amount to set the allowance to



* **Return type**

    `TxReceipt`



* **Returns**

    transaction receipt of the allowance set



#### total_supply()
Get the total minted supply of the token.


* **Return type**

    [`CurrencyValue`](thirdweb.types.md#thirdweb.types.currency.CurrencyValue)



* **Returns**

    total minted supply of the token



#### transfer(to, amount)
Transfer a specified amount of tokens from the connected wallet to a specified address.


* **Parameters**

    
    * **to** (`str`) – wallet address to transfer the tokens to


    * **amount** (`float`) – amount of tokens to transfer



* **Return type**

    `TxReceipt`



* **Returns**

    transaction receipt of the transfer



#### transfer_batch(args)
Transfer tokens from the connected wallet to many wallets.


* **Parameters**

    **args** (`List`[[`TokenAmount`](thirdweb.types.md#thirdweb.types.currency.TokenAmount)]) – list of token amounts and addressed to transfer to



* **Returns**

    transaction receipt of the transfers



#### transfer_from(fr, to, amount)
Transfer a specified amount of tokens from one specified address to another.


* **Parameters**

    
    * **fr** (`str`) – wallet address to transfer the tokens from


    * **to** (`str`) – wallet address to transfer the tokens to


    * **amount** (`float`) – amount of tokens to transfer



* **Return type**

    `TxReceipt`



* **Returns**

    transaction receipt of the transfer


## thirdweb.core.classes.erc_721 module


### _class_ thirdweb.core.classes.erc_721.ERC721(contract_wrapper, storage)
Bases: `thirdweb.core.classes.base_contract.BaseContract`[[`thirdweb.abi.token_erc721.TokenERC721`](thirdweb.abi.md#thirdweb.abi.token_erc721.TokenERC721)]


#### \__init__(contract_wrapper, storage)

#### balance()
Get the token balance of the connected wallet


* **Return type**

    `int`



* **Returns**

    the token balance of the connected wallet



#### balance_of(address)
Get the token balance of a specific address


* **Parameters**

    **address** (`str`) – the address to get the token balance of



* **Return type**

    `int`



#### burn(token_id)
Burn a specified token from the connected wallet.


* **Parameters**

    **token_id** (`int`) – token ID of the token to burn



* **Return type**

    `TxReceipt`



* **Returns**

    transaction receipt of the burn



#### get(token_id)
Get metadata for a token


* **Parameters**

    **token_id** (`int`) – token ID of the token to get the metadata for



* **Return type**

    [`NFTMetadataOwner`](thirdweb.types.md#thirdweb.types.nft.NFTMetadataOwner)



* **Returns**

    the metadata for the token and its owner



#### get_all(query_params=QueryAllParams(start=0, count=100))
Get the metadata of all tokens in the contract


* **Parameters**

    **query_params** ([`QueryAllParams`](thirdweb.types.md#thirdweb.types.nft.QueryAllParams)) – optionally define a QueryAllParams instance to narrow the metadata query to specific tokens



* **Return type**

    `List`[[`NFTMetadataOwner`](thirdweb.types.md#thirdweb.types.nft.NFTMetadataOwner)]



* **Returns**

    the metadata of all tokens in the contract



#### get_owned(address='')
Get the metadata of all tokens owned by a specific address


* **Parameters**

    **address** (`str`) – the address to get the metadata for



* **Return type**

    `List`[[`NFTMetadataOwner`](thirdweb.types.md#thirdweb.types.nft.NFTMetadataOwner)]



* **Returns**

    the metadata of all tokens owned by the address



#### get_total_count()
Get the total number of NFTs minted by this contract


* **Return type**

    `int`



* **Returns**

    the total number of NFTs minted by this contract



#### is_approved(address, operator)
Check whether an operator address is approved for all operations of a specific addresses assets


* **Parameters**

    
    * **address** (`str`) – the address whose assets are to be checked


    * **operator** (`str`) – the address of the operator to check



* **Return type**

    `bool`



* **Returns**

    True if the operator is approved for all operations of the assets, False otherwise



#### is_transfer_restricted()
Check if the contract is restricted to transfers only by admins


* **Return type**

    `bool`



* **Returns**

    True if the contract is restricted to transfers only by admins, False otherwise



#### owner_of(token_id)
Get the owner of a token


* **Parameters**

    **token_id** (`int`) – the token ID of the token to get the owner of



* **Return type**

    `str`



* **Returns**

    the owner of the token



#### set_approval_for_all(operator, approved)
Set the approval of an operator for all operations of a specific address’s assets


* **Parameters**

    
    * **operator** (`str`) – the address of the operator to set the approval for


    * **approved** (`bool`) – the address whos assets the operator is approved to manage



* **Return type**

    `TxReceipt`



* **Returns**

    transaction receipt of the approval setting



#### total_supply()
Get the total number of tokens in the contract


* **Return type**

    `int`



* **Returns**

    the total number of tokens in the contract



#### transfer(to, token_id)
Transfer a specified token from the connected wallet to a specified address.


* **Parameters**

    
    * **to** (`str`) – wallet address to transfer the tokens to


    * **token_id** (`int`) – the specific token ID to transfer



* **Return type**

    `TxReceipt`



* **Returns**

    transaction receipt of the transfer


## thirdweb.core.classes.factory module


### _class_ thirdweb.core.classes.factory.ContractFactory(factory_address, provider, signer=None, options=SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)), storage=<thirdweb.core.classes.ipfs_storage.IpfsStorage object>)
Bases: `thirdweb.core.classes.contract_wrapper.ContractWrapper`[[`thirdweb.abi.t_w_factory.TWFactory`](thirdweb.abi.md#thirdweb.abi.t_w_factory.TWFactory)]


#### \__init__(factory_address, provider, signer=None, options=SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)), storage=<thirdweb.core.classes.ipfs_storage.IpfsStorage object>)
Initializes the contract wrapper.


* **Parameters**

    
    * **contract_abi** – ABI of the thirdweb contract to use


    * **provider** (`Web3`) – web3 provider instance to use


    * **signer** (`Optional`[`LocalAccount`]) – optional account to use for signing transactions



#### deploy(contract_type, contract_metadata)

* **Return type**

    `str`



#### get_deploy_arguments(contract_type, contract_metadata, contract_uri)

* **Return type**

    `List`[`Any`]


## thirdweb.core.classes.ipfs_storage module


### _class_ thirdweb.core.classes.ipfs_storage.IpfsStorage(gateway_url='https://gateway.ipfscdn.io/ipfs/')
Bases: `abc.ABC`


#### \__init__(gateway_url='https://gateway.ipfscdn.io/ipfs/')

#### get(hash)
Gets IPFS data at a given hash and returns it as a dictionary.


* **Parameters**

    **hash** (`str`) – hash of the data to get.



* **Return type**

    `Dict`[`str`, `Any`]



* **Returns**

    dictionary of the data.



#### get_upload_token(contract_address)
Gets an upload token for a given contract address.


* **Return type**

    `str`



#### upload(data, contract_address='', signer_address='')
Uploads data to IPFS and returns the hash of the data.


* **Return type**

    `str`



#### upload_batch(files, file_start_number=0, contract_address='', signer_address='')
Uploads a list of files to IPFS and returns the hash.


* **Return type**

    `str`



#### upload_metadata(metadata, contract_address='', signer_address='')
Uploads metadata to IPFS and returns the hash of the metadata.


* **Return type**

    `str`



#### upload_metadata_batch(metadatas, file_start_number=0, contract_address='', signer_address='')
Uploads a list of metadata to IPFS and returns the hash.


* **Return type**

    [`UriWithMetadata`](thirdweb.types.md#thirdweb.types.storage.UriWithMetadata)


## thirdweb.core.classes.marketplace_auction module


### _class_ thirdweb.core.classes.marketplace_auction.MarketplaceAuction(contract_wrapper, storage)
Bases: `thirdweb.core.classes.base_contract.BaseContract`[[`thirdweb.abi.marketplace.Marketplace`](thirdweb.abi.md#thirdweb.abi.marketplace.Marketplace)]


#### \__init__(contract_wrapper, storage)

#### buyout_listing(listing_id)

* **Return type**

    `TxReceipt`



#### cancel_listing(listing_id)

* **Return type**

    `TxReceipt`



#### close_listing(listing_id, close_for=None)

* **Return type**

    `TxReceipt`



#### create_listing(listing)

* **Return type**

    `int`



#### get_listing(listing_id)

* **Return type**

    [`AuctionListing`](thirdweb.types.md#thirdweb.types.marketplace.AuctionListing)



#### get_winner(listing_id)

* **Return type**

    `str`



#### get_winning_bid(listing_id)

* **Return type**

    `Optional`[[`Offer`](thirdweb.types.md#thirdweb.types.marketplace.Offer)]



#### make_bid(listing_id, price_per_token)

* **Return type**

    `TxReceipt`



#### update_listing(listing)

* **Return type**

    `TxReceipt`


## thirdweb.core.classes.marketplace_direct module


### _class_ thirdweb.core.classes.marketplace_direct.MarketplaceDirect(contract_wrapper, storage)
Bases: `thirdweb.core.classes.base_contract.BaseContract`[[`thirdweb.abi.marketplace.Marketplace`](thirdweb.abi.md#thirdweb.abi.marketplace.Marketplace)]


#### \__init__(contract_wrapper, storage)

#### accept_offer(listing_id, address_or_offerror)

* **Return type**

    `TxReceipt`



#### buyout_listing(listing_id, quantity_desired, receiver=None)

* **Return type**

    `TxReceipt`



#### cancel_listing(listing_id)

* **Return type**

    `TxReceipt`



#### create_listing(listing)

* **Return type**

    `int`



#### get_active_offer(listing_id, address)

* **Return type**

    `Optional`[[`Offer`](thirdweb.types.md#thirdweb.types.marketplace.Offer)]



#### get_listing(listing_id)

* **Return type**

    [`DirectListing`](thirdweb.types.md#thirdweb.types.marketplace.DirectListing)



#### make_offer(listing_id, quantity_desired, currency_contract_address, price_per_token)

* **Return type**

    `TxReceipt`



#### update_listing(listing)

* **Return type**

    `TxReceipt`


## thirdweb.core.classes.provider_handler module


### _class_ thirdweb.core.classes.provider_handler.ProviderHandler(provider, signer=None, options=SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))
Bases: `object`

The provider handler is responsible for managing the connected provider and signer
for any class including the read-only provider.


#### \__init__(provider, signer=None, options=SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))
Initialize the provider handler.


* **Parameters**

    
    * **provider** (`Web3`) – web3 provider instance to use


    * **signer** (`Optional`[`LocalAccount`]) – optional account to use for signing transactions


    * **options** ([`SDKOptions`](thirdweb.types.md#thirdweb.types.sdk.SDKOptions)) – optional SDKOptions instance to specify read-only RPC URL and gas settings



#### get_options()

* **Return type**

    [`SDKOptions`](thirdweb.types.md#thirdweb.types.sdk.SDKOptions)



#### get_provider()
Get the active provider.


* **Return type**

    `Web3`



* **Returns**

    the Web3 instance of the active provider



#### get_signer()
Get the active signer.


* **Return type**

    `Optional`[`LocalAccount`]



* **Returns**

    the Account instance of the active signer, otherwise None



#### is_read_only()
Check if there is no active signer.


#### update_provider(provider)
Update the active provider.


* **Parameters**

    **provider** (`Web3`) – web3 provider instance to use



#### update_signer(signer=None)
Update the active signer.


* **Parameters**

    **signer** (`Optional`[`LocalAccount`]) – optional account to use for signing transactions


## thirdweb.core.classes.registry module


### _class_ thirdweb.core.classes.registry.ContractRegistry(registry_address, provider, signer, options=SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))
Bases: `thirdweb.core.classes.contract_wrapper.ContractWrapper`


#### \__init__(registry_address, provider, signer, options=SDKOptions(read_only_settings=None, gas_settings=GasSettings(max_price_in_gwei=300, speed=<GasSpeed.FASTEST: 'fastest'>)))
Initializes the contract wrapper.


* **Parameters**

    
    * **contract_abi** – ABI of the thirdweb contract to use


    * **provider** (`Web3`) – web3 provider instance to use


    * **signer** (`Optional`[`LocalAccount`]) – optional account to use for signing transactions



#### get_contract_addresses(address)
Get all the contract addresses registered for a given address.


* **Parameters**

    **address** (`str`) – address to get the contract addresses for



* **Return type**

    `List`[`str`]



* **Returns**

    list of contract addresses


## Module contents
