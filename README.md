# line-repeater

A utility for repeating lines, or blocks of lines. Available as a CLI tool, a desktop GUI, and a Python package.


## Features

- Repeat each line (or a block of N lines) a configurable number of times
- Insert a custom separator between each repetition of a line (`--line-sep`)
- Insert a custom separator between each repeated block (`--block-sep`)
- Three interfaces: CLI, GUI, and importable Python package
- Handles edge cases: skips blank lines, strips trailing whitespace inconsistencies, validates input bounds


## Installation

You can either get the pip package for CLI use. Or download the GUI app.

### Standalone Executable

Download the latest .exe from the [Releases](https://github.com/cqveman/line-repeater/releases) page. _No Python installation required_.

### Using pip 

```bash
pip install line-repeater
```


## Usage

### GUI

1. Launch `line-repeater.exe`.
2. Paste (or type) your text into the text box, fill in the parameters, and click Run. The result replaces the content in the text box in place.

**Parameters:**
 
| Field           | Description                                            | Default |
|-----------------|--------------------------------------------------------|---------|
| Repeat N times  | How many times to repeat each line/block               | —       |
| Till line       | Size of each block of lines to repeat together         | `1`     |
| Block separator | String inserted between each repeated block            | `\n`    |
| Line separator  | String inserted between each repetition within a block | None    |

### CLI

```bash
lr <file> <repeat_n_times> [OPTIONS]
```
 
**Arguments:**

| Argument         | Description                                  |
|------------------|----------------------------------------------|
| `file`           | Path to the file to modify (edited in place) |
| `repeat_n_times` | How many times to repeat each line or block  |
 
**Options:**
 
| Option        | Short | Description                                | Default |
|---------------|-------|--------------------------------------------|---------|
| `--till-line` | `-tl` | Repeat blocks of N lines at a time         | `1`     |
| `--block-sep` | `-bs` | Separator between each repeated block      | `\n`    |
| `--line-sep`  | `-ls` | Separator inserted between each repetition | None    |


**Examples:**
 
Repeat every line 3 times:
```bash
lr input.txt 3
```
 
Repeat every line 3 times, separated by a `---` divider:
```bash
lr input.txt 3 --line-sep "---"
```
 
Repeat blocks of 2 lines, 4 times each, with a `===` block separator:
```bash
lr input.txt 4 --till-line 2 --block-sep "==="
```

### API

The `repeater` function can be imported and used directly in your code.

```python
from line_repeater import repeater

with open("file.txt", "r+") as f:
    repeater(
        file=f,                 # File-like object opened in read+write mode
        repeat_n_times=3,       # int - how many times to repeat each line/block
        till_line=1,            # int - block size (number of lines per block)
        block_line_sep="\n",    # str - separator between blocks
        line_sep="---",         # str | None - separator between repetitions
    )
```

> **Note:** `repeater()` modifies the file **in-place**. Make sure to open it in `r+` mode.

**Exceptions:**
 
| Exception    | Condition                                           |
|--------------|-----------------------------------------------------|
| `ValueError` | File/buffer is empty                                |
| `ValueError` | `till_line` exceeds the number of lines in the file |


## License

MIT