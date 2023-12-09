"""
This module contains the LoginFrame class, which represents a frame used for login in the application.

.. module:: login_frame
   :platform: Windows
   :synopsis: This module contains the LoginFrame class.
"""

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
    """
    The LoginFrame class represents a frame used for login in the application.
    """

    def __init__(self, window: tk.Tk, height: int = 450, width: int = 1200,
                  pos_x: int = 0, pos_y: int = 150) -> None:
        """
        Create a LoginFrame object.

        :param window: The parent window.
        :type window: tk.Tk
        :param height: The height of the frame.
        :type height: int
        :param width: The width of the frame.
        :type width: int
        :param pos_x: The x-coordinate position of the frame.
        :type pos_x: int
        :param pos_y: The y-coordinate position of the frame.
        :type pos_y: int
        """
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        """
        Design the LoginFrame.
        """
        self.config(bg = "#000F31")

    def place_objects(self) -> None:
        """
        Place objects on the LoginFrame.
        """
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
            """
            Requests login information from the user, validates it, and performs the login operation.

            :raises EmptyFieldError: If any of the login fields are empty.
            :raises CPFNotFoundError: If the provided CPF is not found in the system.
            :raises InvalidCPFError: If the provided CPF is invalid.
            :raises IncorrectPasswordError: If the provided password is incorrect.
            """
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
        """
        Destroy the LoginFrame and create the appropriate frame based on the user's role.
        """
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
        