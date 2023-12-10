import sys
sys.path.append("./src")
import pandas as pd
import main

class Classes():
    def __init__(self):
        """Initializes a new instance of the Classes class."""
        self.system = main.System()

    def get_classes(self) -> pd.DataFrame:
        """Returns a DataFrame containing all the classes in the system.
        
        :return: A DataFrame containing the classes.
        :rtype: pd.DataFrame
        """
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