import sys
import os
# Adds src directory to python modules path.
sys.path.append(os.path.abspath("./src")) 

import main
import tkinter as tk
import gui.frame as fr
from gui.buttons import DefaultButton
from gui.errorlabel import ErrorLabel
import student.student_frame_factory as sff

class SetGoalsFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 600, width: int = 960,
                     pos_x: int = 720, pos_y: int = 200) -> None:
            """Initialize the SetGoalsFrame class.

            :param window: The Tkinter window object.
            :type window: tk.Tk
            :param height: The height of the frame, defaults to 600.
            :type height: int, optional
            :param width: The width of the frame, defaults to 960.
            :type width: int, optional
            :param pos_x: The x-coordinate position of the frame, defaults to 720.
            :type pos_x: int, optional
            :param pos_y: The y-coordinate position of the frame, defaults to 200.
            :type pos_y: int, optional
            """
            self.system = main.System()

            super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        """Sets the design of the frame.

        This method sets the background color of the frame to "#000F31".
        """
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

            goals = {}
            goals["GoalName"] = self.entry_goal_name.get()
            goals["CardioMin"] = self.entry_cardio_min.get()
            goals["GoalWeight"] = self.entry_goal_weight.get()
            goals["GoalDate"] = self.entry_start_date.get()
            goals["FinalDate"] = self.entry_final_date.get()
            goals["LeanMassPct"] = self.entry_lean_mass.get()
            goals["FatPct"] = self.entry_fat_mass.get()

            def check_date(date: str) -> bool:
                return (len(date) == 10 and date[4] == "-" and date[7] == "-"
                    and date[0:4].isnumeric()
                    and date[5:7].isnumeric() and 0<int(date[5:7])<13
                    and date[8:10].isnumeric() and 0<int(date[8:10])<32)

            if goals["GoalName"] == "":
                self.warning = ErrorLabel(window = self,
                                          text = "Insira um nome para a meta",
                                          pos_x = 50, pos_y = 360,
                                          width = 380, height = 30,
                                          font = ("Arial", 10))
                
            elif (goals["CardioMin"] != ""
                  and not goals["CardioMin"].isnumeric()):
                self.warning = ErrorLabel(window = self,
                                          text = "Insira um valor numérico para o mínimo de aeróbicos",
                                          pos_x = 50, pos_y = 360,
                                          width = 380, height = 30,
                                          font = ("Arial", 10))
                
            elif (goals["GoalWeight"] != ""
                  and not goals["GoalWeight"].isnumeric()):
                self.warning = ErrorLabel(window = self,
                                          text = "Insira um valor numérico para o objetivo de peso",
                                          pos_x = 50, pos_y = 360,
                                          width = 380, height = 30,
                                          font = ("Arial", 10))
                
            elif (goals["GoalDate"]=="" or not check_date(goals["GoalDate"])):
                self.warning = ErrorLabel(window = self,
                                          text = "Formato de data: AAAA-MM-DD",
                                          pos_x = 50, pos_y = 360,
                                          width = 380, height = 30,
                                          font = ("Arial", 10))
                
            elif (goals["FinalDate"]=="" or not check_date(goals["FinalDate"])):
                self.warning = ErrorLabel(window = self,
                                          text = "Formato de data: AAAA-MM-DD",
                                          pos_x = 50, pos_y = 360,
                                          width = 380, height = 30,
                                          font = ("Arial", 10))
                
            elif (goals["LeanMassPct"] != ""
                    and not goals["LeanMassPct"].isnumeric()):
                self.warning = ErrorLabel(window = self,
                                          text = "Insira um valor numérico para a massa magra",
                                          pos_x = 50, pos_y = 360,
                                          width = 380, height = 30,
                                          font = ("Arial", 10))
                
            elif (goals["FatPct"] != ""
                  and not goals["FatPct"].isnumeric()):
                self.warning = ErrorLabel(window = self,
                                          text = "Insira um valor numérico para a massa gorda",
                                          pos_x = 50, pos_y = 360,
                                          width = 380, height = 30,
                                          font = ("Arial", 10))
            
            else:
                # Insert goals in database
                self.update_db(goals)
                self.destroy()
                sff.StudentFrameFactory.get_frame("GoalsFrame", self.window)
        
        self.button_confirm = DefaultButton(text = "Confirmar",
                                            command = confirm_set_goals,
                                            window = self,
                                            pos_x = 50, pos_y = 320,
                                            height = 30, width = 380,
                                            font = ("Arial", 10),)

    
    def destroy(self) -> None:
        """Destroys the set_goals_frame.

        This method overrides the destroy method from the parent class
        and is responsible for destroying the set_goals_frame.
        """
        super().destroy()
        sff.StudentFrameFactory.get_frame("GoalsFrame", self.window)
    
    def update_db(self, goals: dict) -> bool:
        """Updates the database with the new goals
        """
        table = "Goal (IdUser, CardioMin, GoalWeight, GoalDate, FinalDate, \
                LeanMassPct, FatPct)"
        
        for key in goals.keys():
            if goals[key] == "":
                goals[key] = "NULL"

        values = f"({self.system.user}, {goals['CardioMin']}, \
                   {goals['GoalWeight']}, '{goals['GoalDate']}', \
                   '{goals['FinalDate']}', {goals['LeanMassPct']}, \
                   {goals['FatPct']})"
        
        result = self.system.database.insert(table = table, values = values)

        if "1 row affected" in result:
            print("Meta inserida com sucesso")
            return True
        else:
            print("Erro ao inserir meta")
            return False
