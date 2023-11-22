import tkinter as tk

import sys
sys.path.append("./src")

import gui.frame_factory as ff
import gui.frame as fr
import gui.window as wd
import teacher.menu_frame as tmf
import teacher.register_frame as rf

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
        elif type_ == "MenuFrame":
            return tmf.MenuFrame(window)
        elif type_ == "RegisterFrame":
            return rf.RegisterFrame(window)
        elif type_ == "CreateRegisterFrame":
            ...
        elif type_ == "ViewRegisterFrame":
            ...
        else:
            raise fr.FrameNotFound()
        
if __name__ == "__main__":
    window = wd.Window(connect = False)
    frame = TeacherFrameFactory("MenuFrame", window)
    window.mainloop()

    