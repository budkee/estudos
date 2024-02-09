matriz = [[0]*3 for i in range(3)]
for i in range(3):
   for j in range(3):
      matriz[i][j] = i+j
for i in range(3):
   for j in range(3):
      print('{0:d} '.format(matriz[i][j]),end='')
   print()