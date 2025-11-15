import json
from pathlib import Path
from typing import Any


class FileManager:
    def __init__(self, path: Path, nome: str) -> None:
        self.path = path
        self.nome = nome
        self.arquivo = f'{self.path}/{self.nome}'

    def creat_file(self) -> None:
        """
        Essa função apenas cria o arquivo

        :return: None
        """
        with open(self.arquivo, "w", encoding="utf-8"):
            return

    def read_file(self) -> str:
        """
        Essa função retorna o conteúdo de um arquivo

        :return: O conteúdo do arquivo
        """
        with open(self.arquivo, "r", encoding="utf-8") as file:
            conteudo = file.read()

        return conteudo

    def write_file(self, arquivo: str, content: str) -> None:
        """
        Essa função escreve alguma coisa em um arquivo

        :param arquivo: Nome do arquivo que vai ser escrito
        :param content: Contendo a ser adicionado

        :return: None
        """
        with open(self.arquivo, "a", encoding="utf-8") as file:
            file.write(content)

    def creat_json(self, indent: int = 2) -> None:
        """
        Essa função cria um JSON

        :param indent: (Opcional) Indentação do arquivo JSON

        :return: None
        """
        with open(self.arquivo, "w", encoding="utf-8") as file:
            file.write(json.dumps([], indent=indent))

    def read_json(self) -> list:
        """
        Essa função le um JSON

        :param name: O nome do arquivo para ser lido

        :return: Conteúdo do JSON como uma lista
        """
        with open(self.arquivo, "r", encoding="utf-8") as file:
            return json.load(file)

    def write_json(self, name: str, content: dict[str, Any], indent: int = 2) -> None:
        """
        Essa função escreve coisas no JSON

        :param name: O nome do arquivo para ser escrevido
        :param content: Contendo a ser escrevido
        :param indent: (Opcional) Indentação do arquivo JSON

        :return: None
        """
        data: list = self.read_json()

        data.append(content)

        with open(name, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=indent)
