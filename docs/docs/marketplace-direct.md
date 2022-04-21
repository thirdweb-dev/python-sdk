<a id="core.classes.marketplace_direct"></a>

# core.classes.marketplace\_direct

<a id="core.classes.marketplace_direct.MarketplaceDirect"></a>

## MarketplaceDirect Objects

```python
class MarketplaceDirect(BaseContract[Marketplace])
```

<a id="core.classes.marketplace_direct.MarketplaceDirect.get_listing"></a>

#### get\_listing

```python
def get_listing(listing_id: int) -> DirectListing
```

Get a direct listing from the marketplace by ID

**Arguments**:

- `listing_id`: The ID of the listing to get

**Returns**:

The listing

<a id="core.classes.marketplace_direct.MarketplaceDirect.get_active_offer"></a>

#### get\_active\_offer

```python
def get_active_offer(listing_id: int, address: str) -> Optional[Offer]
```

Get an active offer for a direct listing

**Arguments**:

- `listing_id`: The ID of the listing to get the offer for
- `address`: The address of the user to get the offer for

**Returns**:

The offer

<a id="core.classes.marketplace_direct.MarketplaceDirect.create_listing"></a>

#### create\_listing

```python
def create_listing(listing: NewDirectListing) -> int
```

Create a new direct listing

**Arguments**:

- `listing`: The listing to create

**Returns**:

The ID of the listing

<a id="core.classes.marketplace_direct.MarketplaceDirect.make_offer"></a>

#### make\_offer

```python
def make_offer(
    listing_id: int,
    quantity_desired: int,
    currency_contract_address: str,
    price_per_token: Price,
    expiration_date: int = int(MAX_INT, 0)) -> TxReceipt
```

Make an offer on a direct listing

**Arguments**:

- `listing_id`: The ID of the listing to make the offer on
- `quantity_desired`: The quantity desired
- `currency_contract_address`: The address of the currency contract
- `price_per_token`: The price per token

**Returns**:

The transaction receipt

<a id="core.classes.marketplace_direct.MarketplaceDirect.accept_offer"></a>

#### accept\_offer

```python
def accept_offer(listing_id: int, address_or_offerror: str) -> TxReceipt
```

Accept a direct listing offer

**Arguments**:

- `listing_id`: The ID of the listing to accept the offer on
- `address_or_offerror`: The address of the user to accept the offer for

**Returns**:

The transaction receipt

<a id="core.classes.marketplace_direct.MarketplaceDirect.buyout_listing"></a>

#### buyout\_listing

```python
def buyout_listing(listing_id: int,
                   quantity_desired: int,
                   receiver: Optional[str] = None) -> TxReceipt
```

Buyout a direct listing by ID

**Arguments**:

- `listing_id`: The ID of the listing to buyout
- `quantity_desired`: The quantity desired
- `receiver`: The address of the user to receive the tokens

**Returns**:

The transaction receipt

<a id="core.classes.marketplace_direct.MarketplaceDirect.update_listing"></a>

#### update\_listing

```python
def update_listing(listing: DirectListing) -> TxReceipt
```

Update a direct listing

**Arguments**:

- `listing`: The listing to update

**Returns**:

The transaction receipt

<a id="core.classes.marketplace_direct.MarketplaceDirect.cancel_listing"></a>

#### cancel\_listing

```python
def cancel_listing(listing_id: int) -> TxReceipt
```

Cancel a direct listing

**Arguments**:

- `listing_id`: The ID of the listing to cancel

**Returns**:

The transaction receipt

