from gendiff.parse_data import make_diff
from gendiff.gendiff import gen_result
from gendiff import generate_diff

t1 = {
    "one": "two",
    "three": "four",
    "five": {
        "seven": 0,
        "nine": True
    },
    "five1": {
        "seven": 0,
        "nine": {"a": "b", "c": 1},
        "71": {"a": 5, "b": 2, "c": 7},
        "72": {"a": 7, "b": 7, "c": 7}
    },
    "7": 8
}


t2 = {
    "one": "two",
    "three": "four1",
    "five": {
        "seven": 0,
        "nine1": {"a": 1, "b": 2}
    },
    "five1": {
        "seven": 0,
        "71": {"a": 1, "b": 2, "c": 3, "d": 1},
        "72": {"a": 7, "b": 7, "c": 7}
    },
    "7": 8,
    "h": "b2",
    "g1": {
        "alpha": "betta",
        "123": None
    }
}

t1_t2 = {
    "one": ["two", "two"],
    "three": ["four", "four1"],
    "five": {
        "seven": [0, 0],
        "nine": [True, ()],
        "nine1": [(), {"a": 1, "b": 2}]
    },
    "five1": {
        "seven": [0, 0],
        "nine": [{"a": "b", "c": 1}, ()],
        "71": {"a": [5, 1], "b": [2, 2], "c": [7, 3], "d": [(), 1]},
        "72": {"a": [7, 7], "b": [7, 7], "c": [7, 7]}
    },
    "7": [8, 8],
    "h": [(), "b2"],
    "g1": [(), {"alpha": "betta", "123": None}]
}

t1_empty = {
    "one": ["two", ()],
    "three": ["four", ()],
    "five": [{
        "seven": 0,
        "nine": True
    }, ()],
    "five1": [{
        "seven": 0,
        "nine": {"a": "b", "c": 1},
        "71": {"a": 5, "b": 2, "c": 7},
        "72": {"a": 7, "b": 7, "c": 7}
    }, ()],
    "7": [8, ()]
}

t1_t2_str = '''gendiff 1 2
{
    7: 8
    five: {
      - nine: True
      + nine1: {
            a: 1
            b: 2
        }
        seven: 0
    }
    five1: {
        71: {
          - a: 5
          + a: 1
            b: 2
          - c: 7
          + c: 3
          + d: 1
        }
        72: {
            a: 7
            b: 7
            c: 7
        }
      - nine: {
            a: b
            c: 1
        }
        seven: 0
    }
  + g1: {
        123: null
        alpha: betta
    }
  + h: b2
    one: two
  - three: four
  + three: four1
}'''


def test_diff_empty():
    t = make_diff(t1, {})
    assert t == t1_empty


def test_diff_t12():
    t = make_diff(t1, t2)
    assert t == t1_t2


def test_diff_str():
    t = make_diff(t1, t2)
    t_str = gen_result(t, '1', '2')
    print(t_str)
    assert t_str == t1_t2_str


def test_tree_json():
    RESULT_FILE = 'tests/fixtures/result_tree_json.txt'
    FIRST_FILE = "tests/fixtures/tree_file1.json"
    SECOND_FILE = "tests/fixtures/tree_file2.json"

    with open(RESULT_FILE, mode='r', encoding='utf-8') as txt:
        data = ''.join((txt.readlines()))

    assert generate_diff(FIRST_FILE, SECOND_FILE) == data