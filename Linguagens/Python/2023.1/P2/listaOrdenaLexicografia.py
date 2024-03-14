# -*- coding: utf-8 -*-
# Programa: listatelefonica.py
# Programador:
# Data: 25/05/2020
# Este programa lê um conjunto de tam nomes e telefones de uma
# empresa telefônica. Os nomes são dados pelo nome, sobrenome
# e número de telefone. O programa elabora uma lista telefônica
# ordenando o conjunto pelo sobrenome. Os dados são armazenados
# em três listas, nomes, sobrenomes e numeros.
# início do módulo principal.
# descrição das variáveis utilizadas
# list nomes, sobrenomes, numeros
# int tam

# pré: tam nomes[0] sobrenomes[0] numeros[0] nomes[1]
#      sobrenomes[1] numeros[1] .. nomes[tam-1]
#      sobrenomes[tam-1]

# Passo 1. Leia a entrada e inicialize as variáveis
# Passo 1.1. Leia o tamanho do catálogo
tam = int(input())
# Passo 1.2. Inicialize as listas
nomes = ['']*tam 
sobrenomes = ['']*tam 
numeros = ['']*tam
# Passo 1.3. Leia os dados dos assinantes
for i in range(tam): 
   nomes[i],sobrenomes[i],numeros[i]= map(str,input().split())
# Passo 2. Ordene pelo sobrenome dos assinantes
# Passo 2.1. Assuma que houve troca
trocou = True
# Passo 2.2. Compare os termos dois a dois, trocando quando necessário
while (trocou):
# Passo 2.2.1. No início da iteração não houve troca
   trocou = False 
   for i in range(0,tam-1): 
      if sobrenomes[i] > sobrenomes[i+1]:
         sobrenomes[i],sobrenomes[i+1]=sobrenomes[i+1],sobrenomes[i] 
         nomes[i],nomes[i+1]=nomes[i+1],nomes[i] 
         numeros[i],numeros[i+1]=numeros[i+1],numeros[i] 
         trocou = True
# Passo 3. Imprima o catálogo
for i in range(0,tam): 
   print('{0:s} {1:s} {2:s}'.format(sobrenomes[i],nomes[i],numeros[i]))

# pós: para i em {0..tam-1}: sobrenomes[i] nomes[i] numeros[i] and
#      sobrenomes[i] <= sobrenomes[i+1]
# fim do módulo principal