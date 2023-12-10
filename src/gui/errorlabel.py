import tkinter as tk
import sys  
sys.path.append("./src")

class ErrorLabel(tk.Label):
    def __init__(self, window, text, pos_x, pos_y, width=400, height=80, font=("Arial", 14)):
        """
        Initializes an ErrorLabel object.

        :param window: The parent window where the ErrorLabel will be placed.
        :type window: tkinter.Tk or tkinter.Toplevel
        :param text: The text to be displayed in the ErrorLabel.
        :type text: str
        :param pos_x: The x-coordinate of the ErrorLabel's position.
        :type pos_x: int
        :param pos_y: The y-coordinate of the ErrorLabel's position.
        :type pos_y: int
        :param width: The width of the ErrorLabel, defaults to 400.
        :type width: int, optional
        :param height: The height of the ErrorLabel, defaults to 80.
        :type height: int, optional
        :param font: The font of the ErrorLabel, defaults to ("Arial", 14).
        :type font: tuple, optional
        """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        super().__init__(window, text=text, font=font, bg="#DF8350", fg="#000F31")
        self.place(x=self.pos_x, y=self.pos_y, width=self.width, height=self.height)
