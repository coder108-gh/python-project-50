#!usr/bin/env python3
from fixtures.fixrures import t1, t1_empty, t1_t2, t1_t2_plain, t1_t2_str, t2
from gendiff import generate_diff
from gendiff.gendiff import plain, stylish
from gendiff.gendiff import make_diff


def test_diff_empty():
    t = make_diff(t1, {})
    assert t == t1_empty


def test_diff_t12():
    t = make_diff(t1, t2)
    assert t == t1_t2


def test_diff_str():
    t = make_diff(t1, t2)
    t_str = stylish(t)
    assert t_str == t1_t2_str


def test_diff_str_plain():
    t = make_diff(t1, t2)
    t_str = plain(t)
    assert t_str == t1_t2_plain


def test_tree_json():
    RESULT_FILE = 'tests/fixtures/result_tree_json.txt'
    FIRST_FILE = "tests/fixtures/tree_file1.json"
    SECOND_FILE = "tests/fixtures/tree_file2.json"

    with open(RESULT_FILE, mode='r', encoding='utf-8') as txt:
        data = ''.join((txt.readlines()))

    assert generate_diff(FIRST_FILE, SECOND_FILE, 'stylish') == data


def test_tree_yaml():
    RESULT_FILE = 'tests/fixtures/result_tree_yaml.txt'
    FIRST_FILE = "tests/fixtures/tree_file1.yaml"
    SECOND_FILE = "tests/fixtures/tree_file2.yaml"

    with open(RESULT_FILE, mode='r', encoding='utf-8') as txt:
        data = ''.join((txt.readlines()))

    assert generate_diff(FIRST_FILE, SECOND_FILE, 'stylish') == data


def test_tree_mix():
    RESULT_FILE = 'tests/fixtures/result_tree_mix.txt'
    FIRST_FILE = "tests/fixtures/tree_file1.json"
    SECOND_FILE = "tests/fixtures/tree_file2.yaml"

    with open(RESULT_FILE, mode='r', encoding='utf-8') as txt:
        data = ''.join((txt.readlines()))

    assert generate_diff(FIRST_FILE, SECOND_FILE, 'stylish') == data


def test_tree_plain_json():
    RESULT_FILE = 'tests/fixtures/result_tree_plain_json.txt'
    FIRST_FILE = "tests/fixtures/tree_file1.json"
    SECOND_FILE = "tests/fixtures/tree_file2.json"

    with open(RESULT_FILE, mode='r', encoding='utf-8') as txt:
        data = ''.join((txt.readlines()))
    assert generate_diff(FIRST_FILE, SECOND_FILE, 'plain') == data


def test_tree_json_formatter():
    RESULT_FILE = 'tests/fixtures/result_tree_json_format.txt'
    FIRST_FILE = "tests/fixtures/tree_file1.json"
    SECOND_FILE = "tests/fixtures/tree_file2.json"

    with open(RESULT_FILE, mode='r', encoding='utf-8') as txt:
        data = ''.join((txt.readlines()))
    assert generate_diff(FIRST_FILE, SECOND_FILE, 'json') == data
