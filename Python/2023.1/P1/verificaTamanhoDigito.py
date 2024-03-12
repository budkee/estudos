# -*- coding: utf-8 -*-
# Programa: tamanho.py
# Programador:
# Data: 03/05/2010
# Este programa le um numero inteiro indicando a quantidade
# de numeros a serem lidos. O programa le cada um dos numeros
# e a cada numero lido computa a quantidade de digitos do
# numero.
# inicio do módulo principal
# descrição das variáveis utilizadas
# int numero
# int num, digitos

# pré: numero

# Passo 1. Leia um numero
numero = int(input())
# Passo 2. Compute o numero de digitos
# Passo 2.1. Incialize o numero de digitos
digitos = 0
# Passo 2.2. Decomponha o numero
while numero > 0:
# Passo 2.2.1. Retire o digito menos significativo
    numero = numero // 10
# Passo 2.3.1. Adicione 1 a quantidade de digitos
    digitos += 1
# Passo 2.4. Imprime o resultado
print('{0:d}'.format(digitos))

# pos: digitos == n
# fim do módulo principal
