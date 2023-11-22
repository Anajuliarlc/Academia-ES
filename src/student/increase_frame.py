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

class IncreaseFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 960, 
                 pos_x: int = 240, pos_y: int = 200) -> None:
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#000F31")

    def place_objects(self) -> None:
        # select the student's workouts
        system = main.System()
        workouts = system.database.select("Exercise", "ExerciseName", f"IdUser = {system.user}")

        if len(workouts) == 0:
            # show error message
            error = el.ErrorLabel(self, "Você não possui treinos cadastrados", 280, 100)
        

        # drop-down menu
        # clicked = tk.StringVar()
        # clicked.set("Treino a ser alterado")

        # drop = tk.OptionMenu(self, clicked, *workouts_list)
        # drop.place(x=425, y=250, width=200, height=50)

        # button_increase = bt.DefaultButton(text = "Progredir Cargas",
        #                                 window = self.window, pos_x = 425, pos_y = 300,
        #                                 command = lambda: send_request())
        
        def send_request() -> None:
            if clicked.get() == "Treino a ser alterado":
                # show error message
                error = el.ErrorLabel(self, "Selecione um treino", 425, 200)
            else:
                # send request to database
                db_connector = db.DBConnector()
                db_connector.update(...)
                # show message to user
                message = tyf.ThankYouFrame(self, "Solicitação enviada", 425, 200)

    def destroy(self) -> None:
        super().destroy()

if __name__ == "__main__":
    mainframe = wd.Window(connect = False)
    IncreaseFrame(mainframe)
    mainframe.mainloop()