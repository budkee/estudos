# -*- coding: utf-8 -*- 
# Programa: bois06.py
# Programador:
# Data: 21/06/2022  
# Este programa lê um conjunto de números e pesos de um lote bois, 
# calcula a média dos pesos dos bois, determina o conjunto de bois
# com pesos maiores que a média e ordena esse conjunto em ordem 
# crescente.
# inicio do módulo principal  
# descrição as variáveis utilizadas
# list numeros, pesos, numgordos, gordos
# float media
# int tam

# pré: tam numeros[0] pesos[0] .. numeros[tam-1] pesos[tam-1]

# Passo 1. Leia as listas dos pesos
# Passo 1.1. Leia o tamanho da lista
tam = int(input())
# Passo 1.2. Leia os tam elementos das listas
for i in range(0,tam):
# Passo 1.2.1. Leia o número do i-ésimo boi
    numeros.append(int(input()))
# Passo 1.2.2. Leia o peso do i-ésimo boi
    pesos.append(float(input()))

# Passo 2. Compute as listas de bois com pesos maiores que a média
# Passo 2.1. Compute a média dos pesos
soma = 0.0
for i in range(0,tam):
   soma += pesos[i]
media = soma/tam
# Passo 2.2. Selecione os bois com pesos acima da média
# Passo 2.2.1. Inicialize as listas dos bois com pesos acima da média
numgordos = [] # números dos bois "gordos"
gordos = [] # pesos dos bois gordos
# Passo 2.2.2. Percorra a lista dos pesos dos bois
for i in range(0,tam):
# Passo 2.2.2.1. Verifique se o peso i-ésimo boi é maior que a média
    if pesos[i] > media:
        numgordos.append(numeros[i]) # adicione o número do boi i
        gordos.append(pesos[i]) # adicione o peso do boi i
# Passo 2.3. Ordene a lista dos bois gordos 
gordos.sort()
# Passo 2.4. Obtenha os índices da ordenação
indices = sorted(range(len(gordos)), key=lambda k:gordos[k])
# Passo 2.5. Use os índices para ordenar a lista dos números dos bois gordos
numgordos = [numgordos[i] for i in indices]   
# Passo 3. Imprima as listas ordenadas dos bois gordos
print(numgordos)
print(gordos) 

# pós: numgordos gordos and gordos[i] > media and gordo[i] <= gordo[i+1]
# fim do módulo principal