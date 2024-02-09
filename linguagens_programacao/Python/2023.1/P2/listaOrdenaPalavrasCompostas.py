# -*- coding: utf-8 -*-
# Programa: ordenabolha03.py
# Programador:
# Data: 30/03/2016
# Este programa lê um número inteiro indicando o tamanho de um
# conjunto de números inteiros distintos. O programa lê o 
# conjunto numa lista e usando o método de ordenação por bolha, 
# ordena a lista em ordem crescente e imprime a lista ordenada.
# início do módulo principal
# descrição das variáveis utilizadas
# list lista
# int tam, temp
# bool trocou

# pré: tam lista[0]...lista[tam-1]

# Passo 1. Leia a lista
# Passo 1.1. Leia o tamanho da lista
tam = int(input())
# Passo 1.2. Leia os elementos do conjunto
nomes = []
for i in range(0, tam):
   nomes.append(input())

trocou = True
while trocou:
   trocou = False
   for i in range(0,tam-1):
      if nomes[i].split()[-1] > nomes[i+1].split()[-1]:
         nomes[i], nomes[i+1] = nomes[i+1], nomes[i]
         trocou = True
      elif nomes[i].split()[-1] == nomes[i+1].split()[-1]:
         if nomes[i].split()[:-1] > nomes[i+1].split()[:-1]:
            nomes[i], nomes[i+1] = nomes[i+1], nomes[i]
            trocou = True
# Passo 3. Imprima a lista ordenada
for i in range(0, tam):
   print('{0:s}'.format(nomes[i]))

# pós: lista[0] < lista[1] < .. < lista[tam-1]
# fim do módulo principal