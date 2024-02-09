# -*- coding: utf-8 -*-
# Programa: uniao01.py
# Programador:
# Data: 23/10/2019
# Este programa lê duas listas com n e m itens, calcula a união
# das listas e imprime o resultado
# início do módulo principal
# descrição as variáveis utilizadas
# list lista1, lista2, uniao
# int tam1, tam2

# pré: tam1 lista1[0] lista1[1] .. lista1[tam1-1]
#      tam2 lista2[0] lista2[1] .. lista2[tam2-1]

# Passo 1. Leia a entrada
# Passo 1.1. Leia o tamanho da lista1
tam1 = int(input())
# Passo 1.2. Leia os elementos da lista1
lista1 = list(map(int, input().split()))[:tam1]
# Passo 1.3. Leia o tamanho da lista2
tam2 = int(input())
# Passo 1.4. Leia os elementos da lista
lista2 = list(map(int, input().split()))[:tam2]
# Passo 2. Calcule a união das listas
# Passo 2.1. Copie todos elementos da lista1 na lista união
uniao = lista1.copy()
# Passo 2.2. Para cada elemento da lista2
for num in lista2:
# Passo 2.2.1. Verifique se num não está em uniao
   if num not in lista1:
# Passo 2.2.1.1. Insira num em uniao
      uniao.append(num)
""" Ou
# Passo 2.2. Para cada elemento da lista2
for i in range(0,tam2):
# Passo 2.2.1. Verifique se num não está em uniao
   j = 0
   while j < tam1 and lista2[i] != lista1[j]:
      j += 1
# Passo 2.2.1.1. Insira num em uniao
   if j == tam1:
      uniao.append(num)
"""
# Passo 3. Imprima a lista uniao
print(uniao)

# pós: para i em {0..tam3-1}: uniao[i] and
#      uniao[i] == lista1[i], 0 <= i < tam1 and para j em 
#      {tam1..tam3-1} uniao[j] == lista2[k] and lista2[k] !=
#      uniao[i] | 0 <= i < tam1
# fim do módulo principal