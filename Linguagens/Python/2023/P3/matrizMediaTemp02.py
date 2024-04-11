# Passo 1.Inicialize as estruturas e leia a entrada
# Passo 1.1. Leia as dimensões das listas
# lin, col = map(int, input().split())
lin, col = 4, 3
# Passo 1.2. Inicialize as estruturas de dados
temp = [[0]*col for i in range(lin)]
media = [0]*lin

# Passo 1.3. Leia a temperatura de cada local (linha a linha)
for i in range(0, lin):
    temp[i] = list(map(float, input().split()))  # leia a linha i

# Passo 2. Calcule a media das temperaturas de cada horário - some as linhas e divida
# pelo número de colunas

# Passo 2.1 Some as colunas

# Para cada linha, faça:
for i in range(lin):  # fixa linha i

    # Zere a soma para o próximo local
    soma = 0

    # Para cada coluna, compute os valores daquele local
    for j in range(col):  # percorre as colunas de j
        soma = soma + temp[i][j]  # soma os valores das colunas
        #print(temp[i][j], soma)

    # Compute a média daquele horário
    media[i] = soma/col

# Passo 3. Imprima a media linha a linha
saida = [round(item,1) for item in media]
print(saida)
