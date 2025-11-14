type FormaGeometrica = Retangulo | Circulo | Triangulo | Quadrado | Trapezio | Losangulo
from math import pi
from potato.errors import ParamError


class FormaQualquer:
    def area(self) -> float:
        pass

class Retangulo(FormaQualquer):
    def __init__(self, largura: float, altura: float) -> None:
        if largura < 0 or altura < 0:
            raise ParamError(
                "Largura e altura devem ser valores positivos.",
                param='largura | altura',
                esperado='valor positivo'
            )
        self.largura = largura
        self.altura = altura

    def area(self) -> float:
        return self.largura * self.altura


class Circulo(FormaQualquer):
    def __init__(self, raio: float) -> None:
        self.raio = raio

    def area(self) -> float:
        return pi * (self.raio ** 2)


class Triangulo(FormaQualquer):
    def __init__(self, base: float, altura: float) -> None:
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return (self.base * self.altura) / 2


class Quadrado(Retangulo):
    def __init__(self, lado: float) -> None:
        super().__init__(lado, lado)

    def area(self) -> float:
        return self.largura * self.largura


class Trapezio(FormaQualquer):
    def __init__(self, base_grande: float, base: float, altura: float) -> None:
        self.base_grande = base_grande
        self.base = base
        self.altura = altura

    def area(self) -> float:
        return ((self.base_grande + self.base) * self.altura) / 2


class Losangulo(FormaQualquer):
    def __init__(self, diagonal: float, diagonal_maior: float) -> None:
        self.diagonal = diagonal
        self.diagonal_maior = diagonal_maior

    def area(self) -> float:
        return (self.diagonal * self.diagonal_maior) / 2
