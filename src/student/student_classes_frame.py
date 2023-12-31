import sys
sys.path.append("./src")

import tkinter as tk
import gui.frame as fr
import gui.window as wd
import gui.buttons as bt
import student.student_class_frame as scf
import student.student_frame_factory as sff
import student.student_classes as scl

class StudentClassesFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 960, 
                 pos_x: int = 240, pos_y: int = 200) -> None:
        """Initialize the StudentClassesFrame.

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
        self.classes = []
        self.init_class = 0
        self.end_class = 2
        self.actual_classes = {}
        self.classes_functions = scl.StudentClasses()
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        """Design the frame.
        """
        self.config(bg = "#000F31")

    def change_classes(self, right: bool = True) -> None:
        """Change the displayed classes.

        :param right: If True, move to the next set of classes. If False, move to the previous set of classes.
        :type right: bool, optional
        """
        for i in range(self.init_class, self.end_class):
            self.actual_classes[i].destroy()
            self.actual_classes.pop(i)
        if right and (self.end_class < len(self.classes)):
            self.init_class += 1
            self.end_class += 1
        elif (not right) and self.init_class > 1:
            self.init_class -= 1
            self.end_class -= 1

        self.place_classes()

    def place_classes(self) -> None:
        """Place the classes on the frame.
        """
        self.classes = self.classes_functions.get_classes()

        size = len(self.classes)
        if size < 3:
            self.end_class = self.init_class + size
        else:
            self.end_class = self.init_class + 3

        for i in range(self.init_class, self.end_class):
            pos_x = 100 + 280*(i - self.init_class)
            class_name = self.classes["ClassName"][i]
            class_date = self.classes["ClassDate"][i]
            class_description = self.classes["ClassDescription"][i]
            class_i = scf.StudentClass(self, class_name, class_date,
                                       class_description, pos_x = pos_x, pos_y = 80)
            self.actual_classes[i] = class_i
    
    def open_new_class(self) -> None:
        """Open the frame to create a new class.
        """
        self.destroy()
        sff.StudentFrameFactory.get_frame("NewClass", self.window)

    def place_objects(self) -> None:
        """Place the objects on the frame.
        """
        label = tk.Label(self, text = "Aulas", font = ("Arial", 24, "bold"), 
                         bg = "#000F31", fg = "#FEFAD2")
        label.place(x = 425, y = 30, width = 100, height = 30)
        new_class_button = bt.DefaultButton(text = "Nova aula", 
                                         command = self.open_new_class,
                                         window = self, pos_x = 380, pos_y = 360,
                                         font = ("Arial", 20, "bold"),
                                         width = 200, height = 30)
        self.place_classes()

        right_button = bt.DefaultButton(text = ">",
                                         command = self.change_classes,
                                         window = self, pos_x = 20, pos_y = 100)
        right_button.place(x = 900, y = 155, width = 30, height = 100)
        left_button = bt.DefaultButton(text = "<",
                                command = lambda: self.change_classes(False),
                                window = self, pos_x = 20, pos_y = 100)
        left_button.place(x = 30, y = 155, width = 30, height = 100)


    def destroy(self) -> None:
        """Destroy the frame.
        """
        return super().destroy()
    
if __name__ == "__main__":
    mainframe = wd.Window()
    StudentClassesFrame(mainframe)
    mainframe.mainloop()
