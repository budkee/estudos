# Leia duas matrizes e imprima a soma de ambas utilizando função
# Função
def somaMatriz(m, n, a, b, c):

    for i in range(m):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]

    return c


# Leia o número de linhas e colunas
m, n = map(int, input().split())
# Estruture as listas
a = [[0]*n for _ in range(m)]
b = [[0]*n for _ in range(m)]
c = [[0]*n for _ in range(m)]
# Leia a entrada
for i in range(m):
    a[i] = list(map(int, input(f'Insira a {i + 1}ª linha da matriz A: ').split()))

for i in range(m):
    b[i] = list(map(int, input(f'Insira a {i + 1}ª linha da matriz B: ').split()))

# Retire a soma
soma = somaMatriz(m, n, a, b, c)
# Imprima a lista
print(soma)