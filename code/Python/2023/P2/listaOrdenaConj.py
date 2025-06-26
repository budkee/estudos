# -*- coding: utf-8 -*-
# Programa: ordenaalturas.py
# Programador: 
# Data: 28/09/2019
# Este programa lê uma lista de n alturas, ordena as alturas e em ordem
# não decrescente usando o algoritmo de ordenação por seleção e
# imprime a lista ordenada.
# início do módulo principal
# descrição das variáveis utilizadas
# list alturas
# int menorPos, menor, i

# pré: tam alturas[0] alturas[1] .. alturas[tam-1]

# Passo 1. Leia a lista de alturas
# Passo 1.1. Leia o número de elementos da lista
tam = int(input())
# Passo 1.2. Inicialiaze a lista alturas com tam elementos
alturas = [0]*tam
# Passo 1.3. Leia e insira os tam elementos na lista
for i in range(0,tam):
   alturas[i] = int(input())
# Passo 2. Ordene a lista de tam alturas com o método da seleção
# Passo 2.1. Para as sublistas alturas[j:tam-1]
for j in range(0, tam-1): # a última sublista tem apenas um elemento 
# Passo 2.1.1. Calcule a menor altura e armazene na posição j
# Passo 2.1.1.1. Inicialize a posição com o primeiro índice da sublista
   pos = j
# Passo 2.1.1.2. Inicialize menor com o primeiro elemento da sublista
   menor = alturas[j]
# Passo 2.1.1.3. Para as sublistas compute o menor elemento
   for i in range(j+1,tam):
# Passo 2.1.1.3.1. verifique se o i-ésimo elemento é menor que menor
      if menor > alturas[i]:
# Passo 2.1.1.3.1.1. Atribua i ao índice do menor elemento da sublista
         pos = i 
# Passo 2.1.1.3.1.2. Atribua o elemento i ao menor elemento da sublista
         menor = alturas[i]
# Passo 2.1.2. Trocar o menor com alturas[j] no início da sublista
      alturas[pos] = alturas[j]
      alturas[j] = menor
# Passo 3. Imprima o conjunto de alturas ordenada em ordem crescente
print(*alturas, sep=', ')

# pós: para i em {0, 1, .., tam-1}: altura[i], and
#      altura[0] <= altura[1] <= altura[2] <= .. <= altura[k-1]
# fim do módulo principal