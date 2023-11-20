import pandas as pd
import re

import sys 
import os
# Adds src directory to python modules path.
sys.path.append(os.path.abspath("./src")) 

import exc.exceptions as exc

# Temporary class while we don't have a database
class Access:
    def __init__(self, path: str) -> None:
        self.path = path
        self.table = None
        self.update()
    
    def update(self) -> None:
        self.table = pd.read_csv(self.path)

    def write(self) -> None:
        self.table.to_csv(self.path, index=False)

    def select(self, username: str) -> pd.DataFrame:
        return self.table.loc[self.table['CPF'] == username]
    
    def insert(self, username: str, password: str) -> None:
        self.table = self.table.append({'CPF': username, 'Password': password}, 
                                       ignore_index=True)
        self.write()
        self.update()

class UserMeta(type):
    """ User Metaclass for Singleton Pattern application. """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class User(metaclass = UserMeta):
    """User class for interaction with the environment."""
    def __init__(self) -> None:
        self.logged_cpf = None
        self.access = None

    def validate_cpf(self, cpf: str) -> None:
        if cpf == "":
            raise exc.EmptyFieldError("CPF")

        if re.search(r"[^\d.\-]", cpf):
            raise exc.InvalidCPFError(cpf, "O CPF só deve conter números.")

        if len(re.sub(r"[.\-]", "", cpf)) != 11:
            raise exc.InvalidCPFError(cpf, "O CPF deve conter 11 dígitos.")

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

    def login(self, cpf: str, password: str) -> None:
        self.validate_cpf(cpf)
        if password == "": raise exc.EmptyFieldError("senha")

        login_cpf = int(re.sub(r"[.\-]", "", cpf))

        # TODO: Replace with database access and guarantee the cpf type is right
        self.access = Access("data/usuarios.csv")

        if self.access.select(login_cpf).empty:
            raise exc.CPFNotFoundError(cpf, 
                "Verify if the input is correct, or register a new account.")
        
        if self.access.select(login_cpf)['Senha'].values[0] != password:
            raise exc.IncorrectPasswordError()

        self.logged_cpf = login_cpf

    def register(self, cpf: str, password: str) -> None:
        self.validate_cpf(cpf)
        self.validate_password(password)

if __name__ == "__main__":
    # Temporary driver code to test access to database
    access = Access("./data/usuarios.csv")
    access.select(32364696210)
    