# -*- coding: utf-8 -*-
# Programa: contapos.py
# Programador:
# Data: 05/04/2016
# Este programa lê quatro números inteiros, conta quantos números positivos
# foram lidos e imprime o resultado.
# início do módulo principal
# descrição das variáveis utilizadas
# int num1, num2, num3, num4
# int numpos, somapos

# pré: num1 num2 num3 num4

# Passo 1. Leia 4 números inteiros
num1, num2, num3, num4 = map(int, input().split())
num = [num1, num2, num3, num4]
#num1, num2, num3, num4 = map(int, input().split())
# Passo 2. Calcule o numero e a soma de positivos
# Passo 2.1. Inicialize numpositivos e soma
numPos = 0
somaPos = 0
# Passo 2.2. Compute o numero e a soma dos positivos
for i in range(len(num)):
    if num[i] > 0:
        numPos += 1 # numPos = numPos + 1
        somaPos += num[i] # somaPos = somaPos + num[i]
        i += 1
    else:
        continue
        #print('nada aqui')
# Passo 3. Imprima os resultados
print('Número de positivos lidos: {0:d}'.format(numPos))
print('Soma dos números positivos: {0:d}'.format(somaPos))

# pós: numpos == Num i em {1,..4}: num[i] > 0 and
#      somapos == Soma i em {1...4}: num[i] and num[i] > 0
# fim do módulo principal