import tkinter as tk
import sys
import os
# Adds src directory to python modules path.
sys.path.append(os.path.abspath("./src")) 

import gui.frame as fr
from main import System

class ViewGoalsFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 600, width: int = 960,
                 pos_x: int = 240, pos_y: int = 200) -> None:
        self.system = System()

        super().__init__(window, height, width, pos_x, pos_y)

    def design(self) -> None:
        self.config(bg = "#000F31")
    
    def place_objects(self) -> None:
        """Place objects on the frame
        """

        database = self.system.database
        goals = database.select(table = "Goal",
                                columns = "*",
                                condition = f"WHERE IdUser = {self.system.user}")
        
        if len(goals) == 0:
            self.label_no_goals = tk.Label(self,
                                           text = "Você não possui metas",
                                           font = ("Arial", 20, "bold"),
                                           bg = "#000F31",
                                           fg = "#FEFAD2")
            self.label_no_goals.place(x = 0, y = 20, height = 30, width = 960)
            return
        
        # Show the table of goals
        self.table_goals = tk.Label(self,
                                    text = "Tabela de metas",
                                    font = ("Arial", 20, "bold"),
                                    bg = "#000F31",
                                    fg = "#FEFAD2")
        self.table_goals.place(x = 0, y = 20, height = 30, width = 960)
        
        ############################################################

        self.label_header_index = tk.Label(self,
                                           text = "Meta",
                                           font = ("Arial", 10, "bold", "italic"),
                                           bg = "#DF8350",
                                           fg = "#FEFAD2")
        self.label_header_index.place(x = 60, y = 60, height = 30, width = 120)

        self.label_header_cardio_min = tk.Label(self,
                                                text = "Cardio (min)",
                                                font = ("Arial", 10, "bold"),
                                                bg = "#DF8350",
                                                fg = "#FEFAD2")
        self.label_header_cardio_min.place(x = 180, y = 60, height = 30, width = 120)

        self.label_header_goal_weight = tk.Label(self,
                                                    text = "Peso meta (kg)",
                                                    font = ("Arial", 10, "bold"),
                                                    bg = "#DF8350",
                                                    fg = "#FEFAD2")
        self.label_header_goal_weight.place(x = 300, y = 60, height = 30, width = 120)

        self.label_header_goal_date = tk.Label(self,
                                                text = "Data meta",
                                                font = ("Arial", 10, "bold"),
                                                bg = "#DF8350",
                                                fg = "#FEFAD2")
        self.label_header_goal_date.place(x = 420, y = 60, height = 30, width = 120)

        self.label_header_final_date = tk.Label(self,
                                                text = "Data final",
                                                font = ("Arial", 10, "bold"),
                                                bg = "#DF8350",
                                                fg = "#FEFAD2")
        self.label_header_final_date.place(x = 540, y = 60, height = 30, width = 120)

        self.label_header_lean_mass_pct = tk.Label(self,
                                                text = "Massa magra (%)",
                                                font = ("Arial", 10, "bold"),
                                                bg = "#DF8350",
                                                fg = "#FEFAD2")
        self.label_header_lean_mass_pct.place(x = 660, y = 60, height = 30, width = 120)

        self.label_header_fat_pct = tk.Label(self,
                                                text = "Gordura (%)",
                                                font = ("Arial", 10, "bold"),
                                                bg = "#DF8350",
                                                fg = "#FEFAD2")
        self.label_header_fat_pct.place(x = 780, y = 60, height = 30, width = 120)

        ############################################################

        # Contents of the table

        for i in range(len(goals)):
            self.label_index = tk.Label(self,
                                        text = f"{i+1}",
                                        font = ("Arial", 10),
                                        bg = "#DF8350",
                                        fg = "#FEFAD2")
            self.label_index.place(x = 60, y = 90 + 30*i, height = 30, width = 120)

            self.label_cardio_min = tk.Label(self,
                                            text = f"{goals.iloc[i][2]}",
                                            font = ("Arial", 10),
                                            bg = "#DF8350",
                                            fg = "#FEFAD2")
            self.label_cardio_min.place(x = 180, y = 90 + 30*i, height = 30, width = 120)

            self.label_goal_weight = tk.Label(self,
                                                text = f"{goals.iloc[i][3]}",
                                                font = ("Arial", 10),
                                                bg = "#DF8350",
                                                fg = "#FEFAD2")
            self.label_goal_weight.place(x = 300, y = 90 + 30*i, height = 30, width = 120)

            self.label_goal_date = tk.Label(self,
                                            text = f"{goals.iloc[i][4]}",
                                            font = ("Arial", 10),
                                            bg = "#DF8350",
                                            fg = "#FEFAD2")
            self.label_goal_date.place(x = 420, y = 90 + 30*i, height = 30, width = 120)

            self.label_final_date = tk.Label(self,
                                            text = f"{goals.iloc[i][5]}",
                                            font = ("Arial", 10),
                                            bg = "#DF8350",
                                            fg = "#FEFAD2")
            self.label_final_date.place(x = 540, y = 90 + 30*i, height = 30, width = 120)

            self.label_lean_mass_pct = tk.Label(self,
                                            text = f"{goals.iloc[i][6]}",
                                            font = ("Arial", 10),
                                            bg = "#DF8350",
                                            fg = "#FEFAD2")
            self.label_lean_mass_pct.place(x = 660, y = 90 + 30*i, height = 30, width = 120)

            self.label_fat_pct = tk.Label(self,
                                            text = f"{goals.iloc[i][7]}",
                                            font = ("Arial", 10),
                                            bg = "#DF8350",
                                            fg = "#FEFAD2")
            self.label_fat_pct.place(x = 780, y = 90 + 30*i, height = 30, width = 120)


    def destroy(self) -> None:
        super().destroy()
    
    def update_db(self, goals: dict) -> bool:
        pass
