# Programa: contachar2.py
# Programador:
# Data: 15/11/2016
# Este programa lê um texto e um caractere e conta o
# número de ocorrências do caractere (independente se for maiúsculo
# ou minúsculo) na palavra e imprime o resultado.
# início do módulo principal
# descrição das variáveis utilizadas
# int num
# str texto, letra

# pré: texto letra

# Passo 1. Leia um texto e uma letra e inicialize num
# Passo 1.1. Leia um texto
print('Leia um texto: ')
texto = input()
# Passo 1.2. Leia o caractere (letra)
print('Leia um caractere: ')
letra = str(input())
# Passo 1.3. Inicialize o número de caracteres (letra)
num = 0
# Passo 2. Compute o número de caracteres iguais a letra que ocorrem no texto
# Passo 2.1. Para cada char em texto repita
for char in texto:
    # Passo 2.1.1. Verifique se char é igual a letra
    if char.lower() == letra.lower():
        num += 1
# Passo 3. Imprima o número de caracteres iguais a letra no texto
print('{0:d}'.format(num))

# pós: num == Num{char em texto}: char == letra
# fim do módulo principal
