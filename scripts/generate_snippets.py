from typing import Any, Dict
import thirdweb.contracts
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
]

DOC_NAMES = {
    "NFTCollection": "nft-collection",
    "Edition": "edition",
    "Token": "token",
    "Marketplace": "marketplace",
    "NFTDrop": "nft-drop",
    "EditionDrop": "edition-drop",
    "ERC20": "erc20",
    "ERC721": "erc721",
    "ERC1155": "erc1155",
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
    return matches.group(0).replace("```python", "").replace("```", "")


BASE_DOC_URL = "https://docs.thirdweb.com/python"


def describe(cls: object):
    cls_name = cls.__name__  # type: ignore
    doc_url = f"{BASE_DOC_URL}/{DOC_NAMES[cls_name]}"

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
            if not example:
                continue

            reference = f"{doc_url}#{name}"
            for c in classes:
                if c[0] == name:
                    class_url = DOC_NAMES[c[2].__name__]
                    reference = f"{BASE_DOC_URL}/{class_url}#{name}"
                    break

            methods.append(
                {
                    "name": name,
                    "summary": docstring,
                    "example": example,
                    "reference": reference,
                }
            )

    data["methods"] = methods

    properties = []
    spec = inspect.getfullargspec(cls)._asdict()
    for name, val in spec["annotations"].items():
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

    with open("docs/docs/snippets.json", "w") as f:
        j = json.dumps(data, indent=4)
        f.write(j)


generate()
