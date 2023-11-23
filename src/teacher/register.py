"""
Esse arquivo será (infelizmente) desenvolvido com TDD e refactoring em paralelo
ao test_register.py. Peço desculpas adiantadas.
"""

#############################
""" Refactor 1
import exc.exceptions as exc

class Register:
    def __init__(self,
                 name: str,
                 birth: str,
                 cpf: str,
                 rg: str,
                 password: str,
                 phone: str,
                 uf: str,
                 neigh: str,
                 medic: str) -> None:
        pass

    def validate_name(self, name: str) -> None:
        if len(name) > 255:
            raise exc.InvalidLenghtError(255, "nome")
"""
#############################
""" Refactor 2
import exc.exceptions as exc
import re

class Register:
    def __init__(self,
                 name: str,
                 birth: str,
                 cpf: str,
                 rg: str,
                 password: str,
                 phone: str,
                 uf: str,
                 neigh: str,
                 medic: str) -> None:
        pass

    def validate_name(self, name: str) -> str:
        if re.match("Nome do aluno", name): name = ""
        if len(name) > 255 or len(name) == 0:
            raise exc.InvalidLenghtError(255, "nome")
"""        
#############################

""" Refactor 3
import exc.exceptions as exc
import re

class Register:
    def __init__(self,
                 name: str,
                 birth: str,
                 cpf: str,
                 rg: str,
                 password: str,
                 phone: str,
                 uf: str,
                 neigh: str,
                 medic: str) -> None:
        pass

    def validate_name(self, name: str) -> str:
        if re.match("Nome do aluno", name): name = ""
        if len(name) > 255 or len(name) == 0:
            raise exc.WrongLengthError("nome", 255, len(name))
        return name
"""    
#############################

import exc.exceptions as exc
import re

class Register:
    def __init__(self,
                 name: str,
                 birth: str,
                 cpf: str,
                 rg: str,
                 password: str,
                 phone: str,
                 uf: str,
                 neigh: str,
                 medic: str) -> None:
        pass

    def validate_name(self, name: str) -> str:
        if re.match("Nome do aluno", name): name = ""
        if len(name) == 0:
            raise exc.EmptyFieldError("nome")
        if len(name) > 255:
            raise exc.WrongLengthError("nome", 255, len(name))
        return name

    def validate_birth(self, birth: str) -> str:
        if "Data de nascimento (dd/mm/aaaa)" == birth: birth = ""
        if len(birth) == 0:
            raise exc.EmptyFieldError("data de nascimento")
        if not re.match(r"\d{2}/\d{2}/\d{4}", birth):
            raise exc.InvalidDateError(birth, "Use o formato (dd/mm/aaaa)")
        return birth
    
    def validate_cpf(self, cpf: str) -> str:
        if cpf == "" or cpf == "CPF do aluno":
            raise exc.EmptyFieldError("CPF")

        if re.search(r"[^\d.\-]", cpf):
            raise exc.InvalidCPFError(cpf, "O CPF só deve conter números.")

        result_cpf = re.sub(r"[.\-]", "", cpf)

        if len(result_cpf) != 11:
            raise exc.InvalidCPFError(cpf, "O CPF deve conter 11 dígitos.")
        
        return result_cpf

    
        