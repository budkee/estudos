# -*- coding: utf-8 -*-
# Programa: copiappalavra2.py
# Programador:
# Data: 22/10/2012
# Este algoritmo lê uma palavra com pelo menos 5 caracteres, faz uma
# dos três últimos caracteres da palavra numa nova variável
# e imprime a palavra e a nova variável
# início do módulo principal
# descrição das variáveis utilizadas
# string palavra, partepala

# pré: palavra

# Passo 1: leia as entradas
palavra = str(input('Digite a palavra: '))
# Passo 2: retire os 3 últimos caracteres da palavra
partepala = palavra[-3:]
# Passo 3: imprima o resultado
print('palavra = {} - parte = {}'.format(palavra, partepala))


# pós: palavra partepal and partepal == palavra[tam-3:tam]
# fim do módulo principal