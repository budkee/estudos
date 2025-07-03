# Programa: hardy.py
# Programador:
# Data:

# Este programa gera um conjunto de pares de cubos i^3 + j^3
# menores que 10000 e encontra o menor valor que pode ser escrito
# como soma de dois cubos. O programa usa uma matriz triangular
# inferior para armazenar os cubos

# início do módulo principal

# descrição das abstrações utilizadas
# list hardy[[]]
# int num, num1, num2, num3, num4
# int placa

# pré: hardy (vazia)

# Passo 1. Gere a matriz dos cubos
# Passo 1.1. Inicialize uma matriz 23 x 23
hardy = [[0]*23 for i in range(23)]
# Passo 1.2. Gere a matriz com a soma dos cubos
for i in range(23):
   for j in range(i+1): # matriz triangular
      hardy[i][j] = i*i*i + j*j*j
# Passo 2. Efetue a busca de dois cubos iguais na matriz
# Passo 2.1. Para cada número na matriz triangular repita
i = 0
while i < 23:
   j = 0
   while j <= i:
      num = hardy[i][j]
# Passo 2.1.1. Busque num na matriz
      k = 0
      while k < 23:
         l = 0
         while l <= k:
            if num == hardy[k][l] and k != i:
               num1 = i
               num2 = j
               num3 = k
               num4 = l;
               l = 25
               k = 25
               j = 25
               i = 25
            l += 1
         k += 1
      j += 1
   i += 1
# Passo 2.2. Compute o valor da placa
placa = num1 * num1 * num1 + (num2) * (num2) * (num2)
# Passo 3. Imprima os resultados (números e placa)
print(placa, num1, num2, num3, num4)

# pós placa == num1^3 + num2^3 == num3^3 + num4^4
# fim do módulo principal