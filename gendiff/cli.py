import argparse


def parse_args():

    parser = argparse.ArgumentParser(description='Compares two configuration\
        files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f',
        '--format',
        help='set format of output: stylish|plain|json',
        default='stylish'
    )

    args = parser.parse_args()

    return {
        'first_file': args.first_file,
        'second_file': args.second_file,
        'format': args.format
    }
