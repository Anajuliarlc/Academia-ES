import unittest

import sys 
import os
sys.path.append(os.path.abspath("./src")) # Adds src directory to python modules path.

from teacher.register import Register
import exc.exceptions as exc


class TestRegister(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.reg = Register("George", 
                            "01/01/2000", 
                            "12345678900", 
                            "123456789", 
                            "123456", 
                            "123456789", 
                            "SP", 
                            "Jardim", 
                            "Possui depressão e dor na coluna")
        
    def test_validate_name_too_big(self):
        self.assertRaises(exc.InvalidLenghtError, self.reg.validate_name, "A"*256)
    
    def test_validate_name_too_small(self):
        self.assertRaises(exc.InvalidLenghtError, self.reg.validate_name, "")
        self.assertRaises(exc.InvalidLenghtError, self.reg.validate_name, "Nome do aluno")

    def test_validate_name_valid(self):
        self.assertEqual(self.reg.validate_name("George"), "George")
    


if __name__ == "__main__":
    unittest.main()
