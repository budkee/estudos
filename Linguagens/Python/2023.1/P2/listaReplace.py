# -*- coding: utf-8 -*-
# Programa: concatena01.py
# Programador:
# Data: 29/04/2019
# Este programa lê duas strings sem usar operador +, concatena
# e imprime a concatenação das strings.
# início do módulo principal
# descrição das variáveis utilizadas  
# str string1, string2 - strings a serem comparadas
# str concatena - comparação das strings

# pré: c1[0]..c1[tam1-1] c2[0]..c2[tam2-1]

# Passo 1. Leia as strings
string1, string2 = input().split()
# Passo 2. Concatene as strings string1, string2 
# Passo 2.1. Compute os tamanhos das strings
tam1 = len(string1)
tam2 = len(string2)
# Passo 2.2. Inicialize uma palavra para armazenar a concatenação
concatena = ' '*(tam1+tam2)
# Passo 2.3. Copie os caracteres de palavra1 em concatena
for i in range(0,tam1):
   concatena = concatena.replace(concatena[i],palavra1[i],1)
# Passo 2.4. Copie os caracteres de palavra2 em concatena
for j in range(0,tam2):
   concatena = concatena.replace(concatena[i+1+j],palavra2[j],1)
# Passo 3. Imprima a concatenação das palavras.
print('{0} concatenada com {1} == {2}'.format(palavra1, palavra2, concatena)) 
               
# pós: concatena == c1[0]...c1[n-1]c2[0]...c2[m-1]
# fim módulo principal