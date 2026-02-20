import sys

import typer
from typing import Annotated

app = typer.Typer()


@app.command('lr')
def line_repeater(
        file: Annotated[typer.FileText, typer.Argument(
            help='The file to apply repetitions.',
            mode='r+',
        )],
        repeat_n_times: Annotated[int, typer.Argument(
            help='The number of repetitions.',
        )],
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

    for l in file:
        # Skip blank lines
        if not l.strip():
            continue

        # Add '\n' to the end of a line
        if not l.endswith('\n'):
            l = l + '\n'

        for _ in range(1, repeat_n_times + 1):
            _list.append(l)
            if line_sep is not None and _ < repeat_n_times:
                _list.append(f'{line_sep}\n')

        # If a separator is not provided then separate using a blank line
        _list.append(block_line_sep if block_line_sep == '\n' else f'{block_line_sep}\n')

    # Removes the last line separator at EOF
    try:
        _list.pop()
    except IndexError:
        print('File is empty!')
        sys.exit(-1)

    file.seek(0)
    file.truncate()
    file.writelines(_list)

    print(f'Successfully repeated each line {repeat_n_times} times.')

if __name__ == "__main__":
    app()