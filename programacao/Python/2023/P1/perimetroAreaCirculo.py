# Este programa calcula o perimetro e área de um círculo.

# Formato de entrada:
# 2.0

# Formato de saída:
# Raio = 2.00
# Perímetro = 12.57
# Área = 12.57

# Módulos e bibliotecas
from math import pi

# Constantes e variáveis:
# raio, perimetro, area: float

# Passo 1: leia o raio do círculo
raio = float(input('Qual é o raio? (raio > 0) '))

# Passo 2: compute o perímetro e a área do círculo
perimetro = 2 * raio * pi
area = pi * (raio)**2

# Passo 3: imprima o perimetro e a área
print('Raio = {0:5.2f} \nPerímetro = {1:5.2f}\nÁrea = {2:5.2f}'.format(raio, perimetro, area))
