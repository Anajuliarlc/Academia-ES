import tkinter as tk
import sys  
sys.path.append("./src")

class ErrorLabel(tk.Label):
    def __init__(self, window, text, pos_x, pos_y, width = 500, height = 80, font = ("Arial", 28)):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        super().__init__(window, text = text, font = font, bg = "#000F31", fg = "#FEFAD2")
        self.place(x = self.pos_x, y = self.pos_y, width = self.width, height = self.height)