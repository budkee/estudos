# Receba o número de m e n
m, n = map(int, input().split())

# Crie 2 matrizes com (intervalo de) [m linhas, n colunas]:

a = [[0] * n for i in range(m)]
b = [[0] * n for i in range(m)]
soma = [[0] * n for i in range(m)]

# Leia os números

for i in range(0, m):  # linha
    a[i] = list(map(int, input().split()))

for i in range(0, m):  # linha
    b[i] = list(map(int, input().split()))

# Para cada m linhas, some o elemento, a[i][j], com, b[i][j], e armazene em soma[i][j]
for i in range(0, m):
    for j in range(0, n):
        soma[i][j] = a[i][j] + b[i][j]

print(soma)
