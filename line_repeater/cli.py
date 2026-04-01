import typer
from typing import Annotated

from line_repeater.repeater import repeat_lines

app = typer.Typer(add_completion=False)


@app.command()
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
    try:
        repeat_lines(file, repeat_n_times, till_line, block_line_sep, line_sep)
    except (ValueError, IndexError) as e:
        typer.echo(str(e), err=True)
        raise typer.Exit(code=1)

    print(f'Successfully finished repeating.')
