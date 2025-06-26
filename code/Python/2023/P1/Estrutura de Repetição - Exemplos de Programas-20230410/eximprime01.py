# -*- coding: utf-8 -*-
# Programa: eximprime01.py
# Programador:
# Data: 11/05/2016
# Este programa lê um inteiro 0 < num < 1000 e imprime todos os
# valores menores ou iguais a num, sendo dez números por linha.
# início do módulo principal
# descrição das variáveis utilizadas
# int num, contaNum

# pré: num

# Passo 1. Leia um inteiro entre 1 e 1000
print('Entre com um inteiro entre 1 e 999: ')
num = int(input())
# Passo 2. Imprima de 0 a <= a num (10 por linha)
# Passo 2.1. Inicialize a variável que conta os números por linha
contanum = 0
# Passo 2.1. Para cada i em {1,...,num} faça
for i in range(1,num+1):
# Passo 2.2. Verifique se contanum < 10 (0 a 9)
   if contanum < 10:
# Passo 2.2.1. Atualize a quantidade de números na linha
      contanum = contanum + 1
   else:
# Passo 2.2.2. Comece uma nova linha
      print('')
      contanum = 1
# Passo 2.3. Imprima o número
   print('{0:4d}'.format(i),end='')

# pós: imprime 1 até n and 10 números por linha
#      limite == 35
#         1   2   3   4   5   6   7   8   9  10
#        11  12  13  14  15  16  17  18  19  20
#        21  22  23  24  25  26  27  28  29  30
#        31  32  33  34  35
# fim do módulo principal 
