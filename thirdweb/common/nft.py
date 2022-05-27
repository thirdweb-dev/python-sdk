from typing import List, Union, cast

from web3 import Web3
from thirdweb.abi import TokenERC1155, IERC165, TokenERC721
from thirdweb.common.error import UploadException
from thirdweb.constants.contract import INTERFACE_ID_IERC1155, INTERFACE_ID_IERC721
from thirdweb.core.classes.ipfs_storage import IpfsStorage
from thirdweb.types.nft import NFTMetadata, NFTMetadataInput


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


def fetch_token_metadata_for_contract(
    contract_address: str,
    provider: Web3,
    token_id: int,
    storage: IpfsStorage,
):
    erc165 = IERC165(provider, contract_address)
    is_erc721 = erc165.supports_interface.call(INTERFACE_ID_IERC721)
    is_erc1155 = erc165.supports_interface.call(INTERFACE_ID_IERC1155)

    if is_erc721:
        erc721 = TokenERC721(provider, contract_address)
        uri = erc721.token_uri.call(token_id)
    elif is_erc1155:
        erc1155 = TokenERC1155(provider, contract_address)
        uri = erc1155.uri.call(token_id)

    if not uri:
        raise Exception("Contract does not implement ERC721 or ERC1155")

    return fetch_token_metadata(token_id, uri, storage)


def upload_or_extract_uri(
    metadata: Union[NFTMetadataInput, str], storage: IpfsStorage
) -> str:
    if isinstance(metadata, str):
        return metadata
    else:
        return storage.upload_metadata(metadata.to_json())


def is_uri_list(metadatas: List[Union[NFTMetadataInput, str]]) -> bool:
    return all(isinstance(metadata, str) for metadata in metadatas)


def is_metadata_list(metadatas: List[Union[NFTMetadataInput, str]]) -> bool:
    return all(isinstance(metadata, NFTMetadataInput) for metadata in metadatas)


def upload_or_extract_uris(
    metadatas: List[Union[NFTMetadataInput, str]], storage: IpfsStorage
) -> List[str]:
    if is_uri_list(metadatas):
        return cast(List[str], metadatas)
    elif is_metadata_list(metadatas):
        json_metadatas = [
            metadata.to_json() for metadata in cast(List[NFTMetadataInput], metadatas)
        ]
        uri_with_metadata = storage.upload_metadata_batch(json_metadatas)
        return uri_with_metadata.metadata_uris
    else:
        raise UploadException(
            "Metadata must be either a list of strings or a list of NFTMetadata"
        )
