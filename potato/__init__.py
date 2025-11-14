# potato/__init__.py
from potato.geral import mostra, get_num, par, primo
from potato.atalhos import info, warn, err, out
from potato.math import fat, soma, area
from potato.formas import Retangulo, Circulo, Triangulo

__version__ = "0.1.0"
__all__ = [
    'mostra', 'get_num', 'par', 'primo',
    'info', 'warn', 'err', 'out',
    'fat', 'soma', 'area',
    'Retangulo', 'Circulo', 'Triangulo'
]