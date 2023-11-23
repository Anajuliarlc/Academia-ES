import tkinter as tk
import time

import sys
import os
# Adds src directory to python modules path.
sys.path.append(os.path.abspath("./src")) 

import gui.frame as fr
import pandas as pd
from main import System
from gui.buttons import DefaultButton
from gui.errorlabel import ErrorLabel

class SetGoalsFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 600, width: int = 2*480,
                 pos_x: int = 720, pos_y: int = 200) -> None:
        self.system = System()

        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#000F31")
    
    def place_objects(self) -> None:
        """Place objects on the frame
        """

        self.label1 = tk.Label(self,
                               text = "Especifique sua meta",
                               font = ("Arial", 20, "bold"),
                               bg = "#000F31",
                               fg = "#FEFAD2")
        self.label1.place(x = 0, y = 20, height = 30, width = 480)

        #############################################################

        self.label_goal_name = tk.Label(self,
                                        text = "Nome da meta",
                                        font = ("Arial", 10),
                                        bg = "#000F31",
                                        fg = "#FEFAD2")
        self.label_goal_name.place(x = 50, y = 70, height = 20)
        self.entry_goal_name = tk.Entry(self,
                                        font = ("Arial", 10),
                                        bg = "#DF8350",
                                        fg = "#FEFAD2",)
        self.entry_goal_name.place(x = 50, y = 90, height = 30, width = 380)

        #############################################################

        self.label_cardio_min = tk.Label(self,
                                        text = "Mínimo de aeróbicos (opcional)",
                                        font = ("Arial", 10),
                                        bg = "#000F31",
                                        fg = "#FEFAD2")
        self.label_cardio_min.place(x = 50, y = 130, height = 20)
        self.entry_cardio_min = tk.Entry(self,
                                        font = ("Arial", 10),
                                        bg = "#DF8350",
                                        fg = "#FEFAD2",)
        self.entry_cardio_min.place(x = 50, y = 150, height = 30, width = 180)

        #############################################################

        self.label_goal_weight = tk.Label(self,
                                        text = "Objetivo de peso (opcional)",
                                        font = ("Arial", 10),
                                        bg = "#000F31",
                                        fg = "#FEFAD2")
        self.label_goal_weight.place(x = 250, y = 130, height = 20)
        self.entry_goal_weight = tk.Entry(self,
                                        font = ("Arial", 10),
                                        bg = "#DF8350",
                                        fg = "#FEFAD2",)
        self.entry_goal_weight.place(x = 250, y = 150, height = 30, width = 180)

        #############################################################
        
        self.label_start_date = tk.Label(self,
                                        text = "Data de início",
                                        font = ("Arial", 10),
                                        bg = "#000F31",
                                        fg = "#FEFAD2")
        self.label_start_date.place(x = 50, y = 190, height = 20)
        self.entry_start_date = tk.Entry(self,
                                        font = ("Arial", 10),
                                        bg = "#DF8350",
                                        fg = "#FEFAD2",)
        self.entry_start_date.place(x = 50, y = 210, height = 30, width = 180)
        
        #############################################################

        self.label_final_date = tk.Label(self,
                                        text = "Data final",
                                        font = ("Arial", 10),
                                        bg = "#000F31",
                                        fg = "#FEFAD2")
        self.label_final_date.place(x = 250, y = 190, height = 20)
        self.entry_final_date = tk.Entry(self,
                                        font = ("Arial", 10),
                                        bg = "#DF8350",
                                        fg = "#FEFAD2",)
        self.entry_final_date.place(x = 250, y = 210, height = 30, width = 180)

        #############################################################
        
        self.label_lean_mass = tk.Label(self,
                                        text = "Massa magra (opcional)",
                                        font = ("Arial", 10),
                                        bg = "#000F31",
                                        fg = "#FEFAD2")
        self.label_lean_mass.place(x = 50, y = 250, height = 20)
        self.entry_lean_mass = tk.Entry(self,
                                        font = ("Arial", 10),
                                        bg = "#DF8350",
                                        fg = "#FEFAD2",)
        self.entry_lean_mass.place(x = 50, y = 270, height = 30, width = 180)

        #############################################################

        self.label_fat_mass = tk.Label(self,
                                        text = "Massa gorda (opcional)",
                                        font = ("Arial", 10),
                                        bg = "#000F31",
                                        fg = "#FEFAD2")
        self.label_fat_mass.place(x = 250, y = 250, height = 20)
        self.entry_fat_mass = tk.Entry(self,
                                        font = ("Arial", 10),
                                        bg = "#DF8350",
                                        fg = "#FEFAD2",)
        self.entry_fat_mass.place(x = 250, y = 270, height = 30, width = 180)

        #############################################################

        self.warning = tk.Label()

        def confirm_set_goals() -> None:
            self.warning.destroy()

            if self.entry_goal_name.get() == "":
                self.warning = ErrorLabel(window = self,
                                          text = "Insira um nome para a meta",
                                          pos_x = 50, pos_y = 360,
                                          width = 380, height = 30,
                                          font = ("Arial", 10))
                
            elif (self.entry_cardio_min.get() != ""
                  and not self.entry_cardio_min.get().isnumeric()):
                self.warning = ErrorLabel(window = self,
                                          text = "Insira um valor numérico para o mínimo de aeróbicos",
                                          pos_x = 50, pos_y = 360,
                                          width = 380, height = 30,
                                          font = ("Arial", 10))
                
            elif (self.entry_goal_weight.get() != ""
                  and not self.entry_goal_weight.get().isnumeric()):
                self.warning = ErrorLabel(window = self,
                                          text = "Insira um valor numérico para o objetivo de peso",
                                          pos_x = 50, pos_y = 360,
                                          width = 380, height = 30,
                                          font = ("Arial", 10))
                
            elif self.entry_start_date.get() == "":
                self.warning = ErrorLabel(window = self,
                                          text = "Insira uma data de início",
                                          pos_x = 50, pos_y = 360,
                                          width = 380, height = 30,
                                          font = ("Arial", 10))
                
            elif self.entry_final_date.get() == "":
                self.warning = ErrorLabel(window = self,
                                          text = "Insira uma data final",
                                          pos_x = 50, pos_y = 360,
                                          width = 380, height = 30,
                                          font = ("Arial", 10))
                
            elif (self.entry_lean_mass.get() != ""
                    and not self.entry_lean_mass.get().isnumeric()):
                self.warning = ErrorLabel(window = self,
                                          text = "Insira um valor numérico \
                                            para a massa magra",
                                          pos_x = 50, pos_y = 360,
                                          width = 380, height = 30,
                                          font = ("Arial", 10))
                
            elif (self.entry_fat_mass.get() != ""
                  and not self.entry_fat_mass.get().isnumeric()):
                self.warning = ErrorLabel(window = self,
                                          text = "Insira um valor numérico \
                                            para a massa gorda",
                                          pos_x = 50, pos_y = 360,
                                          width = 380, height = 30,
                                          font = ("Arial", 10))
            
            else:
                # Falta a função para inserir os dados no bd
                database = self.system.database
                goals = pd.DataFrame({"IdUser": [self.system.user],
                                      "CardioMin": [self.entry_cardio_min.get()],
                                      "GoalWeight": [self.entry_goal_weight.get()],
                                      "GoalDate": [self.entry_start_date.get()],
                                      "FinalDate": [self.entry_final_date.get()],
                                      "LeanMassPct": [self.entry_lean_mass.get()],
                                      "FatPct": [self.entry_fat_mass.get()]})
                self.update_db(goals)

                self.label1.destroy()
                self.label_goal_name.destroy()
                self.entry_goal_name.destroy()
                self.label_cardio_min.destroy()
                self.entry_cardio_min.destroy()
                self.label_goal_weight.destroy()
                self.entry_goal_weight.destroy()
                self.label_start_date.destroy()
                self.entry_start_date.destroy()
                self.label_final_date.destroy()
                self.entry_final_date.destroy()
                self.label_lean_mass.destroy()
                self.entry_lean_mass.destroy()
                self.label_fat_mass.destroy()
                self.entry_fat_mass.destroy()
                self.button_confirm.destroy()
                self.destroy()

                #import student_frame_factory as sff
                #sff.StudentFrameFactory("ThankYouCard", self.window)

        self.button_confirm = DefaultButton(text = "Confirmar",
                                            command = confirm_set_goals,
                                            window = self,
                                            pos_x = 50, pos_y = 320,
                                            height = 30, width = 380,
                                            font = ("Arial", 10),)

    
    def destroy(self) -> None:
        super().destroy()
    
    def update_db(self, goals: dict) -> bool:
        """Updates the database with the new goals
        """
        table = "Goal (IdUser, CardioMin, GoalWeight, GoalDate, FinalDate, \
                LeanMassPct, FatPct)"
        
        date = time.strftime("%Y-%m-%d")
        values = f"({self.system.user}, '{goals['CardioMin']}', \
                   '{goals['GoalWeight']}', '{goals['GoalDate']}', \
                   '{goals['FinalDate']}', '{goals['LeanMassPct']}', \
                   '{goals['FatPct']}')"
        
        result = self.system.database.insert(table = table, values = values)
        if "1 row affected" in result:
            print("Meta inserida com sucesso")
            return True
        else:
            print("Erro ao inserir meta")
            return False
