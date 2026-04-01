from collections.abc import Iterable


def formatter(lines: list) -> list:
    res = []

    for l in lines:
        # Skip blank lines
        if not l.strip():
            continue

        # Add '\n' to the end of a line
        if not l.endswith('\n'):
            l = l + '\n'

        res.append(l)

    return res


def add_block_sep(_list, block_line_sep):
    # If a separator is not provided then separate using a blank line
    _list.append(block_line_sep if block_line_sep == '\n' else f'{block_line_sep}\n')


def flatten(_list):
    # https://stackoverflow.com/a/2158532/18910884
    for s in _list:
        if isinstance(s, Iterable) and not isinstance(s, (str, bytes)):
            yield from flatten(s)
        else:
            yield s
