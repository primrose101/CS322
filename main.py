from tkinter import Tk
from Editor import Editor

if __name__ == "__main__":
    root = Tk()
    root.title("CFPL Interpreter")
    editor = Editor(root)
    root.resizable(0, 0)
    root.mainloop()
