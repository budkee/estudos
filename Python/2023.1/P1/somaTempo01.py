# Programa elapsed01.py
# Programador:
# Data: 22/09/2010
# Este programa le duas medidas de tempo, dadas dias
# horas e minutos e segundos e efetua a soma dessas
# duas medidas e imprime o resulta da soma.
# início do múdulo principal principal
# descrição das variáveis utilizadas
# int h1, m1, s1, h2, m2, s2
# int totsegundos, minutos, totminutos
# int horas, tothoras

# pré: hh[1], mm[1], ss[1], hh[2], mm[2] ss[2]
#      and para i em {1,2}: 0 <= hh[i] < 24
#      and 0 <= mm[i] < 60 and
#      0 <= ss[i] < 60

# Passo 1. Leia a entrada
h1, m1, s1 = map(int, input().split())
h2, m2, s2 = map(int, input().split())
# Passo 2. Calcule a soma das horas, minutos e segundos
# Passo 2.1. Calcule a soma dos segundos
totsegundos = (s1 + s2) % 60
# Passo 2.2. Calcule a soma dos minutos
minutos = (s1 + s2) // 60                       # minutos relativos aos segundos
totminutos = ((m1+m2) + minutos)%60
# Passo 2.2. Calcule a soma das horas
horas = (m1+m2 + minutos)//60
tothoras = h1 + h2 + horas
# Passo 3. Imprima o resultado
print('{0:2d} Horas {1:2d} Minutos {2:2d} Segundos +'.format(h1, m1, s1))
print('{0:2d} Horas {1:2d} Minutos {2:2d} Segundos ='.format(h2, m2, s2))
print('{0:2d} Horas {1:2d} Minutos {2:2d} Segundos'.format(tothoras, totminutos, totsegundos))

# pós: horas = (m1 + m2 + minutos)//60 && tothoras == (h1 + h2 + horas)%60
#      and minutos = (s1+s2)//60 && totminutos == m1 + m2 + minutos)%60
#      and totsegundos == (s1 + s2)%60
# fim do módulo principal