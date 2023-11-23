import tkinter as tk
from tkinter import ttk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.buttons as bt
import student.measurements as ms

class MeasurementsFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 480, pos_x: int = 240, pos_y: int = 200) -> None:
        self.measurement = ms.Measurements()
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#000F31")

    def insert_history(self) -> None:
        history = self.measurement.get_history()
        #limpar tabela
        try:
            for row in self.table.get_children():
                self.table.delete(row)
        finally:
            for _, row in history.iterrows():
                self.table.insert("", "end", values = (row["MeasDate"],
                                                        row["Weight"],
                                                        row["Height"],
                                                        row["HighWaist"],
                                                        row["LowWaist"],
                                                        row["Bust"],
                                                        row["Biceps"],
                                                        row["Thigh"]))

    def place_objects(self) -> None:
        frame_title = tk.Label(self, text = "Medições",
                                font = ("Arial", 24, "bold"), bg = "#000F31",
                                fg = "#FEFAD2")
        frame_title.place(x = 80, y = 10, height = 30, width = 300)

        columns = ("Data", "Peso", "Altura", "Cintura Alta",
                    "Cintura Baixa", "Busto", "Biceps", "Coxa")
        
        self.table = ttk.Treeview(self, columns = columns, show = "headings")
        self.table.tag_configure(tagname = "font", font = ("Arial", 6, "bold"))

        self.table.heading("Data", text = "Data")
        self.table.column("Data", minwidth = 0, width = 69,
                     stretch = False, anchor = "center")

        for column in columns[1:]:
            self.table.heading(column, text = column)
            self.table.column(column, minwidth = 0, width = 47,
                         stretch = False, anchor = "center")
        self.table.place(x = 40, y = 50, height = 250, width = 400)
        self.insert_history()

        self.update_button = bt.DefaultButton(text = "Atualizar Medidas",
                                                command = self.insert_history,
                                                window = self,
                                                pos_x = 40, pos_y = 320,
                                                height = 50, width = 400)


    def destroy(self) -> None:
        super().destroy()
    