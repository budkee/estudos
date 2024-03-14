# -*- coding: utf-8 -*-
# Programa: exdigitos01.py
# Programador:
# Data: 11/05/2016
# Este programa lê um número, imprime o número digitado
# calcula e imprime a quantidade e soma dos dígitos do número.
# início do módulo principal
# descrição das variáveis utilizadas
# int numero, num, contador, soma

# pré: numero

# Passo 1. Leia o número e inicialize as variáveis
# Passo 1.1. Leia um número inteiro
print('Entre com um inteiro: ')
numero = int(input())
# Passo 1.2. Inicialize contador e soma
contador = 0 # número de dígitos
soma = 0 # soma dos dígitos
# Passo 1.3. Faça uma cópia de num
num = numero # cópia de num
# Passo 2. Enquanto num != 0 faça
while num != 0:
# Passo 2.1. Incremente o número de dígitos
   contador += 1
# Passo 2.2. Adicione o último dígito a soma 
   soma = soma + num % 10
# Passo 2.3. Retire o último dígito de num
   num = num//10
# Passo 3. Imprima os resultados
# Passo 3.1. Imprima o número lido
print('O número digitado é: {0:d}'.format(numero))
# Passo 3.2. Imprima o número de dígitos de numero
print('O número de dígitos é: {0:3d}'.format(contador))
# Passo 3.3. Imprima a soma dos dígitos de numero
print('A soma dos dígitos é : {0:3d}'.format(soma))

# pós: numero == dp..d1d0 and contador == p+1 and
#      soma = dp+..+d1+d0
# fim do módulo principal
