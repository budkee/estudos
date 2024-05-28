# Passo 1.Inicialize as estruturas e leia a entrada
# Passo 1.1. Leia as dimensões das listas
# lin, col = map(int, input().split())
lin, col = 4, 3
# Passo 1.2. Inicialize as estruturas de dados
temp = [[0]*col for i in range(lin)]
media = [0]*col

# Passo 1.3. Leia a temperatura de cada local (linha a linha)
for i in range(0, lin):
    temp[i] = list(map(float, input().split()))  # leia a linha i

# Passo 2. Calcule a media das temperaturas de cada local - some as colunas das listas
# e divida pelo número de linhas
# Passo 2.1 Some as colunas
somaLista = []
# Para cada coluna, faça:
for j in range(0, col):  # fixa coluna j

    # Zere a soma para o próximo local
    soma = 0

    # Para cada linha, compute os valores daquele local
    for i in range(0, lin):  # percorre as linhas de i
        soma = soma + temp[i][j]  # soma os valores das colunas
        #print(temp[i][j], soma)

    # Após a soma de todas as temperaturas do mesmo local, adicione na lista de somas
    somaLista.append(soma)
    #print(somaLista)

    # Compute a média daquele local
    media[j] = somaLista[j]/lin

# Passo 3. Imprima a media linha a linha
for i in range(col):
    print(i+1, round(media[i], 1))

# for j in range(0, col):  # fixa coluna j
#   soma = 0
#    for i in range(0, lin):  # percorre as linhas de i
#         [0][0]:
#         soma = soma + temp[0][0]
#         [1][0]:
#         soma = soma + temp[1][0]
#         [2][0]:
#         soma = soma + temp[2][0]
#         [3][0]:
#         soma = soma + temp[3][0]
#     media[j] = soma/4
