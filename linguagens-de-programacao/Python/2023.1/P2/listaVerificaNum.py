# Leia o tamanho da lista
tam = int(input())
# Inicialize a lista
lista = []
j = 0
# Leia os objetos da lista linha por linha
while len(lista) <= tam-1: # lista[0] 
    l = int(input())
    lista.append(l) 
    #print(lista)
    j += 1
# Leia o elemento de interesse
num = int(input())
# Verifica se pertence a lista ou não
if num in lista: 
    print('sim')
else:
    print('não')

