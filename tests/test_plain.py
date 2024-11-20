from gendiff import generate_diff


def test_plain():
    RESULT_FILE = 'tests/fixtures/result.txt'
    FIRST_FILE = "tests/fixtures/file1.json"
    SECOND_FILE = "tests/fixtures/file2.json"

    with open(RESULT_FILE, mode='r', encoding='utf-8') as txt:
        data = ''.join((txt.readlines()))
    
    assert generate_diff(FIRST_FILE, SECOND_FILE) == data

