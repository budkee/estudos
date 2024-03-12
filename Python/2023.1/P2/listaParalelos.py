# -*- coding: utf-8 -*-
# Programa: listaParalelos.py
# Programador: siriub
# Data: 16/05/23
# Este programa lê dois vetores e verifica se os vetores são paralelos.
# O programa imprime sim em caso afirmativo e nao cao contrário.
# início do módulo principal
# descrição das variáveis utilizadas
# list a, b
# float coef
# str msg
   
# pré: a b

# Passo 1. Leia os vetores
# Passo 1.1. Leia o vetor a
a = list(map(float, input().split()))
# Passo 1.1. Leia o vetor b
b = list(map(float, input().split()))
# Passo 2. Verifique se os vetores são paralelos
# Passo 2.1. Calcule o coeficiente
coef = b[0] / a[0]
# Passo 2.2. Incialize a mensagem
msg = ''
# Passo 2.2 Compare o coeficiene com os demais elementos e 
i = 0 
while i <= len(a)-1:
    dif = coef*a[i] - b[i] 
    if abs(dif) < 0.000001:
        msg = 'sim'
    else:
        msg = 'não'
    i += 1
# Passo 3. Imprima o resultado          
print(msg)

# pós:
# fim do módulo principal