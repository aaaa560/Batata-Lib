# teste.py
from batata.formas import Triangulo, Retangulo
from batata.geral import primo, par
from batata.math import fat, produto
from batata.atalhos import info, warn, err

# Testa formas
t = Triangulo(5, 10)
print(t)  # Deve printar bonito agora!
print(f"Área: {t.area()}")

# Testa matemática
print(primo(17))  # True
print(par(8))     # True
print(fat(5))     # 120
print(produto(2, 3, 4))  # 24

# Testa atalhos
info("Tudo funcionando!")
warn("Cuidado!")
err("Erro de teste")