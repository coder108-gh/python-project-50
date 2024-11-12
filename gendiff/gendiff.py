#!usr/bin/env python3
import argparse
import json

def parse_command_line():

    parser = argparse.ArgumentParser(description='Compares two configuration files \
        and shows a difference.')
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


def main_diff():

    arg_data = parse_command_line()
    first = get_data_from_json(arg_data['first_file'])
    second = get_data_from_json(arg_data['second_file'])
