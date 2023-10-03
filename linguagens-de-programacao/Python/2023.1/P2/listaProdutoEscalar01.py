# Qual o valor que será impresso pelo print ?
numero = [0]*100
print(numero)
for i in range(0,6):
   numero[i] = i * i
for i in range(6,10):
   numero[i] = numero[i-5]
# Imprima
print(numero[i])