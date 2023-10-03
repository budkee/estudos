# -*- coding: utf-8 -*-
# Programa: soma.py
# Programador: Camila de Oliveira Budke
# Data: 11/03/2023
# Este programa lê dois números inteiros calcula a soma dos dois números e imprime os resultados. 

# pré: numero1, numero2

# Passo 1. Leia os dois números
numero1 = int(input('Insira um número: '))
numero2 = int(input('Insira outro número: '))

# Passo 2. Calcule a soma
soma = numero1 + numero2

# Passo 3. Imprima a soma
print('{0:d} + {1:d} = {2:d}'.format(numero1, numero2, soma))
# pós: soma == numero1 + numero2
# fim
