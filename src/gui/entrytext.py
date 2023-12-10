import tkinter as tk
import sys  
sys.path.append("./src")

class EntryText(tk.Entry):
    def __init__(self, window, pos_x, pos_y, width=500, height=80, font=("Arial", 28), password=False):
        """
        Initializes an EntryText object.

        :param window: The window object where the EntryText will be placed.
        :type window: tkinter.Tk or tkinter.Toplevel
        :param pos_x: The x-coordinate of the EntryText's position.
        :type pos_x: int
        :param pos_y: The y-coordinate of the EntryText's position.
        :type pos_y: int
        :param width: The width of the EntryText, defaults to 500.
        :type width: int, optional
        :param height: The height of the EntryText, defaults to 80.
        :type height: int, optional
        :param font: The font of the EntryText, defaults to ("Arial", 28).
        :type font: tuple, optional
        :param password: Specifies whether the EntryText should be a 'hidden password' field, defaults to False.
        :type password: bool, optional
        """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        super().__init__(window, font = font, bg = "#E29E6C", fg = "#FEFAD2")
        self.place(x = self.pos_x, y = self.pos_y, width = self.width, height = self.height)
        if password:
            self.config(show = "*")