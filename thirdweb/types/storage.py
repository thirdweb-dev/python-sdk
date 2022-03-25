from dataclasses import dataclass
from typing import List


@dataclass
class CidWithFileName:
    cid: str
    filenames: List[str]


@dataclass
class UriWithMetadata:
    base_uri: str
    metadata_uris: List[str]
