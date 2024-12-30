import json


def json_formatter(diff: dict) -> str:
    return json.dumps(diff, indent=3)
