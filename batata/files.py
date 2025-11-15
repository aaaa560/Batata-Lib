import json
import csv
from pathlib import Path
from typing import Any
from batata.atalhos import err


class FileManager:
    def __init__(self, path: str, nome: str, indent: int = 2) -> None:
        self.path: Path = Path(path)
        self.nome: str = nome
        self.indent: int = indent

        self.arquivo: str = str(self.path / self.nome)

        self.mode: str
        if self.arquivo.endswith('.csv'):
            self.mode = 'csv'
        elif self.arquivo.endswith('.json'):
            self.mode = 'json'
        elif self.arquivo.endswith('.txt'):
            self.mode = 'txt'
        else:
            self.mode = 'file'

    def creat_file(self) -> None:
        """
        Essa função apenas cria o arquivo

        :return: None
        """
        try:
            with open(self.arquivo, "w", encoding="utf-8"):
                return
        except Exception as e:
            err(f'Erro ao criar o arquivo: {e}')

    def read_file(self) -> str:
        """
        Essa função retorna o conteúdo de um arquivo

        :return: O conteúdo do arquivo
        """
        try:
            with open(self.arquivo, "r", encoding="utf-8") as file:
                conteudo: str = file.read()
        except FileNotFoundError:
            err('Arquivo não encontrado!')
            conteudo: str = ''
        except Exception as e:
            err(f'Erro ao criar o arquivo: {e}')
            conteudo: str = ''

        return conteudo

    def write_file(self, content: str) -> None:
        """
        Essa função escreve alguma coisa em um arquivo

        :param content: Contendo a ser adicionado

        :return: None
        """
        try:
            with open(self.arquivo, "a", encoding="utf-8") as file:
                file.write(content)
        except FileNotFoundError:
            self.creat_file()
            with open(self.arquivo, "a", encoding="utf-8") as file:
                file.write(content)

    def creat_json(self) -> None:
        """
        Essa função cria um JSON

        :param indent: (Opcional) Indentação do arquivo JSON

        :return: None
        """
        with open(self.arquivo, "w", encoding="utf-8") as file:
            file.write(json.dumps([], indent=self.indent))

    def read_json(self) -> list:
        """
        Essa função le um JSON

        :return: Conteúdo do JSON como uma lista
        """
        try:
            with open(self.arquivo, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            err('Arquivo JSON não encontrado! Criando um novo...')
            self.creat_json()
            with open(self.arquivo, "r", encoding="utf-8") as file:
                return json.load(file)
        except Exception as e:
            err(f'Erro ao ler o arquivo JSON: {e}')
            return []

    def write_json(self, content: list[dict[str, Any]]) -> None:
        """
        Essa função escreve coisas no JSON

        :param content: Contendo a ser escrevido

        :return: None
        """
        data: list = self.read_json()

        data.append(content)

        try:
            with open(self.arquivo, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=self.indent)
        except FileNotFoundError as not_file:
            err(f'Arquivo não encontrado: {not_file}! Criando um novo...')
            self.creat_json()
            with open(self.arquivo, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=self.indent)
        except Exception as e:
            err(f'Erro ao escrever no arquivo JSON: {e}')

    def creat_csv(self, header: list[str] | None = None) -> None:
        """
        Essa função cria um arquivo CSV

        :return: None
        """
        try:
            with open(self.arquivo, "w", encoding="utf-8") as file:
                writer = csv.writer(file)
                if header:
                    writer.writerow(header)
                return
        except Exception as e:
            err(f'Erro ao criar o arquivo CSV: {e}')

    def write_csv(self, content: list[str]) -> None:
        try:
            with open(self.arquivo, "a", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(content)
        except FileNotFoundError:
            err('Arquivo CSV não encontrado! Criando um novo...')
            self.creat_csv()
            with open(self.arquivo, "a", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(content)
        except Exception as e:
            err(f'Erro ao escrever no arquivo CSV: {e}')

    def read_csv(self) -> list[list[str]]:
        try:
            with open(self.arquivo, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                return [row for row in reader]
        except FileNotFoundError:
            err('Arquivo CSV não encontrado!')
            return []
        except Exception as e:
            err(f'Erro ao ler o arquivo CSV: {e}')
            return []

    def __repr__(self) -> str:
        return f'FileManager(path={self.path}, nome={self.nome}, arquivo={self.arquivo}, mode={self.mode})'
