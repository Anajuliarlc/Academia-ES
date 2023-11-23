import tkinter as tk
import gui.errorlabel as el
import main
import student.student_frame_factory as sff

def send_request(frame: tk.Frame) -> None:
    if frame.clicked.get() == "Exercício a progredir":
        # show error message
        el.ErrorLabel(frame, "Selecione um exercício", pos_x=280,
                                pos_y=300, width=400, height=50)
    else:
        system = main.System()
        return_message = system.database.query(f"UPDATE Exercise SET WeightExercise = WeightExercise + 2.5 WHERE ExerciseName = \'{frame.clicked.get()}\' AND IdUser = {system.user};")
        print(return_message)
        
        frame.destroy()
        sff.StudentFrameFactory.get_frame("ThankYouFrame", frame.window)