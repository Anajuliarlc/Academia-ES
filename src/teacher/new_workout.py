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

class NewWorkoutFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 960,
                 pos_x: int = 240, pos_y: int = 200):
        """Create a frame to be used as login in the application """
        super().__init__(window, height, width, pos_x, pos_y)
    

    def design(self):
        self.config(bg = "#000F31")

    def place_objects(self):
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

        exercise_entry1 = et.EntryText(self, width = 300, height=30, pos_x = 150, pos_y = 25, font = ("Arial", 16, "bold"))            
        weight_entry1 = et.EntryText(self, width = 40, height=30, pos_x = 470, pos_y = 25, font = ("Arial", 16, "bold"))
        series_entry1 = et.EntryText(self, width = 40, height=30, pos_x = 530, pos_y = 25, font = ("Arial", 16, "bold"))
        repetition_entry1 = et.EntryText(self, width = 40, height=30, pos_x = 585, pos_y = 25, font = ("Arial", 16, "bold"))

        exercise_entrey2 = et.EntryText(self, width = 300, height=30, pos_x = 150, pos_y = 65, font = ("Arial", 16, "bold"))
        weight_entry2 = et.EntryText(self, width = 40, height=30, pos_x = 470, pos_y = 65, font = ("Arial", 16, "bold"))
        series_entry2 = et.EntryText(self, width = 40, height=30, pos_x = 530, pos_y = 65, font = ("Arial", 16, "bold"))
        repetition_entry2 = et.EntryText(self, width = 40, height=30, pos_x = 585, pos_y = 65, font = ("Arial", 16, "bold"))

        exercise_entrey3 = et.EntryText(self, width = 300, height=30, pos_x = 150, pos_y = 105, font = ("Arial", 16, "bold"))
        weight_entry3 = et.EntryText(self, width = 40, height=30, pos_x = 470, pos_y = 105, font = ("Arial", 16, "bold"))
        series_entry3 = et.EntryText(self, width = 40, height=30, pos_x = 530, pos_y = 105, font = ("Arial", 16, "bold"))
        repetition_entry3 = et.EntryText(self, width = 40, height=30, pos_x = 585, pos_y = 105, font = ("Arial", 16, "bold"))

        exercise_entrey4 = et.EntryText(self, width = 300, height=30, pos_x = 150, pos_y = 145, font = ("Arial", 16, "bold"))
        weight_entry4 = et.EntryText(self, width = 40, height=30, pos_x = 470, pos_y = 145, font = ("Arial", 16, "bold"))
        series_entry4 = et.EntryText(self, width = 40, height=30, pos_x = 530, pos_y = 145, font = ("Arial", 16, "bold"))
        repetition_entry4 = et.EntryText(self, width = 40, height=30, pos_x = 585, pos_y = 145, font = ("Arial", 16, "bold"))

        exercise_entrey5 = et.EntryText(self, width = 300, height=30, pos_x = 150, pos_y = 185, font = ("Arial", 16, "bold"))
        weight_entry5 = et.EntryText(self, width = 40, height=30, pos_x = 470, pos_y = 185, font = ("Arial", 16, "bold"))
        series_entry5 = et.EntryText(self, width = 40, height=30, pos_x = 530, pos_y = 185, font = ("Arial", 16, "bold"))
        repetition_entry5 = et.EntryText(self, width = 40, height=30, pos_x = 585, pos_y = 185, font = ("Arial", 16, "bold"))

        exercise_entrey6 = et.EntryText(self, width = 300, height=30, pos_x = 150, pos_y = 225, font = ("Arial", 16, "bold"))
        weight_entry6 = et.EntryText(self, width = 40, height=30, pos_x = 470, pos_y = 225, font = ("Arial", 16, "bold"))
        series_entry6 = et.EntryText(self, width = 40, height=30, pos_x = 530, pos_y = 225, font = ("Arial", 16, "bold"))
        repetition_entry6 = et.EntryText(self, width = 40, height=30, pos_x = 585, pos_y = 225, font = ("Arial", 16, "bold"))

        exercise_entrey7 = et.EntryText(self, width = 300, height=30, pos_x = 150, pos_y = 265, font = ("Arial", 16, "bold"))
        weight_entry7 = et.EntryText(self, width = 40, height=30, pos_x = 470, pos_y = 265, font = ("Arial", 16, "bold"))
        series_entry7 = et.EntryText(self, width = 40, height=30, pos_x = 530, pos_y = 265, font = ("Arial", 16, "bold"))
        repetition_entry7 = et.EntryText(self, width = 40, height=30, pos_x = 585, pos_y = 265, font = ("Arial", 16, "bold"))

        exercise_entrey8 = et.EntryText(self, width = 300, height=30, pos_x = 150, pos_y = 305, font = ("Arial", 16, "bold"))
        weight_entry8 = et.EntryText(self, width = 40, height=30, pos_x = 470, pos_y = 305, font = ("Arial", 16, "bold"))
        series_entry8 = et.EntryText(self, width = 40, height=30, pos_x = 530, pos_y = 305, font = ("Arial", 16, "bold"))
        repetition_entry8 = et.EntryText(self, width = 40, height=30, pos_x = 585, pos_y = 305, font = ("Arial", 16, "bold"))

        exercise_entrey9 = et.EntryText(self, width = 300, height=30, pos_x = 150, pos_y = 345, font = ("Arial", 16, "bold"))
        weight_entry9 = et.EntryText(self, width = 40, height=30, pos_x = 470, pos_y = 345, font = ("Arial", 16, "bold"))
        series_entry9 = et.EntryText(self, width = 40, height=30, pos_x = 530, pos_y = 345, font = ("Arial", 16, "bold"))
        repetition_entry9 = et.EntryText(self, width = 40, height=30, pos_x = 585, pos_y = 345, font = ("Arial", 16, "bold"))

        clicked = tk.StringVar()
        clicked.set("Nome do aluno")
        name_student = tk.OptionMenu(self, clicked, "Aluno 1", "Aluno 2", "Aluno 3", "Aluno 4", "Aluno 5", "Aluno 6", "Aluno 7", "Aluno 8", "Aluno 9")
        name_student.config(background='#E29E6C', foreground='#FEFAD2', activebackground='#DF8350', font = ("Arial", 12, "bold"), fg='#FEFAD2', borderwidth=2, highlightbackground="#000F31")
        name_student.place(x = 642, y = 25, height = 50, width = 300)

        button_save = bt.DefaultButton(text = "Salvar", command = self.destroy, window = self, pos_x = 690, pos_y = 165, width = 200, height = 50)
        button_cancel = bt.DefaultButton(text = "Cancelar", command = self.destroy, window = self, pos_x = 690, pos_y = 285, width = 200, height = 50)

        
        


    def destroy(self):
        super().destroy()


if __name__ == "__main__":
    mainframe = wd.Window(connect = False)
    mf.MenuFrame(mainframe)
    tw.InitialWorkoutsFrame(mainframe)
    NewWorkoutFrame(mainframe)
    mainframe.mainloop()