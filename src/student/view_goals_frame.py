import tkinter as tk
import sys
import os
# Adds src directory to python modules path.
sys.path.append(os.path.abspath("./src")) 

import gui.frame as fr
from main import System

class ViewGoalsFrame(fr.Frame):
    def __init__(self, window: tk.Tk, height: int = 600, width: int = 2*480,
                 pos_x: int = 720, pos_y: int = 200) -> None:
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
            self.label_no_goals.place(x = 0, y = 20, height = 30, width = 480)
        else:
            # Show the table of goals
            self.table_goals = tk.Label(self,
                                        text = "Tabela de metas",
                                        font = ("Arial", 20, "bold"),
                                        bg = "#000F31",
                                        fg = "#FEFAD2")
            self.table_goals.place(x = 0, y = 20, height = 30, width = 480)

            # Create a table with the goals
            self.table = tk.Label(self,
                                  text = goals,
                                  font = ("Arial", 20),
                                  bg = "#E29E6C",
                                  fg = "#FEFAD2")
            self.table.place(x = 50, y = 100, height = 300, width = 380)


    def destroy(self) -> None:
        super().destroy()
    
    def update_db(self, goals: dict) -> bool:
        pass
