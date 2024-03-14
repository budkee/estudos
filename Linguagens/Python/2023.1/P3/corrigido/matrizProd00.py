# Declare a função
def prodMatriz(m, n, a, b, c):

    for i in range(m):
        for j in range(n):
            c[i] = c[i] + (a[i][j] * b[j])

    return c


# Leia a dimensão da matriz
m, n = map(int, input().split())

# Estruture as listas de listas
a = [[0]*n for _ in range(m)]   # Matriz
b = [0]*n   # Vetor
c = [0]*m   # Produto

# Leia a matriz
for i in range(m):
    a[i] = list(map(int, input().split()))

# Leia o vetor
b = list(map(int, input().split()))

# Recolha o produto pela função
prod = prodMatriz(m, n, a, b, c)

# Imprima a função
print(prod)