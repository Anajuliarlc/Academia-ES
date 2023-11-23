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
        name = "Spining"
        date = "2020-12-12 12:00:00"
        description = "Aula de spining"
        max_students = 10
        self.assertTrue(self.classes.insert_class(name, date,
                                                   description, max_students))
        #classes.system.database.delete("Class", "ClassName", name)

    def test_case_insert_time_conflit(self):
        name = "Spining"
        date = "2020-12-12 12:00:00"
        description = "Aula de spining"
        self.classes.insert_class(name, date, description)
        self.assertRaises(ex.TimeConflictError, self.classes.insert_class,
                           name, date, description)
        #self.classes.system.database.delete("Class", "ClassName", name)
        #self.classes.system.database.delete("Class", "ClassName", name)

if __name__ == "__main__":
    unittest.main()
