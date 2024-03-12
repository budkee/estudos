# Programa: permutacao.py
# Programador:
# Data:

# Este programa lê uma matrize de tamanho n x n, e imprime 1 caso a
# matriz seja de permutação e 0 caso contrário.

# início do módulo principal

# descrição das variáveis utilizadas
# list mat[[]]
# int n, linha, coluna, i
# str msg
# bool permutacao

# pré: n mat

# Passo 1. Leia a matriz de entrada
# Passo 1.1. Leia as dimensões da matriz
n = int(input())

# Passo 1.2. Inicialize a estrutura de dados
mat = [[0] * n for _ in range(n)]

# Passo 1.3. Leia os elementos da matriz (linha a linha)
for i in range(n):
    mat[i] = list(map(int, input().split()))
    # ou
    mat[i] = [int(num) for num in input().split()]

# Passo 2. Verifique se a matriz é de permutação
# Passo 2.1. Inicialize as variáveis
permutacao = True
msg = 'P'
i = 0
# Passo 2.2. Verifique as linhas e colunas da matriz
while i < n and permutacao:
    for i in range(n):
        linha = 0  # contar o número de 1´s nas linhas
        coluna = 0  # contar o número de 1´s nas colunas
        # Passo 2.2.1. Para linha i coluna j faça
        for j in range(n):
            # Passo 2.2.1.1 Verifique os elementos da linha i
            if mat[i][j] != 0 and mat[i][j] != 1:
                linha = 2  # tem um número diferente de 0 ou 1 na linha
            elif mat[i][j] == 1:
                linha = linha + 1
            # Passo 2.2.1.2. Verifique os elementos da coluna j
            if mat[j][i] != 0 and mat[j][i] != 1:
                coluna = 2  # tem um número diferente de 0 ou 1 na coluna
            elif mat[j][i] == 1:
                coluna = coluna + 1
        # Passo 2.2.2. Verifique as condições de matriz de permutação
        if linha == 0 or linha > 1 or coluna == 0 or coluna > 1:
            permutacao = False
            msg = 'N'
        i += 1  # testar a próxima linha

# Passo 3. Imprime o resultado
print(msg)

# pós: 'P' and para cada i em {0..m-1} e j em {0..n-1}:
#      soma(mat[i][j])==1 and soma(mat[j][i])==1 or 'N'
# fim do módulo principal
