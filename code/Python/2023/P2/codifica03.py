# Programa: codifica20.py
# Programador:
# Data: 03/06/2016
# Este programa codifica uma mensagem por meio da conversão de
# cada caractere alfanumérico da mensagem para o seu código
# numérico ASCII e adicionando um inteiro positivo a este código.
# O programa deve garantir que esse resultado se mantenha entre
# 48 a 57 no caso dos dígitos, de 65 a 90 no caso dos caracteres
# maiúsculos e de 97 a 122 no caso dos caracteres minúsculos, e
# então converte o número resultante novamente em um caractere
# ASCII alfanumérico.
# início do módulo principal
# descrição das variáveis utilizadas
# str mensagem, mensagemC
# int codificador, tam, codigo

# pré: mensagem codificador

# Passo 1. Leia a entrada e compute o tamanho da mensagem
# Passo 1.1. Leia a mensagem a ser codificada
print('Leia a mensagem a ser codificada: \n')
mensagem = str(input())
# Passo 1.2. Leia o deslocamento
print('Entre com o deslocamento: \n')
codificador = int(input())
# Passo 1.3. Compute o tamanho da mensagem
tam = len(mensagem)
# Passo 2. Codifique a Mensagem
# Passo 2.1. Inicialize a mensagem codificada
mensagemC = ''
# Passo 2.2. Codifique cada um dos caracteres da mensagem
for i in range(0, tam):
    # Passo 2.2.1. Verifique se o caractere é maiúsculo e codifique
    if mensagem[i].isupper():
        codigo = (ord(mensagem[i]) - ord('A') + codificador) % 26 + ord('A')
        mensagemC = mensagemC + chr(codigo)
    # Passo 2.2.2. Verifique se o caractere é minúsculo e codifique
    elif mensagem[i].islower():
        codigo = (ord(mensagem[i]) - ord('a') + codificador) % 26 + ord('a')
        mensagemC = mensagemC + chr(codigo)
    # Passo 2.2.3. Verifique se o caractere é um dígito e codifique
    elif mensagem[i].isnumeric():
        codigo = (ord(mensagem[i]) - ord('0') + codificador) % 10 + ord('0')
        mensagemC = mensagemC + chr(codigo)
    # Passo 2.2.4. Para os demais caracteres não altera
    else:
        mensagemC = mensagemC + mensagem[i]
# Passo 3. Imprima a mensagem codificada
print('{0:s}'.format(mensagemC))

# pós: c[0]..c[n-1] and para i em {0..n-1}:c[i]==mensagem[i]
#      + codificador
# fim do módulo principal
