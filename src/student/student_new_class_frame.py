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
        self.student = scl.StudentClasses()
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#000F31")

    def insert_class(self) -> None:
        name = self.name_entry.get()
        date = self.date_entry.get()
        description = self.description_entry.get()
        max_students = self.max_students_entry.get()
        if (name != "" and
            date != "" and
            description != "" and
            max_students != ""):
            result_query = self.student.insert_class(name, date,
                                                      description, max_students)
            if not result_query:
                warning = el.ErrorLabel(self,
                                    text = "Data no formato 2023-01-01 12:00:00",
                                    pos_x = 300, pos_y = 340, height = 50)
                warning.after(4000, warning.destroy)
            else:
                self.destroy()
        else:
            warning = el.ErrorLabel(self, text = "Preencha todos os campos",
                                    pos_x = 300, pos_y = 340, height = 50)
            warning.after(4000, warning.destroy)
    def validate_int(self, event):
        entry = self.max_students_entry.get()
        if not entry.isdigit():
            self.max_students_entry.delete(0, tk.END)

    def place_objects(self) -> None:
        label = tk.Label(self, text = "Nova aula", font = ("Arial", 24, "bold"),
                         bg = "#000F31", fg = "#FEFAD2")
        
        label.place(x = 400, y = 30, width = 150, height = 30)
        name_label = tk.Label(self, text = "Nome:", font = ("Arial", 16, "bold"),
                              bg = "#000F31", fg = "#FEFAD2")
        name_label.place(x = 200, y = 100, width = 100, height = 30)
        self.name_entry = et.EntryText(self, font = ("Arial", 16, "bold"),
                                        pos_x = 300, pos_y = 100,
                                        width = 400, height = 40)

        date_label = tk.Label(self, text = "Data:", font = ("Arial", 16, "bold"),
                              bg = "#000F31", fg = "#FEFAD2")
        date_label.place(x = 200, y = 160, width = 100, height = 30)
        self.date_entry = et.EntryText(self, font = ("Arial", 16, "bold"),
                                        pos_x = 300, pos_y = 160,
                                        width = 400, height = 40)

        description_label = tk.Label(self, text = "Descrição:",
                                     font = ("Arial", 16, "bold"),
                                     bg = "#000F31", fg = "#FEFAD2")
        description_label.place(x = 180, y = 220, width = 120, height = 30)
        self.description_entry = et.EntryText(self, font = ("Arial", 16, "bold"),
                                                pos_x = 300, pos_y = 220,
                                                width = 400, height = 40)
        
        max_students_label = tk.Label(self, text = "Máximo de alunos:",
                                        font = ("Arial", 16, "bold"),
                                        bg = "#000F31", fg = "#FEFAD2")
        max_students_label.place(x = 100, y = 280, width = 200, height = 30)
        self.max_students_entry = et.EntryText(self, font = ("Arial", 16, "bold"),
                                                pos_x = 300, pos_y = 280,
                                                width = 400, height = 40)
        validation = (self.register(self.validate_int), "%P")
        self.max_students_entry.config(validate = "key",
                            validatecommand = validation)

        create_button = bt.DefaultButton(text = "Criar",
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
        sff.StudentFrameFactory.get_frame("ClassesFrame", self.window)
        super().destroy()


if __name__ == "__main__":
    import main
    main.System().user = 1
    window = wd.Window()
    frame = NewClassFrame(window)
    window.mainloop()