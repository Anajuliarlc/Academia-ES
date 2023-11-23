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
        self.assertRaises(exc.WrongLengthError, self.reg.validate_name, "A"*256)
    
    def test_validate_name_too_small(self):
        self.assertRaises(exc.EmptyFieldError, self.reg.validate_name, "")
        self.assertRaises(exc.EmptyFieldError, self.reg.validate_name, "Nome do aluno")

    def test_validate_name_valid(self):
        self.assertEqual(self.reg.validate_name("George"), "George")
    
    def test_validate_birth_invalid(self):
        self.assertRaises(exc.InvalidDateError, self.reg.validate_birth, "aaa")
        self.assertRaises(exc.EmptyFieldError, self.reg.validate_birth, "")
        self.assertRaises(exc.EmptyFieldError, self.reg.validate_birth, "Data de nascimento (dd/mm/aaaa)")

    def test_validate_birth_valid(self):
        self.assertEqual(self.reg.validate_birth("01/01/2000"), "01/01/2000")

    def test_validate_cpf_invalid(self):
        self.assertRaises(exc.InvalidCPFError, self.reg.validate_cpf, "000.000.000-0a")
        self.assertRaises(exc.EmptyFieldError, self.reg.validate_cpf, "")
        self.assertRaises(exc.EmptyFieldError, self.reg.validate_cpf, "CPF do aluno")

if __name__ == "__main__":
    unittest.main()
