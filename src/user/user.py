import pandas as pd
import re

import sys 
import os
sys.path.append(os.path.abspath("./src")) # Adds src directory to python modules path.

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
        return self.table[self.table['username'] == username]
    
    def insert(self, username: str, password: str) -> None:
        self.table = self.table.append({'CPF': username, 'Password': password}, ignore_index=True)
        self.update()


class User():
    def __init__(self, cpf: str, password: str) -> None:
        self.validate_cpf(cpf)
        self.cpf = cpf

        self.validate_password(password)

        self.access = Access("./src/database/usuarios.csv")
        self.login(self.cpf, password)

    def validate_cpf(self, cpf: str) -> None:
        if cpf == "":
            raise exc.EmptyFieldError("CPF")

        if re.search(r"[^\d.\-]", cpf):
            raise exc.InvalidCPFError(cpf, "O CPF só deve conter números.")

        if len(re.sub(r"[.\-]", "", cpf)) != 11:
            raise exc.InvalidCPFError(cpf, "O CPF deve conter 11 dígitos.")

    def validate_password(self, password: str) -> None:
        if password == "":
            raise exc.EmptyFieldError("'senha'")

    def login(self, username, password):
        pass
    