import tkinter as tk

import sys
sys.path.append("./src")

import gui.frame_factory as ff
import gui.frame as fr
import teacher.classes_frame as tcf
import teacher.new_class_frame as tnc
import gui.window as wd
import teacher.menu_frame as tmf
import teacher.register_frame as rf
import teacher.create_register_frame as crf
import teacher.view_register_frame as vrf
import teacher.current_workouts_frame as cw
import teacher.workouts as tw
import teacher.new_workout as tnw

class TeacherFrameFactory(ff.FrameFactory):
    @staticmethod
    def get_frame(type_: str, window: tk.Tk, height: int = 600, width: int = 800,
                   pos_x: int = 0, pos_y: int = 0) -> fr.Frame:
        """Frame factory for teacher frames

        :param type_: _description_
        :type type_: str
        :param window: _description_
        :type window: tk.Tk
        :param height: _description_, defaults to 600
        :type height: int, optional
        :param width: _description_, defaults to 800
        :type width: int, optional
        :param pos_x: _description_, defaults to 0
        :type pos_x: int, optional
        :param pos_y: _description_, defaults to 0
        :type pos_y: int, optional
        :raises TeacherFrameNotFound: _description_
        :return: _description_
        :rtype: fr.Frame
        """        
        if type_ == "ExampleFrame":
            return fr.ExampleFrame(window, height, width, pos_x, pos_y)
        elif type_ == "NewWorkoutFrame":
            return tnw.NewWorkoutFrame(window)
        elif type_ == "MenuFrame":
            return tmf.MenuFrame(window)
        elif type_ == "RegisterFrame":
            return rf.RegisterFrame(window)
        elif type_ == "CreateRegisterFrame":
            return crf.CreateRegisterFrame(window)
        elif type_ == "ViewRegisterFrame":
            vrf.ViewRegisterFrame(window)
        elif type_ == "ClassesFrame":
            return tcf.ClassesFrame(window)
        elif type_ == "NewClass":
            return tnc.NewClassFrame(window)
        elif type_ == "WorkoutsFrame":
            return tw.InitialWorkoutsFrame(window)
        elif type_ == "CurrentWorkoutsFrame":
            return cw.CurrentWorkouts(window)
        elif type_ == "WorkoutsFrame":
            return tw.InitialWorkoutsFrame(window)
        else:
            raise fr.FrameNotFound()
        
if __name__ == "__main__":
    window = wd.Window()
    frame = TeacherFrameFactory("MenuFrame", window)
    window.mainloop()
