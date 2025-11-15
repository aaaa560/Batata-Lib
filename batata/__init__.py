# batata/__init__.py
from batata.geral import mostra, get_num, par, primo
from batata.atalhos import info, warn, err, out
from batata.math import fat, soma, area
from batata.formas import Retangulo, Circulo, Triangulo
from batata.errors import ParamError, ScrapingError

__version__ = "0.1.0"
__all__ = [
    'mostra', 'get_num', 'par', 'primo',
    'info', 'warn', 'err', 'out',
    'fat', 'soma', 'area',
    'Retangulo', 'Circulo', 'Triangulo',
    'ParamError', 'ScrapingError'
]