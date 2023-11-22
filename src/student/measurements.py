import time
import sys
sys.path.append("./src")
import main

class Measurements():
    def __init__(self) -> None:
        self.system = main.System()

    def update_db(self, measurements: dict) -> bool:
        """
        1 - Write a test that fails
        pass
        """
        table = "Measurements (IdUser, MeasDate, Weight, Height, HighWaist, \
                LowWaist, Bust, Biceps, Thigh)"
        
        date = time.strftime("%Y-%m-%d")
        values = f"({self.system.user}, '{date}', \
                    {measurements['Weight']}, {measurements['Height']}, \
                    {measurements['HighWaist']}, {measurements['LowWaist']}, \
                    {measurements['Bust']}, {measurements['Biceps']}, \
                    {measurements['Thigh']})"
        
        
        result = self.system.database.insert(table = table, values = values)
        if "1 row affected" in result:
            return True
        else:
            return False