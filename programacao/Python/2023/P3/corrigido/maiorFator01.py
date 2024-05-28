def maxfator(numero):
    if numero == 0 or numero == 1:
        return numero

    for i in range(numero - 1, 1, -1):
        if numero % i == 0:
            return i

    return 1

# Obtenha o número inteiro a partir da entrada
n = int(input("Digite um número inteiro (|n| > 1): "))

# Chame a função para calcular o maior fator
maior_fator = maxfator(abs(n))

# Imprima o número inteiro e o seu respectivo maior fator
print(f"Número inteiro: {n}")
print(f"Maior fator: {maior_fator}")
