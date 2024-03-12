# -*- coding: utf-8 -*-
# Programa: soma1.py
# Programador: Camila de Oliveira Budke
# Data: 11/03/2023
# Este programa lê três números inteiros calcula a soma dos três números e imprime os resultados. 
# Declaração das biliotecas utilizadas

# pré: numero1, numero2, numero3

# Passo 1. Leia os três números inteiros
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
# Passo 2. Calcule a soma
soma = n1 + n2 + n3
# Passo 3. Imprima a soma
print('{0:d} + {1:d} + {2:d} = {3:d}'.format(n1, n2, n3, soma))
# pós: soma == numero1 + numero2 = numero3
# fim