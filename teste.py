from potato.geral import mostra, COLORS
from potato.errors import ParamError

raise ParamError(
    '\033[1;31mERRO! \033[1;34mParâmetros inválidos:\033[1;36m',
    param='mode | color',
    esperado=f'{", ".join(key for key in COLORS)} | {", ".join(color for color in COLORS["NOR"])}'
)
