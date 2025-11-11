from typing import Any
from potato.errors import ParamError

CORES: dict[str, dict[str, str]] = {
    'BOLD': {
        'BLACK': '\033[1;30m',
        'RED': '\033[1;31m',
        'GREEN': '\033[1;32m',
        'YELLOW': '\033[1;33m',
        'BLUE': '\033[1;34m',
        'PURPLE': '\033[1;35m',
        'CYAN': '\033[1;36m',
        'GRAY': '\033[1;37m',
        'WHITE': '\033[1;38m'
    },
    'NOR': {
        'BLACK': '\033[;30m',
        'RED': '\033[;31m',
        'GREEN': '\033[;32m',
        'YELLOW': '\033[;33m',
        'BLUE': '\033[;34m',
        'PURPLE': '\033[;35m',
        'CYAN': '\033[;36m',
        'GRAY': '\033[;37m',
        'WHITE': '\033[;38m'
    }
}


def mostra(*valor: Any, end: str | None = '\n', sep: str = ' ', color: str = '', mode: str = '') -> None:
    """
    Print so que traduzido

    :param sep: O separador das strings
    :param end: O que vai estar no final
    :param valor: O que vai ser imprimido
    :param color: Cor opcional
    :param mode: Tipo obrigativo para cores automáticas (NOR ou BOLD)

    :return: None

    Cores disponíveis:
    BLACK, RED, GREEN, YELLOW, BLUE, PURPLE, CYAN, GRAY, WHITE
    Tipos de texto:
    BOLD, NOR
    """

    if color and mode:
        mode = mode.upper()
        color = color.upper()

        if mode not in CORES:
            raise ParamError('\033[1;34mModo invalido!')

        if color not in CORES[mode]:
            raise ParamError('\033[1;34mCor invalida!')

        print(CORES[mode][color], end='')

    print(sep.join(valor), end=end, sep=sep)


def get_num(prompt: str, erro_msg: str = 'Número invalido!', retry: bool = False,
            num_type: str = 'int') -> int | float | None:
    """
    Função para pegar um número

    :param num_type: O tipo do valor a ser retornado deve ser int | float
    :param prompt: O prompt para o usuário
    :param erro_msg: A mensagem de erro
    :param retry: Parametro para verificar se vai se repetir

    :return: Retorna o tipo número do parâmetro do num_type
    """
    while True:
        try:
            match num_type:
                case 'int':
                    return int(input(prompt))
                case 'float':
                    return float(input(prompt))
                case _:
                    raise ParamError(
                        f'{CORES["BOLD"]["RED"]}ERRO! {CORES["BOLD"]["BLUE"]}Parametro num_type deve ser: int | float')
        except ValueError:
            print(erro_msg)
            if not retry:
                break


def divisivel(num1: int | float, num2: int | float) -> bool:
    return num1 % num2 == 0


def fat(num: int, verbose: bool = False) -> int:
    """
    Calcula o fatorial de um número

    :param verbose: Parametro para verificar se vai mostrar o número durante o cálculo
    :param num: O número para pegar o fatorial

    :return: Retorna o número do fatorial
    """

    fatorial: int = 1

    if num < 1:
        return fatorial

    while num >= 2:
        fatorial += num
        if verbose:
            print(fatorial)
        num -= 1

    return fatorial


def par(num: int) -> bool:
    """
    Verifica se um número e par ou não

    :param num: O número para ser verificado

    :return: Retorna True se o número for par e False se for impar
    """
    return num % 2 == 0


def primo(num: int) -> bool:
    """
    Verifica se um número e primo

    :param num: O número para ser verificado

    :return: Retorna True se o número for primo e False se o número não for primo
    """
    if num < 2:
        return False

    if par(num):
        return False

    for in_num in range(2, num):
        if divisivel(num, in_num):
            return False

    return True


def raiz_qdd(num: int | float) -> float:
    return num ** 0.5
