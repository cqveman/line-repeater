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
    root.rowconfigure((0, 2), weight=0)
    root.rowconfigure(1, weight=1)

    # Parameters

    params_frame = tb.Frame(root)
    params_frame.grid(row=0, column=0, padx=16, pady=(16, 8), sticky='ew')

    params_frame.columnconfigure(1, weight=1)
    params_frame.columnconfigure(3, weight=1)

    tb.Label(params_frame, text="Repeat N times").grid(row=0, column=0, padx=(0, 4), sticky='w')
    repeat_n_entry = tb.Entry(params_frame)
    repeat_n_entry.grid(row=0, column=1, padx=(0, 16), sticky='ew')

    tb.Label(params_frame, text="Till line").grid(row=0, column=2, padx=(0, 4), sticky='w')
    till_line_entry = tb.Entry(params_frame)
    till_line_entry.grid(row=0, column=3, sticky='ew')

    tb.Label(params_frame, text="Block separator").grid(row=1, column=0, padx=(0, 4), pady=(6, 0), sticky='w')
    block_sep_entry = tb.Entry(params_frame)
    block_sep_entry.grid(row=1, column=1, padx=(0, 16), pady=(6, 0), sticky='ew')

    tb.Label(params_frame, text="Line separator").grid(row=1, column=2, padx=(0, 4), pady=(6, 0), sticky='w')
    line_sep_entry = tb.Entry(params_frame)
    line_sep_entry.grid(row=1, column=3, pady=(6, 0), sticky='ew')

    # Textbox

    text_frame = tb.Frame(root)
    text_frame.grid(row=1, column=0, padx=16, pady=0, sticky='nsew')
    text_frame.columnconfigure(0, weight=1)
    text_frame.rowconfigure(0, weight=1)

    textbox = tb.Text(text_frame, wrap='none')
    textbox.grid(row=0, column=0, sticky='nsew')

    y_scroll = tb.Scrollbar(text_frame, orient='vertical', command=textbox.yview)
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
