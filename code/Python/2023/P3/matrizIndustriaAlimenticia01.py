# Programa: matrizIndustriaAlimenticia01.py
# Programador:
# Data:

# Este programa lê uma tabela com os custos do transporte e a
# quantidade a ser transportada entre duas fábricas e os depósitos de
# uma dada indústria. O programa computa qual o menor custo do
# transporte e de qual fábrica será feito o transporte.

# início do módulo principal

# descrição das variáveis utilizadas
# list custos[[]] - lista de listas para representar os custos
# list quantidades[] - lista para representar a tabela de quantidades
# list total[] - lista para representar os custos totais
# float valor - valor mínimo do transporte
# str unidade - unidade de produção
# int lin, col - dimensões da tabela de custos

# pré: lin col custos[0][0] custos[0][1]..custos[lin-1][col-1]
#      quantidade[0]..quantidade[col-1]

# Passo 1. Inicialize as estruturas e leia os dados
# Passo 1.1. Leia as dimensões da tabela
lin, col = map(int, input().split())

# Passo 1.2. Inicialize a tabela de custos
custos = [[0.0] * col for i in range(lin)]  # lin linhas, col colunas

# Passo 1.3. Inicialize a lista das quantidades
precos = [0] * col  # col quantidades

# Passo 1.3. Inicialize a lista dos totais
total = [0.0] * lin  # lin fábricas

# Passo 1.4. Leia a tabela custos (linha a linha)
for i in range(0, lin):
    custos[i] = list(map(float, input().split()))  # leia a linha i de custos

# Passo 1.5. Leia a lista das quantidades
quantidades = list(map(int, input().split()))[:col]

# Passo 2. Compute o custo total
for i in range(lin):  # custo total transporte da fábrica i+1
    total[i] = 0.0
    for j in range(col):  # compute o valor das vendas do item j+1
        total[i] = total[i] + custos[i][j] * quantidades[j]

# Passo 2.2. Compute de que unidade fabril será feito o transporte
valor = min(total)  # computa o menor valor da lista
if total.index(valor) == 0:  # computa o índice do menor valor da lista
    msg = 'Três Lagoas'
else:
    msg = 'Coxim'

# Passo 3. Imprima o resultado
print(valor, msg)

# pós: valor == min{total[0],total[1]} and para i em {0,1} total[i] =
#      {0<= j < 4}: custos[i][j]*quantidades[j]
# fim do módulo principal