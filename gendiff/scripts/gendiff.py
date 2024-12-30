#!usr/bin/env python3
from gendiff.cli import parse_args
from gendiff.gendiff import generate_diff


def main_diff():
    arg_data = parse_args()
    result = generate_diff(
        arg_data['first_file'],
        arg_data['second_file'],
        arg_data['format']
    )
    print(result)


def main():
    main_diff()


if __name__ == '__main__':
    main()
