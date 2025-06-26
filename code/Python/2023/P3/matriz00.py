# Primeiro declara a matriz

matriz = [[0]*4 for i in range(3)]
#print(matriz)
#########################
# Outra forma:
mat = [0] * 3

#for i in range(0, 3): # linhas
 #   mat[i] = [0] * 4    # colunas

print(mat)
#########################
# Outra forma:
matr = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

#########################
# Outra forma:
matri = []
matri.append([0,0,0,0])
matri.append([0,0,0,0])
matri.append([0,0,0,0])

# Lendo uma lista de listas
#mat[0] = list(map(int, input().split()))
#mat[1] = list(map(int, input().split()))
#mat[2] = list(map(int, input().split()))

tam = int(input())
for i in range(0, tam-1):
    mat[i] = list(map(int, input().split()))
    print(mat)