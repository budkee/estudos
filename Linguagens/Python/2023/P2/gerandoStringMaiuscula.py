# Importe as bibliotecas
import random, string
# Leia o número de caracteres e a semente
num = int(input())
semente = random.seed(int(input()))
# Inicialize a palavra
palavra = ''
# Declare a lista a ser percorrida para retirar a escolha pseudo-aleatória
alfabeto = string.ascii_uppercase
# Comece o loop até atingir o tamanho de caracteres 
i=0
while i <= num-1:
    char = random.choice(alfabeto)
    palavra += char
    i += 1
print(palavra)