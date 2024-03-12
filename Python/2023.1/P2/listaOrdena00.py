# Leia a lista
lista = list(map(int, input().split()))
tam = len(lista)
# Ordene a lista em ordem não decrescente( ordem crescente que aceita a repetitividade)
for i in range(1, tam):
    
    # Declare a chave de comparação (by Mohit Kumra):
    chave = lista[i]
    
    # Declare o sub-indice (j) do elemento subsequente:
    j = i - 1
    
    # Enquanto o sub-indice (j) for maior ou igual a 0, e, a chave for menor que o elemento subsequente (lista[j]), faça: 
    while j >= 0 and chave < lista[j]:
        # Atribua o elemento subsequente de (j) ao elemento da vez do sub-indice:
        lista[j+1] = lista[j]
        # Alterne o valor do subsequente (j)
        j -= 1
    
    # Finalize o loop atribuindo um valor maior que a chave:
    lista[j+1] = chave

# Imprima sem colchetes
for i in range(tam):
    print("{}".format(lista[i]), end=' ')

