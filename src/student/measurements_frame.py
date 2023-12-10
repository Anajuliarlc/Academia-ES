import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.buttons as bt
import student.student_frame_factory as sff

class MeasurementsFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 480,
                 pos_x: int = 240, pos_y: int = 200) -> None:
        """Creates a frame for managing measurements.

        :param window: The parent window for the frame.
        :type window: tk.Tk
        :param height: The height of the frame, defaults to 400.
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
        """Designs the frame by configuring its background color.
        """
        self.config(bg = "#000F31")
    
    def set_measurement(self) -> None:
        """Destroys the current frame and opens the SetMeasurementFrame.
        """
        self.destroy()
        sff.StudentFrameFactory.get_frame("SetMeasurementFrame", self.window)

    def view_measurement(self) -> None:
        """Destroys the current frame and opens the ViewMeasurementsFrame.
        """
        self.destroy()
        sff.StudentFrameFactory.get_frame("ViewMeasurementsFrame", self.window)

    def place_objects(self) -> None:
        """Places objects on the frame.
        """

        frame_title = tk.Label(self, text = "Medições",
                               font = ("Arial", 24, "bold"), bg = "#000F31",
                               fg = "#FEFAD2")
        frame_title.place(x = 0, y = 20, height = 30, width = 480)
        self.label_view_measurements = bt.DefaultButton(text = "Definir Medidas",
                                                        command = self.set_measurement,
                                                        window = self,
                                                        pos_x = 80, pos_y = 240,
                                                        height = 50, width = 340)
        self.label_view_measurements = bt.DefaultButton(text = "Visualizar Medidas",
                                                        command = self.view_measurement,
                                                        window = self,
                                                        pos_x = 80, pos_y = 140,
                                                        height = 50, width = 340)

    def destroy(self) -> None:
        """Destroys the frame.
        """
        super().destroy()
