# Programa: quadmagico.py
# Programador:
# Data:

# Este programa lê um valor inteiro ímpar n e constrói um
# quadrado mágico n x n. Uma matriz n x n é um quadrado
# magico se a soma das linhas, colunas e diagonais principal
# e secundária tem o mesmo valor.

# início do módulo principal

# descrição das variáveis utilizadas
# list quad[[]] - quadrado mágico
# int lin, col, num
# int templin, tempcol
# int dim - número ímpar

# pré: dim

# Passo 1.Inicialize as estruturas e leia a entrada
# Passo 1.1. Leia as dimensões das listas
dim = int(input())

# Passo 1.2. Inicialize as estruturas de dados
quad = [[0] * dim for i in range(dim)]  # quadrado mágico

# Passo 2 Gere o quadrado mágico de dimensão dim
# Passo 2.1. Coloque o primeiro elemento no quadrado
lin = 0
col = dim // 2
quad[lin][col] = 1
num = 2

# Passo 2.2. Coloque os demais elementos
while num <= dim * dim:

    # Passo 2.2.1. Movimente 1 linha para cima e 1 coluna para direita
    templin = lin - 1
    tempcol = col + 1

    # Passo 2.2.2. Se o movimento saiu na parte de cima na jth coluna
    if templin < 0:

        # Passo 2.2.2.1. vá para a ultima linha na coluna j
        templin = dim - 1

    # Passo 2.2.3. Se o movimento na parte direita da ith linha
    if tempcol > dim - 1:

        # Passo 2.2.3.1. Vá para a primeira coluna na linha i
        tempcol = 0

    # Passo 2.2.4. Se a posição não estiver ocupada
    if quad[templin][tempcol] == 0:
        lin = templin;
        col = tempcol

    # Passo 2.2.5. Caso contrário coloque número abaixo de número-1
    else:
        lin = lin + 1

        # Passo 2.2.5.1. se saiu do quadrado
        if lin > dim - 1:
            lin = 0

    # Passo 2.2.6. Coloque o elemento numero no quadrado
    quad[lin][col] = num

    # Passo 2.2.6. Gere próximo número
    num = num + 1

# Passo 3. Imprima o quadrado mágico
for i in range(dim):  # linhas
    for i in range(lin):
        print(''.join(f'\{j:3d\}' for j in quad[i]))

# pós: quad[i][j]
# fim do módulo principal