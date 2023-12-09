import tkinter as tk
import sys  
sys.path.append("./src")

class EntryText(tk.Entry):
    """
    >>> root = tk.Tk()
    >>> entry = EntryText(root, 10, 20, 500, 80)
    >>> entry.pos_x, entry.pos_y, entry.width, entry.height
    (10, 20, 500, 80)
    """
    def __init__(self, window, pos_x, pos_y, width = 500, height = 80, font = ("Arial", 28), password = False):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        super().__init__(window, font = font, bg = "#E29E6C", fg = "#FEFAD2")
        self.place(x = self.pos_x, y = self.pos_y, width = self.width, height = self.height)
        if password:
            self.config(show = "*")
            
if __name__ == "__main__":
    import doctest
    doctest.testmod()