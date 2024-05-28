# Receba o número de m e n
m, n = map(int, input('Digite o tamanho [m,n] das matrizes: ').split())

# Crie 2 matrizes com (intervalo de) [m linhas, n colunas]:
print('\nEspaços criados: \n')
a = [[0] * n for i in range(m)]
b = [[0] * n for i in range(m)]
soma = [[0] * n for i in range(m)]
# Os espaços
print(a, "+")
print(b, "=")
print("_" * 10)
print(soma)
# Leia os números
print('Matriz A')
for i in range(0, m):  # linha
    a[i] = list(map(int, input().split()))
print(a)
print('Matriz B')
for i in range(0, m):  # linha
    b[i] = list(map(int, input().split()))
print(b)
print('Soma')
# Para cada m linhas, some cada elemento, a[i][j], com, b[i][j], e armazene em soma[i][j]
for i in range(0, m):
    for j in range(0, n):
        soma[i][j] = a[i][j] + b[i][j]

print(a, "+")
print(b, "=")
print("_" * 10)
print(soma)
