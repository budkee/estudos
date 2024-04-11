# Programa:
# Programador:
# Data:

# Este programa lê os dados referentes ao número, nome, as 3 notas das
# provas e as 2 notas dos trabalhos dos alunos da disciplina de Algoritmos
# e Programação I. A média das provas é dada por MP = (P1+P2+P3)/3.0, a
# média dos trabalhos por MT = (T1 + T2)/2.0 e a média final por
# MF = 0.75*MP + 0.25*MT. O programa computa a média final, ordena os
# dados dos alunos usando a média e imprime o número, nome, as notas e a
# média final de cada aluno, onde as médias estão ordenadas em ordem
# não crescente. A entrada é dada por um arquivo onde a primeira linha
# representa o número de estudabtes e as demais linhas representam os
# dados de cada estudante.

# início do módulo principal

# descrição das variáveis utilizadas
# list avalia[[]]
# list nomes, notas
# float media
# str dados, rga, nome, nota
# int tam

# pré: para i em {0..tam-1}:dados = [rga, nomes, notas, media]

# Passo 1. Leia a entrada e inicialize as variáveis
# Passo 1.1. Leia o número de alunos
tam = int(input())
# Passo 1.2. Inicialize as abstrações
rga = ''
nomes = ['', '']
notas = [0.0, 0.0, 0.0, 0.0, 0.0]
media = 0.0
avalia = [[rga, nomes, notas, media] for _ in range(tam)]
# Passo 1.3. Leia os dados dos alunos e calcule as médias
for i in range(tam):
    dados = input()  # lê a linha inteira
    rga, nome, nota = dados.split(', ')  # separa em 3 strings
    nomes = list(nome.split())  # separa os nomes
    notas = list(map(float, nota.split()))  # separa as notas
    avalia[i][0] = rga
    avalia[i][1] = nomes
    avalia[i][2] = notas
    avalia[i][3] = 0.0
# Passo 2. Calcule a média e ordene os dados pela média
# Passo 2.1. Calcule a média das provas e dos trabalhos
for i in range(0, tam):
    mprovas = (avalia[i][2][0] + avalia[i][2][1] + avalia[i][2][2]) / 3.0
    mtrabs = (avalia[i][2][3] + avalia[i][2][4]) / 2.0
    media = 0.75 * mprovas + 0.25 * mtrabs
    avalia[i][3] = round(media, 1)
# Passo 2.2. Ordene a lista avalia[0:i]
for i in range(1, tam):
    key = avalia[i][3]  # chave da ordenação
    temp = avalia[i]  # armazena os dados de i
    # Passo 2.2.1. Procure a pos | avalia[i-1][3]<temp<avalia[i+1][3]
    j = i - 1  # inicie no final da lista avalia[0:i-1]
    while j >= 0 and key > avalia[j][3]:
        # Passo 2.2.1.1. Mova os elementos j para a direita em cada lista
        avalia[j + 1] = avalia[j]
        j = j - 1  # mova a comparação para esquerda
    # Passo 2.2.3. Insira os elementos na posição j (j+1) de cada lista
    avalia[j + 1] = temp
# Passo 3. Imprime os resultados
for i in range(0, tam):
    print('{0:s} {1:s} '.format(avalia[i][0], avalia[i][1][0]), end='')
    print('{0:s} {1:.1f} '.format(avalia[i][1][1], avalia[i][2][0]), end='')
    print('{0:.1f} {1:.1f} '.format(avalia[i][2][1], avalia[i][2][2]), end='')
    print('{0:.1f} {1:.1f} '.format(avalia[i][2][3], avalia[i][2][4]), end='')
    print('{0:.1f}'.format(avalia[i][3]))

# pós: para i em {0..tam-1}:avalia[i] and
#      avalia[i] == [rga, nomes, notas, media] and
#      avalia[i-1][3] <= avalia[i][3] < avalia[i+1][3]
# fim do módulo principal
