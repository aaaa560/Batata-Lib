class ParamError(Exception):
    """Erro para parâmetros inválidos"""

    def __init__(self, message: str = '\033[1;31mERRO! \033[1;34mParâmetro invalido!', code: int | None = None,
                 param: str = '', esperado: str = '') -> None:
        super().__init__(message)
        self.code: int | None = code
        self.message: str = message
        self.param: str = param
        self.esperado: str = esperado

        if param and esperado:
            self.message = f"{message}\n{param} -> {esperado}"
        elif param or esperado:
            if param and not esperado:
                self.message = f"{message}\n{param}"
            elif esperado and not param:
                self.message = f"{message}\nEsperado: {esperado}"

    def __str__(self) -> str:
        if self.code:
            return f'{self.code}: {self.message}'
        return f'{self.message}'
