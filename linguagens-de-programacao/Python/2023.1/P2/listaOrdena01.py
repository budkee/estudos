# Leia a lista
lista = list(map(int, input().split()))
tam = len(lista)
# Ordene a lista em ordem não decrescente( ordem crescente que aceita a repetitividade)
i = 0
while i < tam-1:
    
    j = 0
    
    while j < tam - 2 - i:
        if lista[j] > lista[j+1]:
            temp = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = temp
            j +=1
    i += 1
# Imprima sem colchetes
for i in range(tam):
    print("{}".format(lista[i]), end=' ')

