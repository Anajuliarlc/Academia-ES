import sys
import os
sys.path.append(os.path.abspath("./src"))

import tkinter as tk

import gui.frame as fr
from gui.logo_frame import LogoFrame
from gui.buttons import DefaultButton
from gui.entrytext import EntryText
from gui.errorlabel import ErrorLabel

import exc.exceptions as exc
from login.login_class import Login
from teacher.teacher_frame_factory import TeacherFrameFactory
from student.student_frame_factory import StudentFrameFactory
from main import System

class LoginFrame(fr.Frame):
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
        self.entry_cpf = EntryText(self, 350, 130, height=50)

        label_password = tk.Label(self, 
                                  text = "Senha", 
                                  font = ("Arial", 20), 
                                  bg = "#000F31", 
                                  fg = "#FEFAD2")
        label_password.place(x = 350, y = 200)
        self.entry_password = EntryText(self, 350, 240, height=50, 
                                        password=True)
        
        self.warning = tk.Label()

        def request_login() -> None:
            try:
                self.warning.destroy()
                login_command = Login(self.entry_cpf.get(), 
                                      self.entry_password.get())
                login_command.run()
                self.destroy()

            except (exc.EmptyFieldError,
                    exc.CPFNotFoundError,
                    exc.InvalidCPFError,
                    exc.IncorrectPasswordError) as error: 
                self.warning = ErrorLabel(self, 
                                          error, 
                                          600-len(str(error))*5, 
                                          370, 
                                          width=len(str(error))*10 , 
                                          height=60)
                self.after(8000, self.warning.destroy)

        self.button = DefaultButton("Entrar", 
                                    request_login, 
                                    self, 
                                    500, 310, 200, 40)
        
    def destroy(self) -> None:
        super().destroy()
        system = System()
        LogoFrame(self.window, pos_x=119)
        if not system.database.select("Teacher", 
                                      "IdUser", 
                                      f"WHERE IdUser = {system.user}").empty:
            
            TeacherFrameFactory("MenuFrame", self.window)
        elif not system.database.select("Student", 
                                      "IdUser", 
                                      f"WHERE IdUser = {system.user}").empty:
            StudentFrameFactory("MenuFrame", self.window)
        