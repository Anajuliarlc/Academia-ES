import sys
sys.path.append("./src")
import exc.exceptions as ex
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
        """Inserts a new class in the system.

        :param name: Name of the class.
        :type name: str
        :param date: Date of the class in the format YYYY-MM-DD HH:MM:SS.
        :type date: str
        :param description: Description of the class.
        :type description: str
        :param max_students: Max number of students, defaults to 10
        :type max_students: int, optional
        :raises ex.TimeConflictError: If the class is in the same time of another class.
        :return: True if the class was inserted, False otherwise.
        :rtype: bool
        """        
        table = "Class (IdUser, ClassName, ClassDate, \
                         ClassDescription, StudentsMax)"
        values = f"({self.system.user},'{name}', '{date}',\
                     '{description}', {max_students})"

        actual_classes = self.system.database.select("Class")

        if actual_classes["ClassDate"].str.contains(date).any():
            raise ex.TimeConflictError

        return_query = self.system.database.insert(table, values)
        if "ERROR" in return_query:
            return False
        else:
            return True