import pandas as pd
import re

import sys 
import os
# Adds src directory to python modules path.
sys.path.append(os.path.abspath("./src")) 

from main import System
import exc.exceptions as exc

class Login():
    """Login class for accessing a user's account."""
    def __init__(self, cpf: str, password: str) -> None:
        """
        Initializes the Login class.

        :param cpf: The user's CPF.
        :type cpf: str
        :param password: The user's password.
        :type password: str
        :raises EmptyFieldError: Se o campo senha estiver vazio.
        """
        self.system = System() # Access the system singleton instance.
        self.cpf = self.validate_cpf(cpf)

        if password == "":
            raise exc.EmptyFieldError("senha")
        self.password = password

    def validate_cpf(self, cpf: str) -> str:
        """
        Validates a CPF (Cadastro de Pessoas Físicas) number.

        :param cpf: The CPF number to be validated.
        :type cpf: str
        :return: The validated CPF number without any formatting characters.
        :rtype: str
        :raises EmptyFieldError: If the CPF is an empty string.
        :raises InvalidCPFError: If the CPF contains non-digit characters, 
        or if it does not have exactly 11 digits.
        """
        if cpf == "":
            raise exc.EmptyFieldError("CPF")

        if re.search(r"[^\d.\-]", cpf):
            raise exc.InvalidCPFError(cpf, "O CPF só deve conter números.")

        result_cpf = re.sub(r"[.\-]", "", cpf)

        if len(result_cpf) != 11:
            raise exc.InvalidCPFError(cpf, "O CPF deve conter 11 dígitos.")
        
        return result_cpf

    def run(self) -> None:
        database = self.system.database
        attempt = database.select("User", "*", f"WHERE CPF = {self.cpf}")
        
        if attempt.empty:
            raise exc.CPFNotFoundError(self.cpf, 
            "Verifique se a entrada está correta ou solicite uma nova conta.")
        
        if attempt["UserPassword"].iloc[0] != self.password:
            raise exc.IncorrectPasswordError()
        
        self.system.user = attempt["IdUser"].iloc[0]

if __name__ == "__main__":
    login = Login("12345678901", "password123")
    login.run()
    if login.system.user:
        print("Login successful!")