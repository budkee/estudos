# -*- coding: utf-8 -*-
# Programa: variancia.py
# Programador:
# Data: 04/09/2010
# Este programa lê quatro notas de provas, calcula a média, a variância
# e o devio padrão das quatro provas.
# Declaração dos módulos utilizados
import math

# início do driver principal

# pré: prova1 prova2 prova3 prova4

# Passo 1. Leia as notas das provas.
prova1, prova2, prova3, prova4 = map(float, input().split())
provas = [prova1, prova2, prova3, prova4]
# Passo 2. Calcule a média, variância e desvio padrão
# Passo 2.1. Calcule a soma das notas das provas
somaprovas = prova1 + prova2 + prova3 + prova4
# Passo 2.2. Calcule a média das provas
mediaprovas = somaprovas / 4
# Passo 2.3. Calcule a soma dos quadrados das notas
somaquadrado = 0
for prova in provas:
    somaquadrado += prova ** 2 # somaquadrado = prova1 ** 2 + prova2 ** 2 + prova3 ** 2 + prova4 ** 2
# Passo 2.4. Calcule a variância
variancia = (somaquadrado / 4) - (((1 / 4) ** 2) * (somaprovas ** 2) )
# Passo 2.5. Calcule o desvio padrão
desviopadrao = math.sqrt(variancia)
# Passo 3. Imprima os resultados
print('Primeira Prova    {0:4.1f}'.format(prova1))
print('Segunda Prova     {0:4.1f}'.format(prova2))
print('Terceira Prova    {0:4.1f}'.format(prova3))
print('Quarta Prova      {0:4.1f}'.format(prova4))

print('Média das Provas {0:6.2f}'.format(mediaprovas))
print('Variância        {0:6.2f}'.format(variancia))
print('Desvio Padrão    {0:6.2f}'.format(desviopadrao))

# pós: media == Soma i em {1,2,3,4}: prova[i] && varianca ==
#      ((1/n)(Soma i em {1,2,3,4}: (prova[i])^2) -
#      (1/n^2)(Soma i em {1,2,3,4}: prova[i])^2)) &&
#      desviopadrao == math.sqrt(varianca)
# fim do driver principal
