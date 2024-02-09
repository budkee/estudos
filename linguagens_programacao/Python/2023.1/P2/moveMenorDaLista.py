""" Este programa lê uma quantidade de números inteiros, armazena numa lista, identifica o menor número da lista e reposiciona ele na primeira posição: lista[0]. """

# Leia a lista de números
lista = list(map(int, input().split())) # ou lista = [int(s) for s in input().split()]
# Selecione o menor valor da lista
# menor = min(lista)
# Ou
tam = len(lista)
menor = lista[0]
for i in range(0, tam -1):
    if lista[i] < menor:
        menor = lista[i]
# Remova o menor e coloque ele na primeira posição
# Opção 1:
lista.remove(menor)
lista.insert(0, menor)
print(*lista)

