from gendiff.files import get_data_from_file
import copy


def make_diff(a: dict, b1: dict) -> dict:
    diff = {}
    b = copy.deepcopy(b1)
    for key, value in a.items():
        if b.get(key, None) is None:
            diff[key] = [value, ()]
        elif isinstance(value, dict) and isinstance(b[key], dict):
            diff[key] = make_diff(value, b[key])
            b.pop(key)
        else:
            diff[key] = [value, b[key]]
            b.pop(key)

    for key, value in b.items():
        diff[key] = [(), value]

    return diff


def get_diff_data(file_path1: str, file_path2: str) -> dict:
    first = get_data_from_file(file_path1)
    second = get_data_from_file(file_path2)

    diff = make_diff(first, second)

    # put_data_from_dict(diff, first, 0)
    # put_data_from_dict(diff, second, 1)

    # diff.update(list(map(lambda x: (x[0], [x[1]]), first.items())))
    # list(
    #     map(lambda x: diff[x[0]].append(x[1])
    #         if diff.get(x[0], None) is not None
    #         else diff.update([(x[0], [(), x[1]])]),
    #         second.items())
    # )
    # list(map(lambda x: x[1].append(())
    #          if len(x[1]) < 2 else None,
    #          diff.items()))

    return diff
