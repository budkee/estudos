def multiplicar_matrizes(A, B):
    # Verifica se o número de colunas de A é igual ao número de linhas de B
    if len(A[0]) != len(B):
        print('Produto não definido')
        return

    # Inicializa a matriz produto C com zeros
    m = len(A)
    p = len(B[0])
    C = [[0] * p for _ in range(m)]

    # Calcula o produto das matrizes
    for i in range(m):
        for j in range(p):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]

    # Retorna a matriz produto C
    return C

# Leitura da matriz A
m, n = map(int, input().split())
A = []
for _ in range(m):
    linha = list(map(int, input().split()))
    A.append(linha)

# Leitura da matriz B
r, s = map(int, input().split())
B = []
for _ in range(r):
    linha = list(map(int, input().split()))
    B.append(linha)

# Calcula o produto das matrizes A e B
C = multiplicar_matrizes(A, B)

# Imprime a matriz produto C ou a mensagem 'Produto não definido'
if C:
    for linha in C:
        print(' '.join(map(str, linha)))
