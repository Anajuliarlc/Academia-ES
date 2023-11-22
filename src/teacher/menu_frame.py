import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.window as wd
import teacher.teacher_frame_factory as tff
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

        button_workouts = bt.MenuButton(text = "Treinos", 
                                        command = lambda: self.window.change_frame(tff.TeacherFrameFactory.get_frame("WorkoutsFrame", self.window)),
                                        window = self.window, pos_x = 20, pos_y = 200)
        
        button_classes = bt.MenuButton(text = "Aulas", 
                                       command = lambda: self.window.change_frame(tff.TeacherFrameFactory.get_frame("ClassesFrame", self.window)),
                                       window = self.window, pos_x = 20, pos_y = 300)

        button_register = bt.MenuButton(text = "Matrículas", 
                                        command = lambda: tff.TeacherFrameFactory.get_frame("RegisterFrame", self.window),
                                        window = self.window, pos_x = 20, pos_y = 400)

    def destroy(self) -> None:
        super().destroy() 

if __name__ == "__main__":
    mainframe = wd.Window(connect = False)
    MenuFrame(mainframe)
    mainframe.mainloop()
    