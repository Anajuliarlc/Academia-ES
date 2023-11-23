import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.buttons as bt
import student.student_frame_factory as sff

class MeasurementsFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 480,
                 pos_x: int = 240, pos_y: int = 200) -> None:
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#000F31")
    
    def set_measurement(self) -> None:
        self.destroy()
        sff.StudentFrameFactory.get_frame("SetMeasurementFrame", self.window)

    def view_measurement(self) -> None:
        self.destroy()
        sff.StudentFrameFactory.get_frame("ViewMeasurementFrame", self.window)

    def place_objects(self) -> None:
        """Place objects on the frame
        """

        frame_title = tk.Label(self, text = "Medições",
                                font = ("Arial", 24, "bold"), bg = "#000F31",
                                fg = "#FEFAD2")
        frame_title.place(x = 0, y = 20, height = 30, width = 480)
        self.label_view_measurements = bt.DefaultButton(text = "Definir Medidas",
                                                command = self.set_measurement,
                                                window = self,
                                                pos_x = 40, pos_y = 100,
                                                width = 400, height = 50)
        self.label_view_measurements = bt.DefaultButton(text = "Visualizar Medidas",
                                                command = self.view_measurement,
                                                window = self,
                                                pos_x = 40, pos_y = 200,
                                                width = 400, height = 50)

    def destroy(self) -> None:
        super().destroy()
