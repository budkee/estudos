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
lista = list(map(int,input().split()))[:tam]
# Passo 2. Usando o método do bubble sort ordene a lista
# Passo 2.1. Assuma que houve troca
trocou = True
i = tam
# Passo 2.2. Compare os termos dois a dois, trocando quando necessário
while trocou or i > 1:
# Passo 2.2.1. No início da iteração não houve troca
   trocou = False
   seguinte = lista[tam-1]
   for idx,item in enumerate(lista[i:tam-1]):
      if seguinte < item:
         lista[idx],lista[idx+1]=lista[idx+1],lista[idx]
         seguinte = item
         trocou = True
   i -= 1
""" Ou
# Passo 2. Usando o método do bubble sort ordene a lista
# Passo 2.1. Mova o menor elemento de lista[i:] para lista[i]
for i in range(0,tam-1):
# Passo 2.2. Compare os termos vizinhos de l[i:], trocando quando necessário
   for j in range(tam-1,i,-1):
      if lista[j] < lista[j-1]:
         lista[j-1], lista[j] = lista[j], lista[j-1]
"""
# Passo 3. Imprima a lista ordenada
print(lista)

# pós: lista[0] < lista[1] < .. < lista[tam-1]
# fim do módulo principal