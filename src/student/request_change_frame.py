import tkinter as tk
import sys
sys.path.append("./src")
import gui.frame as fr
import gui.window as wd
import student.student_frame_factory as sff
import gui.buttons as bt
import gui.errorlabel as el
import gui.entrytext as et
import main
import datetime

class RequestChangeFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 960, 
                 pos_x: int = 240, pos_y: int = 200) -> None:
        super().__init__(window, height, width, pos_x, pos_y)
        self.errors = []

    def design(self) -> None:
        self.config(bg = "#000F31")

    def place_objects(self) -> None:
        title_label = tk.Label(self, text="Solicitar Alteração",
                               font=("Arial", 18, "bold"),
                               bg = "#E29E6C", fg = "#FEFAD2")
        title_label.place(x=280, y=10, width=400, height=50)

        # drop-down menu
        clicked = tk.StringVar()
        clicked.set("Motivo da solicitação")

        drop = tk.OptionMenu(self, clicked, "Alteração do professor",
                             "Alteração do horário", "Alteração do local",
                                "Alteração do tipo de aula")
        drop.place(x=280, y=60, width=400, height=50)

        entry_label = tk.Label(self, text="Descreva sua situação",
                               font=("Arial", 14),
                               bg = "#E29E6C", fg = "#FEFAD2")
        entry_label.place(x=280, y=110, width=400, height=50)

        entry_text = et.EntryText(self, pos_x=280, pos_y=160, width=400, height=100)

        def send_request() -> None:
            if clicked.get() == "Motivo da solicitação":
                # show error message
                error = el.ErrorLabel(self, "Selecione um motivo", pos_x=280,
                                      pos_y=300, width=400, height=50)
                self.errors.append(error)
            elif entry_text.get() == "":
                # show error message
                error = el.ErrorLabel(self, "Descreva sua situação", 425, 200)
                self.errors.append(error)
            else:
                system = main.System()
                datetime_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                details = clicked.get() + ": " + entry_text.get()
                return_message = system.database.insert("Request (IdUser, RequestDate, RequestDescription, RequestClosed)", f"({system.user}, \'{datetime_str}\', \'{details}\', false)")
                print(return_message)
                
                for error in self.errors:
                    error.destroy()
                self.button_request_change.destroy()
                self.destroy()
                sff.StudentFrameFactory.get_frame("ThankYouFrame", self.window)

        self.button_request_change = bt.MenuButton(text = "Enviar solicitação",
                                        window = self, pos_x = 280,
                                        pos_y = 240, width=400, height=50,
                                        command = lambda: send_request())

    def destroy(self) -> None:
        super().destroy()

if __name__ == "__main__":
    mainframe = wd.Window(connect = False)
    RequestChangeFrame(mainframe)
    mainframe.mainloop()