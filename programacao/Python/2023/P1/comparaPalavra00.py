# Programa: compara00.py
# Programador:
# Data: 07/11/2016
# Este programa lê duas palavras, compara as palavras, computa a
# maior palavra, lexicograficamente, e imprime a maior.

# início do módulo principal

# descrição das variáveis utilizadas
# str palavra1, palavra2, maior
# pré: palavra1 palavra2
# Passo 1. Leia duas palavras
palavra1 = str(input())
palavra2 = str(input())
# Passo 2. Calcule a maior palavra (lexicograficamente)
if palavra1 > palavra2:
# Passo 2.1. Se palavra1 for maior, atribua palavra1 a maior
   maior = palavra1
# Passo 2.2. Caso contrário, atribua palavra2 a maior
else:
   maior = palavra2
# Passo 3. Imprima a maior palavra
print('A maior palavra é {0:s}'.format(maior))
# pós: maior and maior == max{palavra1, palavra2}
# fim do módulo principal