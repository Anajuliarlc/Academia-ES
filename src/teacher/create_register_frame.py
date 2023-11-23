import sys
import os
sys.path.append(os.path.abspath("./src"))

import tkinter as tk
from tkinter import scrolledtext

import gui.frame as fr
import gui.entrytext as et
import gui.buttons as bt 
import teacher.teacher_frame_factory as tff

class CreateRegisterFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 450, width: int = 960,
                  pos_x: int = 240, pos_y: int = 150) -> None:
        """Create a frame to be used as example in the application """
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
        self.entry_phone.insert(-1, "Telefone (+XX (XX) XXXXX-XXXX)")
        
        self.entry_uf = et.EntryText(self, 20, 250, 
                                        height=20, 
                                        width=400, 
                                        font=("Arial", 12))
        self.entry_uf.insert(-1, "UF")
        
        self.entry_neigh = et.EntryText(self, 20, 280, 
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

        def button_press():
            print("au")

        self.button1 = bt.DefaultButton("Enviar", 
                                    button_press,
                                    self,
                                    450, 267, 473, 35,
                                    font=("Arial", 12, "bold"))
        
    def destroy(self) -> None:
        super().destroy()
        