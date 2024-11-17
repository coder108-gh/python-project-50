#!usr/bin/env python3
import argparse
import json


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


def get_data_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    return data


def gen_result(diff: dict, file_path1, file_path2) -> str:
    sorted_key = sorted(diff)
    elements = [f'gendiff {file_path1} {file_path2}', '{']
    indent, sign_p, sign_add, sign_remove = "  ", "  ", "+ ", "- "
    for key in sorted_key:
        first, second = diff[key]
        if first == second:
            elements.append(f'{indent}{sign_p}{key}: {first}')
        else:
            if not isinstance(first, tuple):
                elements.append(f'{indent}{sign_remove}{key}: {first}')
            if not isinstance(second, tuple):
                elements.append(f'{indent}{sign_add}{key}: {second}')
    elements.append('}')
    return '\n'.join(elements)


def get_diff_data(file_path1: str, file_path2: str) -> dict:
    first = get_data_from_json(file_path1)
    second = get_data_from_json(file_path2)
    diff = {}
    diff.update(list(map(lambda x: (x[0], [x[1]]), first.items())))
    list(
        map(lambda x: diff[x[0]].append(x[1])
            if diff.get(x[0], None) is not None
            else diff.update([(x[0], [(), x[1]])]),
            second.items())
    )
    list(map(lambda x: x[1].append(())
             if len(x[1]) < 2 else None,
             diff.items()))

    return diff


def generate_diff(file_path1: str, file_path2: str) -> dict:
    diff = get_diff_data(file_path1, file_path2)
    return gen_result(diff, file_path1, file_path2)


def main_diff():
    arg_data = parse_command_line()
    result = generate_diff(arg_data['first_file'], arg_data['second_file'])
    print(result)
