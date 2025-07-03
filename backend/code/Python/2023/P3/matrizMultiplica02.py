# Programa: vendas.py
# Programador:
# Data:

# Este programa lê uma tabela com as vendas semanais de uma
# uma empresa feitas por um conjunto de vendedores e os preços dos
# produtos comercializados. O programa computa e imprime o total
# vendido por cada vendedor.

# início do módulo principal

# descrição das variáveis utilizadas
# list vendas[[]] - lista de listas para representar as vendas
# list precos[] - lista para representar a tabela de preços
# list total[] - lista para representar as vendas totais
# int lin, col - dimensões da tabela de vendas

# pré: lin col vendas[0][0] vendas[0][1]..vendas[lin-1][col-1]
#      preco[0]..preco[5]

# Passo 1. Inicialize as estruturas e leia os dados
# Passo 1.1. Leia as dimensões da tabela
lin, col = map(int, input().split())

# Passo 1.2. Inicialize a tabela de vendas
vendas = [[0] * col for i in range(lin)]  # lin linhas, col colunas

# Passo 1.3. Inicialize a lista de preços
precos = [0.0] * col  # col preços

# Passo 1.4. Inicialize a lista dos totais
total = [0] * lin  # lin vendedores

# Passo 1.5. Leia a tabela vendas (linha a linha)
for i in range(0, lin):
    vendas[i] = list(map(int, input().split()))  # leia a linha i de vendas

# Passo 1.6. Leia a lista de preços
precos = list(map(float, input().split()))#[:col]

# Passo 2. Compute o total de vendas
for i in range(lin):  # total de vendas do vendedor i+1
    total[i] = 0.0
    for j in range(col):  # compute o valor das vendas do item j+1
        total[i] = total[i] + vendas[i][j] * precos[j]

# Passo 3. Imprima o resultado
for i in range(lin):
    print('{:.2f}'.format(total[i]))

# pós: total and para i em {0,..,lin-1}: total[i] ==
#      sum j em {0,..,col-1}: vendas[i][j]*precos[j]
# fim do módulo principal