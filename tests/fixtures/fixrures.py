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

t1_t2_plain = """gendiff --format plain 1 2
Property 'five.nine' was removed
Property 'five.nine1' was added with value: [complex value]
Property 'five1.71.a' was updated. From 5 to 1
Property 'five1.71.c' was updated. From 7 to 3
Property 'five1.71.d' was added with value: 1
Property 'five1.nine' was removed
Property 'g1' was added with value: [complex value]
Property 'h' was added with value: 'b2'
Property 'three' was updated. From 'four' to 'four1'"""
