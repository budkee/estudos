# Passo 1. Inicialize a lista de elementos com 0´s
numero = [0]*10 
# Passo 2. Calcule os valores de numero
for i in range(0,6):
   numero[i] = i * i
for i in range(6,10):
   numero[i] = numero[i-5]
# Passo 2. Imprima os valores de numero
for i in range(0,10):
   print('{0:d}'.format(numero[i]),end=' ')