from typing import Any, Dict
from thirdweb.contracts import Marketplace
import inspect
import re


def get_description(cls: object) -> str:
    doc = getattr(cls, "__doc__", "")
    if doc is None:
        return ""
    no_example = re.sub(r"```(.|\n)*```", "", doc)
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


def describe(cls: object):
    data: Dict[str, Any] = {
        "name": type(cls).__name__,
        "summary": get_description(cls),
        "example": get_example(cls),
        "methods": [],
        "properties": [],
        "reference": "",
    }

    fns = [(k, v) for k, v in cls.__dict__.items() if not k.startswith("_")]

    methods = []
    for name, fn in fns:
        if inspect.isfunction(fn):
            docstring = get_description(fn)
            if not docstring:
                continue
            example = get_example(fn)
            if not example:
                continue

            methods.append({"name": name, "summary": docstring, "example": example})

    data["methods"] = methods

    properties = []
    spec = inspect.getfullargspec(cls)._asdict()
    for name, val in spec["annotations"].items():
        docstring = get_description(val)
        if not docstring:
            continue
        example = get_example(val)
        if not example:
            continue

        properties.append(
            {
                "name": name,
                "summary": docstring,
                "example": example,
            }
        )

    data["properties"] = properties

    return data


print(describe(Marketplace))
