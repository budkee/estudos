palavra = str(input())
codigo = sum(ord(palavra[i]) for i in range(0,len(palavra)))
print(codigo)