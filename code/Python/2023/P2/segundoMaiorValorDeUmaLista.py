# Este programa recebe uma quantidade tam de numeros inteiros e retorna o segundo maior valor de uma lista

# Passo 1: Leia a lista de números
lista = list(map(int, input().split()))
# Passo 2: Compute o segundo maior valor da lista
lista.remove(max(lista))   # Remova o primeiro maior
max = max(lista)    # Atribua o segundo maior a max
# Passo 3: Imprima o resultado
print(max)