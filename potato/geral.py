from typing import Any

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


def mostra(*valor: Any, end: str | None = '\n', sep: str = ' ') -> None:
    """Print so que traduzido
    :param sep: O separador das strings
    :param end: O que vai estar no final
    :param valor: O que vai ser imprimido
    """
    print(sep.join(valor), end=end, sep=sep)


def get_int(prompt: str, erro_msg: str = 'Número invalido!', retry: bool = False) -> int | float | None:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(erro_msg)
            if not retry:
                break


def fat(num: int, verbose: bool = False) -> int:
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
    return num % 2 == 0


def primo(num: int) -> bool:
    if num < 2:
        return False

    if par(num):
        return False

    for in_num in range(2, num):
        if in_num % num == 0:
            return False

    return True
