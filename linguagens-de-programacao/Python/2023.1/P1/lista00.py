# Usando um quantificador para expressar o maior elemento da lista
lista = [15, 33, 18, 27]
maior = lista[0]
for i in range(1, 4):
    if lista[i] > maior:
        maior = lista[i]
print(maior)
