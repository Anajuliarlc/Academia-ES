import tkinter as tk

import sys
sys.path.append("./src")
import gui.window as wd
import gui.frame_factory as ff
import gui.frame as fr
import student.menu_frame as smf

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
        elif type_ == "ProgressFrame":
            return gf.GoalsFrame(window)
        elif type_ == "SetGoalsFrame":
            return sgf.SetGoalsFrame(window)
        elif type_ == "ViewGoalsFrame":
            return vgf.ViewGoalsFrame(window)
        else:
            raise fr.FrameNotFound()
        
if __name__ == "__main__":
    window = wd.Window(connect = False)
    frame = StudentFrameFactory("MenuFrame", window)
    window.mainloop()

    
