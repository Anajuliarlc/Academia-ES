import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.window as wd
import student.student_frame_factory as sff
import gui.entrytext as et
import gui.buttons as bt
import gui.errorlabel as el
import student.student_classes as scl

class NewClassFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 960,
                  pos_x: int = 240, pos_y: int = 200) -> None:
        """Creates a new instance of the NewClassFrame class.

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
        self.student = scl.StudentClasses()
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        """Designs the appearance of the frame.
        """
        self.config(bg = "#000F31")

    def insert_class(self) -> None:
        """Inserts a new class into the database.
        """
        idclass = self.classes["IdClass"][self.classes["ClassName"] == self.name.get()]
        IdTeacher = self.classes["IdUser"][self.classes["ClassName"] == self.name.get()]
        idStudent = self.student.system.user
        table = "Take (IdClass, IdTeacher, IdStudent)"
        values = f"({idclass.iloc[0]}, {IdTeacher.iloc[0]}, {idStudent})"
        return_query = self.student.system.database.insert(table, values)
        if "ERROR" in return_query:
            self.warning = el.ErrorLabel(self, text = "Erro ao inserir a aula.",
                                         pos_x = 350, pos_y = 400)
        else:
            self.destroy()

    def change_label(self, event = None):
        """Changes the label of the class.
        """
        class_name = self.name.get()
        date = self.classes["ClassDate"][self.classes["ClassName"] == class_name]
        self.date.set(date.iloc[0] if not date.empty else "")

        description = self.classes["ClassDescription"][self.classes["ClassName"] == class_name]
        self.description.set(description.iloc[0] if not description.empty else "")

        max_students = self.classes["StudentsMax"][self.classes["ClassName"] == class_name]
        self.max_students.set(max_students.iloc[0] if not max_students.empty else "")

        self.date_entry.config(text=self.date.get())
        self.description_entry.config(text=self.description.get())
        self.max_students_entry.config(text=self.max_students.get())

    def place_objects(self) -> None:
        """Places the objects within the frame.
        """
        self.classes = self.student.get_all_classes()
        label = tk.Label(self, text = "Nova aula", font = ("Arial", 24, "bold"),
                         bg = "#000F31", fg = "#FEFAD2")
        
        label.place(x = 400, y = 30, width = 150, height = 30)
        name_label = tk.Label(self, text = "Nome:", font = ("Arial", 16, "bold"),
                              bg = "#000F31", fg = "#FEFAD2")
        name_label.place(x = 200, y = 100, width = 100, height = 20)

        self.name = tk.StringVar()
        self.name.set(self.classes["ClassName"][0])
        self.name_drop = tk.OptionMenu(self, self.name,
                                        *self.classes["ClassName"],
                                        command = self.change_label)
        self.name_drop.config(background='#E29E6C', foreground='#FEFAD2',
                                                    activebackground='#DF8350')
        self.name_drop.place(x = 300, y = 100, width = 400, height = 30)

        date_label = tk.Label(self, text = "Data:", font = ("Arial", 16, "bold"),
                              bg = "#000F31", fg = "#FEFAD2")
        date_label.place(x = 200, y = 150, width = 100, height = 20)

        self.date = tk.StringVar()
        self.date.set(self.classes["ClassDate"][0])
        self.date_entry = tk.Label(self,
                                    text = self.date.get(),
                                    font = ("Arial", 16, "bold"),
                                    bg = "#DF8350",
                                    fg = "#FEFAD2")
        self.date_entry.place(x = 300, y = 150, width = 400, height = 30)
        
        max_students_label = tk.Label(self, text = "Máximo de alunos:",
                                        font = ("Arial", 16, "bold"),
                                        bg = "#000F31", fg = "#FEFAD2")
        max_students_label.place(x = 100, y = 200, width = 200, height = 20)

        self.max_students = tk.StringVar()
        self.max_students.set(self.classes["StudentsMax"][0])
        self.max_students_entry = tk.Label(self,
                                    text = self.max_students.get(),
                                    font = ("Arial", 16, "bold"),
                                    bg = "#DF8350",
                                    fg = "#FEFAD2")
        self.max_students_entry.place(x = 300, y = 200, width = 400, height = 30)

        description_label = tk.Label(self, text = "Descrição:",
                                     font = ("Arial", 16, "bold"),
                                     bg = "#000F31", fg = "#FEFAD2")
        description_label.place(x = 180, y = 280, width = 120, height = 20)

        self.description = tk.StringVar()
        self.description.set(self.classes["ClassDescription"][0])
        self.description_entry = tk.Label(self,
                                    text = self.description.get(),
                                    font = ("Arial", 16, "bold"),
                                    bg = "#DF8350",
                                    fg = "#FEFAD2",
                                    wraplength = 400)
        self.description_entry.place(x = 300, y = 250, width = 400, height = 80)
        
        create_button = bt.DefaultButton(text = "Entrar",
                                         command = self.insert_class,
                                         window = self, pos_x = 350, pos_y = 350,
                                         font = ("Arial", 16, "bold"),
                                         width = 100, height = 30)
    
        cancel_button = bt.DefaultButton(text = "Cancelar",
                                         command = self.destroy,
                                         window = self, pos_x = 550, pos_y = 350,
                                         font = ("Arial", 16, "bold"),
                                         width = 100, height = 30)

    def destroy(self) -> None:
        """Destroys the current frame and returns to the ClassesFrame.
        """
        sff.StudentFrameFactory.get_frame("ClassesFrame", self.window)
        super().destroy()


if __name__ == "__main__":
    import main
    main.System().user = 1
    window = wd.Window()
    frame = NewClassFrame(window)
    window.mainloop()
