# Passo 1: leitura dos números
num1, num2, num3, num4 = map(int, input().split())
lista = [num1, num2, num3, num4]

# Passo 2: oredenação por bolha
n = len(lista)
for i in range(n): # Para cada elemento da lista, faça:
    for j in range(n-i-1): # Ainda para cada elemento desta lista, faça:
        if lista[j] > lista[j+1]: # Se o elemento da vez for maior que o elemento subsequente, faça:
            lista[j], lista[j+1] = lista[j+1], lista[j] # Troque o elemento da vez pelo seu subsequente.

# Passo 3: imprima o resultado
for e in lista:
    print(e, end=' ')