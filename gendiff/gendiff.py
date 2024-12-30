from copy import deepcopy

from gendiff.formatters.json_formatter import json_formatter
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.files import get_extension, read_file
from gendiff.parse_data import parse


def generate_diff(file_path1: str, file_path2: str, format_name='stylish'):
    diff = get_diff_data(file_path1, file_path2)
    formatters = {
        'stylish': stylish,
        'plain': plain,
        'json': json_formatter
    }
    if format_name in formatters:
        return formatters[format_name](diff)
    return f'{format_name} - unknown formatter'


def get_diff_data(file1: str, file2: str) -> dict:
    first = parse(read_file(file1), get_extension(file1))
    second = parse(read_file(file2), get_extension(file2))
    diff = make_diff(first, second)
    return diff


def make_diff(a: dict, b1: dict) -> dict:
    diff = {}
    b = deepcopy(b1)
    for key, value in a.items():
        if key not in b:
            diff[key] = [value, ()]
        elif isinstance(value, dict) and isinstance(b[key], dict):
            diff[key] = make_diff(value, b[key])
            b.pop(key)
        else:
            diff[key] = [value, b[key]]
            b.pop(key)

    for key, value in b.items():
        diff[key] = [(), value]

    return diff
