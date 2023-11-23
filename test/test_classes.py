import unittest
import sys 
import os
sys.path.append(os.path.abspath("./src"))

import exc.exceptions as ex
import teacher.classes as cl
import pandas as pd

class TestClasses(unittest.TestCase):
    classes = cl.Classes()
    classes.system.user = 1
    def test_case_insert_happy_case(self):
        """ If the user insert a class in the database, the system should
        return True
        """
        name = "Spining"
        date = "2020-12-12 12:00:00"
        description = "Aula de spining"
        max_students = 10
        self.assertTrue(self.classes.insert_class(name, date,
                                                   description, max_students))
        condition = "WHERE ClassName = '" + name + "'"
        self.classes.system.database.delete("Class", condition)

    def test_case_insert_time_conflit(self):
        """ If the user try to insert a class in the same time of another class
        the system should raise a TimeConflictError
        """        
        name = "Spining"
        date = "2020-12-12 12:00:00"
        description = "Aula de spining"
        self.classes.insert_class(name, date, description)
        self.assertRaises(ex.TimeConflictError, self.classes.insert_class,
                           name, date, description)
        condition = "WHERE ClassName = '" + name + "'"
        self.classes.system.database.delete("Class", condition)
        self.classes.system.database.delete("Class", condition)

if __name__ == "__main__":
    unittest.main()
