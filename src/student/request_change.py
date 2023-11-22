import gui.errorlabel as el
import main
import student.student_frame_factory as sff
import datetime

def send_request(frame) -> None:
    if frame.clicked.get() == "Motivo da solicitação":
        # show error message
        error = el.ErrorLabel(frame, "Selecione um motivo", pos_x=280,
                                pos_y=300, width=400, height=50)
        frame.errors.append(error)
    elif frame.entry_text.get() == "":
        # show error message
        error = el.ErrorLabel(frame, "Descreva sua situação", 425, 200)
        frame.errors.append(error)
    else:
        system = main.System()
        datetime_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        details = frame.clicked.get() + ": " + frame.entry_text.get()
        return_message = system.database.insert("Request (IdUser, RequestDate, RequestDescription, RequestClosed)", f"({system.user}, \'{datetime_str}\', \'{details}\', false)")
        print(return_message)
        
        frame.destroy()
        sff.StudentFrameFactory.get_frame("ThankYouFrame", frame.window)