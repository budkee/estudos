# Programa: matrizMultiplica00.py
# Programador:
# Data:

# Programa para ler duas matrizes A (lin1 x col1) e B
# (lin2 x col2), de inteiros, tal que col1 == lin2, calcular
# o produto C = A * B (lin1 x col2) e imprimir o resultado.

# início do módulo principal

# descrição das abstrações utilizadas
# list a[[]], b[[]], c[[]]
# int  lin1, col1 - dimensões de a
# int  lin2, col2 - dimensões de b

# pré: lin1 col1 a[0][0]..a[lin1-1][col1-1]
#      lin2 col2 a[0][0]..a[lin2-1][col2-1]

# Passo 1. Leia as Matrizes
# Passo 1.1. Leia a matriz a[[]]
# Passo 1.1.1. Leia o número de linhas e colunas de a
lin1, col1 = map(int,input().split())

# Passo 1.1.2. Inicialize a matriz a[[]]
a = [[0]*col1 for i in range(lin1)]

# Passo 1.1.3. Leia os elementos da matriz
# Passo 1.1.3.1. Leia a linha i
for i in range(lin1): # variação linha
   a[i] = list(map(int,input().split()))

# Passo 1.2. Leia a matriz b[[]]
# Passo 1.2.1. Leia o número de linhas e colunas de b
lin2, col2 = map(int,input().split())

# Passo 1.2.2. Inicialize a matriz b[[]]
b = [[0]*col2 for i in range(lin2)]

# Passo 1.3.3. Leia os elementos da matriz
# Passo 1.3.3.1. Leia a linha i
for i in range(lin2): # variação linha
   b[i] = list(map(int,input().split()))

# Passo 2. Compute a matriz produto
# Passo 2.1. Inicialize a matriz c[[]]
c = [[0]*col2 for i in range(lin1)]

# Passo 2.2. Para i variando de 0 até lin1-1 de a faça
for i in range(lin1):
# Passo 2.2.1. Para j variando de 0 até o col2-1 de b faça
   for j in range(col2):
# Passo 2.2.1.1. Inicialize soma = 0
      soma = 0
# Passo 2.2.1.2. Para k de 0 até col1-1 (lin2-1) de a (b) faça
      for k in range(col1):
# Passo 2.2.1.2.1. Adicione mat1[i][k]*mat2[k][j] a soma
         soma = soma + a[i][k] * b[k][j]

# Passo 2.22.1.3. Atribua soma a c[i][j]
      c[i][j] = soma

# Passo 3. Imprima a matriz produto c
# Passo 3.1.1. Para i variando de 0 a lin3-1 faça
for i in range(lin1):
   print(''.join(f'{j:5d}' for j in c[i]))

# pós: para todo i em {0..lin1-1}:para todo j em {0..col2-1}:c[i][j]
#      and c[i][j] == Soma k em {0..col1-1}:a[i][k]*b[k][j]
# fim do módulo principal