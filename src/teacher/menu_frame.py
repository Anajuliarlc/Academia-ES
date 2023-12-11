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
        """Creates a MenuFrame object.

        :param window: The Tkinter window object.
        :type window: tk.Tk
        :param height: The height of the frame, defaults to 600.
        :type height: int, optional
        :param width: The width of the frame, defaults to 240.
        :type width: int, optional
        :param pos_x: The x-coordinate position of the frame, defaults to 0.
        :type pos_x: int, optional
        :param pos_y: The y-coordinate position of the frame, defaults to 0.
        :type pos_y: int, optional
        """
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        """Designs the appearance of the MenuFrame."""
        self.config(bg = "#DF8350")

    def button_workouts(self):
        """Handles the button click event for the 'Workouts' button."""
        for frame in self.window.active_frames:
            if type(frame).__name__ != "MenuFrame" and type(frame).__name__ != "LogoFrame":
                frame.destroy()
        tff.TeacherFrameFactory.get_frame("WorkoutsFrame", self.window)

    def button_classes(self):
        """Handles the button click event for the 'Classes' button."""
        for frame in self.window.active_frames:
            if type(frame).__name__ != "MenuFrame" and type(frame).__name__ != "LogoFrame":
                frame.destroy()
        tff.TeacherFrameFactory.get_frame("ClassesFrame", self.window)

    def button_register(self):
        """Handles the button click event for the 'Register' button."""
        for frame in self.window.active_frames:
            if type(frame).__name__ != "MenuFrame" and type(frame).__name__ != "LogoFrame":
                frame.destroy()
        tff.TeacherFrameFactory.get_frame("RegisterFrame", self.window)

    def place_objects(self) -> None:
        """Places the objects within the MenuFrame."""
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

    def destroy(self) -> None:
        """Destroys the MenuFrame."""
        super().destroy()

if __name__ == "__main__":
    mainframe = wd.Window()
    MenuFrame(mainframe)
    mainframe.mainloop()
    