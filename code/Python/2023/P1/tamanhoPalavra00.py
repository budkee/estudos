# -*- coding: utf-8 -*-
# Programa: tamanho.py
# Programador:
# Data: 08/07/2016
# Este programa lê um texto, conjunto de
# caracteres visíveis, calcula e imprime o número de
# de caracteres diferentes do espaço na palavra.
# início do módulo principal
# descrição das variáveis utilizadas
# int tamanho
# str texto, caractere

# pré: texto
# Passo 1. Leia um texto
texto = str(input())
# Passo 2. Compute o tamanho do texto sem espaços
# Passo 2.1. Inicialize a quantidade de caracteres
tamanho = 0
# Passo 2.2. Conte os caracteres do texto diferentes de espaço
for caractere in texto:
    if caractere != ' ':
        tamanho = tamanho + 1
# ou
# Passo 2. Compute o tamanho da palavra
#tamanho = sum(1 for caractere in texto if letra != ' ')
# Passo 3. Imprima o número de caracteres do texto
print(tamanho)
# pós: tamanho and tamanho == len(texto)-texto.count(' ')
# fim do módulo principal
