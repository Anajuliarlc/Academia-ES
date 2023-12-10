import unittest

import sys 
import os
sys.path.append(os.path.abspath("./src")) # Adds src directory to python modules path.

from teacher.register import Register
import exc.exceptions as exc


class TestRegister(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.reg = Register(name="George", 
                            birth="01/01/2000", 
                            cpf="12340678900", 
                            rg="123456789", 
                            password="12aA5676", 
                            phone="21123456789", 
                            uf="SP",
                            city="São Paulo", 
                            neigh="Jardim", 
                            medic="Possui depressão e dor na coluna")
        
    def test_validate_name_too_big(self):
        self.assertRaises(exc.WrongLengthError, self.reg.validate_name, "A"*256)
    
    def test_validate_name_too_small(self):
        self.assertRaises(exc.EmptyFieldError, self.reg.validate_name, "")
        self.assertRaises(exc.EmptyFieldError, self.reg.validate_name, "Nome do aluno")

    def test_validate_name_valid(self):
        self.assertEqual(self.reg.validate_name("George"), "George")
    
    def test_validate_birth_invalid(self):
        self.assertRaises(exc.InvalidDateError, self.reg.validate_birth, "aaa")
        self.assertRaises(exc.InvalidDateError, self.reg.validate_birth, "")
        self.assertRaises(exc.InvalidDateError, self.reg.validate_birth, "Data de nascimento (dd/mm/aaaa)")

    def test_validate_birth_valid(self):
        self.assertEqual(self.reg.validate_birth("01/01/2000"), "01/01/2000")

    def test_validate_cpf_invalid(self):
        self.assertRaises(exc.InvalidCPFError, self.reg.validate_cpf, "000.000.000-0a")
        self.assertRaises(exc.EmptyFieldError, self.reg.validate_cpf, "")
        self.assertRaises(exc.EmptyFieldError, self.reg.validate_cpf, "CPF")

    def test_validate_cpf_already_exists(self):
        self.assertRaises(exc.CPFAlreadyExistsError, self.reg.validate_cpf, "123.456.789-01")

    def test_validate_cpf_valid(self):
        self.assertEqual(self.reg.validate_cpf("123.456.789-11"), "12345678911")

    def test_validate_rg_invalid(self):
        self.assertRaises(exc.InvalidRGError, self.reg.validate_rg, "000000000a")
        self.assertRaises(exc.EmptyFieldError, self.reg.validate_rg, "")
        self.assertRaises(exc.EmptyFieldError, self.reg.validate_rg, "RG")

    def test_validate_rg_invalid_lenght(self):
        self.assertRaises(exc.WrongLengthError, self.reg.validate_rg, "0"*12)

    def test_validate_rg_valid(self):
        self.assertEqual(self.reg.validate_rg("123456789"), "123456789")
    
    def test_validate_password_empty(self):
        """Testa o caso da senha estar vazia"""
        self.assertRaises(exc.EmptyFieldError, self.reg.validate_password, "")

    def test_validate_password_invalid_chars(self):
        """Testa o caso da senha conter espaços"""
        self.assertRaises(exc.InvalidPasswordError, self.reg.validate_password,
                        "1Aa 456")
    
    def test_validate_password_invalid_lenght(self):
        """Testa o caso da senha ter tamanho incorreto"""
        self.assertRaises(exc.InvalidPasswordError, self.reg.validate_password,
                           "1Aa456")
        self.assertRaises(exc.InvalidPasswordError, self.reg.validate_password,
                           "1Aa000000000000")
        
    def test_validate_password_invalid_format(self):
        """Testa os casos da senha não conter pelo menos um número, uma letra 
        maiúscula e uma letra minúscula"""
        self.assertRaises(exc.InvalidPasswordError, self.reg.validate_password,
                           "AaAaAaAa")
        self.assertRaises(exc.InvalidPasswordError, self.reg.validate_password,
                           "1a1a1a1a")
        self.assertRaises(exc.InvalidPasswordError, self.reg.validate_password,
                           "1A1A1A1A")
        
    def test_validate_password_invalid_format(self):
        """Testa os casos da senha não conter pelo menos um número, uma letra 
        maiúscula e uma letra minúscula"""
        self.assertRaises(exc.InvalidPasswordError, self.reg.validate_password,
                           "AaAaAaAa")
        self.assertRaises(exc.InvalidPasswordError, self.reg.validate_password,
                           "1a1a1a1a")
        self.assertRaises(exc.InvalidPasswordError, self.reg.validate_password,
                           "1A1A1A1A")
        
    def test_validate_password_valid(self):
        """Testa o caso da senha ser válida"""
        self.assertEqual(self.reg.validate_password("1Aaa456"), "1Aaa456")

    def test_validate_phone_invalid(self):
        """Testa o caso do telefone ser inválido"""
        self.assertRaises(exc.InvalidPhoneError, 
                        self.reg.validate_phone,
                        "123456789a")
        self.assertRaises(exc.EmptyFieldError, self.reg.validate_phone, "")
        self.assertRaises(exc.EmptyFieldError, self.reg.validate_phone, "Telefone ((XX) XXXXX-XXXX)")
    
    def test_validate_phone_valid(self):
        """Testa o caso do telefone ser válido"""
        self.assertEqual(self.reg.validate_phone("12345678910"), "12345678910")

    def test_validate_state_invalid(self):
        """Testa o caso do estado ser inválido"""
        self.assertRaises(exc.InvalidUFError, self.reg.validate_uf, "São Paulo")
        self.assertRaises(exc.EmptyFieldError, self.reg.validate_uf, "")
        self.assertRaises(exc.EmptyFieldError, self.reg.validate_uf, "UF")

    def test_validate_state_valid(self):
        """Testa o caso do estado ser válido"""
        self.assertEqual(self.reg.validate_uf("SP"), "SP")

    def test_validate_neighbourhood_invalid(self):
        """Testa o caso do bairro ser inválido"""
        self.assertRaises(exc.EmptyFieldError, self.reg.validate_neigh, "")
        self.assertRaises(exc.WrongLengthError, self.reg.validate_neigh, "A"*256)

    def test_validate_neighbourhood_valid(self):
        """Testa o caso do bairro ser válido"""
        self.assertEqual(self.reg.validate_neigh("Jardim Botânico"), "Jardim Botânico")

    def test_validate_medic_info(self):
        self.assertEqual(self.reg.validate_medic("Possui depressão e dor na coluna"), "Possui depressão e dor na coluna")
        self.assertEqual(self.reg.validate_medic(""), "")
        self.assertEqual(self.reg.validate_medic("Dados médicos"), "")

if __name__ == "__main__":
    unittest.main()
