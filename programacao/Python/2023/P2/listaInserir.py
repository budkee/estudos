# Leia as entradas: lista, número a ser inserido e a posição de interesse
lista = list(map(int, input().split()))
num, pos = map(int, input().split())

lista.insert(pos, num)

print(lista)