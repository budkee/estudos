# -*- coding: utf-8 -*-
# Programa: primos.py
# Programador:
# Data: 03/05/2016
# Este programa lê um número inteiro, computa se ele é primo e
# imprime uma mensagem correspondente
# início do módulo principal
# descrição das variáveis utilizadas
# int num, div
# str msg

# pré: num
# Passo 1. Leia um número inteiro e inicialize o divisor
# Passo 1.1. Leia um número inteiro
num = int(input())
# Passo 1.2. Inicialize o divisor
div = 2
# Passo 2. Verifique se número tem algum divisor < num
# Passo 2.1. Enquanto num % div != 0 repita
while num % div != 0:
# Passo 2.1.1. Calcule o novo divisor
   div = div + 1
# Passo 2.2. Verifique o maior divisor de num e atribua a msg
   if num == div:
      msg = 'sim'
   else:
      msg = 'não'
# Passo 3. Imprima a resposta
print(msg)

# pós: 'sim' and para todo i em {2,...num-1}: num%div!=0 or 'não'
#      caso contrário
# fim do módulo principal