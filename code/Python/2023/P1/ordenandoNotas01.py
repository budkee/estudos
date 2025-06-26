# Programa: ordenanotas01.py
# Programador:
# Data: 22/09/2016
# Este programa lê uma lista com quatro números inteiros distintos,
# ordena a lista em ordem crescente e imprime o resultado.
# início do módulo principal
# descrição das variáveis utilizadas
# float num1, num2, num3, num4, aux
# pré: [num1, num2, num3, num4]
# Passo 1. Leia os números
num1,num2,num3,num4 = map(int, input().split())
# Passo 2. Ordene os números num1, num2, num3, num4
# Passo 2.1. Calcule o menor valor de num1,num2,num3,num4 e troque com num1
if num2 < num1:
   aux = num1
   num1 = num2
   num2 = aux
if num3 < num1:
   aux = num1
   num1 = num3
   num3 = aux
if num4 < num1:
   aux = num1
   num1 = num4
   num4 = aux
# Passo 2.2. Calcule o menor valor de num2,num3,num4 e troque com num2
if num3 < num2:
   aux = num2
   num2 = num3
   num3 = aux
if num4 < num2:
   aux = num2
   num2 = num4
   num4 = aux
# Passo 2.3. Calcule o menor valor de num3,num4 e troque com num3
if num4 < num3:
   aux = num3
   num3 = num4
   num4 = aux
# Passo 3. Imprima os números ordenados
print(num1, num2, num3, num4)
# pós: para i = {0,1,2}:num[i] | num[i] < num[i+1]
# fim do módulo principal