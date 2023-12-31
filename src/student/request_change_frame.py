import sys
sys.path.append("./src")

import tkinter as tk
import datetime

import gui.frame as fr
import gui.window as wd
import gui.buttons as bt
import gui.entrytext as et
import gui.errorlabel as el
import student.student_frame_factory as sff
import main

class RequestChangeFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 400, width: int = 960, 
                 pos_x: int = 240, pos_y: int = 200) -> None:
        """Creates a frame for requesting a change.

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
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        """Configures the design of the frame.
        """
        self.config(bg = "#000F31")

    def button_send_request(self) -> None:
        """Handles the button click event for sending the request.
        """
        if self.clicked.get() == "Motivo da solicitação":
            # show error message
            error = el.ErrorLabel(self, "Selecione um motivo", pos_x=280,
                                    pos_y=300, width=400, height=50)
        elif self.entry_text.get() == "":
            # show error message
            error = el.ErrorLabel(self, "Descreva sua situação", pos_x=280,
                                    pos_y=300, width=400, height=50)
        else:
            system = main.System()
            datetime_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            details = self.clicked.get() + ": " + self.entry_text.get()
            return_message = system.database.insert("Request (IdUser, RequestDate, RequestDescription, RequestClosed)", f"({system.user}, \'{datetime_str}\', \'{details}\', false)")
            print(return_message)

            for frame in self.window.active_frames:
                if type(frame).__name__ != "MenuFrame" and type(frame).__name__ != "LogoFrame":
                    frame.destroy()
            sff.StudentFrameFactory.get_frame("ThankYouFrame", self.window)

    def place_objects(self) -> None:
        """Places the objects within the frame.
        """
        title_label = tk.Label(self, text="Solicitar Alteração",
                               font=("Arial", 18, "bold"),
                               bg = "#E29E6C", fg = "#FEFAD2")
        title_label.place(x=280, y=10, width=400, height=50)

        # drop-down menu
        self.clicked = tk.StringVar()
        self.clicked.set("Motivo da solicitação")

        self.drop = tk.OptionMenu(self, self.clicked, "Alteração do professor",
                             "Alteração do horário", "Alteração do local",
                                "Alteração do tipo de aula")
        
        self.drop.config(background='#E29E6C', foreground='#FEFAD2', activebackground='#DF8350')
        self.drop.place(x=280, y=60, width=400, height=50)

        self.entry_label = tk.Label(self, text="Descreva sua situação",
                               font=("Arial", 14),
                               bg = "#E29E6C", fg = "#FEFAD2")
        self.entry_label.place(x=280, y=110, width=400, height=50)

        self.entry_text = et.EntryText(self, pos_x=280, pos_y=160, width=400, height=100)

        self.button_request_change = bt.MenuButton(text = "Enviar solicitação",
                                        window = self, pos_x = 280,
                                        pos_y = 240, width=400, height=50,
                                        command = self.button_send_request)

    def destroy(self) -> None:
        """Destroys the frame.
        """
        super().destroy()

if __name__ == "__main__":
    mainframe = wd.Window()
    RequestChangeFrame(mainframe)
    mainframe.mainloop()