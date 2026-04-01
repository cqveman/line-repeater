# line-repeater

A simple CLI tool that repeats lines in a file **in-place**.

## Installation

```bash
pip install line-repeater
```

## Usage

```bash
lr <file> <repeat_n_times> [OPTIONS]
```

### Arguments

| Argument | Description |
|---|---|
| `file` | Path to the file to modify |
| `repeat_n_times` | How many times to repeat each line |

### Options

| Option | Short | Description | Default |
|---|---|---|---|
| `--till-line` | `-tl` | Repeat blocks of N lines at a time | `1` |
| `--block-sep` | `-bs` | Separator between each repeated block | `\n` |
| `--line-sep` | `-ls` | Separator inserted between each repetition | `None` |

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

## License

MIT