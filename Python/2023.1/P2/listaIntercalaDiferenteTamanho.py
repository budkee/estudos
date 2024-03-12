# -*- coding: utf-8 -*-
# Programa: intercala02.py
# Programador:
# Data: 25/01/2016
# Este programa lê duas listas a e b de inteiros, computa a
# intercalação de a e b e imprime o resultado
# a == [1, 3, 5, 7, 9, 0, 11]
# b == [4, 2, 8, 6, 10]
# a intercalado com b
# c = [a[0],b[0],a[1],b[1],a[2],b[2],a[3],b[3],a[4],b[4],a[5],a[6]] 
# c = [1,4,3,2,5,8,7,6,9,10,0,11]
# início do módulo principal
# descrição das variáveis utilizadas
# list a, b, c
# int tam, tama, tamb

# pré: tama tam a[0] a[1] .. a[tama-1] b[0]..b[tamb-1]

# Passo 1. Leia as listas
# Passo 1.1. Leia a lista a
a = list(map(int, input().split()))
# Passo 1.2. Leia a lista b
b = list(map(int, input().split()))
# Passo 1.3. Compute os tamanhos das listas
tama = len(a) 
tamb = len(b) 
# Passo 2. Intercale as listas
# Passo 2.1. Inicialize a lista c
c = []
# Passo 2.2. Para cada elemento de a e b
for i in range(max(tama,tamb)): 
   if i < tama: # se tiver elemento em a para intercalar
      c.append(a[i]) 
   if i < tamb: # se tiver elemento em b para intercalar
      c.append(b[i])
# Passo 3. Imprima a lista intercalada
print(c)

# pós: c == [c[0],c[1]..,c[tama+tamb-1]] and 
#      para i em {0..min{tama,tamb}-1}:c[2*i]==a[i] and
#      c[2*i+1] == b[i] and para i em min{tama,tamb}.. 
#      max{tama,tamb}-1}:c[i] == {a[i] or b[i]}} 
# fim do módulo principal