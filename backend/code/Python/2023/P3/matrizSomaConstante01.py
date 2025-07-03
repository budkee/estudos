# 1. Leia as entradas e inicialize a estrutura de dados
# 1.1 Leia a dimensão da matriz
n = int(input())
# 1.2 Inicialize a estrutura da matriz
matriz = [[0] * n for _ in range(n)]
# 1.3 Leia os dados da matriz linha a linha
for i in range(0, n):
    matriz[i] = list(map(int, input().split()))

# 2. Verifique se a matriz é constante
# 2.1 Tome como verdadeiro a somaConst
somaConst = True
# 2.2 Inicialize as diagonais
somaDiagonal1 = 0
somaDiagonal2 = 0
# 2.3 Inicialize o while
i = 0
# 2.3.1 Enquanto i for menor que o número de linhas/colunas e a soma da constante for
# verdadeira:
while i < n and somaConst:

    # 2.1 Percorra a matriz
    for i in range(0, n):  # Fixa a linha/coluna
        # Inicialize a soma das linhas e das colunas
        somaLinha = 0
        somaColuna = 0

        for j in range(0, n):  # Percorre a coluna/linha
            somaLinha += matriz[i][j]
            somaColuna += matriz[j][i]

        somaDiagonal1 += matriz[i][i]
        somaDiagonal2 += matriz[n - 1 - i][i]

    # 2.2 Verifique se eles não possuem o mesmo resultado
    if somaLinha == somaColuna == somaDiagonal1 == somaDiagonal2:
        msg = 'CONSTANTE'
    else:
        msg = 'NÃO CONSTANTE'

# 3. Imprima o resultado
print(msg)
