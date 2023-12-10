import sys
import os
sys.path.append(os.path.abspath("./src"))

import tkinter as tk
from tkinter import scrolledtext

import gui.frame as fr
import gui.entrytext as et
import gui.buttons as bt 
import teacher.teacher_frame_factory as tff
import teacher.register as reg
import gui.errorlabel as el
import exc.exceptions as exc

class CreateRegisterFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 450, width: int = 960,
                  pos_x: int = 240, pos_y: int = 150) -> None:
        """Create a registration frame for student"""
        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#000F31")

    def place_objects(self) -> None:
        label1 = tk.Label(self,
                          text = "Preencha os dados do aluno:", 
                          font = ("Arial", 20), 
                          bg = "#000F31",
                          fg = "#DF8350")
        label1.place(x = 300, y = 10)

        self.entry_name = et.EntryText(self, 20, 70, 
                                       height=20, 
                                       width=400, 
                                       font=("Arial", 12))
        self.entry_name.insert(-1, "Nome do aluno")

        self.entry_birth = et.EntryText(self, 20, 100, 
                                        height=20, 
                                        width=400, 
                                        font=("Arial", 12))
        self.entry_birth.insert(-1, "Data de nascimento (dd/mm/aaaa)")

        self.entry_cpf = et.EntryText(self, 20, 130, 
                                        height=20, 
                                        width=400, 
                                        font=("Arial", 12))
        self.entry_cpf.insert(-1, "CPF")

        self.entry_rg = et.EntryText(self, 20, 160, 
                                        height=20, 
                                        width=400, 
                                        font=("Arial", 12))
        self.entry_rg.insert(-1, "RG")
        
        self.entry_password = et.EntryText(self, 20, 190, 
                                        height=20, 
                                        width=400, 
                                        font=("Arial", 12))
        self.entry_password.insert(-1, "Senha")
        
        self.entry_phone = et.EntryText(self, 20, 220, 
                                        height=20, 
                                        width=400, 
                                        font=("Arial", 12))
        self.entry_phone.insert(-1, "Telefone ((XX) XXXXX-XXXX)")
        
        self.entry_uf = et.EntryText(self, 20, 250, 
                                        height=20, 
                                        width=400, 
                                        font=("Arial", 12))
        self.entry_uf.insert(-1, "UF")
        
        self.entry_city = et.EntryText(self, 20, 280, 
                                        height=20, 
                                        width=400, 
                                        font=("Arial", 12))
        self.entry_city.insert(-1, "Cidade")
  
        self.entry_neigh = et.EntryText(self, 20, 310, 
                                        height=20, 
                                        width=400, 
                                        font=("Arial", 12))
        self.entry_neigh.insert(-1, "Bairro")

        self.entry_medic = scrolledtext.ScrolledText(self, wrap=tk.WORD, 
                                      width=50, 
                                      height=10,
                                      font=("Arial", 12),
                                      bg = "#E29E6C", 
                                      fg = "#FEFAD2")
        self.entry_medic.place(x = 450, y = 70)
        self.entry_medic.insert(tk.INSERT, "Dados médicos")
        
        self.thanks = tk.Label(self, 
                          text = "Registrado com sucesso!", 
                          font = ("Arial", 20), 
                          bg = "#000F31", 
                          fg = "#DF8350")

        self.warning = tk.Label()

        def register_request():
            try:
                self.warning.destroy()
                request = reg.Register(self.entry_name.get(),
                                        self.entry_birth.get(),
                                        self.entry_cpf.get(),
                                        self.entry_rg.get(),
                                        self.entry_password.get(),
                                        self.entry_phone.get(),
                                        self.entry_uf.get(),
                                        self.entry_city.get(),
                                        self.entry_neigh.get(),
                                        self.entry_medic.get("1.0", tk.END)
                                        )
                request.run()
                self.thanks.place(x = 380, y = 350)
                self.after(4000, self.destroy)
                tff.TeacherFrameFactory("RegisterFrame", self.window)

            except (exc.WrongLengthError,
                    exc.EmptyFieldError,
                    exc.InvalidDateError,
                    exc.InvalidCPFError,
                    exc.CPFAlreadyExistsError,
                    exc.InvalidRGError,
                    exc.InvalidPasswordError,
                    exc.InvalidPhoneError,
                    exc.InvalidUFError) as error:
                
                self.warning = el.ErrorLabel(self, 
                                          error, 
                                          480-len(str(error))*5, 
                                          350, 
                                          width=len(str(error))*10 , 
                                          height=60)
                self.after(8000, self.warning.destroy)

        self.button1 = bt.DefaultButton("Enviar", 
                                    register_request,
                                    self,
                                    450, 267, 473, 64,
                                    font=("Arial", 12, "bold"))
        
    def destroy(self) -> None:
        super().destroy()
        