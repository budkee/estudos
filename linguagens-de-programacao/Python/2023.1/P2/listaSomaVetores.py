# -*- coding: utf-8 -*-
# Programa: somavetores.py
# Programador: siriub
# Data: 16/05/23
# Este programa le dois vetores de inteiros e computa imprime a soma
# início do módulo principal
# descrição das variáveis utilizadas
# list a, b, soma
# int tam

# pré: a b

# Passo 1. Leia os vetores
# Passo 1.1. Leia o vetor a
a = list(map(float, input().split()))
# Passo 1.2. Leia o vetor b
b = list(map(float, input().split()))
# Passo 1.3. Incialize a lista soma
soma = []
# Passo 2. Calcule a soma dos vetores
i = 0 
while i <= len(a)-1:
    c = a[i] + b[i]
    soma.append(c)
    i += 1
# Passo 3. Imprima o vetor soma
print(soma)

# pós: soma and para i em {0..tam-1}:soma[i] == a[i]+b[i]
# fim do módulo principal
