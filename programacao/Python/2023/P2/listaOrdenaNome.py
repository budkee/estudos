# -*- coding: utf-8 -*-
# Programa: ordenanomesbolha.py
# Programador:
# Data: 30/03/2016
# Este programa lê um número inteiro indicando o tamanho de uma
# lista de nomes. O programa lê a lista de nomes e usando o
# método de ordenação por bolha, ordena a lista em ordem
# crescente e imprime a sequência ordenada.
# início do módulo principal
# descrição das variáveis utilizadas
# list nomes
# int tam
# bool trocou

# pré: tam nomes[0] .. nomes[tam-1]

# Passo 1. Leia e inicialize os dados
# Passo 1.1. Leia o tamanho da sequência
tam = int(input('Leia o tamanho da sequência: '))
# Passo 1.2. Leia a lista de nomes
nomes = list(input().split())[:tam]
# Passo 2. Usando o método do bubble sort ordene a lista
# Passo 2.1. Assuma que houve troca
trocou = True
# Passo 2.2. Compare os termos dois a dois, trocando quando necessário
while trocou:
    # Passo 2.2.1. No início da iteração não houve troca
    trocou = False
    for i in range(0, tam - 1):
        if nomes[i] > nomes[i + 1]:
            nomes[i], nomes[i + 1] = nomes[i + 1], nomes[i]
            trocou = True
# Passo 3. Imprima a sequência ordenada
print(nomes)

# pós: nomes[0] <= nomes[1] <= ... <= nomes[tam-1]
# fim do módulo principal
