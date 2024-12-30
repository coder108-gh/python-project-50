from json import loads
from yaml import safe_load


def parse(data: str, format: str) -> dict | None:
    loaders = {
        'json': loads,
        'yaml': safe_load
    }

    if format in loaders:
        return loaders[format](data)
    return None
