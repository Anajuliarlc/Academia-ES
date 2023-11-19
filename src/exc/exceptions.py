class EmptyFieldError(ValueError):
    """Exception raised for empty inputs"""

    def __init__(self):
        self.message = "Os campos não podem estar vazios."
        super().__init__(self.message)

class InvalidCPFError(ValueError):
    """Exception raised for errors in the input CPF (Cadastro de Pessoa Física)."""

    def __init__(self, cpf: str):
        self.message = f"O CPF digitado '{cpf}' é inválido."
        super().__init__(self.message)
