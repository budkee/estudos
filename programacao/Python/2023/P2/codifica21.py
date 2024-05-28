# Programa: codifica21.py
# Programador: Camila Budke
# Data: 03/06/2013
# Este programa codifica uma mensagem usando uma frase de codificação.
# Para cada caractere da frase de codificação é associado um valor
# numérico que será adicionado de forma cíclica a cada um dos
# caracteres da mensagem. A=1, B=2, ect... Transformamos esse resultado
# em um número entre 32 e 126, a variação dos códigos ASCII para
# caracteres que podem ser impressos, e então convertemos o número
# resultante novamente em um caractere.

# pré: String1 String2 && String1 == mensagem && String2 == palavra

# Passo 1. Leia a entrada
# Passo 1.1. Leia a mensagem a ser codificada
# print('Entre com a mensagem a ser codificada numa linha:')
mensagem = str(input().upper())
# Passo 1.2. Entre com a frase codificadora.
# print('Entre com uma frase para ser usada na codificação: ')
palavra = str(input().upper())
# Passo 1.3. Compute o tamanho da mensagem e da palavra codificadora
tammensagem = len(mensagem)
tampalavra = len(palavra)
# Passo 2. Codifique a Mensagem
# Passo 2.1. Inicialize a mensagem codificada
mensagemc = ''
# Passo 2.2. Inicialize a posição na mensagem a ser codificada
i = 0
# Passo 2.3. Codifique os tammensagem caracteres da mensagem
while i < tammensagem:
    # Passo 2.3.1. Codifique o caractere i
    novoCodigo = ord(mensagem[i]) + (ord(palavra[i % tampalavra]) - 64)
    # Passo 2.3.2. Verifique se o número obtido não é um caractere válido
    if novoCodigo < 65:
        # Passo 2.3.2.1. Obtenha o número de um caracter válido
        novoCodigo += 26
    elif novoCodigo > 90:
        novoCodigo -= 26
    # fim if
    # Passo 2.3.2. Concatene o novo caracter a mensagem codificada
    mensagemc += chr(novoCodigo)
    # Passo 2.3.3. Incremente o número do caractere
    i += 1
# fim while
# Passo 3. Imprima a mensagem codificada
#   print('Mensagem Codificada: {0:79s}'.format(Mensagem))
print('{0:79s}'.format(mensagemc))

# pós: c[1]...c[n] && para i em {1,...,n}: c[i]==UmChar[i] + UmUInt
# fim
