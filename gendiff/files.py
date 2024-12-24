from os import path


def get_file_extention(file_name: str) -> str:
    parts = path.splitext(file_name)
    return parts[-1].replace('.', '')


def read_data_from_file(file_name: str):
    with open(file_name, mode='r', encoding='utf-8') as file:
        data = file.read()
    return data
