def calcular_triangulo_pascal(tam):
    # Passo 2.1: Crie a matriz (lista) que armazenará o triângulo
    pascal = [[0] * (tam + 1) for _ in range(tam + 1)]

    # Passo 2.2: Preencha a matriz com os valores do triângulo de Pascal
    for i in range(1, tam + 1):
        for j in range(1, i + 1):
            if j == 1 or j == i:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

    # Passo 3: Imprima o triângulo de Pascal
    for i in range(1, tam + 1):
        for j in range(1, i + 1):
            print('{0:4d}'.format(pascal[i][j]), end='')
        print()


# Passo 1: Obtenha o número de linhas do triângulo de Pascal a partir da entrada
p = int(input())

# Chame a função para calcular e imprimir o triângulo de Pascal
calcular_triangulo_pascal(p)
