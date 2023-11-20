import tkinter as tk
import sys
sys.path.append("./src")
import db.db_connector as db

class Window(tk.Tk):
    def __init__(self, title: str = "Chi-Trapzeio", height: int = 800, width: int = 1000,
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

    def design(self):
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        self.config(bg = "#000000")
        self.iconbitmap("img/icon.ico")


if __name__ == "__main__":
    import login.login_frame_factory as lff
    mainframe = Window(connect = False)
    lff.LoginFrameFactory("ExampleFrame", mainframe)
    mainframe.mainloop()