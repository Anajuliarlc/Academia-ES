import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.window as wd
import student.student_frame_factory as sff


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

        button_workouts = tk.Button(self, text = "Meus treinos", font = ("Arial", 18), 
                                    bg = "#E29E6C", fg = "#FEFAD2", borderwidth=2, 
                                    highlightbackground="#000F31", 
                                    command = lambda: sff.StudentFrameFactory("WorkoutsFrame", self.master))
        button_workouts.place(x = 20, y = 150, width = 200, height = 50)

        button_progress = tk.Button(self, text = "Progresso", font = ("Arial", 18),
                                    bg = "#E29E6C", fg = "#FEFAD2", borderwidth=2, 
                                    highlightbackground="#000F31", 
                                    command = lambda: sff.StudentFrameFactory("ProgressFrame", self.master))
        button_progress.place(x = 20, y = 250, width = 200, height = 50)

        button_classes = tk.Button(self, text = "Aulas", font = ("Arial", 18),
                                   bg = "#E29E6C", fg = "#FEFAD2", borderwidth=2, 
                                   highlightbackground="#000F31", 
                                   command = lambda: sff.StudentFrameFactory("ClassesFrame", self.master))
        button_classes.place(x = 20, y = 350, width = 200, height = 50)

        button_profile = tk.Button(self, text = "Perfil", font = ("Arial", 18),
                                   bg = "#E29E6C", fg = "#FEFAD2", borderwidth=2, 
                                   highlightbackground="#000F31", 
                                   command = lambda: sff.StudentFrameFactory("ProfileFrame", self.master))
        button_profile.place(x = 20, y = 450, width = 200, height = 50)


    def destroy(self) -> None:
        super().destroy()


if __name__ == "__main__":
    mainframe = wd.Window(connect = False)
    MenuFrame(mainframe)
    mainframe.mainloop()