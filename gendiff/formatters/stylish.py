#!usr/bin/env python3

INDENT, SIGN_PLACE, SIGN_ADD, SIGN_REMOVE = "  ", "  ", "+ ", "- "

def stylish(diff: dict, file_path1: str, file_path2: str) -> str: # noqa C901

    elements = [f'gendiff {file_path1} {file_path2}']

    def add_node(node: dict, indent: int, prefix='', old_shift='') -> None:
        def add_pair(shift, sign, key, value):
            if isinstance(value, dict):
                add_node(value, indent + 1, f'{shift}{sign}{key}: ', shift)
            else:
                if value is None:
                    value = 'null'
                elements.append(f'{shift}{sign}{key}: {value}')

        elements.append(prefix + '{')
        shift = INDENT * indent + SIGN_PLACE * (indent - 1)
        keys = sorted(node)
        for key in keys:

            value = node[key]
            if isinstance(value, list):
                first, second = value
                if first == second:
                    add_pair(shift, SIGN_PLACE, key, first)
                else:
                    if not isinstance(first, tuple):
                        add_pair(shift, SIGN_REMOVE, key, first)
                    if not isinstance(second, tuple):
                        add_pair(shift, SIGN_ADD, key, second)

            elif isinstance(value, dict):
                add_node(
                    value,
                    indent + 1,
                    f'{shift}{SIGN_PLACE}{key}: ',
                    shift
                )
            else:
                add_pair(shift, SIGN_PLACE, key, value)

        if len(prefix) == 0:
            elements.append('}')
        else:
            elements.append(f'{old_shift}{SIGN_PLACE}' + '}')

    add_node(diff, 1)
    return '\n'.join(elements)
