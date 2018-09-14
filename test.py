import tkinter as tk
from tkinter import ttk
import os

root = tk.Tk()

top_frame = ttk.Frame(root)
logo = tk.PhotoImage(file=os.path.join(os.path.dirname(__file__), "img", "dance.gif"))
logo = logo.subsample(2)    # Shrink the size by half
label_logo = tk.Label(top_frame, image=logo)
label_logo.image = logo     # Keep a reference so the image exists throughout the lifecycle
instr_to_add = tk.StringVar()
om_instr = ttk.OptionMenu(top_frame, instr_to_add, "VSG-1", "VSG-2")
btn_add = ttk.Button(top_frame, text="Add")
btn_refresh = ttk.Button(top_frame, text="Refresh")

label_logo.grid(row=0, column=0, padx=5, pady=5, sticky="W")
om_instr.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
btn_add.grid(row=0, column=3, columnspan=2, padx=5, pady=5)
btn_refresh.grid(row=0, column=5, columnspan=2, padx=5, pady=5)
top_frame.pack(fill=tk.X, expand=True)

root.mainloop()