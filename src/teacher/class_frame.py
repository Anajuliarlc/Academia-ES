import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr

class Class(tk.Frame):
    def __init__(self, window: tk.Frame, name: str, date: str, description: str,
                 pos_x: int = 0, pos_y: int = 0) -> None:
        self.name = name
        self.date = date
        self.description = description
        super().__init__(window)
        self.design()
        self.place_objects()
        self.place(x = pos_x, y = pos_y, width = 200, height = 250)

    def design(self):
        self.config(bg = "#E29E6C")
    
    def place_objects(self) -> None:
        title = tk.Label(self, text = self.name, font = ("Arial", 14, "bold"),
                          bg = "#DF8350", fg = "#FEFAD2", wraplength = 200)
        title.place(x = 0, y = 0, width = 200, height = 50)
        date = tk.Label(self, text = self.date, font = ("Arial", 10, "bold"),
                          bg = "#E29E6C", fg = "#FFFFFF", wraplength = 200)
        date.place(x = 0, y = 50, width = 200, height = 50)
        description = tk.Label(self, text = self.description,
                                font = ("Arial", 10, "bold"),
                                bg = "#E29E6C", fg = "#FFFFFF",
                                anchor = "nw", justify="left", wraplength = 200)
        description.place(x = 0, y = 100, width = 200, height = 150)

    def destroy(self) -> None:
        return super().destroy()
