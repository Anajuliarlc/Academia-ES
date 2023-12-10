import tkinter as tk
import pandas as pd

class Table():
    def __init__(self, window: tk.Frame, data: pd.DataFrame,
                  widht: int, height: int, font_size: int = 10,
                  pos_x: int = 0, pos_y: int = 0) -> None:
        """
        Initializes a Table object.

        :param window: The parent window/frame where the table will be placed.
        :type window: tk.Frame
        :param data: The data to be displayed in the table.
        :type data: pd.DataFrame
        :param widht: The width of the table.
        :type widht: int
        :param height: The height of the table.
        :type height: int
        :param font_size: The font size of the table cells, defaults to 10.
        :type font_size: int, optional
        :param pos_x: The x-coordinate position of the table, defaults to 0.
        :type pos_x: int, optional
        :param pos_y: The y-coordinate position of the table, defaults to 0.
        :type pos_y: int, optional
        """
        self.window = window
        self.columns = data.columns
        self.data = data
        self.width = widht
        self.height = height
        self.font_size = font_size
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.columns_width = self.width // len(self.columns)
        self.create_table()

    def create_table(self) -> None:
            """
            Create a table in the GUI window with the given columns and data.
            """
            for i in range(len(self.columns)):
                self.label_index = tk.Label(self.window,
                                            text = f"{self.columns[i]}",
                                            font = ("Arial", self.font_size, "bold"),
                                            bg = "#DF8350",
                                            fg = "#FEFAD2")
                self.label_index.place(x = self.pos_x + self.columns_width * i,
                                        y = self.pos_y,
                                        height = 30, width = self.columns_width)
                for j, value in enumerate(self.data[self.columns[i]]):
                    self.label_value = tk.Label(self.window,
                                                text = f"{value}",
                                                font = ("Arial", self.font_size),
                                                bg = "#DF8350",
                                                fg = "#FEFAD2")
                    self.label_value.place(x = self.pos_x + self.columns_width * i,
                                            y = self.pos_y + 30 * (j + 1),
                                            height = 30, width = self.columns_width)
        
        
if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("800x600")
    window.config(bg = "#FFFFFF")
    df = pd.DataFrame([["João", 20, 1.80, 80], ["Maria", 25, 1.70, 60]],
                        columns = ["Nome", "Idade", "Altura", "Peso"])
    table = Table(window, df, 600, 400, 10, 0, 0)
    window.mainloop()