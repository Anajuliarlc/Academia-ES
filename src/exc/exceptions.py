class EmptyFieldError(ValueError):
    """Exception raised for empty inputs"""

    def __init__(self, field: str, msg: str = ""):
        """Raises an exception when a field is empty.

        :param field: Name of the empty field.
        :type field: str
        :param msg: Additional message to be displayed, defaults to "".
        :type msg: str, optional
        """
        self.message = f"O campo {field} não pode estar vazio." + msg
        super().__init__(self.message)

class InvalidCPFError(ValueError):
    """Exception raised for errors in the input CPF (Cadastro de Pessoa Física).
    """

    def __init__(self, cpf: str, msg: str = ""):
        """Raises an exception when a CPF is invalid.

        :param cpf: The invalid CPF that caused the exception.
        :type cpf: str
        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        self.message = f"O CPF digitado '{cpf}' é inválido. " + msg
        super().__init__(self.message)

class CPFNotFoundError(KeyError):
    """Exception raised when inputed CPF is not registered in system."""

    def __init__(self, cpf: str, msg: str = ""):
        """Raises an exception when a CPF is not registered.

        :param cpf: The invalid CPF that caused the exception.
        :type cpf: str
        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        self.message = f"O CPF digitado '{cpf}' não está cadastrado. " + msg
        super().__init__(self.message)