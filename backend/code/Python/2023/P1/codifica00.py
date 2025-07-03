# Programa: codifica00.py
# Programador:
# Data: 27/04/2016
# Este programa lê uma palavra composta por 5 caracteres maiúsculos do
# alfabeto {'A'-'Z'} e um número inteiro no intervalo [0,25]. O programa
# codifica a palavra usando o deslocamento dos caracteres da string de
# entrada e imprime a palavra codificada. O programa usa os códigos ASCII,
# e o Alfabeto é tratado de forma circular, ou seja, 'Z' + 1 == 'A'.
# início do módulo principal
# descrição das variáveis utilizadas
# str palavra, codificada
# str char0, char1, char2, char3, char4
# int deslocamento
# pré: palavra and palavra[i] em {'A'..'Z'} deslocamento
# Passo 1. Leia uma palavra com 5 caracteres maiúsculos e o deslocamento
# Passo 1.1. Leia uma palavra de 5 caracteres maiúsculos do alfabeto
palavra = input('Entre com uma palavra com 5 caracteres maiúsculos: ')
# Passo 1.2. Entre com o deslocamento a ser dado para os caracteres.
codificador = int(input('Entre com um inteiro ente 0 e 25: '))
# Passo 2. Codifique os caracteres da palavra
# Passo 2.1. Codifique o primeiro caractere
char0 = chr((ord(palavra[0]) - ord('A') + codificador)%26 + ord('A'))
# Passo 2.2. Codifique o segundo caractere
char1 = chr((ord(palavra[1]) - ord('A') + codificador)%26 + ord('A'))
# Passo 2.3. Codifique o terceiro caractere
char2 = chr((ord(palavra[2]) - ord('A') + codificador)%26 + ord('A'))
# Passo 2.4. Codifique o quarto caractere
char3 = chr((ord(palavra[3]) - ord('A') + codificador)%26 + ord('A'))
# Passo 2.6. Codifique o quinto caractere
char4 = chr((ord(palavra[4]) - ord('A') + codificador)%26 + ord('A'))
# Passo 2.7. Concatene os caracteres
codificada = char0 + char1 + char2 + char3 + char4
# Passo 3. Imprima a mensagem codificada
print('Codificada: {0:s}'.format(codificada))
# pós: codificada and codificada[i] em {A..Z} and para i em {0,...,4}:codificada[i]==palavra[i] + deslocamento
# fim do módulo principal

# Teste o programa para várias palavras com 5 caracteres maiúsculos.
# O que ocorre se a sua mensagem tem mais de cinco caracteres?
# O que ocorre quando a palavra tem menos de 5 caracteres?
# O que ocorre quando a palavra tem 5 caracteres, mas algum caractere que não seja um caractere entre {'A'..'Z'}?