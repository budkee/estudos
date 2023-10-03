# -*- coding: utf-8 -*-
# Programa: exinvertenum.py
# Programador:
# Data: 11/05/2016
# Este programa lê um número, computa o inverso do número
# digitado e imprime o número na ordem inversa
# início do módulo principal
# descrição das variáveis utilizadas
# int numero, num, inverso, digito

# pré: numero

# Passo 1. Leia o número e inicialize as variáveis
# Passo 1.1. Leia um número inteiro
print('Entre com um inteiro: ')
numero = int(input())
# Passo 1.2. Inicialize as variáveis
inverso = 0 # inverso de nummero
num = numero # cópia de numero
# Passo 2. Enquanto num!=0 obtenha dígitos de num  e monte inverso
while num != 0:
# Passo 2.1. Compute o digito mais a direita
   digito = num % 10
# Passo 2.2. Inclua o digito em inverso
   inverso = inverso*10 + digito
# Passo 2.3. Retire o último dígito de num
   num = num//10
# Passo 3. Imprima os resultados
# Passo 3.1. Imprima o número lido
print('O número digitado é: {0:d}'.format(numero))
# Passo 3.2. Imprima o número inverso
print('O número na ordem inversa é: {0:d}'.format(inverso))

# pós: numero == dp...d1d0 and inverso == d0d1...dp
# fim do módulo principal
