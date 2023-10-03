palavra = str(input())
tam = len(palavra)
i = 0
codigo = 0
while i < tam:
    codigo += ord(palavra[i])
    i += 1
print(codigo)
