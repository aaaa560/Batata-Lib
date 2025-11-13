from typing import Any
from potato.geral import mostra


def info(valor: Any) -> None:
    mostra(valor, color='cyan', mode='bold')


def warn(valor: Any) -> None:
    mostra(valor, color='yellow', mode='bold')


def err(valor: Any) -> None:
    mostra(valor, color='red', mode='bold')


def out(valor: Any) -> None:
    mostra(valor, color='blue', mode='bold')
