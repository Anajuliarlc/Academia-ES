import tkinter as tk
import sys  
sys.path.append("./src")

import gui.errorlabel as el

class ThankYouFrame(el.ErrorLabel):
    def __init__(self, window, text, pos_x, pos_y, width = 400, height = 80, font = ("Arial", 14)):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        super().__init__(window, text = text, font = font)
        self.place(x = self.pos_x, y = self.pos_y, width = self.width, height = self.height)