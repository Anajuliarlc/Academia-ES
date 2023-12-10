import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.window as wd
import gui.buttons as bt
import gui.entrytext as et
import teacher.menu_frame as mf
import teacher.teacher_frame_factory as ttf
import teacher.workouts as tw
import main as mn
import gui.errorlabel as el

class NewWorkoutFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 960,
                 pos_x: int = 240, pos_y: int = 200):
        """Creates a new workout frame.

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
        self.system = mn.System()
        self.get_student()
        self.exercises = {}
        super().__init__(window, height, width, pos_x, pos_y)
    

    def design(self):
        """
        This method sets the background color of the widget to "#000F31".
        """
        self.config(bg = "#000F31")

    def verify_entries(self):
        """ Verifies if all entries are filled correctly
        
        :return: True if all entries are filled, False otherwise.
        :rtype: bool
        
        >>> import gui.window as wd
        >>> window = wd.Window(connect = False)
        >>> frame = NewWorkoutFrame(window)
        >>> frame.exercises = {tk.Entry(window): [tk.Entry(window), tk.Entry(window), tk.Entry(window)]}
        >>> frame.verify_entries()
        False
        """
        for exercise, specifications in self.exercises.items():
            if exercise.get() == "":
                return False
            for specification in specifications:
                if specification.get() == "":
                    return False
        return True

    def button_update(self):
        """
        Updates the student's workout in the database.
        """
        if self.verify_entries():
            self.system.database.delete("Exercise", "Where IdUser = '" + self.users[self.name_student.cget("text")] + "';")
            for exercise, specifications in self.exercises.items():
                value = "(NULL, " + self.users[self.name_student.cget("text")] + ", '" + exercise.get() + "', '" + specifications[0].get() + "', '" + specifications[1].get() + "', '" + specifications[2].get() + "')"
                self.system.database.insert("Exercise", value)
            self.destroy()
            ttf.TeacherFrameFactory.get_frame("WorkoutsFrame", self.window)
        else:
            not_filled = el.ErrorLabel(self, text = "Preencha todos os campos", pos_x = 240, pos_y = 250, width = 300, height = 50)

    def button_cancel(self):
        """
        Cancels the current operation and destroys the window.
        """
        self.destroy()
        ttf.TeacherFrameFactory.get_frame("WorkoutsFrame", self.window)

    def get_student(self):
        """
        Retrieves the list of students from the database.
        """
        query = "SELECT u.Iduser, u.UserName FROM User u, Student s WHERE u.Iduser = s.Iduser;"
        self.students = self.system.database.query(query)
        table = self.students.split("s.Iduser;")[1]
        table = table.split("\n")[4:-4]
        table = [line.split("|")[1:-1] for line in table]
        table = [[column.strip() for column in line] for line in table]
        self.users = {}
        for line in table:
                self.users[line[1]] = line[0]


    def place_objects(self):
        """
        Place the objects on the screen.
        """
        exercise_label = tk.Label(self, text = "Exercícios", font = ("Arial", 12, "bold"), 
                      bg = "#000F31", fg = "#DF8350")
        exercise_label.place(x = 260, y = 0)
        weight_label = tk.Label(self, text = "Peso", font = ("Arial", 12, "bold"),
                    bg = "#000F31", fg = "#DF8350")
        weight_label.place(x = 468, y = 0)
        series_label = tk.Label(self, text = "Séries", font = ("Arial", 12, "bold"),
                        bg = "#000F31", fg = "#DF8350")
        series_label.place(x = 522, y = 0)
        repetition_label = tk.Label(self, text = "Rep", font = ("Arial", 12, "bold"),
                        bg = "#000F31", fg = "#DF8350")
        repetition_label.place(x = 585, y = 0)

        self.exercise_entry1 = et.EntryText(self, width = 300, height=30, pos_x = 150, pos_y = 25, font = ("Arial", 16, "bold"))            
        self.weight_entry1 = et.EntryText(self, width = 40, height=30, pos_x = 470, pos_y = 25, font = ("Arial", 16, "bold"))
        self.series_entry1 = et.EntryText(self, width = 40, height=30, pos_x = 530, pos_y = 25, font = ("Arial", 16, "bold"))
        self.repetition_entry1 = et.EntryText(self, width = 40, height=30, pos_x = 585, pos_y = 25, font = ("Arial", 16, "bold"))
        self.exercises[self.exercise_entry1] = [self.weight_entry1, self.series_entry1, self.repetition_entry1]

        self.exercise_entry2 = et.EntryText(self, width = 300, height=30, pos_x = 150, pos_y = 65, font = ("Arial", 16, "bold"))
        self.weight_entry2 = et.EntryText(self, width = 40, height=30, pos_x = 470, pos_y = 65, font = ("Arial", 16, "bold"))
        self.series_entry2 = et.EntryText(self, width = 40, height=30, pos_x = 530, pos_y = 65, font = ("Arial", 16, "bold"))
        self.repetition_entry2 = et.EntryText(self, width = 40, height=30, pos_x = 585, pos_y = 65, font = ("Arial", 16, "bold"))
        self.exercises[self.exercise_entry2] = [self.weight_entry2, self.series_entry2, self.repetition_entry2]

        self.exercise_entry3 = et.EntryText(self, width = 300, height=30, pos_x = 150, pos_y = 105, font = ("Arial", 16, "bold"))
        self.weight_entry3 = et.EntryText(self, width = 40, height=30, pos_x = 470, pos_y = 105, font = ("Arial", 16, "bold"))
        self.series_entry3 = et.EntryText(self, width = 40, height=30, pos_x = 530, pos_y = 105, font = ("Arial", 16, "bold"))
        self.repetition_entry3 = et.EntryText(self, width = 40, height=30, pos_x = 585, pos_y = 105, font = ("Arial", 16, "bold"))
        self.exercises[self.exercise_entry3] = [self.weight_entry3, self.series_entry3, self.repetition_entry3]

        self.exercise_entry4 = et.EntryText(self, width = 300, height=30, pos_x = 150, pos_y = 145, font = ("Arial", 16, "bold"))
        self.weight_entry4 = et.EntryText(self, width = 40, height=30, pos_x = 470, pos_y = 145, font = ("Arial", 16, "bold"))
        self.series_entry4 = et.EntryText(self, width = 40, height=30, pos_x = 530, pos_y = 145, font = ("Arial", 16, "bold"))
        self.repetition_entry4 = et.EntryText(self, width = 40, height=30, pos_x = 585, pos_y = 145, font = ("Arial", 16, "bold"))
        self.exercises[self.exercise_entry4] = [self.weight_entry4, self.series_entry4, self.repetition_entry4]


        clicked = tk.StringVar()
        clicked.set("Nome do aluno")
        self.name_student = tk.OptionMenu(self, clicked, * self.users.keys())
        self.name_student.config(background='#E29E6C', foreground='#FEFAD2', activebackground='#DF8350', font = ("Arial", 12, "bold"), fg='#FEFAD2', borderwidth=2, highlightbackground="#000F31")
        self.name_student.place(x = 642, y = 25, height = 50, width = 300)

        self.button_save = bt.DefaultButton(text = "Salvar", command = self.button_update, window = self, pos_x = 690, pos_y = 165, width = 200, height = 50)
        self.button_exit = bt.DefaultButton(text = "Cancelar", command = self.button_cancel, window = self, pos_x = 690, pos_y = 285, width = 200, height = 50)


        
    def destroy(self):
        """
        Destroys the object.
        """
        super().destroy()


if __name__ == "__main__":
    # mainframe = wd.Window()
    # mf.MenuFrame(mainframe)
    # tw.InitialWorkoutsFrame(mainframe)
    # NewWorkoutFrame(mainframe)
    # mainframe.mainloop()
    
    import doctest
    doctest.testmod(verbose=True)
