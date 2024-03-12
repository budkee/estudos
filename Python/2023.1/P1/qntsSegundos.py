# Programa: tempodecorrido.py
# Programador: Édson Cáceres
# Data: 21/03/2023

# Este algoritmo lê uma medida de tempo em segundos, calcula
# o valor equivalente em horas, minutos e segundos, onde minutos e
# segundos estão no intervalo [0, 59] e imprime o resultado.

# Formato da entrada: 9010

# Formato da saída: 9010 segundos = 2 Horas, 30 Minutos, 10 Segundos

# Início do módulo principal

# Descrição das variáveis utilizadas
# int totalsegundos, horas, minutos e segundos

# pré: totalsegundos

# Algoritmo: TempoDecorrido
# Passo 1. Leia o total de segundos
totalsegundos = int(input())
# Passo 2. Calcule as horas, minutos, segundos equivalentes
# Passo 2.1. Calcule os segundos equivalentes
segundos = totalsegundos % 60 # resto
# Passo 2.2. Calcule os minutos equivalentes
totalminutos = totalsegundos // 60 # quociente inteiro
minutos = totalminutos % 60
# Passo 2.3. Calcule as horas
horas = totalminutos // 60
# Passo 3. Imprima as horas, minutos e segundos
print('{} segundos = {} horas, {} minutos, {} segundos'.format(totalsegundos,horas,minutos,segundos))

# pós: horas == (totalsegundos//60)//60 and minutos == (totalsegundos//60)%60 and segundos == totalsegundos%60
# fim Algoritmo