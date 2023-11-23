import sys
import os
sys.path.append(os.path.abspath("./src"))

import tkinter as tk
from tkinter import scrolledtext

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
        """Create a frame to be used as example in the application """
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#000F31")

    def place_objects(self) -> None:
        self.system = main.System()
        df = self.system.database.select("Student")
        self.table = tb.Table(self, df, 800, 600, pos_x=20, pos_y=20)

        def press_button():
            self.destroy()
            tff.TeacherFrameFactory("RegisterFrame", self.window)

        self.button1 = bt.DefaultButton("Fechar", 
                                    press_button,
                                    self,
                                    150, 267, 473, 64,
                                    font=("Arial", 12, "bold"))
        
    def destroy(self) -> None:
        super().destroy()
        