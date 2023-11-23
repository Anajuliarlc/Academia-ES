import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.window as wd
import student.student_frame_factory as sff
import gui.buttons as bt
import db.db_connector as db
import gui.errorlabel as el
import student.thank_you_frame as tyf
import main
import student.increase as inc

class IncreaseFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 960, 
                 pos_x: int = 240, pos_y: int = 200) -> None:
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#000F31")

    def place_objects(self) -> None:
        # select the student's workouts
        system = main.System()
        workouts = system.database.select("Exercise", "ExerciseName", f"Where IdUser = {system.user}")

        if len(workouts) == 0:
            # show error message
            el.ErrorLabel(self, "Você não possui treinos cadastrados", 280, 100)

            conclude_button = bt.DefaultButton(text = "Concluir",
                                        command = self.destroy,
                                        window = self, pos_x = 280, pos_y = 200)
            
        else:
            workouts_list = workouts["ExerciseName"].to_list()

            # drop-down menu
            self.clicked = tk.StringVar()
            self.clicked.set("Exercício a progredir")

            drop = tk.OptionMenu(self, self.clicked, *workouts_list)
            
            drop.config(background='#E29E6C', foreground='#FEFAD2', activebackground='#DF8350')
            drop.place(x=280, y=60, width=400, height=50)

        self.button_request_change = bt.MenuButton(text = "Progredir",
                                        window = self, pos_x = 280,
                                        pos_y = 240, width=400, height=50,
                                        command = lambda: inc.send_request(self))

    def destroy(self) -> None:
        super().destroy()

if __name__ == "__main__":
    mainframe = wd.Window(connect = False)
    IncreaseFrame(mainframe)
    mainframe.mainloop()