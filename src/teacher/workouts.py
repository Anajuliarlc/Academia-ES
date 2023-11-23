import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.window as wd
import gui.buttons as bt
import teacher.menu_frame as mf
import teacher.teacher_frame_factory as ttf

class InitialWorkoutsFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 960,
                 pos_x: int = 240, pos_y: int = 200):
        """Create a frame to be used as login in the application """
        super().__init__(window, height, width, pos_x, pos_y)
    
    def design(self):
        self.config(bg = "#000F31")

    def button_new_workout(self):
        for frame in self.window.active_frames:
            if type(frame).__name__ != "MenuFrame" and type(frame).__name__ != "LogoFrame":
                frame.destroy()
        ttf.TeacherFrameFactory.get_frame("NewWorkoutFrame", self.window)

    def button_workout(self):
        for frame in self.window.active_frames:
            if type(frame).__name__ != "MenuFrame" and type(frame).__name__ != "LogoFrame":
                frame.destroy()
        ttf.TeacherFrameFactory.get_frame("CurrentWorkoutsFrame", self.window)

    def button_current_workouts(self):
        for frame in self.window.active_frames:
            if type(frame).__name__ != "MenuFrame" and type(frame).__name__ != "LogoFrame":
                frame.destroy()
        tff.TeacherFrameFactory.get_frame("CurrentWorkoutsFrame", self.window)

    def place_objects(self):
        button_new_workout = bt.DefaultButton(text = "Novo Treino", 
                         command= self.button_new_workout, 
                          window = self.window, pos_x = 340, pos_y = 300)
        button_workout = bt.DefaultButton(text = "Treinos atuais", 
                         command= self.button_workout, 
                          window = self.window, pos_x = 740, pos_y = 300)
        
    def destroy(self):
        super().destroy()

if __name__ == "__main__":
    mainframe = wd.Window(connect = False)
    mf.MenuFrame(mainframe)
    InitialWorkoutsFrame(mainframe)
    mainframe.mainloop()