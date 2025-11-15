from typing import Any
from batata import mostra

__all__ = ['info', 'warn', 'err', 'out']


def info(informacao: Any) -> None:
    """
    Essa função e um atalho para dar informações ao usuário

    :param informacao: O que vai ser mostrado para o usuário

    :return: None
    """
    mostra(f'[INFO]: {informacao}', color='cyan', mode='bold')


def warn(waring: Any) -> None:
    """
    Essa função e um atalho para dar avisos ao usuário

    :param waring: O que vai ser mostrado para o usuário

    :return: None
    """
    mostra(f'[WARN]: {waring}', color='yellow', mode='bold')


def err(erro: Any) -> None:
    """
    Essa função e um atalho para mostrar um erro ao usuário

    :param erro: O que vai ser mostrado para o usuário

    :return: None
    """
    mostra(f'[ERRO]: {erro}', color='red', mode='bold')


def out(valor: Any) -> None:
    """
    Essa função e um atalho para mostrar resultados ao usuário

    :param valor: O que vai ser mostrado para o usuário

    :return: None
    """
    mostra(valor, color='blue', mode='bold')
