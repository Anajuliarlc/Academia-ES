import tkinter as tk
import sys  
sys.path.append("./src")

class EntryText(tk.Entry):
    def __init__(self, window, pos_x, pos_y, width = 500, height = 80, font = ("Arial", 28), password = False):
        self.window = window
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.font = font
        super().__init__(self.window, font = self.font, bg = "#E29E6C", fg = "#FEFAD2")
        self.place(x = self.pos_x, y = self.pos_y, width = self.width, height = self.height)
        if password:
            self.config(show = "*")