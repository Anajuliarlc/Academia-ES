import tkinter as tk
from tkinter import ttk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.buttons as bt

class MeasurementsFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 480, pos_x: int = 240, pos_y: int = 200) -> None:
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#000F31")

    def place_objects(self) -> None:
        dict_example = {"MeasDate": "22/05/2021",
                        "Weight": "80",
                        "Height": "170",
                        "HighWaist": "70.5",
                        "LowWaist": "175",
                        "Bust": "80",
                        "Biceps": "70",
                        "Thigh": "55"}
        frame_title = tk.Label(self, text = "Medições",
                                font = ("Arial", 24, "bold"), bg = "#000F31",
                                fg = "#FEFAD2")
        frame_title.place(x = 80, y = 10, height = 30, width = 300)

        columns = ("Data", "Peso", "Altura", "Cintura Alta",
                    "Cintura Baixa", "Busto", "Biceps", "Coxa")
        
        table = ttk.Treeview(self, columns = columns, show = "headings")
        table.tag_configure(tagname = "font", font = ("Arial", 6, "bold"))

        table.heading("Data", text = "Data")
        table.column("Data", minwidth = 0, width = 69,
                     stretch = False, anchor = "center")

        for column in columns[1:]:
            table.heading(column, text = column)
            table.column(column, minwidth = 0, width = 47,
                         stretch = False, anchor = "center")
        table.place(x = 40, y = 50, height = 250, width = 400)

        table.insert("", "end",
                      values = (dict_example["MeasDate"],
                                 dict_example["Weight"],
                                 dict_example["Height"],
                                 dict_example["HighWaist"],
                                 dict_example["LowWaist"],
                                 dict_example["Bust"],
                                 dict_example["Biceps"], dict_example["Thigh"]))


    def destroy(self) -> None:
        super().destroy()
    