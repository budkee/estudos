dim = int(input())
mat = [[0]*dim for i in range(dim)]

for i in range(dim):
    mat[i] = [int(num) for num in input().split()]

msg = 'P'
i = 0

while i < dim:
    lin = 0
    col = 0
    for j in range(dim):
        if mat[i][j] != 0 and mat[i][j] != 1:
            lin = 2
        elif mat[i][j] == 1:
            lin = lin+1
        if mat[j][i] != 0 and mat[j][i] != 1:
            col = 2
        elif mat[j][i] == 1:
            col = col +1
    if lin == 0 or lin > 1 or col == 0 or col > 1:
        i = 2*dim
        msg = 'N'
    i += 1

print(msg)