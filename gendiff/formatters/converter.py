def get_value_repr(value) -> str:
    if value is None:
        return 'null'
    if isinstance(value, bool) and value:
        return 'true'
    if isinstance(value, bool) and not value:
        return 'false'
    return value


def for_plain(func):
    def repres(value):
        if isinstance(value, dict):
            return '[complex value]'
        if isinstance(value, str):
            return f"'{value}'"
        return func(value)
    return repres


@for_plain
def get_value_repr_plain(value):
    return get_value_repr(value)
