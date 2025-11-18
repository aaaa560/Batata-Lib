from typing import Any
import requests
from difflib import get_close_matches

__all__ = ['get', 'post', 'API', 'PokeAPI', 'GitHubAPI', 'WeatherAPI', 'CurrencyAPI']


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


def get(url: str) -> dict[str, Any]:
    return requests.get(url).json()


def post(url: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    return requests.post(url, json=payload).json()


class GitHubAPI(API):
    """
    Cliente para a API do GitHub
    """
    def __init__(self, token: str | None = None):
        headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if token:
            headers["Authorization"] = f"Bearer {token}"
        
        super().__init__(url='https://api.github.com', headers=headers)
    
    def get_user(self, username: str) -> dict[str, Any]:
        """Busca informações de um usuário"""
        response = self.get(f'users/{username}')
        return response.json()
    
    def get_repos(self, username: str, per_page: int = 30) -> list[dict[str, Any]]:
        """Lista repositórios de um usuário"""
        response = self.get(f'users/{username}/repos', params={'per_page': per_page})
        return response.json()
    
    def get_repo(self, owner: str, repo: str) -> dict[str, Any]:
        """Busca informações de um repositório específico"""
        response = self.get(f'repos/{owner}/{repo}')
        return response.json()
    
    def search_repos(self, query: str, sort: str = 'stars', per_page: int = 10) -> dict[str, Any]:
        """Busca repositórios por query"""
        response = self.get('search/repositories', params={
            'q': query,
            'sort': sort,
            'per_page': per_page
        })
        return response.json()
    
    def get_repo_commits(self, owner: str, repo: str, per_page: int = 30) -> list[dict[str, Any]]:
        """Lista commits de um repositório"""
        response = self.get(f'repos/{owner}/{repo}/commits', params={'per_page': per_page})
        return response.json()


class WeatherAPI(API):
    """
    Cliente para OpenWeatherMap API
    Requer uma chave de API gratuita de https://openweathermap.org/api
    """
    def __init__(self, api_key: str):
        super().__init__(url='https://api.openweathermap.org/data/2.5')
        self.api_key = api_key
    
    def get_current_weather(self, city: str, units: str = 'metric') -> dict[str, Any]:
        """
        Busca o clima atual de uma cidade
        
        :param city: Nome da cidade
        :param units: Sistema de unidades ('metric', 'imperial', 'standard')
        :return: Dados do clima
        """
        response = self.get('weather', params={
            'q': city,
            'appid': self.api_key,
            'units': units
        })
        return response.json()
    
    def get_forecast(self, city: str, units: str = 'metric', cnt: int = 5) -> dict[str, Any]:
        """
        Busca previsão do tempo para os próximos dias
        
        :param city: Nome da cidade
        :param units: Sistema de unidades ('metric', 'imperial', 'standard')
        :param cnt: Número de previsões (máx 40)
        :return: Dados da previsão
        """
        response = self.get('forecast', params={
            'q': city,
            'appid': self.api_key,
            'units': units,
            'cnt': cnt
        })
        return response.json()
    
    def get_weather_by_coords(self, lat: float, lon: float, units: str = 'metric') -> dict[str, Any]:
        """
        Busca o clima por coordenadas geográficas
        
        :param lat: Latitude
        :param lon: Longitude
        :param units: Sistema de unidades
        :return: Dados do clima
        """
        response = self.get('weather', params={
            'lat': lat,
            'lon': lon,
            'appid': self.api_key,
            'units': units
        })
        return response.json()


class CurrencyAPI(API):
    """
    Cliente para ExchangeRate-API
    API gratuita para taxas de câmbio
    """
    def __init__(self, api_key: str | None = None):
        if api_key:
            super().__init__(url=f'https://v6.exchangerate-api.com/v6/{api_key}')
        else:
            # Versão gratuita sem chave (limitada)
            super().__init__(url='https://api.exchangerate-api.com/v4')
        self.api_key = api_key
    
    def get_rates(self, base: str = 'USD') -> dict[str, Any]:
        """
        Busca todas as taxas de câmbio para uma moeda base
        
        :param base: Código da moeda base (ex: 'USD', 'BRL', 'EUR')
        :return: Taxas de câmbio
        """
        if self.api_key:
            response = self.get(f'latest/{base}')
        else:
            response = self.get(f'latest/{base}')
        return response.json()
    
    def convert(self, amount: float, from_currency: str, to_currency: str) -> dict[str, Any]:
        """
        Converte um valor entre duas moedas
        
        :param amount: Valor a ser convertido
        :param from_currency: Moeda de origem (ex: 'USD')
        :param to_currency: Moeda de destino (ex: 'BRL')
        :return: Resultado da conversão
        """
        if self.api_key:
            response = self.get(f'pair/{from_currency}/{to_currency}/{amount}')
            return response.json()
        else:
            # Versão sem chave requer cálculo manual
            rates = self.get_rates(from_currency)
            if 'rates' in rates and to_currency in rates['rates']:
                conversion_rate = rates['rates'][to_currency]
                return {
                    'base': from_currency,
                    'target': to_currency,
                    'amount': amount,
                    'result': amount * conversion_rate,
                    'rate': conversion_rate
                }
            return {'error': 'Currency not found'}
    
    def get_supported_currencies(self) -> dict[str, Any]:
        """
        Lista todas as moedas suportadas
        
        :return: Lista de códigos de moedas
        """
        if self.api_key:
            response = self.get('codes')
            return response.json()
        else:
            # Versão gratuita retorna as moedas via rates
            rates = self.get_rates('USD')
            if 'rates' in rates:
                return {'supported_codes': list(rates['rates'].keys())}
            return {'error': 'Unable to fetch currencies'}


def find_pokemon(query: str) -> list[Any]:
    r: dict[str, Any] = get('https://pokeapi.co/api/v2/pokemon?limit=10000')
    names: list[str] = [p['name'] for p in r['results']]
    matchs: list[Any] = get_close_matches(query, names, n=3, cutoff=0.6)

    return matchs
