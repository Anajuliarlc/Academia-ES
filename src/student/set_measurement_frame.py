import sys
sys.path.append("./src")

import tkinter as tk
import gui.frame as fr
import gui.buttons as bt
import gui.entrytext as et
import student.student_frame_factory as sff
import student.measurements as ms
import gui.errorlabel as el

class SetMeasurementFrame(fr.Frame):
    def __init__(self, window, height: int = 400, width: int = 480,
                 pos_x: int = 240, pos_y: int = 200) -> None:
        """Creates a SetMeasurementFrame object.

        :param window: The parent window for the frame.
        :type window: tkinter.Tk
        :param height: The height of the frame, defaults to 400.
        :type height: int, optional
        :param width: The width of the frame, defaults to 480.
        :type width: int, optional
        :param pos_x: The x-coordinate position of the frame, defaults to 240.
        :type pos_x: int, optional
        :param pos_y: The y-coordinate position of the frame, defaults to 200.
        :type pos_y: int, optional
        """
        self.measurements = ms.Measurements()
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        """Designs the SetMeasurementFrame.
        """
        self.config(bg = "#000F31")

    def get_measurement(self) -> None:
        """Gets the measurements from the entry fields and updates the database.
        """
        measurements = {}
        measurements["Weight"] = self.entry_weight.get()
        measurements["Height"] = self.entry_height.get()
        measurements["HighWaist"] = self.entry_high_waist.get()
        measurements["LowWaist"] = self.entry_low_waist.get()
        measurements["Bust"] = self.entry_bust.get()
        measurements["Biceps"] = self.entry_biceps.get()
        measurements["Thigh"] = self.entry_thigh.get()

        if (measurements["Weight"] == "" or
            measurements["Height"] == "" or
            measurements["HighWaist"] == "" or
            measurements["LowWaist"] == "" or
            measurements["Bust"] == "" or
            measurements["Biceps"] == "" or
            measurements["Thigh"] == ""):
            el.ErrorLabel(self, "Todos os campos devem ser preenchidos",
                            80, 380, 340, 20)
            return
        if (not measurements["Weight"].isnumeric() or
            not measurements["Height"].isnumeric() or
            not measurements["HighWaist"].isnumeric() or
            not measurements["LowWaist"].isnumeric() or
            not measurements["Bust"].isnumeric() or
            not measurements["Biceps"].isnumeric() or
            not measurements["Thigh"].isnumeric()):
            el.ErrorLabel(self, "Todos os campos devem ser numéricos",
                            80, 380, 340, 20)
            return
        
        print(self.measurements.update_db(measurements))
        self.destroy()
        sff.StudentFrameFactory.get_frame("MeasurementsFrame", self.window)

    def place_objects(self) -> None:
        """Places the labels, entry fields, and button in the SetMeasurementFrame.
        """
        self.label_weight = tk.Label(self, text = "Peso (kg):",
                                        font = ("Arial", 12, "bold"),
                                        bg = "#000F31", fg = "#FEFAD2")
        self.label_height = tk.Label(self, text = "Altura (cm):",
                                        font = ("Arial", 12, "bold"),
                                        bg = "#000F31", fg = "#FEFAD2")
        self.label_high_waist = tk.Label(self, text = "Cintura Alta (cm):",
                                        font = ("Arial", 12, "bold"),
                                        bg = "#000F31", fg = "#FEFAD2")
        self.label_low_waist = tk.Label(self, text = "Cintura Baixa (cm):",
                                        font = ("Arial", 12, "bold"),
                                        bg = "#000F31", fg = "#FEFAD2")
        self.label_bust = tk.Label(self, text = "Busto (cm):",
                                        font = ("Arial", 12, "bold"),
                                        bg = "#000F31", fg = "#FEFAD2")
        self.label_biceps = tk.Label(self, text = "Biceps (cm):",
                                        font = ("Arial", 12, "bold"),
                                        bg = "#000F31", fg = "#FEFAD2")
        self.label_thigh = tk.Label(self, text = "Coxa (cm):",
                                        font = ("Arial", 12, "bold"),
                                        bg = "#000F31", fg = "#FEFAD2")
        self.label_weight.place(x = 80, y = 20, height = 30, width = 200)
        self.label_height.place(x = 80, y = 60, height = 30, width = 200)
        self.label_high_waist.place(x = 80, y = 100, height = 30, width = 200)
        self.label_low_waist.place(x = 80, y = 140, height = 30, width = 200)
        self.label_bust.place(x = 80, y = 180, height = 30, width = 200)
        self.label_biceps.place(x = 80, y = 220, height = 30, width = 200)
        self.label_thigh.place(x = 80, y = 260, height = 30, width = 200)

        self.entry_weight = et.EntryText(self, pos_x = 280, pos_y = 20,
                                            height = 30, width = 140)
        self.entry_height = et.EntryText(self, pos_x = 280, pos_y = 60,
                                            height = 30, width = 140)
        self.entry_high_waist = et.EntryText(self, pos_x = 280, pos_y = 100,
                                            height = 30, width = 140)
        self.entry_low_waist = et.EntryText(self, pos_x = 280, pos_y = 140,
                                            height = 30, width = 140)
        self.entry_bust = et.EntryText(self, pos_x = 280, pos_y = 180,
                                            height = 30, width = 140)
        self.entry_biceps = et.EntryText(self, pos_x = 280, pos_y = 220,
                                            height = 30, width = 140)
        self.entry_thigh = et.EntryText(self, pos_x = 280, pos_y = 260,
                                            height = 30, width = 140)
        self.button_confirm = bt.DefaultButton(text = "Confirmar",
                                                command = self.get_measurement,
                                                window = self,
                                                pos_x = 80, pos_y = 320,
                                                height = 50, width = 340)

    def destroy(self) -> None:
        """Destroys the SetMeasurementFrame and creates a new MeasurementsFrame.
        """
        super().destroy()
        sff.StudentFrameFactory.get_frame("MeasurementsFrame", self.window)