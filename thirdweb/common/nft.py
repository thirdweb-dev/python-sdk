from typing import cast
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.nft import NFTMetadata


def fetch_token_metadata(
    token_id: int, token_uri: str, storage: IpfsStorage
) -> NFTMetadata:
    metadata = storage.get(token_uri)
    return NFTMetadata(
        token_id,
        token_uri,
        cast(str, metadata.get("name")),
        metadata.get("description"),
        metadata.get("image"),
        metadata.get("external_url"),
        metadata.get("animation_url"),
        metadata.get("background_color"),
        metadata.get("properties"),
    )
