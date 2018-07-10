"""
Example program (exercise) for GUI in Python
"""
from tkinter import *

def foo():
    print("Welcome to the best project in Capstone Expo")

# Set the window title and size
root = Tk()
root.title("Vector Signal Generator (Beta)")
root.geometry("1280x720")
root.resizable(True, True)

# Add main menu and its sub-menus to the root
main_menu = Menu(root)
root.config(menu=main_menu)
file_menu = Menu(main_menu, tearoff=False)
instrument_menu = Menu(main_menu, tearoff=False)
file_menu.add_command(label="New Project", command=foo)
file_menu.add_command(label="Save", command=foo)
file_menu.add_command(label="Save As...", command=foo)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)
instrument_menu.add_command(label="Add Instrument", command=foo)
instrument_menu.add_command(label="Find Instrument", command=foo)
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Instrument", menu=instrument_menu)

# Add toolbar to the root
toolbar = Frame(root, bg="blue")
btn_insert = Button(toolbar, text="Insert Something", command=foo)
btn_insert.pack(side=LEFT, padx=5, pady=5)
btn_print = Button(toolbar, text="Print", command=foo)
btn_print.pack(side=LEFT, padx=5, pady=5)
toolbar.pack(side=TOP, fill=X)

root.mainloop()