# Programa: codifica21.py
# Programador:
# Data: 03/06/2016
# Este programa codifica uma mensagem usando uma frase
# codificadora. Para cada caractere da frase de codificação é
# associado um valor numérico que será adicionado de forma
# cíclica a cada um dos caracteres da mensagem. 'A'=1, 'B'=2,
# etc. Transformamos esse resultado em um número entre 32 e
# 126, a variação dos códigos ASCII para caracteres que podem
# ser impressos, e então convertemos o número resultante
# novamente em um caractere.
# início do módulo principal
# descrição das variáveis utilizadas
# str  mensagem  - mensagem a ser codificada
#      mensagemC - mensagem codificada
#      palavra   - palavra chave
# int  tam       - tamanho da mensagem
#      tamp      - tamanho da palavra codificadora
# pré: mensagem palavra
# Passo 1. Leia a entrada e compute o tamanho das strings
# Passo 1.1. Leia a mensagem a ser codificada
mensagem = str(input())
# Passo 1.2. Leia a palavra codificadora.
palavra = str(input())
# Passo 1.3. Compute os tamanhos da mensagem e da palavra
tam = len(mensagem)
tamp = len(palavra)
# Passo 1.4. Transforme os caracteres para maiúsculos
mensagem = mensagem.upper()
palavra = palavra.upper()
# Passo 2. Codifique a Mensagem
# Passo 2.1. Inicialize a mensagem codificada
mensagemC = ''
# Passo 2.2. Codifique cada um dos caracteres da mensagem
for i in range(0, tam):
    # Passo 2.2.1. Verifique se o caractere é do alfabeto
    if mensagem[i].isalpha():
        # Passo 2.2.1.1. Codifique o caractere
        codigo = (ord(mensagem[i]) - ord('A') + ord(palavra[i % tamp]) - ord('A') + 1) % 26 + ord('A')
        mensagemC = mensagemC + chr(codigo)
    # Passo 2.2.2. Verifique se o caractere é um dígito
    elif mensagem[i].isnumeric():
        codigo = (ord(mensagem[i]) - ord('0') + ord(palavra[i % tamp]) - ord('A') + 1) % 10 + ord('0')
        mensagemC = mensagemC + chr(codigo)
    # Passo 2.2.3. Para os demais caracteres não altera
    else:
        mensagemC = mensagemC + mensagem[i]
# Passo 3. Imprima a mensagem codificada
print('{0:s}'.format(mensagemC))
# pós: c[1]...c[n] and para i em {1,...,n}: c[i]==mensagem[i] +
#      palavra[i%m] and n == tam and m == tamp
# fim do módulo principal
