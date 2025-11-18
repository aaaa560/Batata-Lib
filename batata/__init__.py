# batata/__init__.py
from batata.geral import mostra, get_num, par, primo, divisivel, raiz_qdd
from batata.aliases import info, warn, err, out, perguntar
from batata.math import fat, soma, area, produto
from batata.formas import Retangulo, Circulo, Triangulo, FormaQualquer, FormaGeometrica
from batata.errors import ParamError, ScrapingError
from batata.scraping import Scraper
from batata.files import FileManager
from batata.colors import COLORS, MODES, Color
from batata.cli import CLI
from batata.apis import get, post, API, PokeAPI, GitHubAPI, WeatherAPI, CurrencyAPI

__version__ = '0.1.3'
__all__ = [
    'mostra', 'get_num', 'par', 'primo',
    'info', 'warn', 'err', 'out', 'perguntar',
    'fat', 'soma', 'area', 'divisivel', 'raiz_qdd', 'produto',
    'Retangulo', 'Circulo', 'Triangulo', 'FormaQualquer', 'FormaGeometrica',
    'ParamError', 'ScrapingError',
    'Scraper',
    'FileManager',
    'COLORS', 'MODES', 'Color',
    'CLI',
    'get', 'post', 'API', 'PokeAPI', 'GitHubAPI', 'WeatherAPI', 'CurrencyAPI'
]
