# -*- coding: utf-8 -*-
# Programa: bois01.py
# Programador:
# Data: 27/10/2020
# Este programa lê um conjunto de dados referentes ao número de
# identificação e o peso dos bois em um frigorífico. O número de
# identificação igual a zero é usado com flag para sinalizar o
# final da entrada. O programa calcula a média dos pesos e o
# peso do boi mais gordo e o peso do boi mais magro, e quantos
# bois obtiveram esses pesos.
# início do módulo principal
# descrição das variáveis utilizadas
# list numeros, pesos
# int   numero     - número de identificação do boi
#       numbois    - número de bois
#       gordo      - número do boi mais gordo
#       magro      - número do boi mais magro
# float peso       - peso do boi
#       maiorPeso  - peso do maior boi
#       menorPeso  - peso do menor boi
#       soma       - soma dos pesos dos bois
#       media      - media dos pesos  

# pré: numeros[0] pesos[0]...numeros[numbois-1]
#      pesos[numbois-1]

# Passo 1. Inicialize as variáveis e leia a entrada
# Passo 1.1. Inicialize as variáveis
maiorPeso = 0.0
menorPeso = 5000.0
soma = 0.0
numbois = 0
numgordo = 0
nummagro = 0
numeros = []
pesos = []
# Passo 1.2. Leia o número e o peso do primeiro boi
numero = int(input())
# Passo 1.3. Enquanto numero > 0 faça
j = 0
while numero > 0:
# Passo 1.3.1. Adicione numero a lista das identificações
    numeros.append(numero)
# Passo 1.3.2. Adicione e leia o peso do boi
    pesos.append(float(input()))
# Passo 1.3.3. Conte o número dos bois
    numbois += 1
# Passo 1.3.4. Leia o número do boi
    numero = int(input())
# Passo 2. Calcule o maior e o menor peso e a soma dos pesos
# Passo 2.1. Para i em [1,numbois] faça
#print(f'Pesos = {pesos}\n')
for i in range(0, numbois):
# Passo 2.2. Calcule o maiorPeso e conte o num de bois com maiorPeso
    #print(f'Índice | Menor Peso | Peso      | Nº de Magros')
    #print(f'i = {i}| {menorPeso}| {pesos[i]}| {nummagro}')
    if pesos[i] > maiorPeso:
# Passo 2.2.1. maiorPeso recebe Peso
        maiorPeso = pesos[i]
# Passo 2.2.3. senão se pesos[i] == maiorPeso incremente numgordo
    elif pesos[i] == maiorPeso:
        numgordo += 1
# Passo 2.3. Calcule o menor peso e conte num de bois com menorPeso
    if pesos[i] < menorPeso: 
# Passo 2.3.1. menorPeso recebe Peso
        menorPeso = pesos[i]
# Passo 2.3.3. senão se pesos[i] == menorPeso incremente nummagro
    elif pesos[i] == menorPeso:
        nummagro += 1
# Passo 2.4. Some os pesos dos bois
    numgordo = pesos.count(maiorPeso)
    nummagro = pesos.count(menorPeso)
soma = sum(pesos)
# Passo 3. Calcule a média
media = soma/numbois
# Passo 4. Imprima os resultados
# Passo 4.1. Imprima a média dos pesos dos bois
print('{0:.2f}'.format(media))
# Passo 4.2. Imprima o número de bois mais gordo e seu peso
print('{0:.2f}{1:5d}'.format(maiorPeso,numgordo))
# Passo 4.3. Imprima o número de bois mais gordo e seu peso
print('{0:.2f}{1:5d}'.format(menorPeso,nummagro))

# pós: soma == Soma i em {0..n-1}:peso[i] and media ==
#      soma/numbois and maiorPeso == max{peso[0]..peso[i-1]} and
#      numgordo == Num i em {0..n-1}:peso[i] == maiorPeso and
#      menorPeso == min{peso[0]..peso[i-1]} and
#      nummagro == Num i em {0..n-1}:peso[i] == menorPeso
# fim do módulo principal
