import sys
import os
sys.path.append(os.path.abspath("./src"))

import tkinter as tk
from tkinter import scrolledtext
import pandas as pd

import gui.frame as fr
import gui.entrytext as et
import gui.buttons as bt 
import teacher.teacher_frame_factory as tff
import teacher.register as reg
import gui.errorlabel as el
import exc.exceptions as exc
import gui.table as tb
import main

class ViewRegisterFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 450, width: int = 960,
                  pos_x: int = 240, pos_y: int = 150) -> None:
        """Initialize the ViewRegisterFrame class.

        :param window: The Tkinter window object.
        :type window: tk.Tk
        :param height: The height of the frame, defaults to 450.
        :type height: int, optional
        :param width: The width of the frame, defaults to 960.
        :type width: int, optional
        :param pos_x: The x-coordinate position of the frame, defaults to 240.
        :type pos_x: int, optional
        :param pos_y: The y-coordinate position of the frame, defaults to 150.
        :type pos_y: int, optional
        """
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        """Design the frame.
        """
        self.config(bg = "#000F31")

    def place_objects(self) -> None:
        """Place objects in the frame.
        """
        self.system = main.System()
        df1 = self.system.database.select("User")
        df2 = self.system.database.select("Student")
        df = pd.merge(df1, df2, on="IdUser")[["UserName", "BirthDate", "CPF", "PhoneNumber", "City", "RegistrationDate", "MedicalData"]]

        self.table = tb.Table(self, df, 920, 30, pos_x=20, pos_y=20)

        # TODO: implement scroll buttons for the table when it exceeds the window size

        def press_button():
            self.destroy()
            tff.TeacherFrameFactory("RegisterFrame", self.window)

        self.button1 = bt.DefaultButton("Fechar",
                                        press_button,
                                        self,
                                        870, 400,
                                        70, 30,
                                        font=("Arial", 12, "bold"))

    def destroy(self) -> None:
        """Destroy the frame.
        """
        super().destroy()
        