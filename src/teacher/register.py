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
""" Refactoring 7
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

""" Refactoring 8
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
        
        if re.search(r"[^\d\-\(\)]", phone):
            raise exc.InvalidPhoneError(phone)
        
        if len(re.sub(r"[^\d]", "", phone)) != 11:
            raise exc.WrongLengthError("telefone", 11, len(re.sub(r"[^\d]", "", phone)))
        
        return re.sub(r"[^\d]", "", phone)
    
    def validate_uf(self, uf: str) -> str:
        if uf == "" or uf == "UF":
            raise exc.EmptyFieldError("UF")
        
        if not re.match(r"[A-Z]{2}", uf):
            raise exc.InvalidUFError(uf, 
                                     "O UF deve ser duas letras maiúsculas.")
        
        return uf
"""
#############################
""" Refactoring 9
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
        
        if re.search(r"[^\d\-\(\)]", phone):
            raise exc.InvalidPhoneError(phone)
        
        if len(re.sub(r"[^\d]", "", phone)) != 11:
            raise exc.WrongLengthError("telefone", 11, len(re.sub(r"[^\d]", "", phone)))
        
        return re.sub(r"[^\d]", "", phone)
    
    def validate_uf(self, uf: str) -> str:
        if uf == "" or uf == "UF":
            raise exc.EmptyFieldError("UF")
        
        if not re.match(r"[A-Z]{2}", uf):
            raise exc.InvalidUFError(uf, 
                                     "O UF deve ser duas letras maiúsculas.")
        
        return uf

    def validate_neigh(self, neigh: str) -> str:
        if neigh == "" or neigh == "Bairro":
            raise exc.EmptyFieldError("bairro")
        
        if len(neigh) > 255:
            raise exc.WrongLengthError("bairro", 255, len(neigh))
        
        return neigh
"""

#############################
""" Refactoring 10
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
        
        if re.search(r"[^\d\-\(\)]", phone):
            raise exc.InvalidPhoneError(phone)
        
        if len(re.sub(r"[^\d]", "", phone)) != 11:
            raise exc.WrongLengthError("telefone", 11, len(re.sub(r"[^\d]", "", phone)))
        
        return re.sub(r"[^\d]", "", phone)
    
    def validate_uf(self, uf: str) -> str:
        if uf == "" or uf == "UF":
            raise exc.EmptyFieldError("UF")
        
        if not re.match(r"[A-Z]{2}", uf):
            raise exc.InvalidUFError(uf, 
                                     "O UF deve ser duas letras maiúsculas.")
        
        return uf

    def validate_neigh(self, neigh: str) -> str:
        if neigh == "" or neigh == "Bairro":
            raise exc.EmptyFieldError("bairro")
        
        if len(neigh) > 255:
            raise exc.WrongLengthError("bairro", 255, len(neigh))
        
        return neigh

    def validate_medic(self, medic: str) -> str:
        if medic == "Dados médicos":
            medic = ""
        return medic
"""

import re

import main
import exc.exceptions as exc
from datetime import datetime

class Register:
    def __init__(self,
                 name: str,
                 birth: str,
                 cpf: str,
                 rg: str,
                 password: str,
                 phone: str,
                 uf: str,
                 city: str,
                 neigh: str,
                 medic: str) -> None:
        
        self.system = main.System()

        self.name = self.validate_name(name)
        self.birth = self.validate_birth(birth)
        self.cpf = self.validate_cpf(cpf)
        self.rg = self.validate_rg(rg)
        self.password = self.validate_password(password)
        self.phone = self.validate_phone(phone)
        self.uf = self.validate_uf(uf)
        self.city = self.validate_city(city)
        self.neigh = self.validate_neigh(neigh)
        self.medic = self.validate_medic(medic)

    def validate_name(self, name: str) -> str:
        if re.match("Nome do aluno", name): name = ""
        if len(name) == 0:
            raise exc.EmptyFieldError("nome")
        if len(name) > 255:
            raise exc.WrongLengthError("nome", 255, len(name))
        return name

    def validate_birth(self, birth: str) -> str:
        try: datetime.strptime(birth, "%d/%m/%Y")
        except ValueError: raise exc.InvalidDateError(birth)
        
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
            raise exc.InvalidPasswordError("A senha deve conter um "
                        "número, uma letra maiúscula e uma minúscula.")
        
        return password
    
    def validate_phone(self, phone: str) -> str:
        if phone == "" or phone == "Telefone ((XX) XXXXX-XXXX)":
            raise exc.EmptyFieldError("telefone")
        
        if re.search(r"[^\d\-\(\)]", phone):
            raise exc.InvalidPhoneError(phone)
        
        if len(re.sub(r"[^\d]", "", phone)) != 11:
            raise exc.WrongLengthError("telefone", 11, len(re.sub(r"[^\d]", "", phone)))
        
        return re.sub(r"[^\d]", "", phone)
    
    def validate_uf(self, uf: str) -> str:
        if uf == "" or uf == "UF":
            raise exc.EmptyFieldError("UF")
        
        if not re.match(r"[A-Z]{2}", uf):
            raise exc.InvalidUFError(uf, 
                                     "O UF deve ser duas letras maiúsculas.")
        
        return uf

    def validate_city(self, city: str) -> str:
        if city == "" or city == "Cidade":
            raise exc.EmptyFieldError("cidade")
        
        if len(city) > 255:
            raise exc.WrongLengthError("cidade", 255, len(city))
        
        return city 

    def validate_neigh(self, neigh: str) -> str:
        if neigh == "" or neigh == "Bairro":
            raise exc.EmptyFieldError("bairro")
        
        if len(neigh) > 255:
            raise exc.WrongLengthError("bairro", 255, len(neigh))
        
        return neigh

    def validate_medic(self, medic: str) -> str:
        if medic == "Dados médicos":
            medic = ""
        return medic

    def run(self):
        true_date = datetime.strptime(self.birth, "%d/%m/%Y")
        self.system.database.insert("User (UserName, BirthDate, CPF, RG, UserPassword)", 
                                    f"(\'{self.name}\', \'{true_date}\', \'{self.cpf}\', \'{self.rg}\', \'{self.password}\')")
        
        user_id = self.system.database.select("User", "IdUser", f"WHERE CPF = {self.cpf}").iloc[0][0]
        current_date = datetime.now()

        self.system.database.insert("Student (IdUser, PhoneNumber, State, City, Neighbourhood, RegistrationDate, MedicalData)", 
                                    f"({user_id}, \'{self.phone}\', \'{self.uf}\', \'{self.city}\', \'{self.neigh}\', \'{current_date}\', \'{self.medic}\')")
        
