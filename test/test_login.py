import unittest

import sys 
import os
sys.path.append(os.path.abspath("./src")) # Adds src directory to python modules path.

from login.login import Login
import exc.exceptions as exc

class TestUser(unittest.TestCase):
    def setUp(self) -> None:
        self.login = Login("12345678901", "password123")

    def test_validate_cpf_empty(self):
        """Testa o caso do CPF estar vazio"""
        self.assertRaises(exc.EmptyFieldError, self.login.validate_cpf, "")     
    
    def test_validate_cpf_invalid_chars(self):
        """Testa o caso do CPF conter caracteres inválidos"""
        self.assertRaises(exc.InvalidCPFError, self.login.validate_cpf, 
                          "999.999.999-9A")     
        self.assertRaises(exc.InvalidCPFError, self.login.validate_cpf, 
                          "999.999.999-9!")     

    def test_validate_cpf_invalid_lenght(self):
        """Testa o caso do CPF ter tamanho incorreto"""
        self.assertRaises(exc.InvalidCPFError, self.login.validate_cpf, "999")     
        self.assertRaises(exc.InvalidCPFError, self.login.validate_cpf, 
                          "999.999.999-999")

    def test_validate_cpf_valid(self):
        """Testa o caso do CPF ser válido"""
        self.assertEqual(self.login.validate_cpf("999.999.999-99"), 
                         "99999999999")
        self.assertEqual(self.login.validate_cpf("01234567890"), 
                         "01234567890")
    
    def test_login_password_empty(self):
        """Testa o caso da senha estar vazia"""
        self.assertRaises(exc.EmptyFieldError, Login, "999.999.999-99", "")
    
    #TODO: Liberar testes que acessam o bd, após solucionar o problema de querys consecutivas

    # def test_login_cpf_not_found(self):
    #     """Testa o caso do CPF não estar cadastrado"""
    #     self.assertRaises(exc.CPFNotFoundError, self.login.run)

    # def test_login_incorrect_password(self):
    #     """Testa o caso da senha estar incorreta"""
    #     self.assertRaises(exc.IncorrectPasswordError, 
    #                       Login("12345678901", "wrong_password123").run)

    # def test_login_success(self):
    #     """Testa o caso de sucesso no login"""
    #     self.login.run()
    #     self.assertEqual(self.login.system.user, self.login.system.database.select("User", "*", f"WHERE CPF = {self.login.cpf}")["IdUser"])

if __name__ == "__main__":
    unittest.main()
