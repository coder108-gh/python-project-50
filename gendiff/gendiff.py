#!usr/bin/env python3
from gendiff.cli import parse_command_line
from gendiff.formatters.json_formatter import json_formatter
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.parse_data import get_diff_data


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


def main_diff():
    arg_data = parse_command_line()
    result = generate_diff(
        arg_data['first_file'],
        arg_data['second_file'],
        arg_data['format']
    )
    print(result)
