#!usr/bin/env python3
import json


def json_formatter(diff: dict, file_path1: str, file_path2: str) -> str:
    header = f'gendiff --format json {file_path1} {file_path2}'
    return header + '\n' + json.dumps(diff, indent=3)
