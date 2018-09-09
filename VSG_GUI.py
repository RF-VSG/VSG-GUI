import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import os

class SigGenUI:

    def __init__(self):
        return

    def load_project(self):
        return

    def save_project(self):
        return

    def exit_app(self):
        # Warn user before exiting the GUI 
        if messagebox.askokcancel("Exit VSG", "Are you sure to exit VSG?"):
            self.root.destroy()

    def create_top_menu(self):
        # Create top menu bar
        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Load Project", command=self.load_project)
        self.file_menu.add_command(label="Save Project", command=self.save_project)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit_app)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Put menu bar into the root
        self.root.config(menu=self.menu_bar)
    
    def create_top_bar(self):
        top_bar_frame = ttk.Frame(self.root)
        top_bar_frame.config(height=25)
        top_bar_frame.pack(fill=tk.X)    # NEED TO CHANGE

        logo = tk.PhotoImage(file=os.path.join("img", "dance.gif"))
        label_logo = ttk.Label(self.root, image=logo)
        label_logo.pack(side=tk.LEFT)                                                  # NEED TO DEBUG

        self.instr_to_add = tk.StringVar()
        om_instr = ttk.OptionMenu(top_bar_frame, self.instr_to_add, "VSG-1", "VSG-2") # DUMMY DEVICES
        om_instr.config(width=30)
        om_instr.pack(side=tk.LEFT, padx=5, pady=5)     # NEED TO CHANGE

        btn_add_instr = ttk.Button(top_bar_frame, text="Add")
        btn_add_instr.pack(side=tk.LEFT, padx=5, pady=5)    # NEED TO CHANGE

        btn_refresh = ttk.Button(top_bar_frame, text="Refresh")
        btn_refresh.pack(side=tk.LEFT, padx=5, pady=5)      # NEED TO CHANGE

    def create_mid_tabs(self):
        nb_mid = ttk.Notebook(self.root)
        nb_mid.config(height=50)
        nb_mid.pack(fill=tk.X)              # NEED TO CHANGE

        page_instr1 = ttk.Frame(nb_mid)
        nb_mid.add(page_instr1, text="VSG-1")

        page_instr2 = ttk.Frame(nb_mid)
        nb_mid.add(page_instr2, text="VSG-2")

    def create_bot_tabs(self):
        style = ttk.Style(self.root)
        style.configure("lefttab.TNotebook", tabposition="wn")  # Bullshit: can only use lower-case, "WN" won't work
        nb_bot = ttk.Notebook(self.root, style="lefttab.TNotebook")

        page_front_panel = ttk.Frame(nb_bot)
        nb_bot.add(page_front_panel, text="Front Panel")

        page_modulation = ttk.Frame(nb_bot)
        nb_bot.add(page_modulation, text="Modulation")

        page_settings = ttk.Frame(nb_bot)
        nb_bot.add(page_settings, text="Settings")

        page_iq = ttk.Frame(nb_bot)
        nb_bot.add(page_iq, text="IQ Board")

        page_rf = ttk.Frame(nb_bot)
        nb_bot.add(page_rf, text="RF Synth")

        page_lf = ttk.Frame(nb_bot)
        nb_bot.add(page_lf, text="LF Synth")

        nb_bot.pack(fill=tk.BOTH, padx=5, pady=5)           # NEED TO CHANGE

    def start(self):
        self.root = tk.Tk()
        self.root.title("Vector Signal Generator (VSG)")
        self.root.geometry("600x600")
        self.create_top_menu()
        self.create_top_bar()
        self.create_mid_tabs()
        self.create_bot_tabs()
        self.root.mainloop()

if __name__ == "__main__":
    gui = SigGenUI()
    gui.start()