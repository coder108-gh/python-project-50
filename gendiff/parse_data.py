#!usr/bin/env python3
from json import loads
from gendiff.files import get_file_extention, read_data_from_file
from yaml import safe_load


def get_data_from(file_name: str, read_func):
    with open(file_name, mode='r', encoding='utf-8') as file:
        data = read_func(file)
    return data


def get_data_from_file(file_name: str) -> dict | None:
    EXT_TO_FORMAT = {
        'json': 'json',
        'yaml': 'yaml',
        'yml': 'yaml'
    }
    ext = get_file_extention(file_name).lower()
    if ext not in EXT_TO_FORMAT:
        return None
    format = EXT_TO_FORMAT[ext]
    data_str = read_data_from_file(file_name)
    return parse(data_str, format)


def parse(data: str, format: str) -> dict | None:
    loaders = {
        'json': loads,
        'yaml': safe_load
    }

    if format in loaders:
        return loaders[format](data)
    return None
