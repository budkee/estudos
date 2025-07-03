# -*- coding: utf-8 -*-
# Programa: areaperimetroT.py
# Programador:
# Data: 04/04/2012
# Diálogo: Este lê o valor dos lados de um triângulo e calcula o
# perímetro e a área do triângulo e imprime o resultado.
# decalaração dos módulos utilizados
import math

# início do driver principal

# pré: lado1 lado2 lado3

# Passo 1. Leia o lado do quadrado
# print('Entre com os valores dos lados do triângulo: ')
lado1 = float(input())
lado2 = float(input())
lado3 = float(input())
# Passo 2. Calcule o perímetro e o semiperímetro
perimetro = lado1 + lado2 + lado3
sp = perimetro / 2
# Passo 3. Calcule a área
area = math.sqrt(sp * (sp - lado1) * (sp - lado2) * (sp - lado3))
# Passo 4. Imprima o lado, perímetro e área
print('Lados = {0:5.2f}, {1:5.2f}, {2:5.2f}'.format(lado1, lado2, lado3))
print('Perímetro = {0:5.2f}'.format(perimetro))
print('Área = {0:5.2f}'.format(area))

# pós: perímetro == lado1 + lado2 +lado3 && semi == perímetro/2
#      área == sqrt(semip*(semip-lado1)*(semip-lado2)*(semip-lado3))