import time
import sys
sys.path.append("./src")
import main

class SetGoals():
    def __init__(self) -> None:
        self.system = main.System()

    def update_db(self, goals: dict) -> bool:
        """Updates the database with the new goals
        """

        table = "Goal (IdUser, CardioMin, GoalWeight, GoalDate, FinalDate, \
                LeanMassPct, FatPct)"
        
        date = time.strftime("%Y-%m-%d")
        values = f"({self.system.user}, '{goals['cardio_min']}', \
                   '{goals['goal_weight']}', '{goals['goal_date']}', \
                   '{goals['final_date']}', '{goals['lean_mass_pct']}', \
                   '{goals['fat_pct']}')"
        
        result = self.system.database.insert(table = table, values = values)
        if "1 row affected" in result:
            return True
        else:
            return False

if __name__ == "__main__":
    import set_goals_frame as sgf
    import gui.window as window
    
    mainframe = window.Window()
    sgf.SetGoalsFrame(mainframe)
    mainframe.mainloop()
