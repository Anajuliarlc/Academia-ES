import tkinter as tk
import sys
sys.path.append("./src")
import db.db_connector as db
import gui.logo_frame as lf

class Window(tk.Tk):
    def __init__(self, title: str = "Chi-Trapézio", height: int = 600, width: int = 1200,
                  pos_x: int = 0, pos_y: int = 0, connect: bool = False) -> None:
        super().__init__()
        self.title = title
        self.height = height
        self.width = width
        self.pos_x = pos_x
        self.pos_y = pos_y
        
        if connect:
            self.database = db.DBConnector()

        self.design()
    
    def change_frame(self, frame: tk.Frame) -> None:
        pass

    def design(self):
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        self.config(bg = "#000F31")
        self.iconbitmap("img/icon.ico")
        lf.LogoFrame(self)


if __name__ == "__main__":
    import login.login_frame_factory as lff
    mainframe = Window(connect = False)
    mainframe.mainloop()