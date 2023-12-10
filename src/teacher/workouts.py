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
        """Initializes the InitialWorkoutsFrame class.

        :param window: The Tkinter window object.
        :type window: tk.Tk
        :param height: The height of the frame, defaults to 400.
        :type height: int, optional
        :param width: The width of the frame, defaults to 960.
        :type width: int, optional
        :param pos_x: The x-coordinate position of the frame, defaults to 240.
        :type pos_x: int, optional
        :param pos_y: The y-coordinate position of the frame, defaults to 200.
        :type pos_y: int, optional
        """
        super().__init__(window, height, width, pos_x, pos_y)
    
    def design(self):
        """Designs the frame.
        """
        self.config(bg = "#000F31")

    def button_new_workout(self):
        """Handles the button click event for creating a new workout.
        """
        for frame in self.window.active_frames:
            if type(frame).__name__ != "MenuFrame" and type(frame).__name__ != "LogoFrame":
                frame.destroy()
        ttf.TeacherFrameFactory.get_frame("NewWorkoutFrame", self.window)

    def button_current_workouts(self):
        """Handles the button click event for viewing current workouts.
        """
        for frame in self.window.active_frames:
            if type(frame).__name__ != "MenuFrame" and type(frame).__name__ != "LogoFrame":
                frame.destroy()
        ttf.TeacherFrameFactory.get_frame("CurrentWorkoutsFrame", self.window)

    def place_objects(self):
        """Places the objects within the frame.
        """
        button_new_workout = bt.DefaultButton(text = "Novo Treino", 
                         command= self.button_new_workout, 
                          window = self.window, pos_x = 340, pos_y = 300)
        button_workout = bt.DefaultButton(text = "Treinos atuais", 
                         command= self.button_current_workouts, 
                          window = self.window, pos_x = 740, pos_y = 300)
        
    def destroy(self):
        """Destroys the frame.
        """
        super().destroy()

if __name__ == "__main__":
    mainframe = wd.Window()
    mf.MenuFrame(mainframe)
    InitialWorkoutsFrame(mainframe)
    mainframe.mainloop()