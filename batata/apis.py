from typing import Any
import requests
from difflib import get_close_matches

__all__ = ['get', 'post', 'API', 'PokeAPI']


class API:
    """
    Classe base para usar APIs
    """

    def __init__(self, url: str, headers: dict[str, str] | None = None) -> None:
        if headers is None:
            headers = {
                "User-Agent": (
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/120.0.0.0 Safari/537.36"
                ),
                "Accept": "*/*",
                "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
            }

        self.url = url
        self.headers = headers

    def get(self, endpoint: str, **payload) -> requests.Response:
        return requests.get(
            url=f'{self.url}/{endpoint}',
            headers=self.headers,
            **payload
        )

    def post(self, endpoint: str, data: Any | None = None, json: list[dict[str, Any]] | None = None,
             **payload) -> requests.Response:
        return requests.post(
            url=f'{self.url}/{endpoint}',
            headers=self.headers,
            data=data,
            json=json,
            **payload
        )


class PokeAPI(API):
    """
    API simples que usa o PokéAPI
    """

    def __init__(self):
        super().__init__(url='https://pokeapi.co/api/v2')

    def get_pokemon_info(self, name: str) -> dict[str, dict[str, Any]]:  # Pega alguns dados brutos do pokemon
        pokemons_name: list[Any] = find_pokemon(name)
        pokemons_data: dict[str, dict[str, Any]] = {}

        for pokemon in pokemons_name:
            data = self.get(endpoint=f'/pokemon/{pokemon}').json()
            abilidades: list[dict[str, Any]] = data['abilities']
            pokemons_data[pokemon] = {}

            for habilidade in abilidades:
                pokemons_data[pokemon].setdefault('abilidades', [])
                pokemons_data[pokemon]['abilidades'].append(habilidade['ability'])

        return pokemons_data


def get(url: str, endpoint: str = '') -> dict[str, Any]:
    return requests.get(f'{url}/{endpoint}').json()


def post(url: str, endpoint: str = '', payload: dict[str, Any] | None = None) -> dict[str, Any]:
    return requests.post(f'{url}/{endpoint}', json=payload).json()


def find_pokemon(query: str) -> list[Any]:
    r: dict[str, Any] = get('https://pokeapi.co/api/v2/pokemon?limit=10000')
    names: list[str] = [p['name'] for p in r['results']]
    matchs: list[Any] = get_close_matches(query, names, n=3, cutoff=0.6)

    return matchs
