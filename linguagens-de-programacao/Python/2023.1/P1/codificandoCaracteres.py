# Cifra de césar:  O programa lê dois caracteres e um numero inteiro e codifica os caracteres através do deslocamento dos caracteres.

letra1 = str(input('Primeira letra: '))
letra2 = str(input('Segunda letra: '))
num = int(input('Qual é a chave? '))

palavra = letra1 + letra2

codificada = chr(ord(letra1) + num) + chr(ord(letra2) + num)

print(codificada)



