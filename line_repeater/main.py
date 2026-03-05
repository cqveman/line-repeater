import sys
from collections.abc import Iterable

import typer
from typing import Annotated

app = typer.Typer()


def formatter(lines: list) -> list:
    _list = []
    for l in lines:
        # Skip blank lines
        if not l.strip():
            continue

        # Add '\n' to the end of a line
        if not l.endswith('\n'):
            l = l + '\n'

        _list.append(l)

    return _list


def flatten(_list):
    for s in _list:
        if isinstance(s, Iterable) and not isinstance(s, (str, bytes)):
            yield from flatten(s)
        else:
            yield s


def add_block_sep(_list, block_line_sep):
    # If a separator is not provided then separate using a blank line
    _list.append(block_line_sep if block_line_sep == '\n' else f'{block_line_sep}\n')


@app.command('lr')
def line_repeater(
        file: Annotated[typer.FileText, typer.Argument(
            help='The file to apply repetitions.',
            mode='r+',
        )],
        repeat_n_times: Annotated[int, typer.Argument(
            help='The number of repetitions.',
        )],
        till_line: Annotated[int, typer.Option(
            '--till-line', '-tl',
            help='Repeats till the Nth line specified. Default value is the 1 (the first line).',
            show_default=False
        )] = 1,
        block_line_sep: Annotated[str, typer.Option(
            '--block-sep', '-bs',
            help='Separates each block of lines. Default value is "\\n".',
            show_default=False
        )] = '\n',
        line_sep: Annotated[str | None, typer.Option(
            '--line-sep', '-ls',
            help='Separates each line with the next one. Default value is None.',
        )] = None
):
    _list = []
    lines = formatter(file.readlines())

    if till_line > len(lines):
        print(f'Too many lines to repeat! The file only has {len(lines)} lines')
        sys.exit(-1)

    elif 1 < till_line <= len(lines):
        for i in range(0, len(lines), till_line):
            for _ in range(1, repeat_n_times + 1):
                _list.append(lines[i:i + till_line])
                # Repeats the line separator like this: LINE *sep* LINE *sep* LINE
                if line_sep is not None and _ < repeat_n_times:
                    _list.append(f'{line_sep}\n')
            add_block_sep(_list, block_line_sep)

    else:
        for l in lines:
            for _ in range(1, repeat_n_times + 1):
                _list.append(l)
                # Repeats the line separator like this: LINE *sep* LINE *sep* LINE
                if line_sep is not None and _ < repeat_n_times:
                    _list.append(f'{line_sep}\n')
            add_block_sep(_list, block_line_sep)

    # Removes the last line separator at EOF
    try:
        _list.pop()
    except IndexError:
        print('File is empty!')
        sys.exit(-1)

    file.seek(0)
    file.truncate()
    file.writelines([line for line in flatten(_list)])

    print(f'Successfully finished repeating.')


if __name__ == "__main__":
    app()
