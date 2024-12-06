from gendiff import generate_diff


def test_plain_json():
    RESULT_FILE = 'tests/fixtures/result_plain_json.txt'
    FIRST_FILE = "tests/fixtures/file1.json"
    SECOND_FILE = "tests/fixtures/file2.json"

    with open(RESULT_FILE, mode='r', encoding='utf-8') as txt:
        data = ''.join((txt.readlines()))

    assert generate_diff(FIRST_FILE, SECOND_FILE) == data


def test_plain_yaml():
    RESULT_FILE = 'tests/fixtures/result_plain_yaml.txt'
    FIRST_FILE = "tests/fixtures/file1.yaml"
    SECOND_FILE = "tests/fixtures/file2.yaml"

    with open(RESULT_FILE, mode='r', encoding='utf-8') as txt:
        data = ''.join((txt.readlines()))

    assert generate_diff(FIRST_FILE, SECOND_FILE) == data


def test_plain_mix():
    RESULT_FILE = 'tests/fixtures/result_plain_mix.txt'
    FIRST_FILE = "tests/fixtures/file1.json"
    SECOND_FILE = "tests/fixtures/file2.yaml"

    with open(RESULT_FILE, mode='r', encoding='utf-8') as txt:
        data = ''.join((txt.readlines()))

    assert generate_diff(FIRST_FILE, SECOND_FILE) == data
