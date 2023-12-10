import tkinter as tk
import sys
sys.path.append("./src")

class StudentClass(tk.Frame):
    def __init__(self, window: tk.Frame, class_name: str, class_date: str,
                 class_description: str, pos_x: int = 0, pos_y: int = 0) -> None:
        """
        Initializes a new instance of the StudentClass class.

        :param window: The parent window/frame.
        :type window: tk.Frame
        :param class_name: The name of the class.
        :type class_name: str
        :param class_date: The date of the class.
        :type class_date: str
        :param class_description: The description of the class.
        :type class_description: str
        :param pos_x: The x-coordinate position of the class frame, defaults to 0.
        :type pos_x: int, optional
        :param pos_y: The y-coordinate position of the class frame, defaults to 0.
        :type pos_y: int, optional
        """
        self.name = class_name
        self.date = class_date
        self.description = class_description
        super().__init__(window)
        self.design()
        self.place_objects()
        self.place(x = pos_x, y = pos_y, width = 200, height = 250)

    def design(self):
        """
        Sets the design properties of the class frame.
        """
        self.config(bg = "#E29E6C")

    def place_objects(self) -> None:
        """
        Places the objects (labels) inside the class frame.
        """
        title = tk.Label(self, text = self.name, font = ("Arial", 14, "bold"),
                         bg = "#DF8350", fg = "#FEFAD2", wraplength = 200)
        title.place(x = 0, y = 0, width = 200, height = 50)

        date = tk.Label(self, text = self.date,
                        font = ("Arial", 10, "bold"),
                        bg = "#E29E6C", fg = "#FFFFFF", wraplength = 200)
        date.place(x = 0, y = 50, width = 200, height = 50)

        description = tk.Label(self, text = self.description,
                               font = ("Arial", 10, "bold"),
                               bg = "#E29E6C", fg = "#FFFFFF",
                               anchor = "nw", justify="left", wraplength = 200)
        description.place(x = 0, y = 100, width = 200, height = 150)

    def destroy(self) -> None:
        """
        Destroys the class frame.
        """
        return super().destroy()
