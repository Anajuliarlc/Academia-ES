import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.window as wd
import gui.buttons as bt
import teacher.class_frame as cf
import teacher.teacher_frame_factory as tff

class ClassesFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 960, 
                 pos_x: int = 240, pos_y: int = 200) -> None:
        self.classes = []
        self.init_class = 0
        self.end_class = 2
        self.actual_classes = {}
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#000F31")

    def change_classes(self, right: bool = True) -> None:
        for i in range(self.init_class, self.end_class):
            self.actual_classes[i].destroy()
            self.actual_classes.pop(i)
        if right and (self.end_class < len(self.classes) - 1):
            self.init_class += 1
            self.end_class += 1
        elif (not right) and self.init_class > 0:
            self.init_class -= 1
            self.end_class -= 1

        self.place_classes()

    def place_classes(self) -> None:
        classes = [["Aula 1", "01/01/2021", "Descrição da aula 1"],
                   ["Aula 2", "02/01/2021", "Descrição da aula 2"],
                   ["Aula 3", "03/01/2021", "Descrição da aula 3"],
                   ["Aula 4", "03/01/2021", "Descrição da aula 3"]]
        self.classes = classes
        for i in range(self.init_class, self.end_class + 1):
            pos_x = 100 + 280*(i - self.init_class)
            class_i = cf.Class(self, self.classes[i][0], self.classes[i][1],
                                self.classes[i][2], pos_x = pos_x,
                                pos_y = 80)
            self.actual_classes[i] = class_i
    
    def open_new_class(self) -> None:
        tff.TeacherFrameFactory.get_frame("NewClass", self.window)

    def place_objects(self) -> None:
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
        return super().destroy()
    
if __name__ == "__main__":
    mainframe = wd.Window(connect = False)
    ClassesFrame(mainframe)
    mainframe.mainloop()