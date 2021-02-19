# UI for CIT-U's First Programming Language

from tkinter import (Text, Frame, Button, RIGHT, DISABLED, NORMAL, END)
from Interpreter import interpret


class Editor:

    line_count = 1

    def __init__(self, master):
        self.master = master

        self.text_editor = Text(master, width=70, height=30, bg="#ffffff",
                                fg="#000000", bd=-3, insertbackground="#111111")
        self.text_editor.grid(row=0, column=1)

        self.console = Text(master, width=50, height=30, bd=-3, fg="#ffffff")
        self.console.grid(row=0, column=2)
        self.console.config(state=DISABLED)

        self.frame = Frame(master, height=50, width=140)
        self.frame.grid(row=1, column=2, ipady=20)

        self.run_button = Button(self.frame, text="RUN", bg="#78AB46", fg="#ffffff", command=self.run)
        self.run_button.pack(side=RIGHT, anchor='e')

        self.line_numbers = Text(width=5, height=30, bg="#d3d3d3", bd=-3, fg="#111111")
        self.line_numbers.tag_configure("center", justify="center")
        self.line_numbers.grid(row=0, column=0)

        self.text_editor.bind("<Key>", self.get_line_count)
        self.text_editor.bind("<Button>", self.get_line_count)
        self.text_editor.bind("<Return>", self.get_line_count_enter)
        self.text_editor.bind("<BackSpace>", self.get_line_count_bs)

        self.update_lines(self.line_count)

    def get_text(self):
        text = self.text_editor.get("1.0", "end-1c")
        self.line_count = len(text.split("\n"))  # updates line_count every time text is get
        return self.text_editor.get("1.0", "end-1c")

    def get_line_count_bs(self, event):
        text = self.get_text()
        count = self.line_count
        if text and text[-1] == "\n":
            count -= 1
        self.update_lines(count)

    def get_line_count(self, event):
        self.get_text()
        self.update_lines(self.line_count)

    def get_line_count_enter(self, event):
        self.get_text()
        self.update_lines(self.line_count+1)

    def update_lines(self, count=1):
        self.line_numbers.config(state=NORMAL)
        self.line_numbers.delete('1.0', END)
        for i in range(1, count+1):
            self.line_numbers.insert(END, f'  {i}\n')
        self.line_numbers.config(state=DISABLED)

    def run(self):
        self.console.config(state=NORMAL)
        code = self.get_text()
        message = interpret(code)
        self.console.delete('1.0', END)
        self.console.insert(END, message)
        self.console.config(state=DISABLED)
