# -*- coding: utf-8 -*-
# Programa: bois02.py
# Programador:
# Data: 24/02/2016
# Este programa lê um conjunto de dados referentes ao número
# de identificação e o peso dos bois em uma fazenda. O programa calcula e
# imprime o maior e o segundo maior peso, o menor e o segundo menor peso
# com os números dos bois e a média do peso dos bois.
# início do módulo principal
# descrição das variáveis utilizadas
# list numeros, pesos
# int numbois - número de bois
# gordo1 - número do boi mais gordo
# gordo2 - número do segundo boi mais gordo
# magro1 - número do boi mais magro
# magro2 - número do segundo boi mais magro
# float maiorPeso1 - peso do boi mais gordo
# maiorpeso2 - peso do segundo boi mais gordo
# menorPeso1 - peso do boi mais magro
# menorpeso2 - peso do segundo boi mais magro
# soma - soma dos pesos dos bois
# media - media dos pesos

# pré: numbois numero[0] peso[0] numero[1] peso[1] ...
#      numero[numbois-1] peso[numbois-1]

# Passo 1. Leia a entrada e inicialize as variáveis
# Passo 1.1. Leia o número de bois
print('Leia o número do bois: ') 
numbois = int(input())
# Passo 1.2. Inicialize as variáveis
maiorPeso1 = 0.0 
maiorPeso2 = 0.0 
menorPeso1 = 5000.0 
maiorPeso2 = 5000.0 
gordo1 = 0 
gordo2 = 0 
magro1 = 0 
magro2 = 0 
soma = 0.0 
numeros = [] 
pesos = []
# Passo 1.2. Repita numbois vezes
for i in range(0,numbois):
# Passo 1.2.1. Leia o número do i-ésimo boi
   numeros.append(int(input()))
# Passo 1.2.2. Leia o peso do i-ésimo boi}
   pesos.append(float(input()))
# Passo 2. Compute os números e pesos dos dois bois com maior e menor peso
for i in range(0,numbois):
# Passo 2.1. Se peso do boi i for maior que o peso do boi mais gordo
   if pesos[i] > maiorPeso1:
# Passo 2.1.1. Troque o maior peso e número anterior com segundo maior peso
      maiorPeso2 = maiorPeso1 
      gordo2 = gordo1
# Passo 2.1.2. Boi mais gordo recebe o peso e número do boi i
      maiorPeso1 = pesos[i] 
      gordo1 = numeros[i]
# Passo 2.2. Senão se peso do boi i > que o segundo boi mais gordo
   elif pesos[i] > maiorPeso2:
# Passo 2.4.1. segundo boi mais gordo recebe peso e número do boi i
      maiorPeso2 = pesos[i] 
      gordo2 = numeros[i]
# Passo 2.3. Se peso do boi i for menor que o peso do boi mais magro
   if pesos[i] < menorPeso1:
# Passo 2.3.1. Troque o menor peso anterior com segundo menor peso
      menorPeso2 = menorPeso1 
      magro2 = magro1
# Passo 2.3.2. Boi mais magro recebe o peso do boi i
      menorPeso1 = pesos[i] 
      magro1 = numeros[i]
# Passo 2.4. Senão se peso do boi i for < que o segundo boi mais magro
   elif pesos[i] < menorPeso2:
# Passo 2.4.1. segundo boi mais gordo recebe peso do boi i
      menorPeso2 = pesos[i] 
      magro2 = numeros[i]
# Passo 2.5. Some o peso dp boi i
   soma = soma + pesos[i]
# Passo 3. Calcule a média dos pesos dos bois
media = soma/numbois
# Passo 4. Imprima os resultados
# Passo 4.1. Imprima a média dos pesos dos bois
print('Média dos pesos de ', end='') 
print('{0:d} bois = {1:7.2f} Kg'.format(numbois, media))
# Passo 4.2 Imprima o número do boi mais gordo e seu peso
print('Boi mais gordo 1 = ', end='') 
print('{0:d} - Peso = {1:7.2f} Kg'.format(gordo1,maiorPeso1))
# Passo 4.3. Imprima o número do segundo boi mais gordo e seu peso
print('Boi mais gordo 2 = ', end = '') 
print('{0:d} - Peso = {1:7.2f} Kg'.format(gordo2,maiorPeso2))
# Passo 4.4 Imprima o número do boi mais magro e seu peso
print('Boi mais magro 1 = ', end = '') 
print('{0:d} - Peso = {1:7.2f} Kg'.format(magro1,menorPeso1))
# Passo 4.5 Imprima o número do segundo boi mais magro e seu peso}
print('Boi mais magro 2 = ', end = '') 
print('{0:d} - Peso = {1:7.2f} Kg'.format(magro2,menorPeso2))

""" Ou
# Passo 4. Imprima os resultados
# Passo 4.1. Imprima a média dos pesos dos bois
print('Média dos pesos de ', end='') 
print('{0:d} bois = {1:7.2f} Kg'.format(numbois, media))
# Passo 4.2 Imprima o número do boi mais gordo e seu peso
print('Boi mais gordo 1 = ', end='') 
print('{0:d} - Peso = {1:7.2f} Kg'.format(gordo1,maiorPeso1)) 
# Passo 4.3. Imprima o número do segundo boi mais gordo e seu peso
print('Boi mais gordo 2 = ', end='') 
print('{0:d} - Peso = {1:7.2f} Kg'.format(gordo2,maiorPeso2))
# Passo 4.4 Imprima o número do boi mais magro e seu peso
print('Boi mais magro 1 = ', end='') 
print('{0:d} - Peso = {1:7.2f} Kg'.format(magro1,menorPeso1))
# Passo 4.5 Imprima o número do segundo boi mais magro e seu peso
print('Boi mais magro 2 = ', end='') 
print('{0:d} - Peso = {1:7.2f} Kg'.format(magro2,menorPeso2))
"""

# pós: media == soma/numbois and soma == Soma i em {0..numbois-1}:peso[i]
#      and maiorPeso1 == peso[j] and maiorPeso2 == peso[k] and
#      para i em {0..numbois-1}:peso[j] >= peso[k] >= peso[i]
#      and gordo1 == numero[j] and gordo2 == numero[k] and
#      menorPeso1 == peso[l] and menorPeso2 == peso[r] and
#      para i em {1..numbois-1}:peso[l] =< peso[r] =< peso[i]
#      and magro1 == numero[l] and magro2 == numero[r]
# fim do módulo principal