# Programa: contapalavras.py
# Programador:
# Data:
# Este programa lê um texto não vazio de caracteres visíveis de um arquivo .txt, calcula
# e imprime o total de palavras do texto.
# início do módulo principal
# descrição das variáveis utilizadas
# str texto, char, charant
# int tam, numpalavras
import sys
# pré: texto

# Passo 1. Leia um texto
texto = sys.stdin.read()
# Passo 2. Conte o número de palavras do texto
# Passo 2. Compute o número de palavras da string
# Passo 2.1. Inicialize a caractere anterior e numpalavras
charant = ' '
numpalavras = 0
# Passo 2.2. Procure os espaços que separam as palavras no texto
for char in texto:
    if (char == ' ' or char == '\n') and (charant != ' ' and charant != '\n'):
        numpalavras = numpalavras + 1
    charant = char
# Passo 2.3. Analise o último caractere do texto
if char != ' ' and char != '\n':
    numpalavras = numpalavras + 1
# Passo 3. Imprima o número de palavras
print('{0:d}'.format(numpalavras))

# pós: número de palavras do texto
# Para rodar o programa no terminal: $ python nomeprograma.py < texto.txt
# fim do módulo principal
