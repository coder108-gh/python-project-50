from .converter import get_value_repr_plain as get_value_repr


def get_new_prefix(prefix: str, key: str) -> str:
    if prefix == '':
        return f'{key}.'
    return f'{prefix}{key}.'


def output_same(key, value) -> str:
    return f"Property '{key}' has not changed the value: \
{get_value_repr(value)}"


def output_update(key, first, second) -> str:
    return f"Property '{key}' was updated. From \
{get_value_repr(first)} to {get_value_repr(second)}"


def output_removed(key) -> str:
    return f"Property '{key}' was removed"


def output_added(key, value) -> str:
    return f"Property '{key}' was added with value: {get_value_repr(value)}"


def plain(diff: dict, show_equal = False) -> str: # noqa C901

    elements = []

    def add_node(node: dict, prefix='') -> None:

        def add_string(key, first, second):
            if first == second:
                if show_equal:
                    elements.append(output_same(f'{prefix}{key}', first))
            elif isinstance(first, tuple):
                elements.append(output_added(f'{prefix}{key}', second))
            elif isinstance(second, tuple):
                elements.append(output_removed(f'{prefix}{key}'))
            else:
                elements.append(output_update(f'{prefix}{key}', first, second))

        keys = sorted(node)
        for key in keys:

            value = node[key]
            if isinstance(value, list):
                first, second = value
                add_string(key, first, second)
            elif isinstance(value, dict):
                add_node(value, get_new_prefix(prefix, key))
            else:
                pass

    add_node(diff, '')
    return '\n'.join(elements)
