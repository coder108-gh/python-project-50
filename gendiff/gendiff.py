#!usr/bin/env python3
import argparse
from gendiff.parse_data import get_diff_data


def parse_command_line():

    parser = argparse.ArgumentParser(description='Compares two configuration\
        files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()

    return {
        'first_file': args.first_file,
        'second_file': args.second_file,
        'format': args.format
    }


def gen_result2(diff: dict, file_path1: str, file_path2: str) -> str:
    sorted_key = sorted(diff)
    elements = [f'gendiff {file_path1} {file_path2}', '{']

    INDENT_STR, SIGN_POS, SIGN_ADD, SIGN_REMOVE = "  ", "  ", "+ ", "- "

    for key in sorted_key:
        first, second = diff[key]
        if first == second:
            elements.append(f'{INDENT_STR}{SIGN_POS}{key}: {first}')
        else:
            if not isinstance(first, tuple):
                elements.append(f'{INDENT_STR}{SIGN_REMOVE}{key}: {first}')
            if not isinstance(second, tuple):
                elements.append(f'{INDENT_STR}{SIGN_ADD}{key}: {second}')
    elements.append('}')
    return '\n'.join(elements)


def gen_result(diff: dict, file_path1: str, file_path2: str) -> str:
    INDENT, SIGN_POS, SIGN_ADD, SIGN_REMOVE = "  ", "  ", "+ ", "- "
    elements = [f'gendiff {file_path1} {file_path2}']

    def add_node(node: dict, indent: int, prefix='', old_shift='') -> None:
        def add_pair(shift, sign, key, value):
            if isinstance(value, dict):
                add_node(value, indent + 1, f'{shift}{sign}{key}: ', shift)
            else:
                if value is None:
                    value = 'null'
                elements.append(f'{shift}{sign}{key}: {value}')

        elements.append(prefix + '{')
        shift = INDENT * indent + SIGN_POS * (indent - 1)
        keys = sorted(node)
        for key in keys:
            value = node[key]
            if isinstance(value, list):
                first, second = value
                if first == second:
                    add_pair(shift, SIGN_POS, key, first)
                else:
                    if not isinstance(first, tuple):
                        add_pair(shift, SIGN_REMOVE, key, first)
                    if not isinstance(second, tuple):
                        add_pair(shift, SIGN_ADD, key, second)

            elif isinstance(value, dict):
                add_node(value, indent + 1, f'{shift}{SIGN_POS}{key}: ', shift)
            else:
                add_pair(shift, SIGN_POS, key, value)

        if len(prefix) == 0:
            elements.append('}')
        else:
            elements.append(f'{old_shift}{SIGN_POS}' + '}')

    add_node(diff, 1)
    print(diff)
    return '\n'.join(elements)


def generate_diff(file_path1: str, file_path2: str) -> str:
    diff = get_diff_data(file_path1, file_path2)
    return gen_result(diff, file_path1, file_path2)


def main_diff():
    arg_data = parse_command_line()
    print(arg_data)
    result = generate_diff(arg_data['first_file'], arg_data['second_file'])
    print(result)
