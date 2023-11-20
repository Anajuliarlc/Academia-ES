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
        self.assertRaises(exc.EmptyFieldError, self.user.validate_cpf, "")     
    
    def test_validate_cpf_invalid_chars(self):
        """Testa o caso do CPF conter caracteres inválidos"""
        self.assertRaises(exc.InvalidCPFError, self.user.validate_cpf, 
                          "999.999.999-9A")     
        self.assertRaises(exc.InvalidCPFError, self.user.validate_cpf, 
                          "999.999.999-9>")

    def test_validate_cpf_invalid_lenght(self):
        """Testa o caso do CPF ter tamanho incorreto"""
        self.assertRaises(exc.InvalidCPFError, self.user.validate_cpf, "999")     
        self.assertRaises(exc.InvalidCPFError, self.user.validate_cpf, 
                          "999.999.999-999")     
    
    def test_login_password_empty(self):
        """Testa o caso da senha estar vazia"""
        self.assertRaises(exc.EmptyFieldError, self.user.login, 
                          "999.999.999-99", "")
    
    def test_login_cpf_not_found(self):
        """Testa o caso do CPF não estar cadastrado"""
        self.assertRaises(exc.CPFNotFoundError, self.user.login, 
                          "00000000000", "123456")

    def test_login_incorrect_password(self):
        """Testa o caso da senha estar incorreta"""
        self.assertRaises(exc.IncorrectPasswordError, self.user.login, 
                          "32364696210", "123456")

    def test_login_success(self):
        """Testa o caso de sucesso no login"""
        self.user.login("32364696210", "JrtJbuCi")
        self.assertEqual(self.user.logged_cpf, int("32364696210"))

    def test_validate_password_empty(self):
        """Testa o caso da senha estar vazia"""
        self.assertRaises(exc.EmptyFieldError, self.user.validate_password, "")

    def test_validate_password_invalid_chars(self):
        """Testa o caso da senha conter espaços"""
        self.assertRaises(exc.InvalidPasswordError, self.user.validate_password,
                        "1Aa 456")
    
    def test_validate_password_invalid_lenght(self):
        """Testa o caso da senha ter tamanho incorreto"""
        self.assertRaises(exc.InvalidPasswordError, self.user.validate_password,
                           "1Aa456")
        self.assertRaises(exc.InvalidPasswordError, self.user.validate_password,
                           "1Aa000000000000")
        
    def test_validate_password_invalid_format(self):
        """Testa os casos da senha não conter pelo menos um número, uma letra 
        maiúscula e uma letra minúscula"""
        self.assertRaises(exc.InvalidPasswordError, self.user.validate_password,
                           "AaAaAaAa")
        self.assertRaises(exc.InvalidPasswordError, self.user.validate_password,
                           "1a1a1a1a")
        self.assertRaises(exc.InvalidPasswordError, self.user.validate_password,
                           "1A1A1A1A")
        

if __name__ == "__main__":
    unittest.main()
