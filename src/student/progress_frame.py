import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import student_frame_factory as sff

class ProgressFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 600, width: int = 480,
                 pos_x: int = 240, pos_y: int = 200) -> None:
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#000F31")

    def place_objects(self) -> None:
        """Place objects on the frame
        """
        sff.StudentFrameFactory.get_frame("GoalsFrame", self.window)
        sff.StudentFrameFactory.get_frame("MeasurementsFrame", self.window)
        
    def destroy(self) -> None:
        super().destroy()