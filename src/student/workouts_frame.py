import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.window as wd
import gui.buttons as bt
import student.student_frame_factory as sff

class WorkoutsFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 960, 
                 pos_x: int = 240, pos_y: int = 200) -> None:
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#000F31")
    

    def button_request_change(self) -> None:
        for frame in self.window.active_frames:
                if type(frame).__name__ != "MenuFrame" and type(frame).__name__ != "LogoFrame":
                    frame.destroy()
        sff.StudentFrameFactory.get_frame("RequestChangeFrame", frame.window)

    def button_increase(self) -> None:
        for frame in self.window.active_frames:
                if type(frame).__name__ != "MenuFrame" and type(frame).__name__ != "LogoFrame":
                    frame.destroy()
        sff.StudentFrameFactory.get_frame("IncreaseFrame", frame.window)

    def place_objects(self) -> None:
        self.button_increase = bt.DefaultButton(text = "Progredir Cargas", 
                                        command = self.button_increase,
                                        window = self, pos_x = 60, pos_y = 50)

        self.button_request_change = bt.DefaultButton(text = "Solicitar alteração",
                                        command = self.button_request_change,
                                        window = self, pos_x = 510, pos_y = 50)
        

    def destroy(self) -> None:
        super().destroy()

if __name__ == "__main__":
    mainframe = wd.Window()
    WorkoutsFrame(mainframe)
    mainframe.mainloop()