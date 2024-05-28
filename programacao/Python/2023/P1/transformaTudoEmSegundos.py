# Programa: transformaTudoEmSegundos.py
# Programador: Édson Cáceres
# Data: 17/05/2016

# Este programa lê uma medida de tempo, dada em horas, minutos e segundos e calcula seu equivalente em segundos.

# Formato da entrada: 3 34 45

# Formato da saída: 3 Horas + 34 Minutos + 45 Segundos = 12885 Segundos

# Início do módulo principal  

# Descrição das variáveis utilizadas
# int horas -> representa o valor da entrada em horas
# int minutos -> representa o valor da entrada em minutos
# int segundos -> representa o valor da entrada em segundos
# int totalDeSegundos -> representa o valor total em segundos

# pré: exi

# Passo 1. Leia a entrada
print('Entre com a quantidade de horas, minutos, segundos')
horas, minutos, segundos = map(int,input().split())
# Passo 2. Calcule o total de segundos
totalDeSegundos = 3600*horas + 60*minutos + segundos
# Passo 3. Imprima o total de segundos
print('{0:d} Horas + {1:d} Minutos + {2:d} Segundos = {3:d} Segundos'. \
              format(horas, minutos, segundos, totalDeSegundos))

# pós: totaldesegundos and totaldesegundos == horas*3600 + minutos*60 + segundos

# fim do módulo principal