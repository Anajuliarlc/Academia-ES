import tkinter as tk

import sys
sys.path.append("./src")
import main
import gui.window as wd
import gui.frame_factory as ff
import gui.frame as fr
import student.menu_frame as smf
import student.progress_frame as pf
import student.measurements_frame as msf
import student.view_measurements_frame as svmsf
import student.set_measurement_frame as ssmf
import student.goals_frame as gf
import student.set_goals_frame as sgf
import student.view_goals_frame as vgf
import student.workouts_frame as swf
import student.request_change_frame as scf
import student.increase_frame as sif
import student.thank_you_frame as styf
import student.profile_frame as spf
import student.register_card_frame as rcf
import student.student_classes_frame as sclf
import student.student_new_class_frame as sncf

class StudentFrameFactory(ff.FrameFactory):
    @staticmethod
    def get_frame(type_: str, window: tk.Tk, height: int = 600, width: int = 800,
                   pos_x: int = 0, pos_y: int = 0) -> fr.Frame:
        """Frame factory for student frames

        :param type_: Type of frame to be created
        :type type_: str
        :param window: Window that will contain the frame
        :type window: tk.Tk
        :param height: Height of the frame, defaults to 600
        :type height: int, optional
        :param width: Width of the frame, defaults to 800
        :type width: int, optional
        :param pos_x: Position x of the frame on window, defaults to 0
        :type pos_x: int, optional
        :param pos_y: Position y of the frame on window, defaults to 0
        :type pos_y: int, optional
        """        
        if type_ == "ExampleFrame":
            return fr.ExampleFrame(window, height, width, pos_x, pos_y)
        elif type_ == "MenuFrame":
            return smf.MenuFrame(window)
        elif type_ == "WorkoutsFrame":
            return swf.WorkoutsFrame(window)
        elif type_ == "RequestChangeFrame":
            return scf.RequestChangeFrame(window)
        elif type_ == "IncreaseFrame":
            return sif.IncreaseFrame(window)
        elif type_ == "ThankYouFrame":
            return styf.ThankYouFrame(window)
        elif type_ == "ProfileFrame":
            return spf.ProfileFrame(window)
        elif type_ == "RegisterCardFrame":
            return rcf.RegisterCardFrame(window)
        elif type_ == "ProgressFrame":
            return pf.ProgressFrame(window)
        elif type_ == "GoalsFrame":
            return gf.GoalsFrame(window)
        elif type_ == "SetGoalsFrame":
            return sgf.SetGoalsFrame(window)
        elif type_ == "ViewGoalsFrame":
            return vgf.ViewGoalsFrame(window)
        elif type_ == "MeasurementsFrame":
            return msf.MeasurementsFrame(window)
        elif type_ == "SetMeasurementFrame":
            return ssmf.SetMeasurementFrame(window)
        elif type_ == "ViewMeasurementsFrame":
            return svmsf.ViewMeasurementsFrame(window)
        elif type_ == "ClassesFrame":
            return sclf.StudentClassesFrame(window)
        elif type_ == "NewClass":
            return sncf.NewClassFrame(window)
        else:
            raise fr.FrameNotFound()
        
if __name__ == "__main__":
    window = wd.Window()
    frame = StudentFrameFactory("MenuFrame", window)
    system = main.System()
    system.user = 3
    StudentFrameFactory("ProgressFrame", window)
    window.mainloop()
