# -*- coding: utf-8 -*-
# Programa: intercalaord03.py
# Programador:
# Data: 27/06/2018
# Este programa lê duas listas ordenadas a e b com tama e tamb
# elementos cada e calcula a lista c ordenada intercalando os
# elementos de a e b e imprime o resultado.
# início do módulo principal
# descrição das variáveis utilizadas
# list a, b, c
# int tama, tamb, tamc

# pré: tama, a, tamb, b

# Passo 1. Leia as listas a e b
# Passo 1.1. Leia a lista a
a = list(map(int, input().split()))
# Passo 1.2. Leia a lista b
b = list(map(int, input().split())) 
# Passo 1.3. Compute os tamanhos das listas
tama = len(a) 
tamb = len(b)
# Passo 2. Intercale as duas listas
# Passo 2.1. Inicialize a lista c
c = []
# Passo 2.2. Inicialize as variáveis índices
i, j = 0, 0
# Passo 2.3. Enquanto existirem elementos em ambas as listas
while i < tama and j < tamb:
# Passo 2.3.1. Se o menor elemento está em a
   if a[i] <= b[j]:
# Passo 2.3.1.1. Armazene o elemento de a em c
      c.append(a[i])
# Passo 2.3.1.2. Vá para o próximo elemento em a
      i = i + 1
# Passo 2.3.2. Se o menor elemento está em bM/span>
   else: 
# Passo 2.3.2.1. Armazene o elemento de b em c
      c.append(b[j])
# Passo 2.3.2.2. Vá para o próximo elemento em b
      j = j + 1
# Passo 2.4. Copie o restante da maior lista em c
c = c + a[i:] + b[j:]
# Passo 3. Imprima a lista c
print(c)

# pós: c = c[0]<=c[1]<=c[2]<= ... <=c[tamC-1] 
#      tamc = tama + tamb
# fim do módulo principal