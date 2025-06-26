# Programa: matrizIndustriaAlimenticia00.py
# Programador:
# Data:

# Este programa lê os valores da produção dos itens de duas
# unidades fabris para quatro períodos. O programa calcula e
# imprime a produção total de cada um dos itens produzidos
# pelas fábricas.

# início do módulo principal

# descrição das variáveis utilizadas
# list tl, cx, mc - lista das listas da produção
# int lin, col - dimensão das listas

# pré: tl[0][0]..tl[2][3] cx[0][0]..cx[2][3]

# Passo 1.Inicialize as estruturas e leia a entrada
# Passo 1.1. Leia as dimensões das listas
lin, col = map(int, input().split())
# Passo 1.2. Inicialize as estruturas de dados
tl = [[0]*col for i in range(lin)]
cx = [[0]*col for i in range(lin)]
mc = [[0] * col for i in range(lin)]  # produção total
# Passo 1.3. Leia a produção de Três Lagoas (linha a linha)
for i in range(0, lin):
    tl[i] = list(map(int, input().split()))  # leia a linha i
# Passo 1.4. Leia a produção de Coxim (linha a linha)
for i in range(0, lin):
    cx[i] = list(map(int, input().split()))  # leia a linha i
# Passo 2. Calcule a produção total da indústria - soma das listas
for i in range(lin):  # fixa linha i
    for j in range(col):  # percorre as colunas da linha i
        mc[i][j] = tl[i][j] + cx[i][j]  # soma dos elementos da linha ij
# Passo 3. Imprima a produção total linha a linha
for i in range(lin):
    print(mc[i])

# pós: mc and mc[i][i] == tl[i][j]+cx[i][j]
# fim do módulo principal
