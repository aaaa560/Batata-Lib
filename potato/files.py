import json
from typing import Any


def creat_file(name: str) -> None:
    """
    Essa função apenas cria o arquivo

    :param name: Nome do arquivo que vai ser criado

    :return: None
    """
    with open(name, "w", encoding="utf-8") as f:
        return


def read_file(arquivo: str) -> str:
    """
    Essa função retorna o conteúdo de um arquivo

    :param arquivo: Nome do arquivo que vai ser lido

    :return: O conteúdo do arquivo
    """
    with open(arquivo, "r", encoding="utf-8") as file:
        conteudo = file.read()

    return conteudo


def write_file(arquivo: str, content: str) -> None:
    """
    Essa função escreve alguma coisa em um arquivo

    :param arquivo: Nome do arquivo que vai ser escrito
    :param content: Contendo a ser adicionado

    :return: None
    """
    with open(arquivo, "a", encoding="utf-8") as file:
        file.write(content)


def creat_json(name: str, indent: int = 2) -> None:
    """
    Essa função cria um JSON

    :param name: O nome do arquivo
    :param indent: (Opcional) Indentação do arquivo JSON

    :return: None
    """
    with open(name, "w", encoding="utf-8") as file:
        file.write(json.dumps([], indent=indent))


def read_json(name: str) -> list:
    """
    Essa função le um JSON

    :param name: O nome do arquivo para ser lido

    :return: Conteúdo do JSON como uma lista
    """
    with open(name, "r", encoding="utf-8") as file:
        return json.load(file)


def write_json(name: str, content: dict[str, Any], indent: int = 2) -> None:
    """
    Essa função escreve coisas no JSON

    :param name: O nome do arquivo para ser escrevido
    :param content: Contendo a ser escrevido
    :param indent: (Opcional) Indentação do arquivo JSON

    :return: None
    """
    data: list = read_json(name)

    data.append(content)

    with open(name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=indent)
