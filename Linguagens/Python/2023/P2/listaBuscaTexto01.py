# -*- coding: utf-8 -*-
# Programa: substring01.py
# Programador:
# Data: 28/04/2015
# Este programa lê um texto e uma palavra e verifica se a
# palavra ocorre no texto, e imprime a o índice da primeira 
# ocorrência da palavra ou caso contrário, o tamanho do texto
# início do módulo principal
# descrição das variáveis utilizadas
# string texto - texto onde a palavra será procurada
# string palavra - palavra
# int posicao - índice

# pré: texto palavra

# Passo 1. Leia as strings e compute o tamanho
# Passo 1.1. Leia o texto.
texto = input() 
# Passo 1.2. Leia a palavra.
palavra = input()
# Passo 2 Procure a palavra no texto e compute a mensagem.
# Passo 2.1. Compute o índice onde ocorre o primeiro caractere
posicao = texto.find(palavra)
# Passo 2.3. Compute a mensagem
if posicao != -1: # encontrou todos caracteres
   resposta = 'sim' 
else: # não encontrou todos caracteres
   resposta = 'não'
# Passo 3. Imprima os resultados
print('{0:s} {1:d}'.format(resposta,posicao))

# pós: resposta == 'sim' and posicao | para i em {l,l+1..l+k-1} j em
#      {0,1..k-1}: texto[i] == palavra[j] and l == posição and
#      k == tamanho(palavra) || resposta == 'não' and posicao == tam(texto)
# fim do módulo principal