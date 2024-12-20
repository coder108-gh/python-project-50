from gendiff.files import get_data_from_file
from copy import deepcopy


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


def get_diff_data(file_path1: str, file_path2: str) -> dict:
    first = get_data_from_file(file_path1)
    second = get_data_from_file(file_path2)
    diff = make_diff(first, second)
    return diff
