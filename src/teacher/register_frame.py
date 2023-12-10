import sys
import os
sys.path.append(os.path.abspath("./src"))

import tkinter as tk

import gui.frame as fr
import gui.buttons as bt 
import teacher.teacher_frame_factory as tff

class RegisterFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 450, width: int = 960,
                  pos_x: int = 240, pos_y: int = 150) -> None:
        """
        Create a frame to be used as an example in the application.

        :param window: The Tkinter window object.
        :param height: The height of the frame.
        :param width: The width of the frame.
        :param pos_x: The x-coordinate position of the frame.
        :param pos_y: The y-coordinate position of the frame.
        """
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        """
        Set the design of the frame.
        """
        self.config(bg="#000F31")

    def place_objects(self) -> None:
        """
        Place objects within the frame.
        """
        label1 = tk.Label(self, 
                          text="Matrículas de Alunos", 
                          font=("Arial", 20), 
                          bg="#000F31",
                          fg="#DF8350")
        label1.place(x=345, y=10)

        def button_press(next_frame: str):
            self.destroy()
            tff.TeacherFrameFactory.get_frame(next_frame, self.window)

        self.button1 = bt.DefaultButton("Criar Matrícula", 
                                    lambda: button_press("CreateRegisterFrame"),
                                    self, 
                                    127, 150,
                                    font=("Arial", 20, "bold"))
        
        self.button2 = bt.DefaultButton("Visualizar Matrículas", 
                                    lambda: button_press("ViewRegisterFrame"),
                                    self, 
                                    536, 150,
                                    font=("Arial", 20, "bold"))
    
    def destroy(self) -> None:
        """
        Destroy the frame.
        """
        super().destroy()
        
        