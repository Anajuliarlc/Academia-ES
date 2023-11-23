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

class IncorrectPasswordError(KeyError):
    """Exception raised when inputed password is incorrect."""

    def __init__(self, msg: str = ""):
        """Raises an exception when a password is wrong.

        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        self.message = "A senha digitada está incorreta. " + msg
        super().__init__(self.message)

class InvalidPasswordError(ValueError):
    """Exception raised when inputed password is invalid."""

    def __init__(self, msg: str = ""):
        """Raises an exception when a password is invalid.

        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        self.message = "A senha digitada é inválida. " + msg
        super().__init__(self.message)

class WrongTypeError(TypeError):
    """Exception raised when inputed type is wrong."""

    def __init__(self, field: str, expected_type: type, actual_type: type, msg: str = "", verbose: bool = False):
        """Raises an exception when a type is wrong.

        :param field: Name of the field with the wrong type.
        :type field: str
        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        if verbose:
            self.message = f"{field} esperava {expected_type}, (recebido = {actual_type})." + msg
        else:
            self.message = msg
        super().__init__(self.message)

class NonLetterError(ValueError):
    """Exception raised when inputed name contains non letters."""

    def __init__(self, field: str, msg: str = ""):
        """Raises an exception when a name contains non letters.

        :param field: Name of the field with the wrong type.
        :type field: str
        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        self.message = f"{field} não pode conter números ou caracteres especiais." + msg
        super().__init__(self.message)

class WrongLengthError(ValueError):
    """Exception raised when inputed length is wrong."""

    def __init__(self, field: str, expected_length: int, actual_length: int, msg: str = ""):
        """Raises an exception when a length is wrong.

        :param field: Name of the field with the wrong length.
        :type field: str
        :param expected_length: Expected length of the field.
        :type expected_length: int
        :param actual_length: Actual length of the field.
        :type actual_length: int
        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        self.message = f"{field} espera {expected_length} dígitos (recebidos = {actual_length}). " + msg
        super().__init__(self.message)

class InvalidCardTypeError(ValueError):
    """Exception raised when inputed card type is invalid."""

    def __init__(self, msg: str = ""):
        """Raises an exception when a card type is invalid."""
        self.message = "O tipo de cartão digitado é inválido." + msg
        super().__init__(self.message)

class WrongFormatError(ValueError):
    """Exception raised when inputed date is in the wrong format."""

    def __init__(self, msg: str = ""):
        """Raises an exception when a date is in the wrong format.

        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        self.message = "O formato para datas é 'MM/AA'." + msg
        super().__init__(self.message)

class LeftZeroError(ValueError):
    """Exception raised when inputed number has left zeros."""

    def __init__(self, msg: str = ""):
        """Raises an exception when a number has left zeros.

        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        self.message = "Primeiro dígito não pode ser 0." + msg
        super().__init__(self.message)

class TimeConflictError(ValueError):
    """Exception raised when a time conflict is found."""

    def __init__(self, msg: str = ""):
        """Raises an exception when a time conflict is found.

        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        self.message = "O horário está em conflito com outro horário. " + msg
        super().__init__(self.message)

class InvalidDateError(ValueError):
    """Exception raised when inputed date is invalid."""

    def __init__(self, input, msg: str = ""):
        """Raises an exception when a date is invalid.

        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        self.message = f"{input} não é uma data válida. " + msg
        super().__init__(self.message)
    
class InvalidRGError(ValueError):
    """Exception raised when inputed RG is invalid."""

    def __init__(self, rg: str, msg: str = ""):
        """Raises an exception when a RG is invalid.

        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        self.message = f"O RG digitado '{rg}' é inválido. " + msg
        super().__init__(self.message)

class CPFAlreadyExistsError(KeyError):
    """Exception raised when inputed CPF is already registered."""

    def __init__(self, cpf: str, msg: str = ""):
        self.message = f"O CPF '{cpf}' já está cadastrado. " + msg
        super().__init__(self.message)

class InvalidPhoneError(ValueError):
    """Exception raised when inputed phone is invalid."""

    def __init__(self, phone: str, msg: str = ""):
        """Raises an exception when a phone is invalid.

        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        self.message = f"O telefone '{phone}' é inválido. " + msg
        super().__init__(self.message)