# -*- coding: utf-8 -*-
# Programa: temperatura02.py
# Programador:
# Data: 21/11/2016
# Este programa lê um conjunto de temperaturas lidas em determinados locais
# durante os dias da semana, computa e imprime a temperatura média em
# cada um dos locais. As medidas são tomadas diariamente, em
# determinados horários e em determinados locais.

# pré: para i em {0..3} and j {0..2}:temp[i][j]

# Passo 1.Inicialize as estruturas e leia a entrada
# Passo 1.1. Leia as dimensões das listas
# lin, col = map(int, input().split())
lin, col = 4, 3
# Passo 1.2. Inicialize as estruturas de dados
temp = [[0] * col for i in range(lin)]
media = [0] * col

# Passo 1.3. Leia a temperatura de cada local (linha a linha)
for i in range(lin):
    temp[i] = list(map(float, input().split()))  # leia a linha i

# Passo 2. Calcule a media das temperaturas de cada horário - some os elementos da coluna e divida
# pelo número de linhas

# Passo 2.1 Some as colunas

# Para cada coluna, faça:
for j in range(col):  # fixa coluna j

    # Zere a soma para o próximo local
    soma = 0.0

    # Para cada linha, compute os valores daquele local
    for i in range(lin):  # percorre as linhas de i
        soma = soma + temp[i][j]  # soma os valores das colunas
        # print(temp[i][j], soma)

    # Compute a média daquele local
    media[j] = soma / lin

# Passo 3. Imprima a media linha a linha
for local in range(col):
    print('{0:d} {1:5.1f}'.format(local + 1, media[local]))

# pós: para j em {0..2}:tempMed[j] and tempMed[j] == (soma
#      i em {0..3}:temp[i][j])/4.0