# -*- coding: utf-8 -*-
# Programa: exlacos00.py
# Programador:
# Data: 11/05/2016
# Este programa demonstra a utilização de laços aninhados.
# Imprime um conjunto de número por linha.
# início do módulo principal
# descrição das variáveis utilizadas
# int lin, col

# pré: lin col

# Passo 1. Leia o número de linhas e colunas
# Passo 1.1. Leia o número de linhas
lin = int(input())
# Passo 1.2. Leia o número de colunas
col = int(input())
# Passo 2. Repita lin vezes (linhas)
for i in range (1, lin+1):
# Passo 2.1. Imprima o número da linha
   print('Linha {0:d}: '.format(i),end='')
# Passo 2.2. Repita col vezes (colunas)
   for j in range(1, col+1):
# Passo 2.2.1. Imprima o número da coluna
      print('{0:3d}'.format(j), end='')
# Passo 2.3. Mude de linha
   print('')
   
# pós: impressão de uma tabela 3 x 5
#      lin == 3 and col == 6
#      Linha 1:   1  2  3  4  5
#      Linha 2:   1  2  3  4  5
#      Linha 3:   1  2  3  4  5
# fim do módulo principal 
