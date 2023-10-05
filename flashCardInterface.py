import tkinter as tk
from tkinter import ttk
import sv_ttk
from mainFrame import *

class FlashCardInterface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flash Cards!")
        self.geometry("1000x800")
    

if __name__ == '__main__':
    interface = FlashCardInterface()

    sv_ttk.set_theme('dark')
    MainFrame(interface)

    interface.mainloop()
