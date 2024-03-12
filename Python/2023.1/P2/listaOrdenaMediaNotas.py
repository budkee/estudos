# -*- coding: utf-8 -*-
# Programa: nomes00.py
# Programador:
# Data: 20/11/2019
# Este programa lê os dados referentes ao número, nome, as 3 notas das
# provas e as 2 notas de trabalho dos alunos da disciplina de Algoritmos e
# Programação I. A média das provas é dada por MP = (P1+P2+P3)/3.0, a
# média dos trabalhos por MT = (T1 + T2)/2.0 e a média final por
# MF = 0.75*MP + 0.25*MT. O programa computa a média final, ordena os
# dados dos alunos usando a média e imprime o número, nome e a média final
# de cada aluno, onde as notas estão ordenadas em ordem não crescente.
# Os dados de cada aluno são dados em uma linha, onde as informações são
# separadas por vírgulas.
# início do módulo principal
# descrição das variáveis utilizadas
# list numeros, nomes, notas, medias
# str dados, avalia
# int tam

# pré: tam para i em {0,.,tam-1}: dados

# Passo 1. Leia a entrada e inicialize as variáveis
# Passo 1.1. Leia o número de alunos
tam = int(input())
# Passo 1.2. Inicialize as abstrações
numeros = ['']*tam 
nomes = ['']*tam 
notas = [0.0]*5 
medias = [0.0]*tam 
# Passo 1.3. Leia os dados dos alunos e calcule as médias
for i in range(tam): 
   dados = input() 
   numeros[i],nomes[i],avalia = dados.split(', ') 
   notas = list(map(float,avalia.split()))
# Passo 1.3.2. Calcule e armazene a média dos trabalhos
   medias[i] = .75*(notas[0]+notas[1]+notas[2])/3.0+.25*(notas[3]+notas[4])/2.0
# Passo 2. Ordene os dados pela média
# Passo 2.1. Ordene a lista medias[0:i]
for i in range (1,tam): 
   temp1 = medias[i] 
   temp2 = numeros[i] # temos que ordenar junto numeros[i] 
   temp3 = nomes[i] # temos que ordenar junto nomes[i] 
# Passo 2.1.1. Insira temp1 em medias[0:i] | medias[i-1] < temp1 < medias[i+1] 
   j = i - 1 # inicie no final da lista medias[0:i-1]
   while j >= 0 and temp1 > medias[j]: 
# Passo 2.1.1.1. Mova os elementos para a direita em cada lista
      medias[j+1] = medias[j] 
      numeros[j+1] = numeros[j] 
      nomes[j+1] = nomes[j] 
      j = j - 1 # mova a comparação para esquerda
# Passo 2.2. Insira os elementos na posição j (j+1) de cada lista
   medias[j+1] = temp1 
   numeros[j+1] = temp2 
   nomes[j+1] = temp3 
# Passo 3. Imprime os resultados
for i in range(0,tam): 
   print('{0:s} {1:s} {2:.1f}'.format(numeros[i],nomes[i],medias[i]))
   
# pós: para i em {0 .. tam-1}:numeros[i] nomes[i] medias[i] and 
#      medias[i] == 0.75*(notas[0]+notas[1]+notas[2])/3.0 +
#      0.25*(notas[3]+notas[4])/2.0 and medias[i] >= medias[i+1]
# fim do módulo principal