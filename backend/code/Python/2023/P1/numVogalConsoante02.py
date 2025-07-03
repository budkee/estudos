# -*- coding: utf-8 -*-
# Programa: vogalconsoante03.py
# Programador:
# Data: 12/04/2022
# Este programa lê um texto, conjunto de caracteres
# visíveis, calcula e imprime o número de vogais e
# consoantes no texto.
# início do módulo principal
# descrição das variáveis utilizadas
# int numvogais, numconsoantes
# str texto, letra

# pré: texto
# Passo 1. Leia a entrada e inicialize as variáveis
# Passo 1.1. Leia um texto
texto = str(input())
# Passo 1.2. Inicialize a lista das vogais
vogais = 'aeiouAEIOU'
# Passo 1.3. Inicialize o número de vogais e de consoantes
numvogais = 0
numconsoantes = 0
# Passo 2. Compute o número de vogais e consoantes
numvogais = sum(1 for letra in texto if letra.isalpha() and letra in vogais)
numconsoantes = sum(1 for letra in texto if letra.isalpha() and letra not in vogais)
# Passo 3. Imprima o número de vogais e consoantes do texto
print('vogais: {0:d}'.format(numvogais))
print('consoantes: {0:d}'.format(numconsoantes))

# pós: numvogais and numconsoantes and
#      numvogais == Num{letra in texto and letra in alfabeto and in vogais} and
#      numconsoantes == Num{letra in texto and letra in alfabeto and not in vogais}
# fim do módulo principal
