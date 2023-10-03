# Programa: somasconst.py
# Programador:
# Data:

# Este programa lê uma matriz quadrada e verifica se ela possui somas
# constantes. Ou seja, se a soma das linhas, colunas e diagonais
# principal e secundária tem o mesmo valor.

# início do módulo principal

# descrição das variáveis utilizadas
# list  matriz[[]] - lista das listas da produção
# int n - dimensão da matriz
# int soma - soma das linhas e colunas
# bool somaconst - variável booleana

# pré: n matriz[0][0]..matriz[lin][col]

# Passo 1. Crie a matriz e leia os elementos
# Passo 1.1. Leia as dimensões das matrizes
n = int(input())

# Passo 1.2. Inicialize a matriz
matriz = [[0] * n for i in range(n)]

# Passo 1.3. Leia a matriz linha a linha
for i in range(0, n):
    matriz[i] = list(map(int, input().split()))

# Passo 2. Verifique se a matriz possui somas constantes
# Passo 2.1. Inicialize as variáveis
somaconst = True
diagonal1 = 0
diagonal2 = 0

# Passo 2.2. Compute a soma das linhas e colunas de matriz
i = 0
while i < n and somaconst:

    # Passo 2.2.1. Inicialize a soma das linhas e colunas
    linha = 0
    coluna = 0

    # Passo 2.2.2. Compute a soma da linha i e coluna j
    for j in range(0, n):
        linha = linha + matriz[i][j]
        coluna = coluna + matriz[j][i]
    diagonal1 = diagonal1 + matriz[i][i]
    diagonal2 = diagonal2 + matriz[i][n - 1 - i]

    # Passo 2.2.3. Registre a primeira soma
    if i == 0:
        soma = linha

    # Passo 2.2.4. Verifique se a soma das linhas é igual a das colunas
    if soma != linha or soma != coluna:
        somaconst = False
    i = i + 1

# Passo 2.3. Verifique os elementos das diagonais
if somaconst and soma == diagonal1 and soma == diagonal2:
    msg = 'CONSTANTE'
else:
    msg = 'NÃO É CONSTANTE'

# Passo 3. Imprima o resultado
print(msg)

# pós: 'CONSTANTE' and matriz tem somas constantes or `'NÃO É CONSTANTE'
# fim do módulo principal
