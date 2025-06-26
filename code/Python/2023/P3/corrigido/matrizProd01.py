# Declare a função
def prodMatriz(m, s, a, b, c):
    for i in range(m):
        for j in range(s):
            c[i][j] = a[i][j] * b[i][j]

    return c


# Matriz A
## Leia a dimensão da matriz
m, n = map(int, input().split())

## Estruture a lista de listas
a = [[0] * n for _ in range(m)]  # Matriz A

## Leia a matriz
for i in range(m):
    a[i] = list(map(int, input().split()))

# Matriz B
## Leia a dimensão da matriz
r, s = map(int, input().split())

## Estruture a lista de listas
b = [[0] * s for _ in range(r)]  # Matriz B

## Leia a matriz
for i in range(r):
    b[i] = list(map(int, input().split()))

# Matriz C
c = [[0] * s for _ in range(m)]  # Produto
print(c)

# Se n = r, recolha o produto pela função
if n == r:
    # Imprima a função
    print(prodMatriz(m, s, a, b, c))
else:
    # Imprima uma mensagem
    print('Produto não definido.')
