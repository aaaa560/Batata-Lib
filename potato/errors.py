class ParamError(Exception):
    """Erro para parâmetros inválidos"""
    def __init__(self, message: str = '\033[1;31mERRO! \033[1;34mParâmetro invalido!', code: int | None = None) -> None:
        super().__init__(message)
        self.code: int | None = code
        self.message: str = message

    def __str__(self) -> str:
        if self.code:
            return f'{self.code}: {self.message}'
        return f'{self.message}'