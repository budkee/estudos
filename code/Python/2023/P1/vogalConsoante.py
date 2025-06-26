# -*- coding: utf-8 -*-
# Programa: vogalconsoante00.py
# Programador:
# Data: 22/08/2022
# Este programa lê uma string com quatro caracteres e
# conta o número de vogais e consoantes da string e
# imprime o resultado. Vogais e consoantes maiúsculas
# e minúsculas são consideradas diferentes.
# início do módulo principal
# descrição das variáveis utilizadas
# int numvogaismai, numconsoantesmai
# int numvogaismin, numconsoantesmin
# str palavra

# pré: palavra

# Passo 1. Leia a entrada e inicialize as variáveis
# Passo 1.1. Leia uma palavra com 4 caracteres
palavra = str(input())
# Passo 1.2. Inicialize o número de vogais e de consoantes
numvogaismai = 0 # maiúsculas
numvogaismin = 0 # minúsculas
numconsoantesmai = 0 # maiúsculas
numconsoantesmin = 0 # minúsculas
# Passo 1.3. Inicialize as vogais
# Passo 1.3.1. Inicialize as vogais maiúsculas
vogaisM = 'AEIOU'
# Passo 1.3.1. Inicialize as vogais minúsculas
vogaism = 'aeiou'
# Passo 2. Compute o número de vogais e consoantes
for i in range(len(palavra)):
    if palavra[i] >= 'A' and palavra[i] <= 'Z': # Se estiver no alfabeto, faça:
       if palavra[i] in vogaisM: # Se a substring da palavra estiver em vogais, faça:
          numvogaismai += 1
       else:
          numconsoantesmai += 1
    elif palavra[i] >= 'a' and palavra[i] <= 'z':
       if palavra[i] in vogaism:
          numvogaismin += 1
       else:
          numconsoantesmin += 1
# Passo 3. Imprima os resultados
print('Num. Vogais Maiúsculas = {0:d}'.format(numvogaismai))
print('Num. Consoantes Maiúsculas = {0:d}'.format(numconsoantesmai))
print('Num. Vogais Minúsculas = {0:d}'.format(numvogaismin))
print('Num. Consoantes Minúsculas = {0:d}'.format(numconsoantesmin))

# pós: número de vogais e consoantes da frase
# fim do módulo principal
