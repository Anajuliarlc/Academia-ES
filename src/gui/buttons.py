import tkinter as tk
import sys  
sys.path.append("./src")

class MenuButton(tk.Button):
    """
    >>> root = tk.Tk()
    >>> button = MenuButton("Menu", lambda: print("Clicked"), root, 10, 20, 200, 50)
    >>> button.pos_x, button.pos_y, button.width, button.height
    (10, 20, 200, 50)
    """
    def __init__(self, text, command, window, pos_x, pos_y, width = 200, height = 50):
        """
        Initializes a Button object, default to the column menu.

        :param text: The text to be displayed on the button.
        :type text: str
        :param command: The function to be executed when the button is clicked.
        :type command: function
        :param window: The window where the button will be placed.
        :param pos_x: The x-coordinate of the button's position.
        :type pos_x: int
        :param pos_y: The y-coordinate of the button's position.
        :type pos_y: int
        :param width: The width of the button (default is 200).
        :type width: int
        :param height: The height of the button (default is 50).
        :type height: int
        """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        super().__init__(window, text = text, font = ("Arial", 18), 
                                    bg = "#E29E6C", fg = "#FEFAD2", borderwidth=2, 
                                    highlightbackground="#000F31", 
                                    command = command)
        self.place(x = self.pos_x, y = self.pos_y, width = self.width, height = self.height)
    

class DefaultButton(tk.Button):
    """
    >>> root = tk.Tk()
    >>> button = DefaultButton("Default", lambda: print("Clicked"), root, 10, 20, 300, 120)
    >>> button.pos_x, button.pos_y, button.width, button.height
    (10, 20, 300, 120)
    """
    def __init__(self, text, command, window, pos_x, pos_y, width = 300, height = 120, font = ("Arial", 28)):
        """
            Initializes a Button object, default to the gym system.

            :param text: The text to be displayed on the button.
            :type text: str
            :param command: The function to be executed when the button is clicked.
            :type command: function
            :param window: The window where the button will be placed.
            :param pos_x: The x-coordinate of the button's position.
            :type pos_x: int
            :param pos_y: The y-coordinate of the button's position.
            :type pos_y: int
            :param width: The width of the button (default is 200).
            :type width: int
            :param height: The height of the button (default is 50).
            :type height: int
            """
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        super().__init__(window, text = text, font = font, 
                                    bg = "#E29E6C", fg = "#FEFAD2", borderwidth=2, 
                                    highlightbackground="#000F31", 
                                    command = command)
        self.place(x = self.pos_x, y = self.pos_y, width = self.width, height = self.height)
   
