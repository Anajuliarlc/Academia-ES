import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.window as wd
import teacher.teacher_frame_factory as tff
import gui.buttons as bt
import login.login_frame_factory as lff
import gui.logo_frame as lf

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
        tff.TeacherFrameFactory.get_frame("WorkoutsFrame", self.window)

    def button_classes(self):
        for frame in self.window.active_frames:
            if type(frame).__name__ != "MenuFrame" and type(frame).__name__ != "LogoFrame":
                frame.destroy()
        tff.TeacherFrameFactory.get_frame("ClassesFrame", self.window)

    def button_register(self):
        for frame in self.window.active_frames:
            if type(frame).__name__ != "MenuFrame" and type(frame).__name__ != "LogoFrame":
                frame.destroy()
        tff.TeacherFrameFactory.get_frame("RegisterFrame", self.window)

    def button_logout(self):
        for frame in self.window.active_frames:
            if type(frame).__name__ != "LogoFrame":
                frame.destroy()
        lf.LogoFrame(self.window)
        lff.LoginFrameFactory.get_frame("LoginFrame", self.window)
        

    def place_objects(self) -> None:
        menu_label = tk.Label(self, text = "MENU", font = ("Arial", 24, "bold"), 
                              bg = "#DF8350", fg = "#FEFAD2")
        menu_label.place(x = 70, y = 50)

        button_workouts = bt.MenuButton(text = "Treinos", 
                                        command = self.button_workouts, 
                                        window = self, pos_x = 20, pos_y = 200)
        
        button_classes = bt.MenuButton(text = "Aulas", 
                                       command = self.button_classes,
                                       window = self, pos_x = 20, pos_y = 300)

        button_register = bt.MenuButton(text = "Matrículas", 
                                        command = self.button_register,
                                        window = self, pos_x = 20, pos_y = 400)
        
        button_logout = bt.MenuButton(text = "Sair", 
                                      command = self.button_logout,
                                      window = self, pos_x = 20, pos_y = 500)

    def destroy(self) -> None:
        super().destroy() 

if __name__ == "__main__":
    mainframe = wd.Window()
    MenuFrame(mainframe)
    mainframe.mainloop()
    