import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.window as wd
import student.student_frame_factory as sff
import gui.buttons as bt


class MenuFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 600, width: int = 240, 
                 pos_x: int = 0, pos_y: int = 0) -> None:
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#DF8350")

    def place_objects(self) -> None:
        menu_label = tk.Label(self, text = "MENU", font = ("Arial", 24, "bold"), 
                              bg = "#DF8350", fg = "#FEFAD2")
        menu_label.place(x = 80, y = 50)

        button_workouts = bt.MenuButton(text = "Meus Treinos", 
                                        command = lambda: self.window.change_frame(sff.StudentFrameFactory.get_frame("WorkoutsFrame", self.window)),
                                        window = self.window, pos_x = 20, pos_y = 150)

        button_progress = bt.MenuButton(text = "Progresso",
                                        command = lambda: self.window.change_frame(sff.StudentFrameFactory.get_frame("ProgressFrame", self.window)),
                                        window = self.window, pos_x = 20, pos_y = 250)

        button_classes = bt.MenuButton(text = "Aulas",
                                        command = lambda: self.window.change_frame(sff.StudentFrameFactory.get_frame("ClassesFrame", self.window)),
                                        window = self.window, pos_x = 20, pos_y = 350)

        button_profile = bt.MenuButton(text = "Perfil",
                                        command = lambda: self.window.change_frame(sff.StudentFrameFactory.get_frame("ProfileFrame", self.window)),
                                        window = self.window, pos_x = 20, pos_y = 450)

    def destroy(self) -> None:
        super().destroy()


if __name__ == "__main__":
    mainframe = wd.Window(connect = False)
    MenuFrame(mainframe)
    mainframe.mainloop()