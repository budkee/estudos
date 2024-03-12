# Programa: matrizMediaUmidade.py
# Programador:
# Data:

# Este programa lê 3 medidas diárias de umidade do ar em 4 locais
# distintos, computa a média da umidade para cada um dos
# horários de medição e imprime o resultado

# início do módulo principal

# descrição das variáveis utilizadas
# list  umidade - lista das listas das umidades
# list  media - lista com as medias
# float soma

# pré: umidade[0] == umidade[0][0] umidade[0][1] umidade[0][2]
#      umidade[1] == umidade[1][0] umidade[1][1] umidade[1][2]
#      umidade[2] == umidade[2][0] umidade[2][1] umidade[2][2]
#      umidade[3] == umidade[3][0] umidade[3][1] umidade[3][2]

# Passo 1. Leia a entrada e crie as estruturas de dados
# Passo 1.1. Inicialize as estruturas de dados
umidade = [[0.0] * 3 for i in range(4)]  # tabela 4 x 3
media = [0.0] * 3  # média de 3 colunas
# Passo 1.2. Leia a tabela das umidades
for i in range(0, 4):
    umidade[i] = list(map(float, input().split()))  # leia a linha i
# Passo 2. Calcule as médias para cada horário
for j in range(0, 3):  # fixa coluna
    soma = 0.0
    for i in range(0, 4):  # varia a linha
        soma = soma + umidade[i][j]  # soma dos elementos da coluna
    media[j] = soma / 4.0  # media da coluna j
# Passo 3. Imprima a lista da umidade média em cada horário
# Passo 3.1. Ajuste os elementos da lista com duas casas decimais
saida = [round(item, 2) for item in media]
# Passo 3.2. Imprima a saída
print(saida)

# pós: para j em {0..2}:media[j] and media[j] == soma
#      (i em {0..3}:umidade[i][j]))/4.0
# fim do módulo principal
