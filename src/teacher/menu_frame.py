import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.window as wd
import teacher.teacher_frame_factory as tff


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

        button_workouts = tk.Button(self, text = "Treinos", font = ("Arial", 18), 
                                    bg = "#E29E6C", fg = "#FEFAD2", borderwidth=2, 
                                    highlightbackground="#000F31", 
                                    command = lambda: tff.TeacherFrameFactory("WorkoutsFrame", self.master))
        button_workouts.place(x = 20, y = 200, width = 200, height = 50)

        button_classes = tk.Button(self, text = "Aulas", font = ("Arial", 18),
                                   bg = "#E29E6C", fg = "#FEFAD2", borderwidth=2, 
                                   highlightbackground="#000F31", 
                                   command = lambda: tff.TeacherFrameFactory("ClassesFrame", self.master))
        button_classes.place(x = 20, y = 300, width = 200, height = 50)

        button_register = tk.Button(self, text = "Matrículas", font = ("Arial", 18),
                                   bg = "#E29E6C", fg = "#FEFAD2", borderwidth=2, 
                                   highlightbackground="#000F31", 
                                   command = lambda: tff.TeacherFrameFactory("RegisterFrame", self.master))
        button_register.place(x = 20, y = 400, width = 200, height = 50)


    def destroy(self) -> None:
        super().destroy()


if __name__ == "__main__":
    mainframe = wd.Window(connect = False)
    MenuFrame(mainframe)
    mainframe.mainloop()