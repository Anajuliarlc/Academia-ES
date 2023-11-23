import sys
sys.path.append("./src")
import pandas as pd
import main

class Classes():
    def __init__(self):
        self.system = main.System()

    def get_classes(self) -> pd.DataFrame:
        return self.system.database.select("Class")
    
    def insert_class(self, name: str, date: str,
                      description: str, max_students: int = 10) -> bool:
        """1: Refactor
        pass
        """
        table = "Class (IdUser, ClassName, ClassDate, \
                         ClassDescription, StudentsMax)"
        values = f"({self.system.user},'{name}', '{date}',\
                     '{description}', {max_students})"
        return_query = self.system.database.insert(table, values)
        if "ERROR" in return_query:
            return False
        else:
            return True