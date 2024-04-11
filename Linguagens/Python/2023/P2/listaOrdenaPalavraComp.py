# -*- coding: utf-8 -*-
# Programa: ordenanome01.py
# Programador:
# Data: 29/04/2018
# Este programa lê um número inteiro indicando o tamanho de uma
# lista de nomes. O programa lê a lista de nomes e usando o
# método de ordenação por bolha, ordena a lista em ordem
# crescente usando o sobrenome e imprime a sequência ordenada.
# início do módulo principal
# descrição das variáveis utilizadas 
# list nomes - lista com os nomes a serem ordenados 
# int tam - tamanho da lista 
# bool trocou - indica se ocorreu troca

# pré: tam nomes[0]...nomes[tam-1]

# Passo 1. Leia e inicialize os dados
# Passo 1.1. Leia o tamanho da lista
tam = int(input('Leia o tamanho da lista: '))
# Passo 1.2. Inicialize a lista
nomes = []
# Passo 1.3. Leia a lista de nomes
for i in range (0,tam):
   nomes.append(input())
# Passo 2. Usando o método do bubble sort ordene a lista
# Passo 2.1. Assuma que houve troca
trocou = True
# Passo 2.2. Compare os termos dois a dois, trocando quando necessário
while (trocou):
# Passo 2.2.1. No início da iteração não houve troca
   trocou = False
   for i in range(0,tam-1):
      if nomes[i].split()[-1] > nomes[i+1].split()[-1]:
         nomes[i], nomes[i+1] = nomes[i+1], nomes[i]
         trocou = True
      # sobrenomes iguais
      elif nomes[i].split()[-1] == nomes[i+1].split()[-1]:
         if nomes[i].split()[:-1] > nomes[i+1].split()[:-1]:
            nomes[i], nomes[i+1] = nomes[i+1], nomes[i]
            trocou = True            
# Passo 3. Imprima a sequência ordenada
print(nomes)

# pós: nomes[0] < nomes[1] < ... < nomes[tam-1]
# fim módulo principal