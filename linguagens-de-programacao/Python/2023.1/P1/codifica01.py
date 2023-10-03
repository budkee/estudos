# Passo 1. Leia uma palavra com 5 caracteres maiúsculos e o deslocamento
# Passo 1.1. Leia uma palavra de 5 caracteres maiúsculos do alfabeto
palavra = input('Entre com uma palavra com 6 caracteres maiúsculos: ')
# Passo 1.2. Entre com o deslocamento a ser dado para os caracteres.
codificador = int(input('Entre com um inteiro entre 0 e 25: '))
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
# Passo 2.7. Codifique o sexto caractere
char5 = chr((ord(palavra[5]) - ord('A') + codificador)%26 + ord('A'))
# Passo 2.8. Concatene os caracteres
codificada = char0 + char1 + char2 + char3 + char4 + char5
# Passo 3. Imprima a mensagem codificada
print('Codificada: {0:s}'.format(codificada))