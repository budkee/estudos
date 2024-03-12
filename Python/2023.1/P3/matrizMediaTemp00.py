# Declaração da lista com 3 colunas (j) e 4 linhas (i)
tabTemp = [ [0.0]*3 for i in range(4)]
#print(tabTemp)

# Inicialize a lista de médias
media = [0]*4
#print(media)

# Leitura das temperaturas
for i in range(0,4):
    tabTemp[i] = list(map(float, input().split()))
#print(tabTemp)

# Calcule a média para cada horário (cada coluna)
for i in range(4): # Linha - fixa
    soma = 0
    for j in range(3): # Coluna - variável
        soma += tabTemp[i][j] # Soma dos elementos da linha
    media[i] = soma/3

# Imprima o resultado
saida = [round(item, 1) for item in media]
print(saida)
