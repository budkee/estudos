#!/usr/bin/python
# -*- coding: utf-8 -*-
# Programa elapsed02.py
# Programador:
# Data: 22/09/2010
# Este programa le duas horas decorridas, dadas em minutos e
# segundos e efetua a soma dessas duas medidas.

# início do driver principal

# pre: dd[1], hh[1], mm[1], dd[1], hh[2], mm[2] &&
#      para i em {1,2}: dd[i] em unsigned int && 0 <= hh[i] <=24
#      && 0 <= mm[i] <= 60

# Passo 1. Leia a entrada
d1, h1, m1, s1 = map(int, input().split())
d2, h2, m2, s2 = map(int, input().split())
# Passo 2. Calcule a soma das horas, minutos e segundos
# Passo 2.1. Calcule a soma dos segundos
totsegundos = (s1 + s2) % 60
# Passo 2.2. Calcule a soma dos minutos
minutos = (s1 + s2) // 60                     # minutos relativo aos segundos
totminutos = (m1 + m2 + minutos) % 60
# Passo 2.2. Calcule a soma das horas
horas = (m1 + m2 + minutos) // 60              # horas relativo aos minutos
tothoras = (h1 + h2 + horas) % 24
# Passo 2.3. Calcule a soma dos dias
dias = (h1 + h2 + horas) // 24                  # dias relativo às horas
totdias = d1 + d2 + dias
# Passo 3. Imprima o resultado
print('{0:2d} Dias {1:2d} Horas {2:2d} Minutos {3:2d} Segundos +'.format(d1, h1, m1, s1))
print('{0:2d} Dias {1:2d} Horas {2:2d} Minutos {3:2d} Segundos ='.format(d2, h2, m2, s2))
print('{0:2d} Dias {1:2d} Horas {2:2d} Minutos {3:2d} Segundos'.format(totdias, tothoras, totminutos, totsegundos))

# pós: totdias == d1+d2+dias && dias == (h1+h2+horas)//24 &&
#      horas = (m1 + m2 + minutos)//60 && tothoras == (h1 + h2 + horas)%24
#      && minutos = (s1+s2)//60 && totminutos == (m1 + m2 + minutos)%60
#      && totsegundos == (s1 + s2)%60