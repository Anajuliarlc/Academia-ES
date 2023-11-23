import tkinter as tk
import pandas as pd

class Table():
    def __init__(self, window: tk.Frame, data: pd.DataFrame,
                  width: int, height: int, font_size: int = 10,
                  pos_x: int = 0, pos_y: int = 0) -> None:
        self.window = window
        self.columns = data.columns
        self.data = data
        self.width = width
        self.height = height
        self.font_size = font_size
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.columns_width = self.width // len(self.columns)
        self.create_table()

    def create_table(self) -> None:
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