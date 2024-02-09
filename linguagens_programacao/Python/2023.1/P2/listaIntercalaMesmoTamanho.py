# -*- coding: utf-8 -*- 
# Programa: intercala00.py
# Programador:
# Data: 25/01/2016
# Este programa lê duas listas a e b de inteiros, representando
# dois conjuntos, ambos com o mesmo número de elementos,
# computa a intercalação de a e b e imprime o resultado
# Intercalação de listas de mesmo tamanho.
# a == [1, 3, 5, 7, 9]
# b == [4, 2, 8, 6, 10]
# a intercalado com b
# c == [a[0],b[0],a[1],b[1],a[2],b[2],a[3],b[3],a[4],b[4]]
# nesse caso específico, as duas listas tem o mesmo tamanho
# c == [1,4,3,2,5,8,7,6,9,10]
# início do módulo principal
# descrição das variáveis utilizadas
# list a, b, c
# int tam

# pré: tam a[0]..a[tam-1] b[0]..b[tam-1]

# Passo 1. Leia as listas a e b e inicialize a lista c
# Passo 1.1. Leia o tamanho das listas
tam = int(input())
# Passo 1.2. Leia a lista a
a = list(map(int, input().split()))[:tam]
# Passo 1.3. Leia a lista b
b = list(map(int, input().split()))[:tam]
# Passo 1.4. Inicalize a lista c
c = [0]*2*tam
# Passo 2. Intercale as listas
for i in range (0,tam): 
   c[2*i] = a[i] 
   c[2*i+1] = b[i]
""" Ou
# Passo 2. Intercale as listas
c = [] 
for i in range (0,tam): 
   c.append(a[i]) 
   c.append(b[i])
"""

""" Ou 
# Passo 2. Intercale as listas
c = [c[i] for i in range(tam) for c in [a,b]] 

"""

""" Ou
# Passo 2. Intercale os vetores
c = [0]*2*tam 
c[::2] = a 
c[1::2] = b
"""
# Passo 3. Imprima a lista intercalada
print(c)

# pós: c == [a[0], b[0],..,a[tam-1], b[tam-1]
# fim do módulo principal