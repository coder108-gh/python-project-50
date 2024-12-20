#!usr/bin/env python3
import json


def json_formatter(diff: dict) -> str:
    return json.dumps(diff, indent=3)
