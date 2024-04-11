# Concatenando trechos de palavras: o programa lê duas palavras e um inteiro, concatena o prefixo de uma ao sufixo de outra.

# Formato de Entrada
# primeiro
# segundo
# 3

# Formato de Saida
# prindo

# Passo 1: leia as entradas
palavra1 = input('Primeira palavra: ')
palavra2 = input('Segunda palavra: ')
k = int(input('Digite um número inteiro: '))
# Passo 2: compute o prefixo da palavra 1
prefixo = palavra1[:k]
# Passo 2.1: compute o tamanho e o sufixo da palavra 2
tam = len(palavra2)
sufixo = palavra2[tam-k:]
# Passo 3: concatene o prefixo com o sufixo
palavra = prefixo + sufixo

# Passo 3: imprima a palavra concatenada
print('{0} concatenada com {1} == {2}'.format(prefixo, sufixo, palavra))