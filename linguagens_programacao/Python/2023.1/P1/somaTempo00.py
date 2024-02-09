# Programa: tempodecorrido01.py
# Programador:
# Data: 22/09/2010
# Este algoritmo lê duas medidas de tempo em horas, minutos e segundos, onde onde minutos e segundos são valores no intervalo [0, 59] e computa a soma das medidas em horas, minutos e segundos, de tal forma que os valores de minutos e segundos permaneçam no intervalo [0, 59] e imprime o resultado

# início do módulo principal
# descrição das variáveis utilizadas
# int horas1, minutos1, segundos1, horas2, minutos2, segundos2
# int minutos, horas, tothoras, totminutos, totsegundos
# pré: horas1 minutos1 segundos1 horas2 minutos2 segundos2
# Passo 1. Leia as medidas em horas, minutos e segundos
# Passo 1.1. Leia a medidas 1 em horas, minutos e segundos
print('Entre com as horas, minutos e segundos da primeira leitura: ')
horas1, minutos1, segundos1 = map(int, input().split())
# Passo 1.2. Leia a medidas 2 em horas, minutos e segundos
print('Entre com as horas, minutos e segundos da segunda leitura: ')
horas2, minutos2, segundos2 = map(int, input().split())
# Passo 2. Calcule a soma das medidas
# Passo 2.1. Calcule o total de segundos
totsegundos = (segundos1 + segundos2) % 60
# Passo 2.2. Calcule o total de minutos
minutos = (segundos1 + segundos2) // 60
totminutos = ((minutos1+minutos2) + minutos)%60
# Passo 2.3. Calcule o total de horas
horas = (minutos1+minutos2 + minutos)//60
tothoras = horas1 + horas2 + horas
# Passo 3. Imprima a somas das medidas
print('{0:2d} horas {1:2d} minutos {2:2d} segundos +'.format(horas1, minutos1, segundos1))
print('{0:2d} horas {1:2d} minutos {2:2d} segundos ='.format(horas2, minutos2, segundos2))
print('{0:2d} horas {1:2d} minutos {2:2d} segundos'.format(tothoras, totminutos, totsegundos))
# pós: tothoras == (horas1 + horas2 + (minutos1 + minutos2 + (segundos1 + segundos2)//60)//60 and totminutos == (minutos1 + minutos2 +(segundos1 + segundos2)%60 and totsegundos == (segundos1 + segundos2)%60

# fim do módulo principal