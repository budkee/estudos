# Receba o número de m e n
m, n = list(map(int, input().split()))

# Crie 2 matrizes com (intervalo de) [m linhas, n colunas]:

a = [[0] * n for i in range(m)]
b = [[0] * n for i in range(m)]
soma = [[0] * n for i in range(m)]

# Leia os números

# Para cada m linhas, leia as n colunas
for i in range(0, m-1):
    for j in range(0, n-1):
        a[i][j] = list(map(int, input().split()))
        b[i][j] = list(map(int, input().split()))

# Para cada m linhas, some cada elemento, a[i][j], com, b[i][j], e armazene em soma[i][j]
for i in range(0, m-1):
    for j in range(0, n-1):
        soma[i][j] = a[i][j] + b[i][j]

# Imprima o resultado da soma
print(soma)