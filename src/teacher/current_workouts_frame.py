import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.window as wd
import gui.buttons as bt
import teacher.menu_frame as mf
import gui.table as tb
import main
import pandas as pd
import teacher.teacher_frame_factory as ttf

class CurrentWorkouts(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 960,
                 pos_x: int = 240, pos_y: int = 200):
        """Create a frame to be used as login in the application """
        super().__init__(window, height, width, pos_x, pos_y)
        self.error_label = None
    
    def design(self):
        self.config(bg = "#000F31")

    def get_student(self):
        self.system = main.System()
        query = "SELECT u.Iduser, u.UserName FROM User u, Student s WHERE u.Iduser = s.Iduser;"
        self.students = self.system.database.query(query)
        table = self.students.split("s.Iduser;")[1]
        table = table.split("\n")[4:-4]
        table = [line.split("|")[1:-1] for line in table]
        table = [[column.strip() for column in line] for line in table]
        self.users = {}
        for line in table:
            self.users[line[1]] = line[0]

        return self.users

    def button_load_workouts(self):
        if self.error_label != None:
            self.error_label.destroy()

        if self.clicked.get() != "Escolha um aluno":
            id_selected_user = self.students[self.clicked.get()]
            student_df = self.system.database.select("Exercise",
                                                     "*",
                                                     "WHERE Iduser = " + id_selected_user)
            student_df = student_df[["ExerciseName",
                                     "SerNum", "RepNum",
                                     "WeightExercise"]].rename(columns = {"ExerciseName": "Exercício",
                                                                          "SerNum": "Séries",
                                                                          "RepNum": "Repetições",
                                                                          "WeightExercise": "Peso"})
            self.table = tb.Table(self, student_df, width= 600, height= 200,
                                    pos_x= 280, pos_y= 100)
        else:
            self.error_label = tk.Label(self, text = "Escolha um aluno",
                                        font = ("Arial", 20, "bold"), 
                                        bg = "#000F31", fg = "#FEFAD2",
                                        width= 600, height= 200)
            self.error_label.place(x = 280, y = 100)

    def button_cancel(self):
        self.destroy()
        ttf.TeacherFrameFactory.get_frame("WorkoutsFrame", self.window)

    def place_objects(self):
        self.title_label = tk.Label(self, text = "Treinos atuais", 
                                    font = ("Arial", 20, "bold"), 
                                    bg = "#000F31", fg = "#FEFAD2")
        self.title_label.place(x = 230, y = 0, height = 30, width = 400)

        self.students = self.get_student()
    
        # drop-down menu
        self.clicked = tk.StringVar()
        self.clicked.set("Escolha um aluno")

        self.drop = tk.OptionMenu(self, self.clicked, *self.students.keys())
        
        self.drop.config(background='#E29E6C', foreground='#FEFAD2', activebackground='#DF8350')
        self.drop.place(x=60, y=100, width=200, height=50)

        self.buttun_load = bt.DefaultButton(text = "Carregar", 
                         command= self.button_load_workouts, 
                         window = self.window, pos_x = 300, pos_y = 400,
                         height = 50, width = 200)
        self.button_exit = bt.DefaultButton(text = "Cancelar",
                                            command = self.button_cancel,
                                            window = self, pos_x = 60,
                                            pos_y = 300, width = 200,
                                            height = 50)
        
    def destroy(self):
        super().destroy()

if __name__ == "__main__":
    mainframe = wd.Window(connect = False)
    mf.MenuFrame(mainframe)
    CurrentWorkouts(mainframe)
    mainframe.mainloop()