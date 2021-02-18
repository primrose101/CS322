from tkinter import *
from Interpreter import check_completion


def handle_run_click():
    lines = text_editor.get("1.0", "end-1c").split('\n')
    state = check_completion(lines)
    message = 'Code is complete' if state else 'Code has errors'
    console.config(state=NORMAL)
    console.delete('1.0', END)
    console.insert(END, message)
    console.config(state=DISABLED)


root = Tk()

# UI components
text_editor = Text(root, width=80, height=50, bg="#ffffff", fg="#000000", bd=-3, insertbackground="#111111")
console = Text(root, width=60, height=50, bd=-3, fg="#ffffff")
frame = Frame(root, height=50, width=140)
run_button = Button(frame, text="RUN", bg="#78AB46", fg="#ffffff", command=handle_run_click)
line_numbers = Text(width=5, height=50, bg="#d3d3d3", bd=-3, fg="#111111")

# UI States
console.config(state=DISABLED)
line_numbers.tag_configure("center", justify="center")
root.resizable(0, 0)

# UI Positions
text_editor.grid(row=0, column=1)
console.grid(row=0, column=2)
root.title("CFPL Interpreter")
line_numbers.grid(row=0, column=0)
frame.grid(row=1, column=2, ipady=20)
run_button.pack(side=RIGHT, anchor='e')


def update_lines(count):
    line_numbers.config(state=NORMAL)
    line_numbers.delete('1.0', END)
    for i in range(1, count+1):
        line_numbers.insert(END, f'  {i}\n')
    line_numbers.config(state=DISABLED)


def get_line_count_bs(event):
    text = text_editor.get("1.0", "end-1c")
    count = len(text.split("\n"))
    if text and text[-1] == "\n":
        count -= 1
    update_lines(count)


def get_line_count(event):
    text = text_editor.get("1.0", "end-1c")
    count = len(text.split("\n"))
    update_lines(count)


def get_line_count_enter(event):
    count = text_editor.get("1.0", "end-1c").count("\n")+2
    update_lines(count)


# Binds
text_editor.bind("<Key>", get_line_count)
text_editor.bind("<Button>", get_line_count)
text_editor.bind("<Return>", get_line_count_enter)
text_editor.bind("<BackSpace>", get_line_count_bs)

root.mainloop()
