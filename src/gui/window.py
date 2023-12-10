import tkinter as tk
import sys
sys.path.append("./src")
import db.db_connector as db
import gui.logo_frame as lf


class Window(tk.Tk):
    def __init__(self, title: str = "Chi-Trapézio", height: int = 600, 
                 width: int = 1200,pos_x: int = 0, pos_y: int = 0) -> None:
        """
        Initializes the Window class.

        :param title: The title of the window, defaults to "Chi-Trapézio"
        :type title: str, optional
        :param height: The height of the window, defaults to 600
        :type height: int, optional
        :param width: The width of the window, defaults to 1200
        :type width: int, optional
        :param pos_x: The x-coordinate position of the window, defaults to 0
        :type pos_x: int, optional
        :param pos_y: The y-coordinate position of the window, defaults to 0
        :type pos_y: int, optional
        """
        super().__init__()
        self.title(title)
        self.height = height
        self.width = width
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.active_frames = []

        self.design()

    def change_frame(self, frame: tk.Frame) -> None:
        pass

    def change_frame(self, frame: tk.Frame) -> None:
        """Changes the current frame to the one passed as argument

        :param frame: Frame to be displayed
        :type frame: tk.Frame
        """    
        pass

    def design(self):
        """Design the window.
        """
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        self.config(bg = "#000F31")
        self.iconbitmap("img/icon.ico")
        lf.LogoFrame(self)

    
if __name__ == "__main__":
    import login.login_frame_factory as lff
    mainframe = Window()
    mainframe.mainloop()
