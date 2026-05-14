import io
from line_repeater._core.repeater import repeater


def gui():
    import ttkbootstrap as tb
    from tkinter import messagebox

    root = tb.Window(themename='superhero')
    root.title("Line Repeater")
    root.geometry("900x650")
    root.resizable(False, False)
    root.place_window_center()

    root.columnconfigure(0, weight=1)
    root.rowconfigure((0, 1), weight=1)

    # Parameters

    params_frame = tb.Frame(root)
    params_frame.grid(row=0, column=0, padx=16, pady=(16, 8), sticky='ew')

    tb.Label(params_frame, text="Repeat N times").grid(row=0, column=0, padx=(0, 4), sticky='w')
    repeat_n_entry = tb.Entry(params_frame, width=8)
    repeat_n_entry.grid(row=0, column=1, padx=(0, 16))

    tb.Label(params_frame, text="Till line").grid(row=0, column=2, padx=(0, 4), sticky='w')
    till_line_entry = tb.Entry(params_frame, width=8)
    till_line_entry.grid(row=0, column=3, padx=(0, 16))

    tb.Label(params_frame, text="Block separator").grid(row=0, column=4, padx=(0, 4), sticky='w')
    block_sep_entry = tb.Entry(params_frame, width=14)
    block_sep_entry.grid(row=0, column=5, padx=(0, 16))

    tb.Label(params_frame, text="Line separator").grid(row=0, column=6, padx=(0, 4), sticky='w')
    line_sep_entry = tb.Entry(params_frame, width=14)
    line_sep_entry.grid(row=0, column=7)

    # Textbox

    text_frame = tb.Frame(root)
    text_frame.grid(row=1, column=0, padx=16, pady=0, sticky='nsew')
    text_frame.columnconfigure(0, weight=1)
    text_frame.rowconfigure(0, weight=1)

    textbox = tb.Text(text_frame, wrap='none')
    textbox.grid(row=0, column=0, sticky='nsew')

    y_scroll = tb.Scrollbar(text_frame, orient='vertical', command=textbox.yview())
    y_scroll.grid(row=0, column=1, sticky='ns')
    x_scroll = tb.Scrollbar(text_frame, orient='horizontal', command=textbox.xview)
    x_scroll.grid(row=1, column=0, sticky='ew')

    textbox.configure(yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    def run():
        try:
            repeat_n = int(repeat_n_entry.get())
        except ValueError:
            messagebox.showerror("Error", "'Repeat N times must be an integer.")
            return

        till = till_line_entry.get() or 1
        block_sep = block_sep_entry.get() or '\n'
        line_sep = line_sep_entry.get() or None

        content = textbox.get("1.0", "end-1c")

        try:
            buf = io.StringIO(content)
            repeater(buf, repeat_n, till, block_sep, line_sep)
            result = buf.getvalue()
        except (ValueError, IndexError) as e:
            messagebox.showerror("Error", str(e))
            return

        textbox.delete("1.0", 'end-1c')
        textbox.insert("1.0", result)

    tb.Button(root, text="Run", command=run, bootstyle='primary') \
        .grid(row=2, column=0, padx=16, pady=(8, 16), sticky='ew')

    root.mainloop()


if __name__ == "__main__":
    gui()
