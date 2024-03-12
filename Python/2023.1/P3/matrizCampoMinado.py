# Inicialize as estruturas de dados
campo = [[0]*4 for i in range(4)]

# Leia o campo minado linha a linha
for i in range(4):
    campo[i] = list(map(int, input().split()))

# Leia o número de pontos a serem analisados
n = int(input())

# Verifique os pontos
for i in range(0, n):
# Leia as coordenadas
    x, y = map(int, input().split())
    # Verifique se o ponto lido é uma bomba
    if campo[x-1][y-1] == 1:
        msg = '1'
    else:
        msg = '0'
    print(msg)
