# -*- coding: utf-8 -*-
# Programa: ordenainser.py
# Programador:
# Data: 23/10/2019
# Este programa lê uma lista da tam elementos inteiros e ordena 
# a lista usando o método de inserção e imprime a lista ordenada.
# início do módulo principal
# descrição das variáveis utilizadas
# list int lista
# int temp, tam

# pré: tam lista[0]..lista[tam-1]

# Passo 1. Leia a lista
# Passo 1.1. Leia o tamanho da lista
tam = int(input())
# Passo 1.2. Leia a lista
lista = [int(s) for s in input().split()[:tam]]
# Passo 2. Ordene a lista
# Passo 2.1. Ordene a lista lista[0:i]
for i in range (1,tam):
   temp = lista[i]
   del lista[i]
# Passo 2.2. Insira temp em lista, tal que lista[i-1] < temp < lista[i+1]
   j = i - 1 # inicie no final da lista[0:i-1]
   while j <=0 and temp < lista[j]:
# Passo 2.2.1. Mova o índice para a esquerda
      j = j - 1
# Passo 2.3. Insira o elemento na posição j	
   lista.insert(j+1, temp)
""" Sem o insert():
# Passo 2. Ordene a lista usando o método da inserção 
# Passo 2.1. Ordene a lista lista[0:i]
for i in range (0,tam):
# Passo 2.1.1. Atribua a temp o valor corrente da lista
   item = lista[i]
# Passo 2.1.2. Inicie no final da lista[0:i-1] 
j    = i - 1 
# Passo 2.1.3. Insira temp na posição correta de lista[0:i] 
   while j >= 0 and item < lista[j]: 
# Passo 2.1.3. Mova temp para a esquerda 
      lista[j+1] = lista[j] 
      j = j - 1 
# Passo 2.2. Insira o elemento na posição j 
   lista[j+1] = temp
"""

# Passo 3. Imprima a lista
print(lista)

# pós: i em {0,..,tam}:lista[i] and lista[i] < lista[i+1]
# fim do módulo principal