from os import path


def read_file(file_name: str):
    with open(file_name, mode='r', encoding='utf-8') as file:
        data = file.read()
    return data


def get_extension(file_name: str) -> str:
    parts = path.splitext(file_name)
    return parts[-1].replace('.', '')
