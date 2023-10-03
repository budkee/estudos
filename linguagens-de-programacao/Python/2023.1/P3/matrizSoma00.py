# Crie 2 matrizes com (intervalo de) [m linhas, n colunas]:

# Receba o número de m e n
m, n = list(map(int, input().split()))

# Forma extensa:
#   Construa as linhas(m) de cada matriz
a = [0] * m # Matriz 1
b = [0] * m # Matriz 2

# Para cada linha(m) declarada, construa as n colunas
for i in range(0,n):
    a[i] = [0]*n    # Matriz 1
    b[i] = [1]*n    # Matriz 2

# Forma compacta:
#   Para cada elemento em m, construa n elementos de coluna

a = [[0] * n for i in range(m)]
b = [[0] * n for i in range(m)]
