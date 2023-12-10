class EmptyFieldError(ValueError):
    """Exception raised for empty inputs.
    
    >>> try:
    ...     raise EmptyFieldError('username', ' Por favor, preencha este campo.')
    ... except EmptyFieldError as e:
    ...     str(e)
    'O campo username não pode estar vazio. Por favor, preencha este campo.'
    """

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

    >>> try:
    ...     raise InvalidCPFError('123.456.789-00', ' Por favor, verifique o CPF digitado.')
    ... except InvalidCPFError as e:
    ...     str(e)
    "O CPF digitado \'123.456.789-00\' é inválido.  Por favor, verifique o CPF digitado."
    >>> try:
    ...     raise InvalidCPFError('000.000.000-00')
    ... except InvalidCPFError as e:
    ...     str(e)
    "O CPF digitado \'000.000.000-00\' é inválido. "
    >>> try:
    ...     raise InvalidCPFError('abc.def.ghi-jk')
    ... except InvalidCPFError as e:
    ...     str(e)
    "O CPF digitado \'abc.def.ghi-jk\' é inválido. "
    """

    def __init__(self, cpf: str, msg: str = ""):
        """Raises an exception when a CPF is invalid.

        :param cpf: The invalid CPF that caused the exception.
        :type cpf: str
        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        self.message = f'O CPF digitado \'{cpf}\' é inválido. ' + msg
        super().__init__(self.message)

class CPFNotFoundError(KeyError):
    """Exception raised when inputed CPF is not registered in system.

    >>> try:
    ...     raise CPFNotFoundError('123.456.789-00', ' Por favor, verifique o CPF digitado.')
    ... except CPFNotFoundError as e:
    ...     str(e)
    "O CPF digitado \'123.456.789-00\' não está cadastrado.  Por favor, verifique o CPF digitado."
    >>> try:
    ...     raise CPFNotFoundError('000.000.000-00')
    ... except CPFNotFoundError as e:
    ...     str(e)
    "O CPF digitado \'000.000.000-00\' não está cadastrado. "
    >>> try:
    ...     raise CPFNotFoundError('abc.def.ghi-jk')
    ... except CPFNotFoundError as e:
    ...     str(e)
    "O CPF digitado \'abc.def.ghi-jk\' não está cadastrado. "
    """

    def __init__(self, cpf: str, msg: str = ""):
        """Raises an exception when a CPF is not registered.

        :param cpf: The invalid CPF that caused the exception.
        :type cpf: str
        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        self.message = f"O CPF digitado '{cpf}' não está cadastrado. " + msg
        super().__init__(self.message)

    def __str__(self):
        return self.message

class IncorrectPasswordError(KeyError):
    """Exception raised when inputed password is incorrect.
    
    >>> try:
    ...     raise IncorrectPasswordError()
    ... except IncorrectPasswordError as e:
    ...     e
    IncorrectPasswordError('A senha digitada está incorreta. ')
    """

    def __init__(self, msg: str = ""):
        """Raises an exception when a password is wrong.

        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        self.message = "A senha digitada está incorreta. " + msg
        super().__init__(self.message)

class InvalidPasswordError(ValueError):
    """Exception raised when inputed password is invalid.
    
    >>> try:
    ...     raise InvalidPasswordError('Use uma senha mais forte.')
    ... except InvalidPasswordError as e:
    ...     str(e)
    'A senha digitada é inválida. Use uma senha mais forte.'
    """

    def __init__(self, msg: str = ""):
        """Raises an exception when a password is invalid.

        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        self.message = "A senha digitada é inválida. " + msg
        super().__init__(self.message)

class WrongTypeError(TypeError):
    """Exception raised when inputed type is wrong.

    >>> try:
    ...     raise WrongTypeError('idade', int, str, ' Valor inválido.', True)
    ... except WrongTypeError as e:
    ...     str(e)
    "idade esperava <class \'int\'>, (recebido = <class \'str\'>). Valor inválido."
    >>> try:
    ...     raise WrongTypeError('idade', int, str, ' Valor inválido.', False)
    ... except WrongTypeError as e:
    ...     str(e)
    ' Valor inválido.'
    """

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

    def __str__(self):
        return self.message

class NonLetterError(ValueError):
    """Exception raised when inputed name contains non letters.

    >>> try:
    ...     raise NonLetterError('nome', ' Por favor, verifique o nome digitado.')
    ... except NonLetterError as e:
    ...     str(e)
    'nome não pode conter números ou caracteres especiais. Por favor, verifique o nome digitado.'
    >>> try:
    ...     raise NonLetterError('sobrenome')
    ... except NonLetterError as e:
    ...     str(e)
    'sobrenome não pode conter números ou caracteres especiais.'
    """

    def __init__(self, field: str, msg: str = ""):
        """Raises an exception when a name contains non letters.

        :param field: Name of the field with the wrong type.
        :type field: str
        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        self.message = f"{field} não pode conter números ou caracteres especiais." + msg
        super().__init__(self.message)

    def __str__(self):
        return self.message

class WrongLengthError(ValueError):
    """Exception raised when inputed length is wrong.

    >>> try:
    ...     raise WrongLengthError('CPF', 11, 10, ' Por favor, verifique o CPF digitado.')
    ... except WrongLengthError as e:
    ...     str(e)
    'CPF espera 11 dígitos (recebidos = 10).  Por favor, verifique o CPF digitado.'
    >>> try:
    ...     raise WrongLengthError('CEP', 8, 9)
    ... except WrongLengthError as e:
    ...     str(e)
    'CEP espera 8 dígitos (recebidos = 9). '
    """

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

    def __str__(self):
        return self.message

