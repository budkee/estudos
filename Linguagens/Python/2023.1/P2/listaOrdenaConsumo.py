# -*- coding: utf-8 -*-
# Programa: consumo2.py
# Programador:
# Data: 25/05/2020
# Este programa um inteiro tam e tam blocos de linhas, cada
# representando a identificação, a quantidade de quilômetros 
# viajados e a quantidade de litros de combustível utilizado, 
# respectivamente, pelos veículos de uma frota. O programa 
# calcula quantidade de quilômetros por litro de combustível 
# para cada veículo. Após o cálculo da média, o programa ordena 
# os veículos pela média de consumo de combustível e imprime 
# uma tabela ordenada com os veículos e as respectivas médias.
# início do módulo principal
# descrição das variáveis utilizadas
# list veiculos, veiculosn 
# list kms
# list consumos, medias
# float menor
# int tam, menorPos, aux

# pré: veiculos[0] kms[0] consumos[0] veiculos[1] kms[1]
#      consumos[1] ... veiculos[tam-1] kms[tam-1] consumos[tam-1]

# Passo 1. Leia a tabela
# Passo 1.1. Leia o tamanho da frota
tam = int(input())
# Passo 1.2. Inicialize as lista
veiculos = [0]*tam 
kms = [0]*tam 
consumos = [0.0]*tam 
medias = [0.0]*tam 
# Passo 1.3. Leia a identificação, quilometragem e consumo
for i in range(0,tam): 
# Passo 1.3.1. Leia a identificação do veículo
   veiculos[i] = int(input()) 
# Passo 1.3.2. Leia a quilometragem
   kms[i] = int(input()) 
# Passo 1.3.3. Leia o consumo
   consumos[i] = float(input()) 
# Passo 2. Calcule o consumo médio dos veículos
   for i in range(0,tam): 
      medias[i] = kms[i]/consumos[i] 
# Passo 3. Monte a tabela ordenada
# Passo 3.1. Faça uma cópia da lista veiculos
veiculosn = veiculos.copy() 
# Passo 3.2. Ordene a listas medias e veículosn
for i in range(0,tam-1): 
# Passo 3.2.1. Compute o menor elem em media[i]..media[tam-2]
   menor = min(medias[i:]) 
   menorPos = medias[i:].index(menor)
# Passo 3.2.2. Trocar o menor com media[i] no iníc. da sublista
   medias[i + menorPos] = medias[i] 
   medias[i] = menor
# Passo 3.1.3. Trocar a posição do veículo correspondente
   aux = veiculosn[i] 
   veiculosn[i] = veiculosn[i+menorPos]
   veiculosn[i+menorPos] = aux 
# Passo 4. Imprima os resultados
for i in range(0,tam): 
    print('{0:d} {1:5.2f}'.format(veiculosn[i], medias[i]))

""" 
Gere um arquivo para entrada e outro para saida:
$ python consumo2.py < consumo2.in > consumo2.out 
E depois compare pelo terminal:
$ diff consumo.out consumo.sol
"""
# pós: para i em {0..tam-1}:veiculosn[i] media[i] and
#      media[i] == kms[i]/consumos[i] and
#      para i em {0,...,tam-2}:media[i] <= media[i+1]
# fim do módulo principal