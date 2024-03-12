# Programa: palavras.py
# Programador:
# Data: 26/04/2012
# Este programa lê uma linha de caracteres ASCII visíveis (sem caracteres
# de controle, computa o número de palavras na linha de entrada (conjunto
# de caracteres ASCII visíveis separados por um caractere espaço) e
# imprime o resultado. Os sinais de pontuação são considerados como parte
# das palavras.

# início do módulo principal

# descrição das variáveis utilizadas
# list palavras
# str frase
# int numpalavras
# pré: um fluxo de caracteres c[0]c[1]...c[n] and n >= 0 and para todoh i em {0,...,n}: c[i] em ASCII visível
# Passo 1. Leia uma string
frase = str(input())
# Passo 2. Compute o número de palavras
# Passo 2.1. Transforme a string numa lista de palavras
palavras = frase.split()
# Passo 2.2. Calcule o número de elementos da lista
tam = len(palavras)
# Passo 3. Imprima o número de palavras
print('{0:d}'.format(tam))
# pós: numpalavras == número de palavras do texto de entrada
# fim do módulo principal