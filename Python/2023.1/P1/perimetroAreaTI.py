# Programa: perimetroareaTI.py
# Programador:
# Data: 23/08/2020
# Este programa lê o valor da base e o lado de um
# triângulo isósceles, calcula e imprime o perímetro e a
# área do triângulo no formato especificado.
# declaração das bibliotecas utilizadas
import math
# início do módulo principal
# descrição das variáveis utilizadas
# float base, lado, perimetro, area

# pré: base lado

# Passo 1. Leia a base e os catetos do triângulo isósceles
print('Entre com os valores dos lados do triângulo: ')
base = int(input('base: '))
lado = int(input('lado: '))
# Passo 2. Calcule o perímetro e a área do triângulo
# Passo 2.1. Calcule o perímetro do triângulo
perimetro = lado*2 + base
# Passo 2.2. Calcule a área do triângulo
# Passo 2.1.1. Calcule o valor da altura
altura = math.sqrt(lado**2 - (base/2)**2)

area = (base*altura)/2
# Passo 3. Imprima o perímetro e área
print('Perímetro = {:.2f}\n'
      'Área = {:.2f}'.format(perimetro, area))

# pós: perimetro == catetoop + catetoad + hipotenusa and
#      area == (catetoop*catetoad)/2.0
# fom do módulo principal