import tkinter as tk
from tkinter import ttk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.buttons as bt
import gui.table as tb
import student.measurements as ms
import pandas as pd

class ViewMeasurementsFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 960,
                  pos_x: int = 240, pos_y: int = 200) -> None:
        """Creates a frame for viewing measurements.

        :param window: The Tkinter window object.
        :type window: tk.Tk
        :param height: The height of the frame, defaults to 400.
        :type height: int, optional
        :param width: The width of the frame, defaults to 960.
        :type width: int, optional
        :param pos_x: The x-coordinate position of the frame, defaults to 240.
        :type pos_x: int, optional
        :param pos_y: The y-coordinate position of the frame, defaults to 200.
        :type pos_y: int, optional
        """
        self.measurement = ms.Measurements()
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        """Designs the appearance of the frame.
        """
        self.config(bg = "#000F31")

    def place_objects(self) -> None:
        """Places objects within the frame.
        """
        frame_title = tk.Label(self, text = "Medições",
                               font = ("Arial", 24, "bold"), bg = "#000F31",
                               fg = "#FEFAD2")
        frame_title.place(x = 400, y = 10, height = 30, width = 200)

        history = self.measurement.get_history()

        table = tb.Table(self, history, 800, 300, 10, 80, 50)

    def destroy(self) -> None:
        """Destroys the frame.
        """
        super().destroy()
    