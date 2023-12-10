import sys
sys.path.append("./src")
import pandas as pd
import main
import db

class StudentClasses():
    def __init__(self):
        """Initializes a new instance of the StudentClasses class."""
        self.system = main.System()

    def get_classes(self) -> pd.DataFrame:
        """Retrieves the classes for the student.

        Returns:
            pd.DataFrame: A DataFrame containing the class information.
        """
        db_connector = db.db_connector.DBConnector()
        query = f" SELECT c.ClassName, c.ClassDate, c.ClassDescription, c.StudentsMax FROM Class as c, Take as t where t.IdStudent = {self.system.user} and t.IdTeacher = c.IdUser and t.IdClass = c.IdClass;"

        result = db_connector.query(query)
        print(result)

        table = result.split("c.IdClass;")
        table = table[1]
        table = table.split("\n")
        table = table[2:-4]
        
        columns = table[0].split("|")[1:-1]
        columns = [column.strip() for column in columns]
        
        table = table[2:]
        table = [row.split("|")[1:-1] for row in table]
        table = [[value.strip() for value in row] for row in table]
        table = pd.DataFrame(table, columns = columns)
        print(table)

        return table
    
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
