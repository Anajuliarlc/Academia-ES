class EmptyFieldError(ValueError):
    """Exception raised for empty inputs"""

    def __init__(self, field: str):
        self.message = f"O campo {field} não pode estar vazio."
        super().__init__(self.message)

class InvalidCPFError(ValueError):
    """Exception raised for errors in the input CPF (Cadastro de Pessoa Física)."""

    def __init__(self, cpf: str, msg: str = ""):
        self.message = f"O CPF digitado '{cpf}' é inválido. " + msg
        super().__init__(self.message)
