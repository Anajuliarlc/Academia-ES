import unittest

import sys 
import os
sys.path.append(os.path.abspath("./src")) # Adds src directory to python modules path.

from user.user import User
import exc.exceptions as exc

class TestUser(unittest.TestCase):
    def test_validate_cpf_empty(self):
        """Testa se o CPF está vazio"""
        self.assertRaises(exc.EmptyFieldError, User, "", "123456")     
    
    def test_validate_cpf_invalid_chars(self):
        """Testa se o CPF contém caracteres inválidos"""
        self.assertRaises(exc.InvalidCPFError, User, "999.999.999-9A", "123456")     
        self.assertRaises(exc.InvalidCPFError, User, "999.999.999-9>", "123456")

    def test_validate_cpf_invalid_lenght(self):
        """Testa se o CPF contém o tamanho correto"""
        self.assertRaises(exc.InvalidCPFError, User, "999", "123456")     
        self.assertRaises(exc.InvalidCPFError, User, "999.999.999-999", "123456")     
    
    def test_validate_password_empty(self):
        """Testa se a senha está vazia"""
        self.assertRaises(exc.EmptyFieldError, User, "999.999.999-99", "")
    
if __name__ == "__main__":
    unittest.main()
