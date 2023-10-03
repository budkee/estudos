# Leia as entradas: lista, número a ser inserido e a posição de interesse
lista = list(map(int, input().split()))
index = int(input())
# Retire e retorne o valor da lista
print(lista.pop(index))
# Imprima a lista
print(lista)