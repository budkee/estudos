palavra = str(input())
codigo = 0
for i in range(0,len(palavra)):
   codigo += ord(palavra[i])
print(codigo)
