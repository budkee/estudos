# Programa: cel2far.py
# Programador:
# Data: 16/05/97
# Este programa lê uma dada temperatura em Celsius e
# computa e imprime a temperatura equivalente em Fahreinheit.
# início do módulo principal
# descrição das variáveis utilizadas
# float tempC, tempF

# pré: tempC

# Passo 1. Leia a medida de temperatura em Fahreinheit
tempC = float(input(''))
# Passo 2. Calcule a temperatura equivalente em Celsius
tempF = (9/5)*tempC + 32
# Passo 3. Imprima os resultados
print('{0:5.1f} C = {1:5.1f} F.'.format(tempC, tempF))

# pós: tempF == 9.0/5.0 * tempC + 32
# fom do módulo principal