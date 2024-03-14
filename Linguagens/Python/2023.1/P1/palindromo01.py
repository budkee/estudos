# -*- coding: utf-8 -*-
# Programa: palpalindromo.py
# Programador:
# Data: 11/11/2016
# Este programa lê uma palavra e constrói a palavra inversa
# caractere a caractere, verifica se ela é palíndromo e
# imprime se é ou não palíndromo.
# início do módulo principal
# descrição das variáveis utilizadas
# str palavra, letra, inversa, msg

# pré: palavra

# Passo 1. Leia uma palavra
palavra = str(input())
# Passo 2. Verifique se a palavra é palíndromo
# Passo 2.1. Compute o inverso da palavra
# Passo 2.1.1. Inicialize a palavra inversa
inversa = ''
# Passo 2.1.2. Para cada letra em palavra insira em inversa
for letra in palavra:
    inversa = letra + inversa  # insira letra na frente de inversa
# Passo 2.3. Verifique se a palavra é palíndromo
if palavra.lower() == inversa.lower():
    msg = 'palíndromo'
else:
    msg = 'não é palíndromo'
# Passo 3. Imprima se a palavra é palíndromo.
print('{0:s}'.format(msg))

# pós: 'palíndromo' and para {0,..,n-1}: palavra[i] ==
#      palavra[n-i-1] or 'não é palíndromo'
# fim do módulo principal
