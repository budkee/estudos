# Algoritmo: Cifrador de César 01
# Passo 1. Leia uma palavra com 5 caracteres visíveis e o deslocamento
# Passo 1.1. Leia uma palavra
palavra = input('Digite uma palavra com até 5 caracteres: ')
# Passo 1.2. Leia o deslocamento
desloc = int(input('Digite o valor do deslocamento: '))
# Passo 2. Codifique a palavra
# Passo 2.1. Codifique o primeiro caractere
# Passo 2.1.1. Se o caractere for do alfabeto maiúsculo
if palavra[0].isupper():
# Passo 2.1.1.1. Codifique o caractere
    char0 = chr((ord(palavra[0]) - ord('A') + desloc) % 26 + ord('A')) # Número codificado dentro do intervalo [0,25]
# Passo 2.1.2. Se o caractere for do alfabeto minúsculo
elif palavra[0].islower():
# Passo 2.1.2.1. Codifique o caractere
    char0 = chr( (ord(palavra[0]) - ord('a') + desloc) % 26 + ord('a') )
# Passo 2.1.3. Se o caractere nõo for do alfabeto
else:
# Passo 2.1.3.1. Mantenha o caractere
    char0 = palavra[0]
# Passo 2.2. Codifique o segundo caractere
if palavra[1].isupper():
    char1 = chr((ord(palavra[1]) - ord('A') + desloc) % 26 + ord('A')) # Número codificado dentro do intervalo [0,25]
elif palavra[1].islower():
    char1 = chr( (ord(palavra[1]) - ord('a') + desloc) % 26 + ord('a'))
else:
    char1 = palavra[1]
# Passo 2.3. Codifique o terceiro caractere
if palavra[2].isupper():
    char2 = chr( (ord(palavra[2]) - ord('A') + desloc) % 26 + ord('A'))
elif palavra[2].islower():
    char2 = chr((ord(palavra[2]) - ord('a') + desloc) % 26 + ord('a'))
else:
    char2 = palavra[2]
# Passo 2.4. Codifique o quarto caractere
if palavra[3].isupper():
    char3 = chr((ord(palavra[3]) - ord('A') + desloc) % 26 + ord('A'))
elif palavra[3].islower():
    char3 = chr((ord(palavra[3]) - ord('a') + desloc) % 26 + ord('a'))
else:
    char3 = palavra[3]
# Passo 2.5. Codifique o quinto caractere
if palavra[4].isupper():
    char4 = chr((ord(palavra[4]) - ord('A') + desloc) % 26 + ord('A'))
elif palavra[4].islower():
    char4 = chr((ord(palavra[4]) - ord('a') + desloc) % 26 + ord('a'))
else:
    char4 = palavra[4]
# Passo 2.6. Concatene os caracteres codificados
codificada = char0 + char1 + char2 + char3 + char4
# Passo 3. Imprima a palavra codificada
print('A palavra {0:s} codificada fica: {1:s}'.format(palavra, codificada))
# fim do algoritmo