import typer
from typing import Annotated

from line_repeater.repeater import repeater

app = typer.Typer(add_completion=False)


@app.command()
def line_repeater(
        file: Annotated[typer.FileText, typer.Argument(
            help='Path to the file to modify.',
            mode='r+',
        )],
        repeat_n_times: Annotated[int, typer.Argument(
            help='How many times to repeat each line.',
        )],
        till_line: Annotated[int, typer.Option(
            '--till-line', '-tl',
            help='Repeat blocks of N lines at a time. Default value is 1 (the first line).',
            show_default=False
        )] = 1,
        block_line_sep: Annotated[str, typer.Option(
            '--block-sep', '-bs',
            help='Separator between each repeated block. Default value is "\\n".',
            show_default=False
        )] = '\n',
        line_sep: Annotated[str | None, typer.Option(
            '--line-sep', '-ls',
            help='Separator inserted between each repetition. Default value is None.',
        )] = None
):
    try:
        repeater(file, repeat_n_times, till_line, block_line_sep, line_sep)
    except (ValueError, IndexError) as e:
        typer.echo(str(e), err=True)
        raise typer.Exit(code=1)

    print(f'Successfully finished repeating.')
