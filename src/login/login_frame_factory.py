import tkinter as tk

import sys
sys.path.append("./src")
import gui.frame_factory as ff
import gui.frame as fr

class LoginFrameFactory(ff.FrameFactory):
    @staticmethod
    def get_frame(type_: str, window: tk.Tk, height: int = 600, width: int = 800,
                   pos_x: int = 0, pos_y: int = 0) -> fr.Frame:
        """Frame factory for the login frames

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
        else:
            raise fr.FrameNotFound()
        
if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("800x600")
    window.resizable(False, False)
    window.title("Login")
    window.config(bg = "#FFFFFF")

    frame = LoginFrameFactory("ExampleFrame", window)
    window.mainloop()

    frame = LoginFrameFactory("ClassFrame", window)