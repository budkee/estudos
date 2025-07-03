# -*- coding: utf-8 -*-
# Programa: palindromo00.py
# Programador:
# Data: 09/08/2022
# Este programa que lê uma string com quatro caracteres
# palavra[0:4]. O seu programa deve inverter a ordem dos
# caracteres de palavra gerar a string
# inversa = palavra[::-1] (sem usar slicing) e imprimir o
# resultado.
# início do módulo principal
# descrição das variáveis utilizadas
# str palavra, inversa

# pré: palavra

# Passo 1. Leia a palabra
palavra = str(input())
# Passo 2. Inverta a palavra
inversa = palavra[::-1]
# Passo 3. Imprima a palavra invertida
print('{0:s}'.format(inversa))

# pós: palavra[::-1]
# fim do módulo principal