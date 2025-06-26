# -*- coding: utf-8 -*-
# Programa: maiormenor.py
# Programador:
# Data: 05/04/2016
# Este programa lê dois números inteiros, calcula o maior e o
# menor entre os números e imprime o resultado.
# início do módulo principal
# descrição das variáveis utilizadas
# int num1, num2
# int maior, divisor

# pré: num1 num2

# Passo 1. Leia dois números inteiros
print('Leia três inteiros num1, num2 e num3: ')
num1, num2, num3 = map(int, input('').split())
# Passo 2. Calcule o maior e o menor entre num1, num2 e num3
maior = num1
menor = num1
# Passo 2.1 Compare o maior número:
if num2 > maior:
    maior = num2
elif num2 < menor:
    menor = num2
if num3 > maior:
    maior = num3
elif num3 < menor:
    menor = num3
# Passo 3. Imprima os resultados
print('Maior = {0:d}'.format(maior))
print('Menor = {0:d}'.format(menor))

# pós: maior == max(num1,num2) and menor == min(num1,num2)}
# fim do módulo principal
