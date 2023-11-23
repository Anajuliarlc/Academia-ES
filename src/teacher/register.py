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
        
        return name
        