import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.window as wd
import student.student_frame_factory as sff
import gui.buttons as bt
import login.login_frame_factory as lff

class MenuFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 600, width: int = 240, 
                 pos_x: int = 0, pos_y: int = 0) -> None:
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#DF8350")

    def button_workouts(self):
        for frame in self.window.active_frames:
            if type(frame).__name__ != "MenuFrame" and type(frame).__name__ != "LogoFrame":
                frame.destroy()
        sff.StudentFrameFactory.get_frame("WorkoutsFrame", self.window)

    def button_progress(self):
        for frame in self.window.active_frames:
            if type(frame).__name__ != "MenuFrame" and type(frame).__name__ != "LogoFrame":
                frame.destroy()
        sff.StudentFrameFactory.get_frame("ProgressFrame", self.window)

    def button_classes(self):
        for frame in self.window.active_frames:
            if type(frame).__name__ != "MenuFrame" and type(frame).__name__ != "LogoFrame":
                frame.destroy()
        sff.StudentFrameFactory.get_frame("ClassesFrame", self.window)

    def button_profile(self):
        for frame in self.window.active_frames:
            if type(frame).__name__ != "MenuFrame" and type(frame).__name__ != "LogoFrame":
                frame.destroy()
        sff.StudentFrameFactory.get_frame("ProfileFrame", self.window)

    def button_logout(self):
        for frame in self.window.active_frames:
            if type(frame).__name__ != "LogoFrame":
                frame.destroy()
        lff.LoginFrameFactory.get_frame("LoginFrame", self.window)

    def place_objects(self) -> None:
        menu_label = tk.Label(self, text = "MENU", font = ("Arial", 24, "bold"), 
                              bg = "#DF8350", fg = "#FEFAD2")
        menu_label.place(x = 70, y = 50)

        button_workouts = bt.MenuButton(text = "Meus Treinos", 
                                        command = self.button_workouts,
                                        window = self.window, pos_x = 20, pos_y = 150)

        button_progress = bt.MenuButton(text = "Progresso",
                                        command = self.button_progress,
                                        window = self, pos_x = 20, pos_y = 240)

        button_classes = bt.MenuButton(text = "Aulas",
                                        command = self.button_classes,
                                        window = self, pos_x = 20, pos_y = 330)

        button_profile = bt.MenuButton(text = "Perfil",
                                        command = self.button_profile,
                                        window = self.window, pos_x = 20, pos_y = 420)
        
        button_logout = bt.MenuButton(text = "Sair", 
                                      command = self.button_logout,
                                      window = self, pos_x = 20, pos_y = 510)

    def destroy(self) -> None:
        super().destroy()


if __name__ == "__main__":
    mainframe = wd.Window(connect = True)
    MenuFrame(mainframe)
    mainframe.mainloop()