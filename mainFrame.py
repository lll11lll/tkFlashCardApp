# Nick Greiner
# 08/03/2023
# The main frame in which all the other frames are rendered onto.

import tkinter as tk
from tkinter import ttk
from flashCardStatistics import FlashCardStatistics
from term import TermFrame
from options import OptionFrame
class MainFrame(ttk.Frame):
    def __init__(self, flashCardInterferace):
        super().__init__(flashCardInterferace)
        
        self.TermFrame = TermFrame(self)
        self.OptionFrame = OptionFrame(self, termFrame=self.TermFrame)

        self.pack()
