# -*- coding: utf-8 -*-
# Programa: .py
# Programador: 
# Data: 07/05/2020
# Este programa lê um conjunto de alturas, conta-as calcula e
# imprime a média, e o número de alturas maiores ou iguais a média.
# A entrada é dada por uma lista de n números reais (alturas), uma
# em cada linha, e a ultima linha contém o número 0.0 que sinaliza
# o final da entrada. Use o append() para ler os elementos da lista.
# A saída consiste em imprimir a média e a quantidade de alturas
# que são maiores ou iguais a média. O valor da média das alturas
# deve ser impresso com duas casas decimais ({0:.2f}).
# início do módulo principal
# descrição das variáveis utilizadas
# list  alturas[]
# float media
# int   num, tam

# pré: alturas[0]..alturas[tam-1]

# Inicialize a lista e a soma da condição
lista = []
soma = 0

# Entre com a primeira altura, adicione na lista e acrescente o valor a soma da altura
altura = float(input())
lista.append(altura)
somaAlt = altura
# Leia as outras alturas, digitando 0 para sair
while altura > 0:
    altura = float(input())
    lista.append(altura)
    somaAlt += altura
# Compute a média das alturas
media = somaAlt / (len(lista)-1)
# Compute o número de alturas maiores ou iguais a média
for altura in lista:
    if altura >= media:
        soma += 1
# Imprima o resultado
print('{:.2f}'.format(media))
print('{}'.format(soma))


# pós: media and num
# fim do módulo principal
