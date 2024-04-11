# Leia o número de linhas e colunas
lin, col = map(int, input().split())

# Inicialize as estruturas de dados da matriz e da transposta
matriz = [[0] * col for _ in range(lin)]
transposta = [[0] * lin for _ in range(col)]

# Leia a matriz
for i in range(0, lin):
    matriz[i] = list(map(int, input().split()))

# Faça a transposição
for i in range(0, col):
    for j in range(0, lin):
        transposta[i][j] = matriz[j][i]

# Imprima a transposta
for i in range(0, col):
    print(transposta[i])