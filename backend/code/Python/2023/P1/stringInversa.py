# Leia a frase:
frase = str(input())
# Concatene as letras ao contrário:
invertida = ''
for i in range(len(frase)):
    invertida = frase[i] + invertida
print(invertida)
