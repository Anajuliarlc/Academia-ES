import sys
sys.path.append("./src")

import time
import pandas as pd

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
        print(result)
        if "1 row affected" in result:
            return True
        else:
            return False
        
    def get_history(self) -> pd.DataFrame:
        """ Get the measurements history of the user
        
        :return: Dataframe with the measurements history
        :rtype: pd.DataFrame
        """
        table = "Measurements"
        condition = "WHERE IdUser = " + str(self.system.user)
        df = self.system.database.select(table = table, condition = condition)
        df["MeasDate"] = pd.to_datetime(df["MeasDate"], format = "%Y-%m-%d")
        df["MeasDate"] = df["MeasDate"].dt.strftime("%d/%m/%Y")
        df = df.drop(columns = ["IdUser"])
        df = df.drop(columns = ["IdMeas"])
        columns = ["Data", "Peso", "Altura", "Cintura Alta", "Cintura Baixa",
                    "Busto", "Biceps", "Coxa"]
        df.columns = columns
        df = df.sort_values(by = "Data", ascending = False)
        return df
    