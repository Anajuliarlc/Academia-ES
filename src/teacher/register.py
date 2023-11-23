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

""" Refactoring 4
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
"""
#############################

""" Refactoring 5
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
        if cpf == "" or cpf == "CPF":
            raise exc.EmptyFieldError("CPF")

        if re.search(r"[^\d.\-]", cpf):
            raise exc.InvalidCPFError(cpf, "O CPF só deve conter números.")

        result_cpf = re.sub(r"[.\-]", "", cpf)

        if len(result_cpf) != 11:
            raise exc.InvalidCPFError(cpf, "O CPF deve conter 11 dígitos.")
        
        return result_cpf
    
    def validate_rg(self, rg: str) -> str:
        if rg == "" or rg == "RG":
            raise exc.EmptyFieldError("RG")

        if re.search(r"[^\d.\-]", rg):
            raise exc.InvalidRGError(rg, "O RG só deve conter números.")

        if len(re.sub(r"[.\-]", "", rg)) > 11:
            raise exc.WrongLengthError("RG", 11, len(re.sub(r"[.\-]", "", rg)))

        return re.sub(r"[.\-]", "", rg)
"""
#############################
""" Refactoring 6    
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
        if cpf == "" or cpf == "CPF":
            raise exc.EmptyFieldError("CPF")

        if re.search(r"[^\d.\-]", cpf):
            raise exc.InvalidCPFError(cpf, "O CPF só deve conter números.")

        result_cpf = re.sub(r"[.\-]", "", cpf)

        if len(result_cpf) != 11:
            raise exc.InvalidCPFError(cpf, "O CPF deve conter 11 dígitos.")
        
        return result_cpf
    
    def validate_rg(self, rg: str) -> str:
        if rg == "" or rg == "RG":
            raise exc.EmptyFieldError("RG")

        if re.search(r"[^\d.\-]", rg):
            raise exc.InvalidRGError(rg, "O RG só deve conter números.")

        if len(re.sub(r"[.\-]", "", rg)) > 11:
            raise exc.WrongLengthError("RG", 11, len(re.sub(r"[.\-]", "", rg)))

        return re.sub(r"[.\-]", "", rg)

    def validate_password(self, password: str) -> None:
        if password == "":
            raise exc.EmptyFieldError("senha")
        
        if re.search(r"[\s\n]", password):
            raise exc.InvalidPasswordError("A senha não deve conter espaços.")
        
        if len(password) < 7 or len(password) > 14:
            raise exc.InvalidPasswordError(
                "A senha deve conter entre 7 e 14 caracteres."
                )

        if not (re.search(r"[\d]+", password) 
                and re.search(r"[A-Z]+", password) 
                and re.search(r"[a-z]+", password)):
            raise exc.InvalidPasswordError("A senha deve conter pelo menos um "
                        "número, uma letra maiúscula e uma letra minúscula.")
"""
#############################
"""
import re

import main
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
        self.system = main.System()

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
        if cpf == "" or cpf == "CPF":
            raise exc.EmptyFieldError("CPF")

        if re.search(r"[^\d.\-]", cpf):
            raise exc.InvalidCPFError(cpf, "O CPF só deve conter números.")

        result_cpf = re.sub(r"[.\-]", "", cpf)

        if len(result_cpf) != 11:
            raise exc.InvalidCPFError(cpf, "O CPF deve conter 11 dígitos.")
        
        if not self.system.database.select("User", "*", f"WHERE CPF = {result_cpf}").empty:
            raise exc.CPFAlreadyExistsError(cpf)
        
        return result_cpf
    
    def validate_rg(self, rg: str) -> str:
        if rg == "" or rg == "RG":
            raise exc.EmptyFieldError("RG")

        if re.search(r"[^\d.\-]", rg):
            raise exc.InvalidRGError(rg, "O RG só deve conter números.")

        if len(re.sub(r"[.\-]", "", rg)) > 11:
            raise exc.WrongLengthError("RG", 11, len(re.sub(r"[.\-]", "", rg)))

        return re.sub(r"[.\-]", "", rg)

    def validate_password(self, password: str) -> None:
        if password == "":
            raise exc.EmptyFieldError("senha")
        
        if re.search(r"[\s\n]", password):
            raise exc.InvalidPasswordError("A senha não deve conter espaços.")
        
        if len(password) < 7 or len(password) > 14:
            raise exc.InvalidPasswordError(
                "A senha deve conter entre 7 e 14 caracteres."
                )

        if not (re.search(r"[\d]+", password) 
                and re.search(r"[A-Z]+", password) 
                and re.search(r"[a-z]+", password)):
            raise exc.InvalidPasswordError("A senha deve conter pelo menos um "
                        "número, uma letra maiúscula e uma letra minúscula.")
        
        return password
"""
#############################


import re

import main
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
        self.system = main.System()

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
        if cpf == "" or cpf == "CPF":
            raise exc.EmptyFieldError("CPF")

        if re.search(r"[^\d.\-]", cpf):
            raise exc.InvalidCPFError(cpf, "O CPF só deve conter números.")

        result_cpf = re.sub(r"[.\-]", "", cpf)

        if len(result_cpf) != 11:
            raise exc.InvalidCPFError(cpf, "O CPF deve conter 11 dígitos.")
        
        if not self.system.database.select("User", "*", f"WHERE CPF = {result_cpf}").empty:
            raise exc.CPFAlreadyExistsError(cpf)
        
        return result_cpf
    
    def validate_rg(self, rg: str) -> str:
        if rg == "" or rg == "RG":
            raise exc.EmptyFieldError("RG")

        if re.search(r"[^\d.\-]", rg):
            raise exc.InvalidRGError(rg, "O RG só deve conter números.")

        if len(re.sub(r"[.\-]", "", rg)) > 11:
            raise exc.WrongLengthError("RG", 11, len(re.sub(r"[.\-]", "", rg)))

        return re.sub(r"[.\-]", "", rg)

    def validate_password(self, password: str) -> None:
        if password == "":
            raise exc.EmptyFieldError("senha")
        
        if re.search(r"[\s\n]", password):
            raise exc.InvalidPasswordError("A senha não deve conter espaços.")
        
        if len(password) < 7 or len(password) > 14:
            raise exc.InvalidPasswordError(
                "A senha deve conter entre 7 e 14 caracteres."
                )

        if not (re.search(r"[\d]+", password) 
                and re.search(r"[A-Z]+", password) 
                and re.search(r"[a-z]+", password)):
            raise exc.InvalidPasswordError("A senha deve conter pelo menos um "
                        "número, uma letra maiúscula e uma letra minúscula.")
        
        return password
    
    def validate_phone(self, phone: str) -> str:
        if phone == "" or phone == "Telefone ((XX) XXXXX-XXXX)":
            raise exc.EmptyFieldError("telefone")
        
        if re.search(r"[^\d\+\-\(\)]", phone):
            raise exc.InvalidPhoneError(phone)
        
        if len(re.sub(r"[^\d]", "", phone)) != 11:
            raise exc.WrongLengthError("telefone", 11, len(re.sub(r"[^\d]", "", phone)))
        
        return re.sub(r"[^\d]", "", phone)