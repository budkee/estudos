# -*- coding: utf-8 -*-
# Programa: semrepeticao01.py
# Programador:
# Data: 23/10/2019
# Este programa lê uma lista de n > 0 números inteiros, retira os
# elementos repetidos da lista e imprime o a lista resultante na
# mesma ordem da entrada.
# início do módulo principal
# descrição as variáveis utilizadas
# list lista, novalista
# int tam

# pré: tam lista[0] lista[1] .... lista[tam-1]

# Passo 1. Leia a entrada
# Passo 1.1. Leia o tamanho da lista
tam = int(input())
# Passo 1.2. Leia os elementos da lista
lista= list(map(int, input().split()))[:tam]
# Passo 2. Retire os elementos repetidos da lista
# Passo 2.1. Inicialize a nova lista
novalista = []
# Passo 2.2. Para cada elemento da lista
for num in lista:
# Passo 2.2.1. Verifique se num não está em novalista
   if num not in novalista:
# Passo 2.2.1.1. Insira num em novalista
      novalista.append(num)
# Passo 3. Imprima a lista sem repetição na ordem da entrada
print(novalista)

# pós: para i,j em {0..tamnova-1}:a´[i] != a´[j] and i != j and
#      tamnova <= tam
# fim do módulo principal