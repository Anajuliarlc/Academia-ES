import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.window as wd
import student.student_frame_factory as sff
import gui.buttons as bt


class ProfileFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 600, width: int = 240, 
                 pos_x: int = 0, pos_y: int = 0) -> None:
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#DF8350")

    def place_objects(self) -> None:
        # student info

        button_increase = bt.DefaultButton(text = "Cadastrar Cartão", 
                                        command = lambda: self.window.change_frame(sff.StudentFrameFactory.get_frame("RegisterPaymentMethodFrame", self.window)),
                                        window = self.window, pos_x = 750, pos_y = 250)

    def destroy(self) -> None:
        super().destroy()

if __name__ == "__main__":
    mainframe = wd.Window(connect = False)
    ProfileFrame(mainframe)
    mainframe.mainloop()