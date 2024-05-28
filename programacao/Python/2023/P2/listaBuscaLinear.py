# -*- coding: utf-8 -*- 
# Programa: buscapreco.py
# Programador:
# Data: 30/03/2016
# Este programa lê uma lista numero de tam inteiros representando
# os produtos de um depósito, e um inteiro num representando um
# dado produto. O programa faz uma busca para verificar se num está
# na lista numero. A busca é feita por meio da comparação de cada
# um dos 0 <= i < tam, numero[i] com num. Caso num pertença a
# numero, o programa retorna o preco[pos], caso contrário retorna
# uma informação de que num não pertence a numero.
# início do módulo principal
# descrição das variáveis utilizadas
# list numeros, precos
# int tam, num
# bool encontrou

# pré: numeros[0] numeros[1] .. numeros[tam-1]
#      precos[0] precos[1] .. precos[tam-1] num

# Passo 1. Leia a entrada
# Passo 1.1. Leia a lista dos números
numeros = list(map(int,input().split()))
# Passo 1.2. Leia a lista dos precos
precos = list(map(float,input().split()))
# Passo 1.3. Leia o elemento a ser buscado
num = int(input())
# Passo 1.4. Compute o tamanho das lista
lam = len(numemeros)
# Passo 2. Procure o produto na lista numero
# Passo 2.1. Inicialize as variáveis da busca
i = 0 # posição inicial da busca
encontrou = False # num ainda não foi encontrado
msg = 'produto não existente' 
# Passo 2.2. Percorra a lista buscando o produto
while i < tam and not encontrou:
# Passo 2.2.1. Verifique se num está na posição i
   if num == numero[i]:
      encontrou = True # encontrou
      msg = '{0:d} {1:.2f}'.format(numero[i],preco[i]) 
   else: i = i + 1 # nova posição para busca
# Passo 3. Imprima o resultado
print(msg)

# pré: numero[i], preco[i] and existe i em {0,..,tam-1}:numero[i]
#      == num or produto inexistente
# fim do módulo principal