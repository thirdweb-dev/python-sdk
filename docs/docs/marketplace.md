<a id="contracts.marketplace"></a>

# contracts.marketplace

Interface for interacting with a marketplace contract

<a id="contracts.marketplace.Marketplace"></a>

## Marketplace Objects

```python
class Marketplace(BaseContract[MarketplaceABI])
```

Create your own whitelabel marketplace that enables users to buy and sell any digital assets.

```python
from thirdweb import ThirdwebSDK
from eth_account import Account
from web3 import Web3

// You can switch out this provider and RPC URL for your own
provider = Web3(Web3.HTTPProvider("<RPC_URL>"))
// This will create a random account to use for signing transactions
signer = Account.create()

sdk = ThirdwebSDK(provider, signer)
contract = sdk.get_marketplace("<CONTRACT_ADDRESS>")
```

<a id="contracts.marketplace.Marketplace.get_listing"></a>

#### get\_listing

```python
def get_listing(listing_id: int) -> Union[DirectListing, AuctionListing]
```

Get a listing from the marketplace by ID

**Arguments**:

- `listing_id`: ID of the listing to get

**Returns**:

Listing object

<a id="contracts.marketplace.Marketplace.get_active_listings"></a>

#### get\_active\_listings

```python
def get_active_listings() -> List[Union[DirectListing, AuctionListing]]
```

Get all the currently active listings from the marketplace.

**Returns**:

List of listings

<a id="contracts.marketplace.Marketplace.get_all_listings"></a>

#### get\_all\_listings

```python
def get_all_listings(
    filter: MarketplaceFilter = None
) -> List[Union[DirectListing, AuctionListing]]
```

Get all the listings that have ever been made on this marketplace.

**Arguments**:

- `filter`: Filter to apply to the listings

**Returns**:

List of listings

<a id="contracts.marketplace.Marketplace.get_total_count"></a>

#### get\_total\_count

```python
def get_total_count() -> int
```

Get the total number of listings on this marketplace.

**Returns**:

Total number of listings

<a id="contracts.marketplace.Marketplace.is_restricted_to_lister_role_only"></a>

#### is\_restricted\_to\_lister\_role\_only

```python
def is_restricted_to_lister_role_only() -> bool
```

Check whether only wallets with the lister role can make listings.

**Returns**:

True if only lister wallets can make listings

<a id="contracts.marketplace.Marketplace.get_bid_buffer_bps"></a>

#### get\_bid\_buffer\_bps

```python
def get_bid_buffer_bps() -> int
```

Get the bid buffer basis points for this marketplace.

**Returns**:

Bid buffer basis points

<a id="contracts.marketplace.Marketplace.get_time_buffer_in_seconds"></a>

#### get\_time\_buffer\_in\_seconds

```python
def get_time_buffer_in_seconds() -> int
```

Get the time buffer for this marketplace in seconds

**Returns**:

Time buffer in seconds

<a id="contracts.marketplace.Marketplace.buyout_listing"></a>

#### buyout\_listing

```python
def buyout_listing(listing_id: int,
                   quantity_desired: Optional[int] = None,
                   receiver: Optional[str] = None) -> TxReceipt
```

Buyout a listing by listing ID

**Arguments**:

- `listing_id`: ID of the listing to buyout
- `quantity_desired`: Quantity to buyout
- `receiver`: Address to send the asset to

**Returns**:

Transaction receipt of buyout

<a id="contracts.marketplace.Marketplace.set_bid_buffer_bps"></a>

#### set\_bid\_buffer\_bps

```python
def set_bid_buffer_bps(buffer_bps: int) -> TxReceipt
```

Set the bid buffer basis points for this marketplace.

**Arguments**:

- `buffer_bps`: Bid buffer basis points

**Returns**:

Transaction receipt

<a id="contracts.marketplace.Marketplace.set_time_buffer_in_seconds"></a>

#### set\_time\_buffer\_in\_seconds

```python
def set_time_buffer_in_seconds(buffer_in_seconds: int) -> TxReceipt
```

Set the time buffer of the marketplace.

**Arguments**:

- `buffer_in_seconds`: Time buffer in seconds

**Returns**:

Transaction receipt

<a id="contracts.marketplace.Marketplace.allow_listing_from_specific_asset_only"></a>

#### allow\_listing\_from\_specific\_asset\_only

```python
def allow_listing_from_specific_asset_only(contract_address: str) -> TxReceipt
```

Restrict marketplace so only specific asset can be listed.

**Arguments**:

- `contract_address`: Address of the asset contract

<a id="contracts.marketplace.Marketplace.allow_listing_from_any_asset"></a>

#### allow\_listing\_from\_any\_asset

```python
def allow_listing_from_any_asset() -> TxReceipt
```

Allow asset to be listed on the marketplace.

**Returns**:

Transaction receipt

