import sys
import os
sys.path.append(os.path.abspath("./src"))

import tkinter as tk

import gui.frame as fr
import gui.logo_frame as lf
import gui.buttons as bt
import gui.entrytext as et
import gui.errorlabel as el

import exc.exceptions as exc
import login.login_class as lc
import teacher.teacher_frame_factory as tff
import student.student_frame_factory as sff
import main 

class LoginFrame(fr.Frame):
    """ Create a frame to be used as login in the application
    
    >>> import gui.window as wd
    >>> window = wd.Window(connect = False)
    >>> frame = LoginFrame(window)
    >>> frame.height, frame.width
    (450, 1200)
    >>> frame.pos_x, frame.pos_y
    (0, 150)
    """
    def __init__(self, window: tk.Tk, height: int = 450, width: int = 1200,
                  pos_x: int = 0, pos_y: int = 150) -> None:
        """Create a frame to be used as example in the application """
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#000F31")

    def place_objects(self) -> None:
        label1 = tk.Label(self, 
                          text = "Insira suas credenciais:", 
                          font = ("Arial", 20), 
                          bg = "#000F31", 
                          fg = "#DF8350")
        label1.place(x = 455, y = 10)

        label_cpf = tk.Label(self, 
                             text = "CPF", 
                             font = ("Arial", 20), 
                             bg = "#000F31", 
                             fg = "#FEFAD2")
        label_cpf.place(x = 350, y = 90)
        self.entry_cpf = et.EntryText(self, 350, 130, height=50)

        label_password = tk.Label(self, 
                                  text = "Senha", 
                                  font = ("Arial", 20), 
                                  bg = "#000F31", 
                                  fg = "#FEFAD2")
        label_password.place(x = 350, y = 200)
        self.entry_password = et.EntryText(self, 350, 240, height=50, 
                                        password=True)
        
        self.warning = tk.Label()

        def request_login() -> None:
            try:
                self.warning.destroy()
                login_command = lc.Login(self.entry_cpf.get(), 
                                      self.entry_password.get())
                login_command.run()
                self.destroy()

            except (exc.EmptyFieldError,
                    exc.CPFNotFoundError,
                    exc.InvalidCPFError,
                    exc.IncorrectPasswordError) as error: 
                self.warning = el.ErrorLabel(self, 
                                          error, 
                                          600-len(str(error))*5, 
                                          370, 
                                          width=len(str(error))*10 , 
                                          height=60)
                self.after(8000, self.warning.destroy)

        self.button = bt.DefaultButton("Entrar", 
                                    request_login, 
                                    self, 
                                    500, 310, 200, 40)
        
    def destroy(self) -> None:
        super().destroy()
        system = main.System()
        lf.LogoFrame(self.window, pos_x=119)
        if not system.database.select("Teacher", 
                                      "IdUser", 
                                      f"WHERE IdUser = {system.user}").empty:
            
            tff.TeacherFrameFactory("MenuFrame", self.window)
        elif not system.database.select("Student", 
                                      "IdUser", 
                                      f"WHERE IdUser = {system.user}").empty:
            sff.StudentFrameFactory("MenuFrame", self.window)
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()