import sys
import os
sys.path.append(os.path.abspath("./src"))

import tkinter as tk

import gui.frame as fr
from gui.buttons import DefaultButton

import teacher.teacher_frame_factory as tff
import exc.exceptions as exc
from login.login_class import Login
from main import System

class RegisterFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 450, width: int = 960,
                  pos_x: int = 240, pos_y: int = 150) -> None:
        """Create a frame to be used as example in the application """
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#000F31")

    def place_objects(self) -> None:
        label1 = tk.Label(self, 
                          text = "Matrículas de Alunos", 
                          font = ("Arial", 20), 
                          bg = "#000F31",
                          fg = "#DF8350")
        label1.place(x = 345, y = 10)

        def button_press(next_frame: str):
            self.destroy()
            tff.TeacherFrameFactory.get_frame(next_frame, self.window)

        self.button1 = DefaultButton("Criar Matrícula", 
                                    lambda: button_press("CreateRegisterFrame"),
                                    self, 
                                    60, 100)
        
        self.button2 = DefaultButton("Visualizar Matrículas", 
                                    lambda: button_press("ViewRegisterFrame"),
                                    self, 
                                    510, 100)
    
    def destroy(self) -> None:
        super().destroy()
        
        