from typing import Any, Dict, List, cast
import thirdweb.contracts
import thirdweb.core.classes
import inspect
import json
import re

CONTRACTS = [
    "NFTCollection",
    "Edition",
    "Token",
    "Marketplace",
    "NFTDrop",
    "EditionDrop",
    "Multiwrap",
]

CLASSES = [
    thirdweb.core.classes.contract_events.ContractEvents,
    thirdweb.core.classes.contract_metadata.ContractMetadata,
    thirdweb.core.classes.contract_platform_fee.ContractPlatformFee,
    thirdweb.core.classes.contract_roles.ContractRoles,
    thirdweb.core.classes.contract_royalty.ContractRoyalty,
    thirdweb.core.classes.contract_sales.ContractPrimarySale,
    thirdweb.core.classes.erc_20.ERC20,
    thirdweb.core.classes.erc_721.ERC721,
    thirdweb.core.classes.erc_1155.ERC1155,
]

DOC_NAMES = {
    "NFTCollection": "nft-collection",
    "Edition": "edition",
    "Token": "token",
    "Marketplace": "marketplace",
    "NFTDrop": "nft-drop",
    "EditionDrop": "edition-drop",
    "Multiwrap": "multiwrap",
    "ERC20": "erc20",
    "ERC721": "erc721",
    "ERC1155": "erc1155",
    "WalletAuthenticator": "wallet-authenticator",
    "ContractEvents": "contract-events",
    "ContractMetadata": "contract-metadata",
    "ContractPlatformFee": "contract-platform-fee",
    "ContractRoles": "contract-roles",
    "ContractRoyalty": "contract-royalty",
    "ContractPrimarySale": "contract-sales"
}


def get_description(cls: object) -> str:
    doc = getattr(cls, "__doc__", "")
    if doc is None:
        return ""
    # no_example = re.sub(r"```(.|\n)*```", "", doc)
    no_example = doc.split("\n\n")[0]
    cleaned = no_example.replace("\n", "").strip()
    return cleaned


def get_example(cls: object) -> str:
    doc = getattr(cls, "__doc__", "")
    if doc is None:
        return ""
    matches = re.search(r"```(.|\n)*```", doc)
    if matches is None:
        return ""
    example = matches.group(0).replace("```python", "").replace("```", "")
    return inspect.cleandoc(example)

def get_extensions(cls: object) -> List[str]:
    doc = getattr(cls, "__doc__", "")
    if doc is None:
        return []
    matches = re.search(r"(?<=:extension: )(.*)(?=\n)", doc)
    if matches is None:
        return []
    return matches.group(0).split(" | ")

BASE_DOC_URL = "https://docs.thirdweb.com/python"


def describe(cls: object):
    cls_name = cls.__name__  # type: ignore
    doc_url = f"{BASE_DOC_URL}/{DOC_NAMES[cls_name]}" if cls_name in DOC_NAMES else ""

    data: Dict[str, Any] = {
        "name": cls_name,
        "summary": get_description(cls),
        "example": get_example(cls),
        "methods": [],
        "properties": [],
        "reference": doc_url,
    }

    inspected = inspect.getmembers(cls, predicate=inspect.isfunction)
    classes = inspect.classify_class_attrs(cls)  # type: ignore
    fns = [(k, v) for k, v in inspected if not k.startswith("_")]

    methods = []
    for name, fn in fns:
        if inspect.isfunction(fn):
            docstring = get_description(fn)
            example = get_example(fn)
            extensions = get_extensions(fn)

            reference = f"{doc_url}#{name}"
            for c in classes:
                if c[0] == name and c[2].__name__ in DOC_NAMES:
                    class_url = DOC_NAMES[c[2].__name__]
                    reference = f"{BASE_DOC_URL}/{class_url}#{name}"
                    break

            methods.append(
                {
                    "name": name,
                    "summary": docstring,
                    "example": example,
                    "reference": reference,
                    "extensions": extensions
                }
            )

    data["methods"] = methods

    properties = []
    spec = [
        (k, v)
        for k, v in inspect.getmembers(cls, lambda a: not (inspect.isroutine(a)))
        if not k.startswith("_")
    ]
    for name, val in spec:
        docstring = get_description(val)

        example = get_example(val)
        if not example:
            continue
    
        properties.append(
            {
                "name": name,
                "summary": docstring,
                "example": example,
                "reference": "",
            }
        )

    data["properties"] = properties

    return data


def generate():
    data = {}
    for contract in CONTRACTS:
        cls = getattr(thirdweb.contracts, contract)
        data[contract] = describe(cls)
    
    for cls in CLASSES:
        data[cls.__name__] = describe(cls)

    cls = thirdweb.core.auth.WalletAuthenticator
    data["WalletAuthenticator"] = describe(cls)

    with open("docs/docs/snippets.json", "w") as f:
        j = json.dumps(data, indent=4)
        f.write(j)

def generate_features():
    features: Dict[str, List[Dict[str, Any]]] = {}

    with open('docs/docs/snippets.json') as snippets_file:
        snippets: Dict[str, Dict[str, Any]] = json.load(snippets_file)

    methods: List[Dict[str, Any]] = []
    for cls in snippets.values():
        for method in cls["methods"]:
            if len(method["extensions"]) > 0:
                methods.append({
                    "name": method["name"],
                    "summary": method["summary"],
                    "examples": {
                        "python": method["example"]
                    },
                    "reference": {
                        "python": method["reference"]
                    },
                    "extensions": method["extensions"]
                })
    
    for method in methods:
        for extension in method["extensions"]:
            cleaned_method = {
                "name": method["name"],
                "summary": method["summary"],
                "examples": method["examples"],
                "reference": method["reference"]
            }

            if extension in features:
                features[extension].append(cleaned_method)
            else:
                features[extension] = [cleaned_method]

    with open("docs/docs/feature_snippets.json", "w") as f:
        j = json.dumps(features, indent=4)
        f.write(j)   

generate()
generate_features()