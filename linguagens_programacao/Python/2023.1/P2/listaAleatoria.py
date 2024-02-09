import random
# Gere uma lista de tamanho tam com números pseudo aleatórios ímpares contidos no intervalo [101,999]
# Leia o tamanho da lista e a semente
tam = int(input())
semente = random.seed(int(input()))
# Inicialize a lista
lista = []
# Compute os números aleatórios e adicione na lista
while len(lista) <= tam-1:
    aleat = random.randrange(101 , 1000, 2)
    lista.append(aleat)
print(lista)