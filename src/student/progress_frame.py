import sys
sys.path.append("./src")

import tkinter as tk

import gui.frame as fr
import student.student_frame_factory as sff

class ProgressFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 600, width: int = 480,
                 pos_x: int = 240, pos_y: int = 200) -> None:
        """Initialize the ProgressFrame class.

        :param window: The Tkinter window object.
        :type window: tk.Tk
        :param height: The height of the frame, defaults to 600.
        :type height: int, optional
        :param width: The width of the frame, defaults to 480.
        :type width: int, optional
        :param pos_x: The x-coordinate position of the frame, defaults to 240.
        :type pos_x: int, optional
        :param pos_y: The y-coordinate position of the frame, defaults to 200.
        :type pos_y: int, optional
        """
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        """Design the frame.
        """
        self.config(bg = "#000F31")

    def place_objects(self) -> None:
        """Place objects on the frame.
        """
        sff.StudentFrameFactory.get_frame("GoalsFrame", self.window)
        sff.StudentFrameFactory.get_frame("MeasurementsFrame", self.window)
        
    def destroy(self) -> None:
        """Destroy the frame.
        """
        super().destroy()