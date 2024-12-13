#!usr/bin/env python3
import argparse
from gendiff.parse_data import get_diff_data
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


def parse_command_line():

    parser = argparse.ArgumentParser(description='Compares two configuration\
        files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output',
        default='stylish'
    )

    args = parser.parse_args()

    return {
        'first_file': args.first_file,
        'second_file': args.second_file,
        'format': args.format
    }


def generate_diff(file_path1: str, file_path2: str, format_name='stylish'):
    diff = get_diff_data(file_path1, file_path2)
    formatters = {
        'stylish': stylish,
        'plain': plain
    }
    if format_name in formatters:
        return formatters[format_name](diff, file_path1, file_path2)
    return f'{format_name} - unknown formatter'


def main_diff():
    arg_data = parse_command_line()
    result = generate_diff(
        arg_data['first_file'],
        arg_data['second_file'],
        arg_data['format']
    )
    print(result)
