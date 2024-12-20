from json import load
import os.path as path
from yaml import safe_load


def get_file_extention(file_name: str) -> str:
    parts = path.splitext(file_name)
    return parts[-1].replace('.', '')


def get_data_from(file_name: str, read_func):
    with open(file_name, mode='r', encoding='utf-8') as file:
        data = read_func(file)
    return data


def get_data_from_file(file_name: str) -> dict | None:
    JSON_EXT = ['json']
    YAML_EXT = ['yaml', 'yml']
    ext = get_file_extention(file_name).lower()
    if ext in JSON_EXT:
        return get_data_from(file_name, read_func=load)
    elif ext in YAML_EXT:
        return get_data_from(file_name, read_func=safe_load)
    else:
        return None
