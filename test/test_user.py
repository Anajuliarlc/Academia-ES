import unittest

import sys 
import os
sys.path.append(os.path.abspath("./src")) # Adds src directory to python modules path.

from user.user import User
import exc.exceptions as exc

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_validate_cpf_empty(self):
        """Testa o caso do CPF estar vazio"""
        self.assertRaises(exc.EmptyFieldError, self.user.login, "", "123456")     
    
    def test_validate_cpf_invalid_chars(self):
        """Testa o caso do CPF conter caracteres inválidos"""
        self.assertRaises(exc.InvalidCPFError, self.user.login, "999.999.999-9A", "123456")     
        self.assertRaises(exc.InvalidCPFError, self.user.login, "999.999.999-9>", "123456")

    def test_validate_cpf_invalid_lenght(self):
        """Testa o caso do CPF ter tamanho incorreto"""
        self.assertRaises(exc.InvalidCPFError, self.user.login, "999", "123456")     
        self.assertRaises(exc.InvalidCPFError, self.user.login, "999.999.999-999", "123456")     
    
    def test_validate_password_empty(self):
        """Testa o caso da senha estar vazia"""
        self.assertRaises(exc.EmptyFieldError, self.user.login, "999.999.999-99", "")
    
    def test_CPF_not_found(self):
        """Testa o caso do CPF não estar cadastrado"""
        self.assertRaises(exc.CPFNotFoundError, self.user.login, "00000000000", "123456")

    def test_incorrect_password(self):
        """Testa o caso da senha estar incorreta"""
        self.assertRaises(exc.IncorrectPasswordError, self.user.login, "32364696210", "123456")

if __name__ == "__main__":
    unittest.main()
