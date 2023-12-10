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
    """ Class that represents the register operation.
    """
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
        """
        Initializes an object of the Register class.

        :param name: The name of the student.
        :type name: str
        :param birth: The birth date of the student.
        :type birth: str
        :param cpf: The CPF of the student.
        :type cpf: str
        :param rg: The RG of the student.
        :type rg: str
        :param password: The password of the student.
        :type password: str
        :param phone: The phone number of the student.
        :type phone: str
        :param uf: The state of the student.
        :type uf: str
        :param city: The city of the student.
        :type city: str
        :param neigh: The neighborhood of the student.
        :type neigh: str
        :param medic: The student's doctor.
        :type medic: str
        """
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
            """Validates the name of the student.

            :param name: The name of the student.
            :type name: str
            :raises exc.EmptyFieldError: If the name is empty.
            :raises exc.WrongLengthError: If the name exceeds the maximum length of 255 characters.
            :return: The validated name.
            :rtype: str
            """
            if re.match("Nome do aluno", name): name = ""
            if len(name) == 0:
                raise exc.EmptyFieldError("nome")
            if len(name) > 255:
                raise exc.WrongLengthError("nome", 255, len(name))
            return name

    def validate_birth(self, birth: str) -> str:
        """
        Validates the birth date.

        :param birth: The birth date to be validated.
        :type birth: str
        :raises exc.EmptyFieldError: If the birth date is empty.
        :raises exc.InvalidDateError: If the birth date is not in the format (dd/mm/aaaa).
        :return: The validated birth date.
        :rtype: str
        """
        if "Data de nascimento (dd/mm/aaaa)" == birth:
            birth = ""
        if len(birth) == 0:
            raise exc.EmptyFieldError("data de nascimento")

        try:
            datetime.strptime(birth, "%d/%m/%Y")
        except ValueError:
            raise exc.InvalidDateError(birth, "Use o formato (dd/mm/aaaa)")

        return birth
    
    def validate_cpf(self, cpf: str) -> str:
        """
        Validates the given CPF.

        :param cpf: The CPF to be validated.
        :type cpf: str
        :raises exc.EmptyFieldError: If the CPF is empty or equal to "CPF".
        :raises exc.InvalidCPFError: If the CPF contains non-digit characters.
        :raises exc.InvalidCPFError: If the CPF does not have 11 digits.
        :raises exc.CPFAlreadyExistsError: If the CPF already exists in the database.
        :return: The validated CPF.
        :rtype: str
        """
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
            """Validates the RG number.

            :param rg: The RG number to be validated.
            :type rg: str
            :raises exc.EmptyFieldError: If the RG field is empty.
            :raises exc.InvalidRGError: If the RG contains invalid characters.
            :raises exc.WrongLengthError: If the RG has an incorrect length.
            :return: The validated RG number without special characters.
            :rtype: str
            """
            if rg == "" or rg == "RG":
                raise exc.EmptyFieldError("RG")

            if re.search(r"[^\d.\-]", rg):
                raise exc.InvalidRGError(rg, "O RG só deve conter números.")

            if len(re.sub(r"[.\-]", "", rg)) > 11:
                raise exc.WrongLengthError("RG", 11, len(re.sub(r"[.\-]", "", rg)))

            return re.sub(r"[.\-]", "", rg)

    def validate_password(self, password: str) -> None:
        """
        Validates the given password.

        :param password: The password to be validated.
        :type password: str
        :raises exc.EmptyFieldError: If the password is empty.
        :raises exc.InvalidPasswordError: If the password contains spaces.
        :raises exc.InvalidPasswordError: If the password length is not between 7 and 14 characters.
        :raises exc.InvalidPasswordError: If the password does not contain at least one digit, one uppercase letter, and one lowercase letter.
        :return: None
        :rtype: None
        """
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
        """Validates a phone number.

        :param phone: The phone number to be validated.
        :type phone: str
        :raises exc.EmptyFieldError: If the phone number is empty or equal to "Telefone ((XX) XXXXX-XXXX)".
        :raises exc.InvalidPhoneError: If the phone number contains invalid characters.
        :raises exc.WrongLengthError: If the phone number has an incorrect length.
        :return: The validated phone number.
        :rtype: str
        """
        if phone == "" or phone == "Telefone ((XX) XXXXX-XXXX)":
            raise exc.EmptyFieldError("telefone")
        
        if re.search(r"[^\d\-\(\)]", phone):
            raise exc.InvalidPhoneError(phone)
        
        if len(re.sub(r"[^\d]", "", phone)) != 11:
            raise exc.WrongLengthError("telefone", 11, len(re.sub(r"[^\d]", "", phone)))
        
        return re.sub(r"[^\d]", "", phone)
    
    def validate_uf(self, uf: str) -> str:
            """
            Validates the UF (Unidade Federativa) code.

            :param uf: The UF code to be validated.
            :type uf: str
            :raises exc.EmptyFieldError: If the UF code is empty or equal to "UF".
            :raises exc.InvalidUFError: If the UF code is not in the format of two uppercase letters.
            :return: The validated UF code.
            :rtype: str
            """
            if uf == "" or uf == "UF":
                raise exc.EmptyFieldError("UF")
            
            if not re.match(r"[A-Z]{2}", uf):
                raise exc.InvalidUFError(uf, 
                                         "O UF deve ser duas letras maiúsculas.")
            
            return uf

    def validate_city(self, city: str) -> str:
            """Validates the city field.

            :param city: The city to be validated.
            :type city: str
            :raises exc.EmptyFieldError: If the city is empty or equal to "Cidade".
            :raises exc.WrongLengthError: If the city length exceeds 255 characters.
            :return: The validated city.
            :rtype: str
            """
            if city == "" or city == "Cidade":
                raise exc.EmptyFieldError("cidade")
            
            if len(city) > 255:
                raise exc.WrongLengthError("cidade", 255, len(city))
            
            return city

    def validate_neigh(self, neigh: str) -> str:
            """Validates the neighborhood field.

            :param neigh: The neighborhood value to be validated.
            :type neigh: str
            :raises exc.EmptyFieldError: If the neighborhood field is empty or equal to "Bairro".
            :raises exc.WrongLengthError: If the length of the neighborhood field exceeds 255 characters.
            :return: The validated neighborhood value.
            :rtype: str
            """
            if neigh == "" or neigh == "Bairro":
                raise exc.EmptyFieldError("bairro")
            
            if len(neigh) > 255:
                raise exc.WrongLengthError("bairro", 255, len(neigh))
            
            return neigh

    def validate_medic(self, medic: str) -> str:
            """Validates the medic information.

            :param medic: The medic information to be validated.
            :type medic: str
            :return: The validated medic information.
            :rtype: str
            """
            if medic == "Dados médicos":
                medic = ""
            return medic

    def run(self):
            """
            Executes the registration process for a student.

            This method inserts the student's information into the database, including their name, birthdate, CPF, RG, and password.
            It also retrieves the user ID from the database based on the CPF provided.
            Finally, it inserts additional information into the Student table, such as phone number, state, city, neighborhood, registration date, and medical data.

            :return: None
            :rtype: None
            """
            true_date = datetime.strptime(self.birth, "%d/%m/%Y")
            self.system.database.insert("User (UserName, BirthDate, CPF, RG, UserPassword)", 
                                        f"(\'{self.name}\', \'{true_date}\', \'{self.cpf}\', \'{self.rg}\', \'{self.password}\')")
            
            user_id = self.system.database.select("User", "IdUser", f"WHERE CPF = {self.cpf}").iloc[0][0]
            current_date = datetime.now()

            self.system.database.insert("Student (IdUser, PhoneNumber, State, City, Neighbourhood, RegistrationDate, MedicalData)", 
                                        f"({user_id}, \'{self.phone}\', \'{self.uf}\', \'{self.city}\', \'{self.neigh}\', \'{current_date}\', \'{self.medic}\')")
               
