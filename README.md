# line-repeater

A simple CLI tool that repeats lines in a file **in-place**.

## Installation

### Using pip

```bash
pip install line-repeater
```

### Standalone executable

Download the latest `.exe` from the [Releases](https://github.com/cqveman/line-repeater/releases) page. _No Python
installation required._

---

## CLI Usage

```bash
lr <file> <repeat_n_times> [OPTIONS]
```

### Arguments

| Argument         | Description                        |
|------------------|------------------------------------|
| `file`           | Path to the file to modify         |
| `repeat_n_times` | How many times to repeat each line |

### Options

| Option        | Short | Description                                | Default |
|---------------|-------|--------------------------------------------|---------|
| `--till-line` | `-tl` | Repeat blocks of N lines at a time         | `1`     |
| `--block-sep` | `-bs` | Separator between each repeated block      | `\n`    |
| `--line-sep`  | `-ls` | Separator inserted between each repetition | `None`  |

### Examples

Repeat every line 3 times:

```bash
lr file.txt 3
```

Repeat every line 3 times, separated by `---`:

```bash
lr file.txt 3 --block-sep "---"
```

Repeat blocks of 2 lines, 4 times each:

```bash
lr file.txt 4 --till-line 2
```

---

## API

You can also use `repeater()` directly in your code.

```python
from line_repeater import repeater

repeater(file, repeat_n_times, till_line, block_line_sep, line_sep)
```

### Parameters

| Parameter        | Type          | Description                                | Default |
|------------------|---------------|--------------------------------------------|---------|
| `file`           | `TextIO`      | An open file object in `r+` mode           | _       |
| `repeat_n_times` | `int`         | How many times to repeat each line/block   | _       |
| `till_line`      | `int`         | Repeat blocks of N lines at a time         | `1`     |
| `block_line_sep` | `str`         | Separator between each repeated block      | `"\n"`  |
| `line_sep`       | `str \| None` | Separator inserted between each repetition | `None`  |

### Example

```python
from line_repeater import repeater

with open("file.txt", "r+") as f:
    repeater(
        file=f,
        repeat_n_times=3,
        till_line=1,
        block_line_sep="\n",
        line_sep="---",
    )
```

> **Note:** `repeater()` modifies the file **in-place**. Make sure to open it in `r+` mode. Raises `ValueError` if
`till_line` exceeds the number of lines.

---

## License

MIT
