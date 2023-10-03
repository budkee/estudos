# -*- coding: utf-8 -*-
# Programa: substring00.py
# Programador:
# Data: 28/04/2015
# Este programa lê um texto e uma palavra e verifica se a
# palavra ocorre no texto, e imprime a o índice da primeira ocorrência
# da palavra ou caso contrário, o tamanho do texto
# início do módulo principal
# descrição das variáveis utilizadas
# string texto - texto onde a palavra será procurada
# string palavra - palavra
# int tamtexto - tamanho do texto
# int tampalavra - tamanho da palavra
# int posicao, i, j - índices

# pré: texto palavra

# Passo 1. Leia as strings e compute o tamanho
# Passo 1.1. Leia o texto
texto = input()
# Passo 1.2. Leia a palavra
palavra = input()
# Passo 1.3. Compute o tamanho das strings
tam1 = len(texto) 
tam2 = len(palavra)
# Passo 2 Procure a palavra no texto
# Passo 2.1. Inicialize os índices das strings
i = 0 
j = 0
# Passo 2.2. Compare os tam2 caracteres de palavra em texto
while i < tam1 and j < tam2: 
   if texto[i] == palavra[j]:
      i = i + 1 # vá para o próximo caractere em texto
      j = j + 1 # vá para o próximo caractere em palavra
   else: 
      i = i - j + 1 # vá ao caractere seguinte do início comparação
      j = 0 # vá para o caractere inicial em palavra
# Passo 2.3. Compute a posição
if j == tam2: # encontrou todos caracteres
   posicao = i-j 
   resposta = 'sim' 
else: # não encontrou todos caracteres 
   posicao = tam1 
   resposta = 'não'
# Passo 3. Imprima os resultados
print('{0:s} {1:d}'.format(resposta,posicao))

# pós: resposta == 'sim' and posicao | para i em {l,l+1..l+k-1} j em 
#      {0,1..k-1}: texto[i] == palavra[j] and l == posição
#     k == tamanho(palavra) or resposta == 'não' and posicao == tam(texto) 
# fim do módulo principal