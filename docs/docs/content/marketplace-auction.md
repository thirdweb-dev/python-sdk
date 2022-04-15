<a id="core.classes.marketplace_auction"></a>

# core.classes.marketplace\_auction

<a id="core.classes.marketplace_auction.MarketplaceAuction"></a>

## MarketplaceAuction Objects

```python
class MarketplaceAuction(BaseContract[Marketplace])
```

<a id="core.classes.marketplace_auction.MarketplaceAuction.get_listing"></a>

#### get\_listing

```python
def get_listing(listing_id: int) -> AuctionListing
```

Get an auction listing from the marketplace by ID

**Arguments**:

- `listing_id`: The ID of the listing to get

**Returns**:

The auction listing

<a id="core.classes.marketplace_auction.MarketplaceAuction.get_winning_bid"></a>

#### get\_winning\_bid

```python
def get_winning_bid(listing_id: int) -> Optional[Offer]
```

Get the winning bid on an auction listing

**Arguments**:

- `listing_id`: The ID of the listing to get the winning bid for

**Returns**:

The winning bid

<a id="core.classes.marketplace_auction.MarketplaceAuction.get_winner"></a>

#### get\_winner

```python
def get_winner(listing_id) -> str
```

Get the winner of an auction that has already ended.

**Arguments**:

- `listing_id`: The ID of the listing to get the winner for

**Returns**:

The winning bidder

<a id="core.classes.marketplace_auction.MarketplaceAuction.create_listing"></a>

#### create\_listing

```python
def create_listing(listing: NewAuctionListing) -> int
```

Create a new auction listing

**Arguments**:

- `listing`: The listing to create

**Returns**:

The ID of the listing

<a id="core.classes.marketplace_auction.MarketplaceAuction.buyout_listing"></a>

#### buyout\_listing

```python
def buyout_listing(listing_id: int) -> TxReceipt
```

Buyout an auction listing

**Arguments**:

- `listing_id`: The ID of the listing to buyout

**Returns**:

The transaction receipt

<a id="core.classes.marketplace_auction.MarketplaceAuction.make_bid"></a>

#### make\_bid

```python
def make_bid(listing_id: int, price_per_token: Price) -> TxReceipt
```

Make a bid on an auction listing

**Arguments**:

- `listing_id`: The ID of the listing to bid on
- `price_per_token`: The price per token to bid

**Returns**:

The transaction receipt

<a id="core.classes.marketplace_auction.MarketplaceAuction.cancel_listing"></a>

#### cancel\_listing

```python
def cancel_listing(listing_id: int) -> TxReceipt
```

Cancel an auction listing

**Arguments**:

- `listing_id`: The ID of the listing to cancel

**Returns**:

The transaction receipt

<a id="core.classes.marketplace_auction.MarketplaceAuction.update_listing"></a>

#### update\_listing

```python
def update_listing(listing: AuctionListing) -> TxReceipt
```

Update a listing on the marketplace

**Arguments**:

- `listing`: The listing to update

**Returns**:

The transaction receipt

