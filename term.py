# Nick Greiner
# 08/03/2023
# This is the frame for the term

import tkinter as tk
import json
from tkinter import ttk
from options import questionNum, questionOptions

getTerm = questionOptions('questionData.json')


class TermFrame(tk.LabelFrame):
    def __init__(self, mainFrame):
        super().__init__(mainFrame, text='Term', width=770, height=350, background='white', labelanchor='n', bd=5, foreground='black')

        self.currentQuestion = (getTerm[f'Question{questionNum}']['question'])


        options = {'pady': (10,0)}
        self.termLabel = ttk.Label(self, text=self.currentQuestion, font="Garamond 12 bold", foreground='black', background='white')
        self.termLabel.pack(expand=True, anchor='center')
        self.pack(**options)
        self.pack_propagate(0)

    def updateTerm(self):
        global questionNum
        questionNum += 1
        self.currentQuestion = (getTerm[f'Question{questionNum}']['question'])
        self.termLabel.config(text=self.currentQuestion)