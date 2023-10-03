def construir_quadrado_magico(n):
    # Passo 1: Inicialize o quadrado com zeros
    quad = [[0] * n for _ in range(n)]

    # Passo 2: Coloque o número 1 no meio da primeira linha
    i = 0
    j = n // 2
    quad[i][j] = 1

    # Passo 3: Preencha o quadrado com os números restantes
    for num in range(2, n**2 + 1):
        # Movimente uma linha para cima e uma coluna para a direita
        i -= 1
        j += 1

        # Verifique as condições para movimento
        if i < 0 and j >= n:
            i += 2
            j -= 1
        elif i < 0:
            i = n - 1
        elif j >= n:
            j = 0
        elif quad[i][j] != 0:
            i += 2
            j -= 1

        # Coloque o próximo número no quadrado
        quad[i][j] = num

    # Passo 4: Imprima o quadrado mágico linha a linha
    for i in range(n):
        for j in range(n):
            print(quad[i], end=' ')
        print()

# Passo 0: Obtenha o tamanho do quadrado mágico a partir da entrada
n = int(input("Digite o tamanho do quadrado mágico (ímpar e <= 50): "))

# Chame a função para construir e imprimir o quadrado mágico
construir_quadrado_magico(n)
