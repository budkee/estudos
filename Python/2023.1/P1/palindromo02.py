# -*- coding: utf-8 -*-
# Programa: palindromo.py
# Programador:
# Data: 03/05/2016
# Este programa lê um número inteiro, indicando a
# quantidade de números a serem lidos. O programa le cada
# um dos números e a cada número lido computa se ele é
# palíndromo.

# início do módulo principal

# descrição das variáveis utilizadas
# int numero, num, reverso, digito

# pré: num == d[k]d[k-1]...d[1]d[0]

# Passo 1: leia o numero e inicie as variáveis
num = int(input())
qntDigitos = 0
aux = num
# Passo 2.1: Encontre a quantidade de digitos
while aux > 0:
    qntDigitos += 1
    aux //= 10
# Passo 2.2:
palindromo = True
while palindromo == True:
    for i in range(qtd_digitos // 2):
        digito_i = (num // (10**i)) % 10
        digito_n_i_1 = (num // (10**(qtd_digitos-i-1))) % 10
        if digito_i != digito_n_i_1:
            palindromo = False
    # Passo 4. Imprima a resposta
    print('{0}'.format(mensagem))

# pós: (sim and d[k]d[k-1]...d[1]d[0] == d[0]d[1]...d[k-1]d[k]) or não
# fim do módulo principal
