from line_repeater._utils import *


def repeater(file, repeat_n_times, till_line, block_line_sep, line_sep):
    _list = []
    lines = formatter(file.readlines())

    if len(lines) == 0:
        raise ValueError('File is empty.')

    if till_line > len(lines):

        raise ValueError('Too many lines to repeat.')

    elif 1 < till_line <= len(lines):

        for i in range(0, len(lines), till_line):
            for _ in range(1, repeat_n_times + 1):

                _list.append(lines[i:i + till_line])  # It counts each block of lines as ONE line/string
                # Repeats the line separator like this: LINE *sep* LINE *sep* LINE
                if line_sep is not None and _ < repeat_n_times:
                    _list.append(f'{line_sep}\n')

            add_block_sep(_list, block_line_sep)

    else:  # Repeat line by line

        for l in lines:
            for _ in range(1, repeat_n_times + 1):

                _list.append(l)
                # Repeats the line separator like this: LINE *sep* LINE *sep* LINE
                if line_sep is not None and _ < repeat_n_times:
                    _list.append(f'{line_sep}\n')

            add_block_sep(_list, block_line_sep)

    # Removes the last BLOCK LINE separator at EOF
    _list.pop()

    file.seek(0)
    file.truncate()
    file.writelines([line for line in flatten(_list)])
