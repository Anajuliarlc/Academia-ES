import tkinter as tk

import sys
sys.path.append("./src")
import gui.frame_factory as ff
import gui.frame as fr

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
        else:
            raise fr.FrameNotFound()
        
if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("800x600")
    window.resizable(False, False)
    window.title("Teacher")
    window.config(bg = "#FFFFFF")

    frame = TeacherFrameFactory("ExampleFrame", window)
    window.mainloop()

    frame = TeacherFrameFactory("ClassFrame", window)