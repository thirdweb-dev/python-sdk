# thirdweb.constants package

## Submodules

## thirdweb.constants.addresses module


### thirdweb.constants.addresses.get_contract_address_by_chain_id(chain_id, contract_name)

* **Return type**

    `str`


## thirdweb.constants.chains module


### _class_ thirdweb.constants.chains.ChainId(value)
Bases: `enum.Enum`

An enumeration.


#### AVALANCHE(_ = 4311_ )

#### FANTOM(_ = 25_ )

#### GOERLI(_ = _ )

#### HARDHAT(_ = 3133_ )

#### LOCALHOST(_ = 133_ )

#### MAINNET(_ = _ )

#### MUMBAI(_ = 8000_ )

#### POLYGON(_ = 13_ )

#### RINKEBY(_ = _ )
## thirdweb.constants.contract module

## thirdweb.constants.currency module


### thirdweb.constants.currency.get_native_token_by_chain_id(chain_id)

* **Return type**

    [`NativeToken`](thirdweb.types.md#thirdweb.types.currency.NativeToken)


## thirdweb.constants.role module


### _class_ thirdweb.constants.role.Role(value)
Bases: `enum.Enum`

An enumeration.


#### ADMIN(_ = 'admin_ )

#### ASSET(_ = 'asset_ )

#### EDITOR(_ = 'editor_ )

#### LISTER(_ = 'lister_ )

#### MINTER(_ = 'minter_ )

#### PAUSER(_ = 'pauser_ )

#### TRANSFER(_ = 'transfer_ )

### thirdweb.constants.role.get_role_hash(role)

* **Return type**

    `HexBytes`


## thirdweb.constants.rpc module

## thirdweb.constants.urls module

## Module contents
