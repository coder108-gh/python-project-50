#!usr/bin/env python3
from gendiff.gendiff import generate_diff, parse_command_line


def main_diff():
    arg_data = parse_command_line()
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
