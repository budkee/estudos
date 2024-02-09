# Passo 1: Ler a entrada do usuário
entrada = input().split('\n')

# Passo 2: Extrair os valores de m e n
m, n = map(int, entrada[0].split())

# Passo 3: Ler os valores da matriz a
matriz_a = []
for i in range(1, m+1):
    linha = list(map(int, entrada[i].split()))
    matriz_a.append(linha)

# Passo 4: Ler os valores da matriz b
matriz_b = []
for i in range(m+1, 2*m+1):
    linha = list(map(int, entrada[i].split()))
    matriz_b.append(linha)

# Passo 5: Criar a matriz_c vazia
matriz_c = []

# Passo 6-9: Calcular a matriz soma c
for i in range(m):
    linha_c = []
    for j in range(n):
        elemento_c = matriz_a[i][j] + matriz_b[i][j]
        linha_c.append(elemento_c)
    matriz_c.append(linha_c)

# Passo 10: Imprimir a matriz soma c
for linha in matriz_c:
    print(linha)
