# -*- coding: utf-8 -*-
# Programa: eximprime00.py
# Programador:
# Data: 11/05/2016
# Este programa lê um inteiro 0 < limite < 1000 e imprime todos
# os valores menores ou iguais a limite, sendo um número por
# linha.
# início do módulo principal
# descrição das variáveis utilizadas
# int limite

# pré: limite

# Passo 1. Leia um inteiro inteiro positivo menor que 1000
print('Entre com o limite: ')
limite = int(input())
# Passo 2. Imprima os números <= limite, um em cada linha
# Passo 2.1. Para cada i em {1,...,limite} faça
for i in range(1, limite + 1):
    # Passo 2.2. Imprima o número
    print('{0:4d}'.format(i))

# pós: imprime 1 até n <= limite
#      limite == 6
#         1
#         2
#         3
#         4
#         5
#         6
# fim do módulo principal
