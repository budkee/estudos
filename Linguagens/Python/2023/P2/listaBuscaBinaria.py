# -*- coding: utf-8 -*-
# Programa: buscabinpreco.py
# Programador:
# Data: 30/03/2016
# Este programa lê uma lista numero de tam inteiros ordenados
# representando os produtos de um depósito, e um inteiro num
# representado um dado produto. O programa faz uma busca
# binária para verificar se num está na lista numero. A busca
# é feita por meio da comparação de num com numeros[i], onde
# i == (0 + tam-1)/2. Se num == numeros[i], o passo retorna
# o índice i, caso contrário, o passo verifica se num é
# maior ou menor que numeros[i]. Caso num seja menor, a
# sublista dos produtos numeros[i..tam-1] é descartada, caso
# contrário, a sublista numeros[0..i] é descartada. O mesmo 
# procedimento é aplicado na sublista restante, até que num seja 
# encoontrado, ou a sublista seja vazia e nesse caso imprima que 
# num é um produto inexistente
# início do módulo principal
# descrição das variáveis utilizadas
# list numeros. precos
# int tam, num, primeiro, ultimo, meio
# bool encontrou

# pré: tam numeros[0] numeros[1] .. numeros[tam-1]
#      precos[0] precos[1] .. precos[tam-1] num
#      and numeros[i] < numeros[i+1]

# Passo 1. Leia a entrada
# Passo 1.1. Leia a lista dos números
numeros = list(map(int,input().split()))
# Passo 1.2. Leia a lista dos precos
precos = list(map(float,input().split()))
# Passo 1.3. Leia o elemento a ser buscado
num = int(input())
# Passo 1.4. Compute o tamanho das listas
tam = len(numeros)
# Passo 2. Procure o produto na lista numeros
# Passo 2.1. Inicialize as variáveis da busca
primeiro = 0 # valor do limite esquerdo
ultimo = tam-1 # valor do limite direito
encontrou = False # num ainda não foi encontrado
msg = 'produto inexistente'
# Passo 2.2. Percorra a lista buscando o produto
while primeiro <= ultimo and not encontrou: 
# Passo 2.2.1. Calcule o ponto médio do intervalo
   meio = (primeiro + ultimo)//2 
# Passo 2.2.1. Verifique em que parte da lista num está
   if num > numeros[meio]: 
      primeiro = meio + 1 # verificar na parte superior
   elif num < numeros[meio]: 
      ultimo = meio - 1 # verificar na parte inferior
   else: 
      encontrou = True # achou, sair do while
      i = meio 
      msg = '{0:d} {1:.2f}'.format(numeros[i],precos[i]) 
# Passo 3. Imprima o resultado
print(msg) 

# pré: numeros[i], precos[i] and existe i em {0,..,tam-1}:numero[i]
#      == num or 'produto inexistente' 
# fim do módulo principal