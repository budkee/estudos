# Entre com o número de linhas e colunas de A
m, n = map(int, input().split())

# Lista da matriz A
a = [[0]*n for i in range(m)] # n colunas e m linhas

# Lista da matriz transposta de A
at = [[0]*m for i in range(n)] # m colunas e n linhas

# Leia a matriz A linha a linha
for i in range(m): # Linha fixa de a
    a[i] = list(map(int, input().split()))

# Compute a transposta de A (at)
for i in range(n): # Linha fixa de at
    for j in range(m): # Coluna variável de at
        at[i][j] = a[j][i]

# Imprima a matriz transposta (at) linha por linha
for i in range(n):
    print(at[i])
