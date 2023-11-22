import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.window as wd
import student.student_frame_factory as sff
import gui.buttons as bt


class WorkoutsFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 960, 
                 pos_x: int = 240, pos_y: int = 200) -> None:
        super().__init__(window, height, width, pos_x, pos_y)

    
    def request_change(self) -> None:
        sff.StudentFrameFactory.get_frame("RequestChangeFrame", self.window)
        self.destroy()

    def design(self) -> None:
        self.config(bg = "#000F31")

    def place_objects(self) -> None:
        def go_to_increase() -> None:
            sff.StudentFrameFactory.get_frame("IncreaseFrame", self.window)
            self.destroy()

        self.button_increase = bt.DefaultButton(text = "Progredir Cargas", 
                                        command = lambda: go_to_increase(),
                                        window = self, pos_x = 60, pos_y = 50)

        self.button_request_change = bt.DefaultButton(text = "Solicitar alteração",
                                        command = self.request_change,
                                        window = self, pos_x = 510, pos_y = 50)
        

    def destroy(self) -> None:
        super().destroy()

if __name__ == "__main__":
    mainframe = wd.Window(connect = False)
    WorkoutsFrame(mainframe)
    mainframe.mainloop()