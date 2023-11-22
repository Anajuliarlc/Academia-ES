import sys
import os
sys.path.append(os.path.abspath("./src"))

import tkinter as tk
import gui.frame as fr
from login_class import Login

class LoginFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 600, width: int = 800,
                  pos_x: int = 0, pos_y: int = 0) -> None:
        """Create a frame to be used as example in the application """
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self["bg"] = "red"

    def place_objects(self) -> None:
        self.title = tk.Label(self, text = "Bem vindo!", font = ("Arial", 20, "bold"))
        self.title.place(x = 300, y = 20, height = 30, width = 200)
        
        self.label1 = tk.Label(self, text = "Insira suas credenciais:", font = ("Arial", 18))
        self.label1.place(x = 150, y = 60, height = 20, width = 500)

        self.label_cpf = tk.Label(self, text = "CPF:", font = ("Arial", 12, "bold"))
        self.label_cpf.place(x = 220, y = 100, height = 20, width = 100)
        self.entry_cpf = tk.Entry(self)
        self.entry_cpf.place(x = 320, y = 100, height = 20, width = 200)

        self.label_pass = tk.Label(self, text = "Senha:", font = ("Arial", 12, "bold"))
        self.label_pass.place(x = 220, y = 120, height = 20, width = 100)
        self.entry_pass = tk.Entry(self, show = "*")
        self.entry_pass.place(x = 320, y = 120, height = 20, width = 200)

        def request_login() -> None:
            try:
                login_command = Login(self.entry_cpf.get(), self.entry_pass.get())
                login_command.run()
            except Exception as error: 
                self.warning = tk.Label(self, text = str(error), font = ("Arial", 12, "bold"), fg = "red")
                self.warning.place(x = 220, y = 200, height = 20, width = 300)

        self.button = tk.Button(self, text = "Entrar")
        self.button["command"] = request_login
        self.button.place(x = 200, y = 150, height = 40, width = 200)
        
    def destroy(self) -> None:
        super().destroy()