class InvalidCardTypeError(ValueError):
    """Exception raised when inputed card type is invalid.

    >>> try:
    ...     raise InvalidCardTypeError(' Por favor, verifique o tipo de cartão digitado.')
    ... except InvalidCardTypeError as e:
    ...     str(e)
    'O tipo de cartão digitado é inválido. Por favor, verifique o tipo de cartão digitado.'
    """

    def __init__(self, msg: str = ""):
        """Raises an exception when a card type is invalid."""
        self.message = "O tipo de cartão digitado é inválido." + msg
        super().__init__(self.message)

class WrongFormatError(ValueError):
    """Exception raised when inputed date is in the wrong format.

    >>> try:
    ...     raise WrongFormatError(' Por favor, verifique a data digitada.')
    ... except WrongFormatError as e:
    ...     str(e)
    "O formato para datas é \'MM/AA\'. Por favor, verifique a data digitada."
    """

    def __init__(self, msg: str = ""):
        """Raises an exception when a date is in the wrong format.

        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        self.message = "O formato para datas é 'MM/AA'." + msg
        super().__init__(self.message)

class LeftZeroError(ValueError):
    """Exception raised when inputed number has left zeros.

    >>> try:
    ...     raise LeftZeroError(' Por favor, verifique o número digitado.')
    ... except LeftZeroError as e:
    ...     str(e)
    'Primeiro dígito não pode ser 0. Por favor, verifique o número digitado.'
    """

    def __init__(self, msg: str = ""):
        """Raises an exception when a number has left zeros.

        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        self.message = "Primeiro dígito não pode ser 0." + msg
        super().__init__(self.message)

class TimeConflictError(ValueError):
    """Exception raised when a time conflict is found.

    >>> try:
    ...     raise TimeConflictError(' Por favor, verifique os horários.')
    ... except TimeConflictError as e:
    ...     str(e)
    'O horário está em conflito com outro horário.  Por favor, verifique os horários.'
    """

    def __init__(self, msg: str = ""):
        """Raises an exception when a time conflict is found.

        :param msg: Additional message to be displayed, defaults to ""
        :type msg: str, optional
        """
        self.message = "O horário está em conflito com outro horário. " + msg
        super().__init__(self.message)

class InvalidDateError(ValueError):
    """Exception raised when inputed date is invalid.

    >>> try:
    ...     raise InvalidDateError('30/02/2022', ' Por favor, verifique a data digitada.')
    ... except InvalidDateError as e:
    ...     str(e)
    '30/02/2022 não é uma data válida.  Por favor, verifique a data digitada.'
    """

    def __init__(self, input, msg: str = ""):
        """Raises an exception when a date is invalid."""
        self.message = f"{input} não é uma data válida. " + msg
        super().__init__(self.message)

class InvalidRGError(ValueError):
    """Exception raised when inputed RG is invalid.

    >>> try:
    ...     raise InvalidRGError('123456789', ' Por favor, verifique o RG digitado.')
    ... except InvalidRGError as e:
    ...     str(e)
    "O RG digitado \'123456789\' é inválido.  Por favor, verifique o RG digitado."
    """

    def __init__(self, rg: str, msg: str = ""):
        """Raises an exception when a RG is invalid."""
        self.message = f"O RG digitado '{rg}' é inválido. " + msg
        super().__init__(self.message)

class CPFAlreadyExistsError(KeyError):
    """Exception raised when inputed CPF is already registered.

    >>> try:
    ...     raise CPFAlreadyExistsError('12345678901', ' Por favor, verifique o CPF digitado.')
    ... except CPFAlreadyExistsError as e:
    ...     str(e)
    "O CPF \'12345678901\' já está cadastrado.  Por favor, verifique o CPF digitado."
    """

    def __init__(self, cpf: str, msg: str = ""):
        """Raises an exception when a CPF is already registered."""
        self.message = f'O CPF \'{cpf}\' já está cadastrado. ' + msg
        super().__init__(self.message)
        
    def __str__(self):
        return self.message

class InvalidPhoneError(ValueError):
    """Exception raised when inputed phone is invalid.

    >>> try:
    ...     raise InvalidPhoneError('123456789', ' Por favor, verifique o telefone digitado.')
    ... except InvalidPhoneError as e:
    ...     str(e)
    "O telefone \'123456789\' é inválido.  Por favor, verifique o telefone digitado."
    """

    def __init__(self, phone: str, msg: str = ""):
        """Raises an exception when a phone is invalid."""
        self.message = f"O telefone '{phone}' é inválido. " + msg
        super().__init__(self.message)

class InvalidUFError(ValueError):
    """Exception raised when inputed state is invalid.

    >>> try:
    ...     raise InvalidUFError('SP', ' Por favor, verifique o estado digitado.')
    ... except InvalidUFError as e:
    ...     str(e)
    "O estado \'SP\' é inválido.  Por favor, verifique o estado digitado."
    """

    def __init__(self, state: str, msg: str = ""):
        """Raises an exception when a state is invalid."""
        self.message = f"O estado '{state}' é inválido. " + msg
        super().__init__(self.message)
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)